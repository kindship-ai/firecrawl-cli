import os
import json
import click
from typing import List, Optional
from firecrawl import FirecrawlApp
from .formatters import clean_markdown, extract_main_content, format_output
from .utils import sanitize_filename
from .config import get_api_key


def handle_scrape(
    url: str,
    formats: List[str],
    output: Optional[str],
    api_key: Optional[str],
    clean: bool,
    main_content: bool,
    format_as: str,
):
    """Handle the scrape command logic"""
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


def handle_crawl(
    url: str,
    limit: int,
    formats: List[str],
    output_dir: Optional[str],
    poll_interval: int,
    api_key: Optional[str],
    metadata: bool,
):
    """Handle the crawl command logic"""
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
                        page["metadata"].get("sourceURL", "").rstrip("/").split("/")[-1]
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


def handle_map_urls(url: str, output: Optional[str], api_key: Optional[str]):
    """Handle the map-urls command logic"""
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
