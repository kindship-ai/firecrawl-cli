---
source: undefined
title: Go SDK | Firecrawl
description: Firecrawl Go SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
language: en
crawl_date: 2024-11-21T17:20:45.324Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Go

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

> Note: this is using [v0 version of the Firecrawl API](/v0/introduction) which is being deprecated. We recommend switching to [v1](/sdks/go).

## [​](\#installation)  Installation

To install the Firecrawl Go SDK, you can use go get:

Copy

```bash
go get github.com/mendableai/firecrawl-go

```

## [​](\#usage)  Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` struct.

Here’s an example of how to use the SDK with error handling:

Copy

```go
import (
  "fmt"
  "log"

  "github.com/mendableai/firecrawl-go"
)

func main() {
  // Initialize the FirecrawlApp with your API key
  app, err := firecrawl.NewFirecrawlApp("YOUR_API_KEY")
  if err != nil {
    log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
  }

  // Scrape a single URL
  scrapedData, err := app.ScrapeURL("docs.firecrawl.dev", nil)
  if err != nil {
    log.Fatalf("Error occurred while scraping: %v", err)
  }
  fmt.Println(scrapedData)

  // Crawl a website
  params := map[string]any{
    "pageOptions": map[string]any{
      "onlyMainContent": true,
    },
  }

  crawlResult, err := app.CrawlURL("docs.firecrawl.dev", params)
  if err != nil {
    log.Fatalf("Error occurred while crawling: %v", err)
  }
  fmt.Println(crawlResult)
}

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

Copy

```go
scrapedData, err := app.ScrapeURL("docs.firecrawl.dev", nil)
if err != nil {
  log.Fatalf("Failed to scrape URL: %v", err)
}
fmt.Println(scrapedData)

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Copy

```go
crawlParams := map[string]any{
  "crawlerOptions": map[string]any{
    "excludes": []string{"blog/*"},
    "includes": []string{}, // leave empty for all pages
    "limit": 1000,
  },
  "pageOptions": map[string]any{
    "onlyMainContent": true,
  },
}
crawlResult, err := app.CrawlURL("docs.firecrawl.dev", crawlParams, true, 2, idempotencyKey)
if err != nil {
  log.Fatalf("Failed to crawl URL: %v", err)
}
fmt.Println(crawlResult)

```

### [​](\#checking-crawl-status)  Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.

Copy

```go
status, err := app.CheckCrawlStatus(jobId)
if err != nil {
  log.Fatalf("Failed to check crawl status: %v", err)
}
fmt.Println(status)

```

### [​](\#canceling-a-crawl-job)  Canceling a Crawl Job

To cancel a crawl job, use the `CancelCrawlJob` method. It takes the job ID as a parameter and returns the cancellation status of the crawl job.

Copy

```go
canceled, err := app.CancelCrawlJob(jobId)
if err != nil {
  log.Fatalf("Failed to cancel crawl job: %v", err)
}
fmt.Println(canceled)

```

### [​](\#extracting-structured-data-from-a-url)  Extracting structured data from a URL

With LLM extraction, you can easily extract structured data from any URL. Here is how you to use it:

Copy

```go
jsonSchema := map[string]any{
  "type": "object",
  "properties": map[string]any{
    "top": map[string]any{
      "type": "array",
      "items": map[string]any{
        "type": "object",
        "properties": map[string]any{
          "title":       map[string]string{"type": "string"},
          "points":      map[string]string{"type": "number"},
          "by":          map[string]string{"type": "string"},
          "commentsURL": map[string]string{"type": "string"},
        },
        "required": []string{"title", "points", "by", "commentsURL"},
      },
      "minItems":    5,
      "maxItems":    5,
      "description": "Top 5 stories on Hacker News",
    },
  },
  "required": []string{"top"},
}

llmExtractionParams := map[string]any{
  "extractorOptions": firecrawl.ExtractorOptions{
    ExtractionSchema: jsonSchema,
  },
}

scrapeResult, err := app.ScrapeURL("https://news.ycombinator.com", llmExtractionParams)
if err != nil {
  log.Fatalf("Failed to perform LLM extraction: %v", err)
}
fmt.Println(scrapeResult)

```

### [​](\#search-for-a-query)  Search for a query

To search the web, get the most relevant results, scrap each page and return the markdown, use the `Search` method. The method takes the query as a parameter and returns the search results.

Copy

```go
query := "What is firecrawl?"
searchResult, err := app.Search(query)
if err != nil {
  log.Fatalf("Failed to search: %v", err)
}
fmt.Println(searchResult)

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

[Node](/v0/sdks/node) [Rust](/v0/sdks/rust)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Scraping a URL](#scraping-a-url)
- [Crawling a Website](#crawling-a-website)
- [Checking Crawl Status](#checking-crawl-status)
- [Canceling a Crawl Job](#canceling-a-crawl-job)
- [Extracting structured data from a URL](#extracting-structured-data-from-a-url)
- [Search for a query](#search-for-a-query)
- [Error Handling](#error-handling)

