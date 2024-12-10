import click
import warnings
from typing import List, Optional
from .config import load_config, save_config, get_api_key
from .lib import handle_scrape, handle_crawl, handle_map_urls

# Suppress Pydantic warning about schema field
warnings.filterwarnings(
    "ignore",
    message='Field name "schema" in "FirecrawlApp.ExtractParams" shadows an attribute in parent "BaseModel"',
)


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
        handle_scrape(url, formats, output, api_key, clean, main_content, format_as)
    except Exception as e:
        click.echo(f"\nError: {str(e)}", err=True)


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
        handle_crawl(url, limit, formats, output_dir, poll_interval, api_key, metadata)
    except Exception as e:
        click.echo(f"\nError: {str(e)}", err=True)


@click.command(help="Map all URLs on a website")
@click.argument("url")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--api-key", help="FireCrawl API key (or set FIRECRAWL_API_KEY env var)")
def map_urls(url: str, output: Optional[str], api_key: Optional[str]):
    """Get a map of all URLs on a website"""
    try:
        handle_map_urls(url, output, api_key)
    except Exception as e:
        click.echo(f"\nError: {str(e)}", err=True)


cli.add_command(scrape)
cli.add_command(crawl)
cli.add_command(map_urls)
cli.add_command(config)
