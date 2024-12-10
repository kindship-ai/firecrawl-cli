---
source: undefined
title: Rust SDK | Firecrawl
description: Firecrawl Rust SDK is a library to help you easily scrape and crawl websites, and output the data in a format ready for use with language models (LLMs).
language: en
crawl_date: 2024-11-21T17:20:43.136Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

SDKs

Rust

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#installation)  Installation

To install the Firecrawl Rust SDK, add the following to your `Cargo.toml`:

Rust

Copy

```yaml
# Add this to your Cargo.toml
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }

```

## [​](\#usage)  Usage

First, you need to obtain an API key from [firecrawl.dev](https://firecrawl.dev). Then, you need to initialize the `FirecrawlApp`. From there, you can access functions like `FirecrawlApp::scrape_url`, which let you use our API.

Here’s an example of how to use the SDK in Rust:

Rust

Copy

```rust
use firecrawl::{crawl::{CrawlOptions, CrawlScrapeOptions, CrawlScrapeFormats}, FirecrawlApp, scrape::{ScrapeOptions, ScrapeFormats}};

#[tokio::main]
async fn main() {
    // Initialize the FirecrawlApp with the API key
    let app = FirecrawlApp::new("fc-YOUR_API_KEY").expect("Failed to initialize FirecrawlApp");

    // Scrape a URL
    let options = ScrapeOptions {
        formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
        ..Default::default()
    };

    let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

    match scrape_result {
        Ok(data) => println!("Scrape Result:\n{}", data.markdown.unwrap()),
        Err(e) => eprintln!("Map failed: {}", e),
    }

    // Crawl a website
    let crawl_options = CrawlOptions {
        scrape_options: CrawlScrapeOptions {
            formats: vec![ CrawlScrapeFormats::Markdown, CrawlScrapeFormats::HTML ].into(),
            ..Default::default()
        }.into(),
        limit: 100.into(),
        ..Default::default()
    };

    let crawl_result = app
        .crawl_url("https://mendable.ai", crawl_options)
        .await;

    match crawl_result {
        Ok(data) => println!("Crawl Result (used {} credits):\n{:#?}", data.credits_used, data.data),
        Err(e) => eprintln!("Crawl failed: {}", e),
    }
}

```

### [​](\#scraping-a-url)  Scraping a URL

To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a `Document`.

Rust

Copy

```rust
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("Scrape Result:\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("Map failed: {}", e),
}

```

### [​](\#scraping-with-extract)  Scraping with Extract

With Extract, you can easily extract structured data from any URL. You need to specify your schema in the JSON Schema format, using the `serde_json::json!` macro.

Rust

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

let llm_extraction_options = ScrapeOptions {
    formats: vec![ ScrapeFormats::Extract ].into(),
    extract: ExtractOptions {
        schema: json_schema.into(),
        ..Default::default()
    }.into(),
    ..Default::default()
};

let llm_extraction_result = app
    .scrape_url("https://news.ycombinator.com", llm_extraction_options)
    .await;

match llm_extraction_result {
    Ok(data) => println!("LLM Extraction Result:\n{:#?}", data.extract.unwrap()),
    Err(e) => eprintln!("LLM Extraction failed: {}", e),
}

```

### [​](\#crawling-a-website)  Crawling a Website

To crawl a website, use the `crawl_url` method. This will wait for the crawl to complete, which may take a long time based on your starting URL and your options.

Rust

Copy

```rust
let crawl_options = CrawlOptions {
    scrape_options: CrawlScrapeOptions {
        formats: vec![ CrawlScrapeFormats::Markdown, CrawlScrapeFormats::HTML ].into(),
        ..Default::default()
    }.into(),
    limit: 100.into(),
    ..Default::default()
};

let crawl_result = app
    .crawl_url("https://mendable.ai", crawl_options)
    .await;

match crawl_result {
    Ok(data) => println!("Crawl Result (used {} credits):\n{:#?}", data.credits_used, data.data),
    Err(e) => eprintln!("Crawl failed: {}", e),
}

```

#### [​](\#crawling-asynchronously)  Crawling asynchronously

To crawl without waiting for the result, use the `crawl_url_async` method. It takes the same parameters, but it returns a `CrawlAsyncRespone` struct, containing the crawl’s ID. You can use that ID with the `check_crawl_status` method to check the status at any time. Do note that completed crawls are deleted after 24 hours.

Rust

Copy

```rust
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... later ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("Crawl is done: {:#?}", status.data);
} else {
    // ... wait some more ...
}

```

### [​](\#map-a-url-alpha)  Map a URL (Alpha)

Map all associated links from a starting URL.

Rust

Copy

```rust
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("Mapped URLs: {:#?}", data),
    Err(e) => eprintln!("Map failed: {}", e),
}

```

## [​](\#error-handling)  Error Handling

The SDK handles errors returned by the Firecrawl API and by our dependencies, and combines them into the `FirecrawlError` enum, implementing `Error`, `Debug` and `Display`. All of our methods return a `Result<T, FirecrawlError>`.

[Go](/sdks/go)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Scraping a URL](#scraping-a-url)
- [Scraping with Extract](#scraping-with-extract)
- [Crawling a Website](#crawling-a-website)
- [Crawling asynchronously](#crawling-asynchronously)
- [Map a URL (Alpha)](#map-a-url-alpha)
- [Error Handling](#error-handling)

