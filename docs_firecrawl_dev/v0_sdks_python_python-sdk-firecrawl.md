---
source: undefined
title: Python SDK | Firecrawl
description: Firecrawl Python SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
language: en
crawl_date: 2024-11-21T17:20:44.203Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Python

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

> Note: this is using [v0 version of the Firecrawl API](/v0/introduction) which is being deprecated. We recommend switching to [v1](/sdks/python).

## [​](\#installation)  Installation

To install the Firecrawl Python SDK, you can use pip:

Copy

```bash
pip install firecrawl-py==0.0.16

```

## [​](\#usage)  Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.

Here’s an example of how to use the SDK:

Copy

```python
from firecrawl import FirecrawlApp

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')

# Scrape a single URL
url = 'https://docs.firecrawl.dev'
scraped_data = app.scrape_url(url)

# Crawl a website
crawl_url = 'https://docs.firecrawl.dev'
params = {
    'pageOptions': {
        'onlyMainContent': True
    }
}
crawl_result = app.crawl_url(crawl_url, params=params)

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

Copy

```python
url = 'https://example.com'
scraped_data = app.scrape_url(url)

```

### [​](\#extracting-structured-data-from-a-url)  Extracting structured data from a URL

With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:

Copy

```python
class ArticleSchema(BaseModel):
    title: str
    points: int
    by: str
    commentsURL: str

class TopArticlesSchema(BaseModel):
    top: List[ArticleSchema] = Field(..., max_items=5, description="Top 5 stories")

data = app.scrape_url('https://news.ycombinator.com', {
    'extractorOptions': {
        'extractionSchema': TopArticlesSchema.model_json_schema(),
        'mode': 'llm-extraction'
    },
    'pageOptions':{
        'onlyMainContent': True
    }
})
print(data["llm_extraction"])

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website, use the `crawl_url` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

The `wait_until_done` parameter determines whether the method should wait for the crawl job to complete before returning the result. If set to `True`, the method will periodically check the status of the crawl job until it is completed or the specified `timeout` (in seconds) is reached. If set to `False`, the method will return immediately with the job ID, and you can manually check the status of the crawl job using the `check_crawl_status` method.

Copy

```python
crawl_url = 'https://example.com'
params = {
    'crawlerOptions': {
        'excludes': ['blog/*'],
        'includes': [], # leave empty for all pages
        'limit': 1000,
    },
    'pageOptions': {
        'onlyMainContent': True
    }
}
crawl_result = app.crawl_url(crawl_url, params=params, wait_until_done=True, timeout=5)

```

If `wait_until_done` is set to `True`, the `crawl_url` method will return the crawl result once the job is completed. If the job fails or is stopped, an exception will be raised.

### [​](\#checking-crawl-status)  Checking Crawl Status

To check the status of a crawl job, use the `check_crawl_status` method. It takes the job ID as a parameter and returns the current status of the crawl job.

Copy

```python
job_id = crawl_result['jobId']
status = app.check_crawl_status(job_id)

```

### [​](\#search-for-a-query)  Search for a query

Used to search the web, get the most relevant results, scrap each page and return the markdown.

Copy

```python
query = 'what is mendable?'
search_result = app.search(query)

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

[Node](/v0/sdks/node)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Scraping a URL](#scraping-a-url)
- [Extracting structured data from a URL](#extracting-structured-data-from-a-url)
- [Crawling a Website](#crawling-a-website)
- [Checking Crawl Status](#checking-crawl-status)
- [Search for a query](#search-for-a-query)
- [Error Handling](#error-handling)

