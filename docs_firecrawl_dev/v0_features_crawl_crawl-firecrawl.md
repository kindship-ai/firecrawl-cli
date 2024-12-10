---
source: undefined
title: Crawl | Firecrawl
description: Firecrawl can recursively search through a urls subdomains, and gather the content
language: en
crawl_date: 2024-11-21T17:20:51.651Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Features

Crawl

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

Firecrawl thoroughly crawls websites, ensuring comprehensive data extraction while bypassing any web blocker mechanisms. Here’s how it works:

1. **URL Analysis:**
Begins with a specified URL, identifying links by looking at the sitemap and then crawling the website. If no sitemap is found, it will crawl the website following the links.

2. **Recursive Traversal:**
Recursively follows each link to uncover all subpages.

3. **Content Scraping:**
Gathers content from every visited page while handling any complexities like JavaScript rendering or rate limits.

4. **Result Compilation:**
Converts collected data into clean markdown or structured output, perfect for LLM processing or any other task.


This method guarantees an exhaustive crawl and data collection from any starting URL.

## [​](\#crawling)  Crawling

### [​](\#crawl-endpoint)  /crawl endpoint

Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.

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

crawl_result = app.crawl_url('mendable.ai', {'crawlerOptions': {'excludes': ['blog/*']}})

# Get the markdown
for result in crawl_result:
    print(result['markdown'])

```

### [​](\#job-id-response)  Job ID Response

If you are not using the sdk or prefer to use webhook or a different polling method, you can set the `wait_until_done` to `false`.
This will return a jobId.

For cURL, /crawl will always return a jobId where you can use to check the status of the crawl.

Copy

```json
{ "jobId": "1234-5678-9101" }

```

### [​](\#check-crawl-job)  Check Crawl Job

Used to check the status of a crawl job and get its result.

Python

JavaScript

Go

Rust

cURL

Copy

```python
status = app.check_crawl_status(job_id)

```

#### [​](\#response)  Response

Copy

```json
{
  "status": "completed",
  "current": 22,
  "total": 22,
  "data": [\
    {\
      "content": "Raw Content ",\
      "markdown": "# Markdown Content",\
      "provider": "web-scraper",\
      "metadata": {\
        "title": "Mendable | AI for CX and Sales",\
        "description": "AI for CX and Sales",\
        "language": null,\
        "sourceURL": "https://www.mendable.ai/"\
      }\
    }\
  ]
}

```

[Scrape](/v0/features/scrape) [LLM Extract](/v0/features/extract)

On this page

- [Crawling](#crawling)
- [/crawl endpoint](#crawl-endpoint)
- [Installation](#installation)
- [Usage](#usage)
- [Job ID Response](#job-id-response)
- [Check Crawl Job](#check-crawl-job)
- [Response](#response)

