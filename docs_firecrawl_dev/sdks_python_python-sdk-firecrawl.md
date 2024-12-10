---
source: undefined
title: Python SDK | Firecrawl
description: Firecrawl Python SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
language: en
crawl_date: 2024-11-21T17:20:42.069Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Python

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#installation)  Installation

To install the Firecrawl Python SDK, you can use pip:

Python

Copy

```bash
pip install firecrawl-py

```

## [​](\#usage)  Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.

Here’s an example of how to use the SDK:

Python

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_status = app.scrape_url(
  'https://firecrawl.dev',
  params={'formats': ['markdown', 'html']}
)
print(scrape_status)

# Crawl a website:
crawl_status = app.crawl_url(
  'https://firecrawl.dev',
  params={
    'limit': 100,
    'scrapeOptions': {'formats': ['markdown', 'html']}
  }
)
print(crawl_status)

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

Python

Copy

```python
# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev', params={'formats': ['markdown', 'html']})
print(scrape_result)

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website, use the `crawl_url` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Python

Copy

```python
crawl_status = app.crawl_url(
  'https://firecrawl.dev',
  params={
    'limit': 100,
    'scrapeOptions': {'formats': ['markdown', 'html']}
  },
  poll_interval=30
)
print(crawl_status)

```

### [​](\#asynchronous-crawling)  Asynchronous Crawling

To crawl a website asynchronously, use the `crawl_url_async` method. It returns the crawl `ID` which you can use to check the status of the crawl job. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Python

Copy

```python
crawl_status = app.async_crawl_url(
  'https://firecrawl.dev',
  params={
    'limit': 100,
    'scrapeOptions': {'formats': ['markdown', 'html']}
  }
)
print(crawl_status)

```

### [​](\#checking-crawl-status)  Checking Crawl Status

To check the status of a crawl job, use the `check_crawl_status` method. It takes the job ID as a parameter and returns the current status of the crawl job.

Python

Copy

```python
crawl_status = app.check_crawl_status("<crawl_id>")
print(crawl_status)

```

### [​](\#cancelling-a-crawl)  Cancelling a Crawl

To cancel an asynchronous crawl job, use the `cancel_crawl` method. It takes the job ID of the asynchronous crawl as a parameter and returns the cancellation status.

Python

Copy

```python
cancel_crawl = app.cancel_crawl(id)
print(cancel_crawl)

```

### [​](\#map-a-website)  Map a Website

Use `map_url` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.

Python

Copy

```python
# Map a website:
map_result = app.map_url('https://firecrawl.dev')
print(map_result)

```

### [​](\#crawling-a-website-with-websockets)  Crawling a Website with WebSockets

To crawl a website with WebSockets, use the `crawl_url_and_watch` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Python

Copy

```python
# inside an async function...
nest_asyncio.apply()

# Define event handlers
def on_document(detail):
    print("DOC", detail)

def on_error(detail):
    print("ERR", detail['error'])

def on_done(detail):
    print("DONE", detail['status'])

    # Function to start the crawl and watch process
async def start_crawl_and_watch():
    # Initiate the crawl job and get the watcher
    watcher = app.crawl_url_and_watch('firecrawl.dev', { 'excludePaths': ['blog/*'], 'limit': 5 })

    # Add event listeners
    watcher.add_event_listener("document", on_document)
    watcher.add_event_listener("error", on_error)
    watcher.add_event_listener("done", on_done)

    # Start the watcher
    await watcher.connect()

# Run the event loop
await start_crawl_and_watch()

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

[Overview](/sdks/overview) [Node](/sdks/node)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Scraping a URL](#scraping-a-url)
- [Crawling a Website](#crawling-a-website)
- [Asynchronous Crawling](#asynchronous-crawling)
- [Checking Crawl Status](#checking-crawl-status)
- [Cancelling a Crawl](#cancelling-a-crawl)
- [Map a Website](#map-a-website)
- [Crawling a Website with WebSockets](#crawling-a-website-with-websockets)
- [Error Handling](#error-handling)

