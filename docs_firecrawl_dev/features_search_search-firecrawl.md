---
source: undefined
title: Search | Firecrawl
description: Make a serp request, and get all the content with a single API request
language: en
crawl_date: 2024-11-21T17:20:44.231Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Features

Search

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

## [​](\#searching-the-web-and-scraping-the-results-with-firecrawl)  Searching the web and scraping the results with Firecrawl

Firecrawl integrates its SERP (Search Engine Results Page) API with its robust scraping infrastructure to provide a seamless search and scrape functionality through a single endpoint. Here’s why:

1. **Unified Search Query:**
Users submit a search query via the SERP endpoint.

2. **Automated Result Scraping:**
Firecrawl automatically processes the search results and utilizes its scraping capabilities to extract data from each result page.

3. **Data Delivery:**
The scraped data from all result pages is compiled and delivered in a clean markdown - ready to use.


This integration allows users to efficiently perform web searches and obtain comprehensive, scraped data from multiple sources with minimal effort.

For more details, refer to the [Search Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/search).

## [​](\#search-any-query)  Search any query

### [​](\#search-endpoint)  /search endpoint

Used to search the web, get the most relevant results, scrape each page and return the markdown.

```bash
curl -X POST https://api.firecrawl.dev/v0/search \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "query": "firecrawl",
      "pageOptions": {
        "fetchPageContent": true // false for a fast serp api
      }
    }'

```

```json
{
  "success": true,
  "data": [\
    {\
      "url": "https://docs.firecrawl.dev",\
      "markdown": "# Markdown Content",\
      "provider": "web-scraper",\
      "metadata": {\
        "title": "Firecrawl | Scrape the web reliably for your LLMs",\
        "description": "AI for CX and Sales",\
        "language": null,\
        "sourceURL": "https://docs.firecrawl.dev/"\
      }\
    }\
  ]
}

```

### [​](\#with-python-sdk)  With Python SDK

#### [​](\#installing-python-sdk)  Installing Python SDK

```bash
pip install firecrawl-py

```

#### [​](\#search-a-query)  Search a query

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="YOUR_API_KEY")

result = app.search(query="What is firecrawl?")

```

The response will be similar to the one shown in the curl command above.

### [​](\#with-javascript-sdk)  With JavaScript SDK

#### [​](\#installing-javascript-sdk)  Installing JavaScript SDK

```bash
npm install @mendable/firecrawl-js

```

#### [​](\#search-a-query-2)  Search a query

```javascript
import FirecrawlApp from '@mendable/firecrawl-js';

// Initialize the FirecrawlApp with your API key
const app = new FirecrawlApp({ apiKey: 'YOUR_API_KEY' });

// Perform a search
const result = await app.search('What is firecrawl?');

```

The response will be similar to the one shown in the curl command above.

### [​](\#with-go-sdk)  With Go SDK

#### [​](\#installing-go-sdk)  Installing Go SDK

```bash
go get github.com/mendableai/firecrawl-go

```

#### [​](\#search-a-query-3)  Search a query

```go
import (
  "fmt"
  "log"

  "github.com/mendableai/firecrawl-go"
)

func main() {
  app, err := firecrawl.NewFirecrawlApp("YOUR_API_KEY")
  if err != nil {
      log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
  }

  query := "What is firecrawl?"
  searchResult, err := app.Search(query)
  if err != nil {
    log.Fatalf("Failed to search: %v", err)
  }
  fmt.Println(searchResult)
}

```

### [​](\#with-rust-sdk)  With Rust SDK

#### [​](\#installing-rust-sdk)  Installing Rust SDK

Add the following to your `Cargo.toml`:

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

#### [​](\#search-a-query-4)  Search a query

```rust
async fn main() {
  let api_key = "YOUR_API_KEY";
  let api_url = "https://api.firecrawl.dev";
  let app = FirecrawlApp::new(api_key, api_url).expect("Failed to initialize FirecrawlApp");

  let query = "What is firecrawl?";
  let search_result = app.search(query).await;

  match search_result {
    Ok(data) => println!("Search Result: {}", data),
    Err(e) => eprintln!("Failed to search: {}", e),
  }
}

```

[LLM Extract](/v0/features/extract) [Langchain](/integrations/langchain)

On this page

- [Searching the web and scraping the results with Firecrawl](#searching-the-web-and-scraping-the-results-with-firecrawl)
- [Search any query](#search-any-query)
- [/search endpoint](#search-endpoint)
- [With Python SDK](#with-python-sdk)
- [Installing Python SDK](#installing-python-sdk)
- [Search a query](#search-a-query)
- [With JavaScript SDK](#with-javascript-sdk)
- [Installing JavaScript SDK](#installing-javascript-sdk)
- [Search a query](#search-a-query-2)
- [With Go SDK](#with-go-sdk)
- [Installing Go SDK](#installing-go-sdk)
- [Search a query](#search-a-query-3)
- [With Rust SDK](#with-rust-sdk)
- [Installing Rust SDK](#installing-rust-sdk)
- [Search a query](#search-a-query-4)

