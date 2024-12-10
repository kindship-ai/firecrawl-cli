---
source: undefined
title: Node SDK | Firecrawl
description: Firecrawl Node SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
language: en
crawl_date: 2024-11-21T17:20:42.086Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Node

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#installation)  Installation

To install the Firecrawl Node SDK, you can use npm:

Node

Copy

```bash
npm install @mendable/firecrawl-js

```

## [​](\#usage)  Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.

Here’s an example of how to use the SDK with error handling:

Node

Copy

```js
import FirecrawlApp, { CrawlParams, CrawlStatusResponse } from '@mendable/firecrawl-js';

const app = new FirecrawlApp({apiKey: "fc-YOUR_API_KEY"});

// Scrape a website
const scrapeResponse = await app.scrapeUrl('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

if (!scrapeResponse.success) {
  throw new Error(`Failed to scrape: ${scrapeResponse.error}`)
}

console.log(scrapeResponse)

// Crawl a website
const crawlResponse = await app.crawlUrl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

if (!crawlResponse.success) {
  throw new Error(`Failed to crawl: ${crawlResponse.error}`)
}

console.log(crawlResponse)

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL with error handling, use the `scrapeUrl` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

Node

Copy

```js
// Scrape a website:
const scrapeResult = await app.scrapeUrl('firecrawl.dev', { formats: ['markdown', 'html'] });

if (!scrapeResult.success) {
  throw new Error(`Failed to scrape: ${scrapeResult.error}`)
}

console.log(scrapeResult)

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website with error handling, use the `crawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Node

Copy

```js
const crawlResponse = await app.crawlUrl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
})

if (!crawlResponse.success) {
  throw new Error(`Failed to crawl: ${crawlResponse.error}`)
}

console.log(crawlResponse)

```

### [​](\#asynchronous-crawling)  Asynchronous Crawling

To crawl a website asynchronously, use the `crawlUrlAsync` method. It returns the crawl `ID` which you can use to check the status of the crawl job. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Node

Copy

```js
const crawlResponse = await app.asyncCrawlUrl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

if (!crawlResponse.success) {
  throw new Error(`Failed to crawl: ${crawlResponse.error}`)
}

console.log(crawlResponse)

```

### [​](\#checking-crawl-status)  Checking Crawl Status

To check the status of a crawl job with error handling, use the `checkCrawlStatus` method. It takes the `ID` as a parameter and returns the current status of the crawl job.

Node

Copy

```js
const crawlResponse = await app.checkCrawlStatus("<crawl_id>");

if (!crawlResponse.success) {
  throw new Error(`Failed to check crawl status: ${crawlResponse.error}`)
}

console.log(crawlResponse)

```

### [​](\#cancelling-a-crawl)  Cancelling a Crawl

To cancel an asynchronous crawl job, use the `cancelCrawl` method. It takes the job ID of the asynchronous crawl as a parameter and returns the cancellation status.

Node

Copy

```js
const cancelCrawl = await app.cancelCrawl(id);
console.log(cancelCrawl)

```

### [​](\#mapping-a-website)  Mapping a Website

To map a website with error handling, use the `mapUrl` method. It takes the starting URL as a parameter and returns the mapped data as a dictionary.

Node

Copy

```js
const mapResult = await app.mapUrl('https://firecrawl.dev');

if (!mapResult.success) {
  throw new Error(`Failed to map: ${mapResult.error}`)
}

console.log(mapResult)

```

### [​](\#crawling-a-website-with-websockets)  Crawling a Website with WebSockets

To crawl a website with WebSockets, use the `crawlUrlAndWatch` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Node

Copy

```js
const watch = await app.crawlUrlAndWatch('mendable.ai', { excludePaths: ['blog/*'], limit: 5});

watch.addEventListener("document", doc => {
  console.log("DOC", doc.detail);
});

watch.addEventListener("error", err => {
  console.error("ERR", err.detail.error);
});

watch.addEventListener("done", state => {
  console.log("DONE", state.detail.status);
});

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message. The examples above demonstrate how to handle these errors using `try/catch` blocks.

[Python](/sdks/python) [Go](/sdks/go)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Scraping a URL](#scraping-a-url)
- [Crawling a Website](#crawling-a-website)
- [Asynchronous Crawling](#asynchronous-crawling)
- [Checking Crawl Status](#checking-crawl-status)
- [Cancelling a Crawl](#cancelling-a-crawl)
- [Mapping a Website](#mapping-a-website)
- [Crawling a Website with WebSockets](#crawling-a-website-with-websockets)
- [Error Handling](#error-handling)

