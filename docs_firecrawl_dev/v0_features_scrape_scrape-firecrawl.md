---
source: undefined
title: Scrape | Firecrawl
description: Turn any url into clean data
language: en
crawl_date: 2024-11-21T17:20:44.226Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Features

Scrape

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

## [​](\#scraping-with-firecrawl)  Scraping with Firecrawl

Firecrawl converts web pages into markdown, ideal for LLM applications. Here’s why:

1. **Complexities Managed:**
Handles proxies, caching, rate limits, and JavaScript-blocked content for smooth scraping.

2. **Dynamic Content:**
Gathers data from JavaScript-rendered websites, pdfs, images etc.

3. **Markdown or Structured data conversion:**
Converts collected data into clean markdown or structured output, perfect for LLM processing or any other task.


For more details, refer to the [Scrape Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## [​](\#scrape-a-url)  Scrape a URL

### [​](\#scrape-endpoint)  /scrape endpoint

Used to scrape a URL and get its content.

### [​](\#installation)  Installation

Python

JavaScript

Go

Rust

Copy

```bash
pip install firecrawl-py

```

### [​](\#usage)  Usage

Python

JavaScript

Go

Rust

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="YOUR_API_KEY")

content = app.scrape_url("https://mendable.ai")

```

### [​](\#response)  Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

Copy

```json
{
  "success": true,
  "data": {
    "content": "Raw Content ",
    "markdown": "# Markdown Content",
    "provider": "web-scraper",
    "metadata": {
      "title": "Mendable | AI for CX and Sales",
      "description": "AI for CX and Sales",
      "language": null,
      "sourceURL": "https://www.mendable.ai/"
    }
  }
}

```

[Integrations](/integrations) [Crawl](/v0/features/crawl)

On this page

- [Scraping with Firecrawl](#scraping-with-firecrawl)
- [Scrape a URL](#scrape-a-url)
- [/scrape endpoint](#scrape-endpoint)
- [Installation](#installation)
- [Usage](#usage)
- [Response](#response)

