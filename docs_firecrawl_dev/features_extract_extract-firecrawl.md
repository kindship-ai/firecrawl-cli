---
source: undefined
title: Extract | Firecrawl
description: Extract structured data from pages via LLMs
language: en
crawl_date: 2024-11-21T17:20:42.044Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Features

LLM Extract

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

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

Python

Node

cURL

Copy

```python
from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')

class ExtractSchema(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

data = app.scrape_url('https://docs.firecrawl.dev/', {
    'formats': ['extract'],
    'extract': {
        'schema': ExtractSchema.model_json_schema(),
    }
})
print(data["extract"])

```

Output:

JSON

```json
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
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
    }
}

```

### [​](\#extracting-without-schema-new)  Extracting without schema (New)

You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

cURL

Copy

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev/",
      "formats": ["extract"],
      "extract": {
        "prompt": "Extract the company mission from the page."
      }
    }'

```

Output:

JSON

```json
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
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
    }
}

```

### [​](\#extract-object)  Extract object

The `extract` object accepts the following parameters:

- `schema`: The schema to use for the extraction.
- `systemPrompt`: The system prompt to use for the extraction.
- `prompt`: The prompt to use for the extraction without a schema.

[Map (Alpha)](/features/map) [Langchain](/integrations/langchain)

On this page

- [Scrape and extract structured data with Firecrawl](#scrape-and-extract-structured-data-with-firecrawl)
- [Extract structured data](#extract-structured-data)
- [/scrape (with extract) endpoint](#scrape-with-extract-endpoint)
- [Extracting without schema (New)](#extracting-without-schema-new)
- [Extract object](#extract-object)

