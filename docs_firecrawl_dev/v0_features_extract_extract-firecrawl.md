---
source: undefined
title: Extract | Firecrawl
description: Extract structured data from pages via LLMs
language: en
crawl_date: 2024-11-21T17:20:45.291Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Features

LLM Extract

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

## [​](\#scrape-and-extract-structured-data-with-firecrawl)  Scrape and extract structured data with Firecrawl

Firecrawl leverages Large Language Models (LLMs) to efficiently extract structured data from web pages. Here’s how:

1. **Schema Definition:**
Define the URL to scrape and the desired data schema using JSON Schema (following OpenAI tool schema). This schema specifies the data structure you expect to extract from the page.

2. **Scrape Endpoint:**
Pass the URL and the schema to the scrape endpoint. Documentation for this endpoint can be found here:
[Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)

3. **Structured Data Retrieval:**
Receive the scraped data in the structured format defined by your schema. You can then use this data as needed in your application or for further processing.


This method streamlines data extraction, reducing manual handling and enhancing efficiency.

## [​](\#extract-structured-data)  Extract structured data

### [​](\#scrape-with-extract-endpoint)  /scrape (with extract) endpoint

Used to extract structured data from scraped pages.

```bash
curl -X POST https://api.firecrawl.dev/v0/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev/",
      "extractorOptions": {
        "mode": "llm-extraction",
        "extractionPrompt": "Based on the information on the page, extract the information from the schema. ",
        "extractionSchema": {
          "type": "object",
          "properties": {
            "company_mission": {
                      "type": "string"
            },
            "supports_sso": {
                      "type": "boolean"
            },
            "is_open_source": {
                      "type": "boolean"
            },
            "is_in_yc": {
                      "type": "boolean"
            }
          },
          "required": [\
            "company_mission",\
            "supports_sso",\
            "is_open_source",\
            "is_in_yc"\
          ]
        }
      }
    }'

```

```json
{
    "success": true,
    "data": {
      "content": "Raw Content",
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
      "llm_extraction": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      }
    }
}

```

### [​](\#using-python-sdk)  Using Python SDK

```python
from firecrawl import FirecrawlApp

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key', version='v0')

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

### [​](\#with-javascript-sdk)  With JavaScript SDK

```js
import FirecrawlApp from "@mendable/firecrawl-js";
import { z } from "zod";

const app = new FirecrawlApp({
  apiKey: "fc-YOUR_API_KEY",
  version: "v0"
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

const scrapeResult = await app.scrapeUrl("https://news.ycombinator.com", {
  extractorOptions: { extractionSchema: schema },
});

console.log(scrapeResult.data["llm_extraction"]);

```

### [​](\#with-go-sdk)  With Go SDK

Go

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
}

```

### [​](\#with-rust-sdk)  With Rust SDK

Rust

```rust
use firecrawl::FirecrawlApp;

#[tokio::main]
async fn main() {
    // Initialize the FirecrawlApp with the API key
    let api_key = "YOUR_API_KEY";
    let api_url = "https://api.firecrawl.dev";
    let app = FirecrawlApp::new(api_key, api_url).expect("Failed to initialize FirecrawlApp");

    // Define schema to extract contents into
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
            "extractionSchema": json_schema,
            "mode": "llm-extraction"
        },
        "pageOptions": {
            "onlyMainContent": true
        }
    });

    let llm_extraction_result = app
        .scrape_url("https://news.ycombinator.com", Some(llm_extraction_params))
        .await;
    match llm_extraction_result {
        Ok(data) => println!("LLM Extraction Result:\n{}", data["llm_extraction"]),
        Err(e) => eprintln!("LLM Extraction failed: {}", e),
    }
}

```

[Crawl](/v0/features/crawl) [Search](/features/search)

On this page

- [Scrape and extract structured data with Firecrawl](#scrape-and-extract-structured-data-with-firecrawl)
- [Extract structured data](#extract-structured-data)
- [/scrape (with extract) endpoint](#scrape-with-extract-endpoint)
- [Using Python SDK](#using-python-sdk)
- [With JavaScript SDK](#with-javascript-sdk)
- [With Go SDK](#with-go-sdk)
- [With Rust SDK](#with-rust-sdk)

