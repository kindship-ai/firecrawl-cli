---
source: undefined
title: Node SDK | Firecrawl
description: Firecrawl Node SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
language: en
crawl_date: 2024-11-21T17:20:45.318Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Node

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

> Note: this is using [v0 version of the Firecrawl API](/v0/introduction) which is being deprecated. We recommend switching to [v1](/sdks/node).

## [​](\#installation)  Installation

To install the Firecrawl Node SDK, you can use npm:

Copy

```bash
npm install @mendable/firecrawl-js@0.0.36

```

## [​](\#usage)  Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.

Here’s an example of how to use the SDK with error handling:

Copy

```js
import FirecrawlApp from '@mendable/firecrawl-js';

// Initialize the FirecrawlApp with your API key
const app = new FirecrawlApp({ apiKey: "YOUR_API_KEY" });

// Scrape a single URL
const url = 'https://docs.firecrawl.dev';
const scrapedData = await app.scrapeUrl(url);

// Crawl a website
const crawlUrl = 'https://docs.firecrawl.dev';
const params = {
  crawlerOptions: {
    excludes: ['blog/'],
    includes: [], // leave empty for all pages
    limit: 1000,
  },
  pageOptions: {
      onlyMainContent: true
  }
};

const crawlResult = await app.crawlUrl(crawlUrl, params);

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL with error handling, use the `scrapeUrl` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

Copy

```js
const url = 'https://example.com';
const scrapedData = await app.scrapeUrl(url);

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website with error handling, use the `crawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Copy

```js
const crawlUrl = 'https://example.com';

const params = {
  crawlerOptions: {
    excludes: ['blog/'],
    includes: [], // leave empty for all pages
    limit: 1000,
  },
  pageOptions: {
    onlyMainContent: true
  }
};

const waitUntilDone = true;
const pollInterval = 5;

const crawlResult = await app.crawlUrl(
  crawlUrl,
  params,
  waitUntilDone,
  pollInterval
);

```

### [​](\#checking-crawl-status)  Checking Crawl Status

To check the status of a crawl job with error handling, use the `checkCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.

Copy

```js
const status = await app.checkCrawlStatus(jobId);

```

### [​](\#extracting-structured-data-from-a-url)  Extracting structured data from a URL

With LLM extraction, you can easily extract structured data from any URL. We support zod schema to make it easier for you too. Here is how you to use it:

Copy

```js
import FirecrawlApp from "@mendable/firecrawl-js";
import { z } from "zod";

const app = new FirecrawlApp({
  apiKey: "fc-YOUR_API_KEY",
});

// Define schema to extract contents into
const schema = z.object({
  top: z
    .array(
      z.object({
        title: z.string(),
        points: z.number(),
        by: z.string(),
        commentsURL: z.string(),
      })
    )
    .length(5)
    .describe("Top 5 stories on Hacker News"),
});

const scrapeResult = await app.scrapeUrl("https://firecrawl.dev", {
  extractorOptions: { extractionSchema: schema },
});

console.log(scrapeResult.data["llm_extraction"]);

```

### [​](\#search-for-a-query)  Search for a query

With the `search` method, you can search for a query in a search engine and get the top results along with the page content for each result. The method takes the query as a parameter and returns the search results.

Copy

```js
const query = 'what is mendable?';
const searchResults = await app.search(query, {
  pageOptions: {
    fetchPageContent: true // Fetch the page content for each search result
  }
});

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message. The examples above demonstrate how to handle these errors using `try/catch` blocks.

[Python](/v0/sdks/python) [Go](/v0/sdks/go)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Scraping a URL](#scraping-a-url)
- [Crawling a Website](#crawling-a-website)
- [Checking Crawl Status](#checking-crawl-status)
- [Extracting structured data from a URL](#extracting-structured-data-from-a-url)
- [Search for a query](#search-for-a-query)
- [Error Handling](#error-handling)

