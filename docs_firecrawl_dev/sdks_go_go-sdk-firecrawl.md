---
source: undefined
title: Go SDK | Firecrawl
description: Firecrawl Go SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
language: en
crawl_date: 2024-11-21T17:20:42.088Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Go

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#installation)  Installation

To install the Firecrawl Go SDK, you can use go get:

Go

Copy

```bash
go get github.com/mendableai/firecrawl-go

```

## [​](\#usage)  Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the `API key` as a parameter to the `FirecrawlApp` struct.
3. Set the `API URL` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `https://api.firecrawl.dev`.
4. Set the `version` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `v1`.

Here’s an example of how to use the SDK with error handling:

Go

Copy

```go
import (
	"fmt"
	"log"
	"github.com/google/uuid"
	"github.com/mendableai/firecrawl-go"
)

func ptr[T any](v T) *T {
	return &v
}

func main() {
	// Initialize the FirecrawlApp with your API key
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
	}

  // Scrape a website
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("Failed to send scrape request: %v", err)
  }

  fmt.Println(scrapeStatus)

	// Crawl a website
  idempotencyKey := uuid.New().String() // optional idempotency key
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Failed to send crawl request: %v", err)
	}

	fmt.Println(crawlStatus)
}

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

Go

Copy

```go
// Scrape a website
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("Failed to scrape URL: %v", err)
}

fmt.Println(scrapeResult)

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Go

Copy

```go
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("Failed to send crawl request: %v", err)
}

fmt.Println(crawlStatus)

```

### [​](\#checking-crawl-status)  Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.

Go

Copy

```go
// Get crawl status
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("Failed to get crawl status: %v", err)
}

fmt.Println(crawlStatus)

```

### [​](\#map-a-website)  Map a Website

Use `MapUrl` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.

Go

Copy

```go
// Map a website
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("Failed to map URL: %v", err)
}

fmt.Println(mapResult)

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

[Node](/sdks/node) [Rust](/sdks/rust)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Scraping a URL](#scraping-a-url)
- [Crawling a Website](#crawling-a-website)
- [Checking Crawl Status](#checking-crawl-status)
- [Map a Website](#map-a-website)
- [Error Handling](#error-handling)

