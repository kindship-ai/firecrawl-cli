import click
import os
import json
import warnings
import re
from pathlib import Path
from typing import List, Optional
from firecrawl import FirecrawlApp

# Suppress Pydantic warning about schema field
warnings.filterwarnings(
    "ignore",
    message='Field name "schema" in "FirecrawlApp.ExtractParams" shadows an attribute in parent "BaseModel"',
)


def clean_markdown(content: str) -> str:
    """Remove navigation, cookie notices, and other clutter from markdown content"""
    lines = content.split("\n")
    cleaned_lines = []
    skip_section = False

    for line in lines:
        # Skip cookie consent and navigation sections
        if any(
            marker in line.lower()
            for marker in [
                "cookie",
                "consent",
                "privacy",
                "navigation",
                "this website uses",
                "necessary cookies",
                "marketing cookies",
                "statistics cookies",
                "preferences cookies",
                "unclassified cookies",
            ]
        ):
            skip_section = True
            continue

        # Resume capturing content at headings
        if skip_section and line.startswith("#"):
            skip_section = False

        if not skip_section:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()


def extract_main_content(content: str) -> str:
    """Extract the main article content from markdown"""
    lines = content.split("\n")
    content_lines = []
    in_content = False

    for line in lines:
        # Start capturing at first heading
        if line.startswith("#"):
            in_content = True

        if in_content:
            content_lines.append(line)

    return "\n".join(content_lines).strip()


def format_output(content: str, format_type: str) -> str:
    """Format the content based on the specified format"""
    if format_type == "plain":
        # Remove markdown formatting
        text = content
        text = text.replace("**", "")  # Remove bold
        text = text.replace("*", "")  # Remove italic
        text = text.replace("###", "")  # Remove h3
        text = text.replace("##", "")  # Remove h2
        text = text.replace("#", "")  # Remove h1

        # Remove links but keep text
        while "[" in text and "](" in text:
            start = text.find("[")
            mid = text.find("](")
            end = text.find(")", mid)
            if start != -1 and mid != -1 and end != -1:
                link_text = text[start + 1 : mid]
                text = text[:start] + link_text + text[end + 1 :]
            else:
                break

        return text.strip()

    elif format_type == "json":
        # Extract title and content
        lines = content.split("\n")
        title = ""
        content_lines = []

        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
            else:
                content_lines.append(line)

        return json.dumps(
            {"title": title, "content": "\n".join(content_lines).strip()}, indent=2
        )

    return content  # Default to markdown


def get_config_file() -> Path:
    """Get the path to the config file"""
    config_dir = Path.home() / ".firecrawl"
    config_dir.mkdir(exist_ok=True)
    return config_dir / "config.json"


def load_config() -> dict:
    """Load configuration from file"""
    config_file = get_config_file()
    if config_file.exists():
        with open(config_file) as f:
            return json.load(f)
    return {}


def save_config(config: dict):
    """Save configuration to file"""
    config_file = get_config_file()
    with open(config_file, "w") as f:
        json.dump(config, f, indent=2)
    # Secure the config file
    config_file.chmod(0o600)


def get_api_key():
    """Get API key from config, environment variable, or prompt user"""
    # Try environment first
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if api_key:
        return api_key

    # Try config file
    config = load_config()
    api_key = config.get("api_key")
    if api_key:
        return api_key

    # Prompt user
    api_key = click.prompt(
        "Please enter your FireCrawl API key (get one at https://firecrawl.dev)",
        type=str,
        hide_input=True,
    )

    # Save to config if user wants to
    if click.confirm(
        "Would you like to save the API key for future use?", default=True
    ):
        config["api_key"] = api_key
        save_config(config)
        click.echo("API key saved to ~/.firecrawl/config.json")
    else:
        # If not saving to config, at least save for current session
        os.environ["FIRECRAWL_API_KEY"] = api_key
        click.echo("API key saved for this session")

    return api_key


@click.group()
def cli():
    """FireCrawl CLI - Convert websites to markdown with ease"""
    pass


@click.command(help="Configure FireCrawl CLI settings")
def config():
    """Configure FireCrawl CLI settings"""
    config = load_config()

    # Always prompt for API key in config command
    api_key = click.prompt(
        "Enter your FireCrawl API key (get one at https://firecrawl.dev)",
        type=str,
        default=config.get("api_key", ""),
        hide_input=True,
        show_default=False,
    )

    config["api_key"] = api_key
    save_config(config)
    click.echo("Configuration saved to ~/.firecrawl/config.json")


@click.command(help="Scrape a single URL and convert it to markdown")
@click.argument("url")
@click.option(
    "--formats",
    "-f",
    multiple=True,
    default=["markdown"],
    type=click.Choice(["markdown", "html", "screenshot"]),
    help="Output formats (default: markdown)",
)
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--api-key", help="FireCrawl API key (or set FIRECRAWL_API_KEY env var)")
@click.option(
    "--clean", is_flag=True, help="Remove navigation, cookie notices, and other clutter"
)
@click.option(
    "--main-content", is_flag=True, help="Extract only the main article content"
)
@click.option(
    "--format-as",
    type=click.Choice(["markdown", "plain", "json"]),
    default="markdown",
    help="Output format type (default: markdown)",
)
def scrape(
    url: str,
    formats: List[str],
    output: Optional[str],
    api_key: Optional[str],
    clean: bool,
    main_content: bool,
    format_as: str,
):
    """Scrape a URL and get its content in the specified format"""
    try:
        with click.progressbar(
            length=100,
            label=f"Scraping {url}",
        ) as bar:
            api_key = api_key or get_api_key()
            app = FirecrawlApp(api_key=api_key)
            bar.update(30)

            result = app.scrape_url(url, params={"formats": list(formats)})
            bar.update(70)

            content = result.get("markdown", result.get("html", ""))

            # Apply content processing
            if clean:
                content = clean_markdown(content)
            if main_content:
                content = extract_main_content(content)
            if format_as != "markdown":
                content = format_output(content, format_as)

            if output:
                with open(output, "w") as f:
                    f.write(content)
                click.echo(f"\nContent saved to {output}")
            else:
                click.echo(content)

    except Exception as e:
        click.echo(f"\nError: {str(e)}", err=True)


def sanitize_filename(title: str, max_length: int = 50) -> str:
    """Convert a title to a clean filename"""
    # Remove any text after certain markers that indicate end of main title
    markers = ["|", "-", "—", "–", ":", "•"]
    for marker in markers:
        if marker in title:
            title = title.split(marker)[0]

    # Remove any non-alphanumeric characters (except spaces)
    clean = re.sub(r"[^\w\s-]", "", title)
    # Replace spaces with dashes
    clean = clean.strip().replace(" ", "-")
    # Convert to lowercase
    clean = clean.lower()
    # Remove any repeated dashes
    clean = re.sub(r"-+", "-", clean)
    # Truncate to max length while keeping whole words
    if len(clean) > max_length:
        clean = clean[:max_length].rsplit("-", 1)[0]
    return clean


@click.command(help="Crawl a website and all its subpages")
@click.argument("url")
@click.option("--limit", "-l", default=100, help="Maximum number of pages to crawl")
@click.option(
    "--formats",
    "-f",
    multiple=True,
    default=["markdown"],
    type=click.Choice(["markdown", "html", "screenshot"]),
    help="Output formats (default: markdown)",
)
@click.option("--output-dir", "-o", type=click.Path(), help="Output directory path")
@click.option("--poll-interval", "-p", default=30, help="Polling interval in seconds")
@click.option("--api-key", help="FireCrawl API key (or set FIRECRAWL_API_KEY env var)")
@click.option(
    "--metadata/--no-metadata",
    default=False,
    help="Save metadata files (default: False)",
)
def crawl(
    url: str,
    limit: int,
    formats: List[str],
    output_dir: Optional[str],
    poll_interval: int,
    api_key: Optional[str],
    metadata: bool,
):
    """Crawl a website and get content from all accessible pages"""
    try:
        api_key = api_key or get_api_key()
        app = FirecrawlApp(api_key=api_key)

        with click.progressbar(
            length=100,
            label=f"Starting crawl of {url}",
        ) as bar:
            result = app.crawl_url(
                url,
                params={"limit": limit, "scrapeOptions": {"formats": list(formats)}},
                poll_interval=poll_interval,
            )
            bar.update(100)

        if output_dir:
            import os

            os.makedirs(output_dir, exist_ok=True)

            with click.progressbar(
                result["data"],
                label="Saving crawled pages",
                item_show_func=lambda p: f"Saving page {p['metadata']['title'] if p else ''}",
            ) as pages:
                for page in pages:
                    # Get title from metadata, fallback to URL if no title
                    title = page["metadata"].get("title", "")
                    if not title:
                        # Extract last part of URL path as fallback
                        url_path = (
                            page["metadata"]
                            .get("sourceURL", "")
                            .rstrip("/")
                            .split("/")[-1]
                        )
                        title = url_path if url_path else "untitled"

                    # Create clean filename
                    filename = sanitize_filename(title)

                    # Add index if file exists
                    base_filename = filename
                    counter = 1
                    while os.path.exists(f"{output_dir}/{filename}"):
                        filename = f"{base_filename}-{counter}"
                        counter += 1

                    if "markdown" in formats:
                        with open(f"{output_dir}/{filename}.md", "w") as f:
                            f.write(page["markdown"])
                    elif "html" in formats:
                        with open(f"{output_dir}/{filename}.html", "w") as f:
                            f.write(page["html"])

                    # Save metadata only if requested
                    if metadata:
                        with open(f"{output_dir}/{filename}_metadata.json", "w") as f:
                            json.dump(page["metadata"], f, indent=2)

            click.echo(f"\nCrawl results saved to {output_dir}")
        else:
            click.echo(json.dumps(result, indent=2))

    except Exception as e:
        click.echo(f"\nError: {str(e)}", err=True)


@click.command(help="Map all URLs on a website")
@click.argument("url")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--api-key", help="FireCrawl API key (or set FIRECRAWL_API_KEY env var)")
def map_urls(url: str, output: Optional[str], api_key: Optional[str]):
    """Get a map of all URLs on a website"""
    try:
        with click.progressbar(
            length=100,
            label=f"Mapping URLs for {url}",
        ) as bar:
            api_key = api_key or get_api_key()
            app = FirecrawlApp(api_key=api_key)
            bar.update(30)

            result = app.map_url(url)
            bar.update(70)

            if output:
                with open(output, "w") as f:
                    json.dump(result, f, indent=2)
                click.echo(f"\nURL map saved to {output}")
            else:
                click.echo(json.dumps(result, indent=2))

    except Exception as e:
        click.echo(f"\nError: {str(e)}", err=True)


cli.add_command(scrape)
cli.add_command(crawl)
cli.add_command(map_urls)
cli.add_command(config)
