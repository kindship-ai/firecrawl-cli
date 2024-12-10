# FireCrawl CLI

A command-line interface for FireCrawl - Convert websites to markdown with ease. This CLI tool allows you to scrape websites, crawl entire domains, and map website structures using the FireCrawl API.

## Features

- 🔍 **Single Page Scraping**: Convert any webpage to clean markdown
- 🕸️ **Website Crawling**: Crawl entire websites and save as markdown
- 🗺️ **URL Mapping**: Generate a map of all URLs on a website
- 🧹 **Content Cleaning**: Remove cookie notices, navigation, and other clutter
- 📄 **Multiple Formats**: Output as markdown, plain text, or JSON
- 🔐 **Secure Configuration**: Save your API key securely

## Installation

### Option 1: Install from GitHub

```bash
git clone https://github.com/kindship-ai/firecrawl-cli.git
cd firecrawl-cli
python setup.py install
```

### Option 2: Install for Development

1. Clone the repository:

```bash
git clone https://github.com/kindship-ai/firecrawl-cli.git
cd firecrawl-cli
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:

```bash
python setup.py develop
```

## Configuration

Before using the CLI, you need to configure your FireCrawl API key. You can do this in several ways:

1. Using the config command:

```bash
firecrawl config
```

2. Setting an environment variable:

```bash
export FIRECRAWL_API_KEY=your-api-key
```

3. Passing it directly in commands:

```bash
firecrawl scrape URL --api-key your-api-key
```

## Commands

### 1. Scrape Single Page

Convert a single webpage to markdown.

```bash
firecrawl scrape <URL> [OPTIONS]
```

Options:

- `--clean`: Remove navigation, cookie notices, and other clutter
- `--main-content`: Extract only the main article content
- `--format-as [markdown|plain|json]`: Output format type (default: markdown)
- `-o, --output`: Output file path
- `-f, --formats`: Input formats to request (markdown, html, screenshot)
- `--api-key`: FireCrawl API key (optional if set via config or env var)

Examples:

```bash
# Basic scrape to stdout
firecrawl scrape https://example.com

# Save clean markdown to file
firecrawl scrape https://example.com --clean -o article.md

# Get plain text with main content only
firecrawl scrape https://example.com --main-content --format-as plain
```

### 2. Crawl Website

Crawl an entire website and save all pages as markdown files.

```bash
firecrawl crawl <URL> [OPTIONS]
```

Options:

- `--limit, -l`: Maximum number of pages to crawl (default: 100)
- `--formats, -f`: Input formats to request (markdown, html, screenshot)
- `--output-dir, -o`: Output directory path
- `--poll-interval, -p`: Polling interval in seconds (default: 30)
- `--metadata/--no-metadata`: Save metadata files (default: False)
- `--api-key`: FireCrawl API key (optional if set via config or env var)

Examples:

```bash
# Basic crawl with default settings
firecrawl crawl https://example.com -o output/

# Crawl with limit and metadata
firecrawl crawl https://example.com --limit 50 --metadata -o output/

# Crawl with custom formats and polling
firecrawl crawl https://example.com -f markdown -f html --poll-interval 60 -o output/
```

### 3. Map URLs

Generate a map of all URLs on a website.

```bash
firecrawl map-urls <URL> [OPTIONS]
```

Options:

- `--limit, -l`: Maximum number of URLs to map (default: 100)
- `-o, --output`: Output file path (JSON format)
- `--poll-interval, -p`: Polling interval in seconds (default: 30)
- `--api-key`: FireCrawl API key (optional if set via config or env var)

Examples:

```bash
# Map URLs to stdout
firecrawl map-urls https://example.com

# Save URL map to file with limit
firecrawl map-urls https://example.com --limit 200 -o sitemap.json
```

### 4. Configure API Key

Save your FireCrawl API key for future use.

```bash
firecrawl config [OPTIONS]
```

Options:

- `--show`: Display current API key
- `--unset`: Remove saved API key

Examples:

```bash
# Set API key interactively
firecrawl config

# Show current API key
firecrawl config --show

# Remove saved API key
firecrawl config --unset
```

## Output Formats

The CLI supports multiple output formats:

1. **Markdown** (default):

   - Clean, formatted markdown
   - Preserves headings, links, and images
   - Ideal for documentation

2. **HTML**:

   - Raw HTML content
   - Includes original page structure
   - Useful for archiving

3. **Plain Text**:

   - Text-only content
   - Removes all formatting
   - Good for analysis or processing

4. **Metadata** (JSON):
   - Page information (title, URL, etc.)
   - Crawl statistics
   - Available when using --metadata flag

## Requirements

- Python 3.7+
- click>=8.1.7
- firecrawl-py>=1.0.0
- pydantic>=2.0.0

## License

MIT License - see LICENSE file for details.
