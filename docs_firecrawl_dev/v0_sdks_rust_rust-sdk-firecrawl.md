---
source: undefined
title: Rust SDK | Firecrawl
description: Firecrawl Rust SDK is a library to help you easily scrape and crawl websites, and output the data in a format ready for use with language models (LLMs).
language: en
crawl_date: 2024-11-21T17:20:45.327Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Rust

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

> Note: this is using [v0 version of the Firecrawl API](/v0/introduction) which is being deprecated. We recommend switching to [v1](/sdks/rust).

## [​](\#installation)  Installation

To install the Firecrawl Rust SDK, add the following to your `Cargo.toml`:

Copy

```toml
[dependencies]
firecrawl = "^0.1"
tokio = { version = "^1", features = ["full"] }
serde = { version = "^1.0", features = ["derive"] }
serde_json = "^1.0"
uuid = { version = "^1.10", features = ["v4"] }

[build-dependencies]
tokio = { version = "1", features = ["full"] }

```

## [​](\#usage)  Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` struct.

Here’s an example of how to use the SDK in Rust:

Copy

```rust
use firecrawl::FirecrawlApp;

#[tokio::main]
async fn main() {
  let api_key = "YOUR_API_KEY";
  let api_url = "https://api.firecrawl.dev";
  let app = FirecrawlApp::new(api_key, api_url).expect("Failed to initialize FirecrawlApp");

  // Scrape a single URL
  let scrape_result = app.scrape_url("https://docs.firecrawl.dev", None).await;
  match scrape_result {
    Ok(data) => println!("Scraped Data: {}", data),
    Err(e) => eprintln!("Error occurred while scraping: {}", e),
  }
  // Crawl a website
  let crawl_params = json!({
    "pageOptions": {
      "onlyMainContent": true
    }
  });

  let crawl_result = app.crawl_url("https://docs.firecrawl.dev", Some(crawl_params)).await;

  match crawl_result {
    Ok(data) => println!("Crawl Result: {}", data),
    Err(e) => eprintln!("Error occurred while crawling: {}", e),
  }
}

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL with error handling, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a `serde_json::Value`.

Copy

```rust
let scrape_result = app.scrape_url("https://docs.firecrawl.dev", None).await;

match scrape_result {
  Ok(data) => println!("Scraped Data: {}", data),
  Err(e) => eprintln!("Failed to scrape URL: {}", e),
}

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website, use the `crawl_url` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

Copy

```rust
let crawl_params = json!({
  "crawlerOptions": {
    "excludes": ["blog/"],
    "includes": [], // leave empty for all pages
    "limit": 1000
  },
  "pageOptions": {
    "onlyMainContent": true
  }
});
let crawl_result = app.crawl_url("https://docs.firecrawl.dev", Some(crawl_params)).await;

match crawl_result {
  Ok(data) => println!("Crawl Result: {}", data),
  Err(e) => eprintln!("Failed to crawl URL: {}", e),
}

```

### [​](\#checking-crawl-status)  Checking Crawl Status

To check the status of a crawl job, use the `check_crawl_status` method. It takes the job ID as a parameter and returns the current status of the crawl job.

Copy

```rust
let job_id = "your_job_id_here";
let status = app.check_crawl_status(job_id).await;

match status {
  Ok(data) => println!("Crawl Status: {}", data),
  Err(e) => eprintln!("Failed to check crawl status: {}", e),
}

```

### [​](\#canceling-a-crawl-job)  Canceling a Crawl Job

To cancel a crawl job, use the `cancel_crawl_job` method. It takes the job ID as a parameter and returns the cancellation status of the crawl job.

Copy

```rust
let job_id = "your_job_id_here";
let canceled = app.cancel_crawl_job(job_id).await;

match canceled {
  Ok(status) => println!("Cancellation Status: {}", status),
  Err(e) => eprintln!("Failed to cancel crawl job: {}", e),
}

```

### [​](\#extracting-structured-data-from-a-url)  Extracting structured data from a URL

With LLM extraction, you can easily extract structured data from any URL. Here is how you to use it:

Copy

```rust
let json_schema = json!({
  "type": "object",
  "properties": {
    "top": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
        "title": {"type": "string"},
        "points": {"type": "number"},
        "by": {"type": "string"},
        "commentsURL": {"type": "string"}
      },
      "required": ["title", "points", "by", "commentsURL"]
      },
      "minItems": 5,
      "maxItems": 5,
      "description": "Top 5 stories on Hacker News"
    }
  },
  "required": ["top"]
});

let llm_extraction_params = json!({
  "extractorOptions": {
    "extractionSchema": json_schema
  }
});

let scrape_result = app.scrape_url("https://news.ycombinator.com", Some(llm_extraction_params)).await;

match scrape_result {
  Ok(data) => println!("LLM Extraction Result: {}", data),
  Err(e) => eprintln!("Failed to perform LLM extraction: {}", e),
}

```

### [​](\#search-for-a-query)  Search for a query

To search the web, get the most relevant results, scrape each page and return the markdown, use the `search` method. The method takes the query as a parameter and returns the search results.

Copy

```rust
let query = "What is firecrawl?";
let search_result = app.search(query).await;

match search_result {
  Ok(data) => println!("Search Result: {}", data),
  Err(e) => eprintln!("Failed to search: {}", e),
}

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

[Go](/v0/sdks/go)

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

