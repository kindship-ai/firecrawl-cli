---
source: undefined
title: Advanced Scraping Guide | Firecrawl
description: Learn how to improve your Firecrawl scraping with advanced options.
language: en
crawl_date: 2024-11-21T17:20:44.221Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Get Started

Advanced Scraping Guide

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

This guide will walk you through the different endpoints of Firecrawl and how to use them fully with all its parameters.

## [​](\#basic-scraping-with-firecrawl-scrape)  Basic scraping with Firecrawl (/scrape)

To scrape a single page and get clean markdown content, you can use the `/scrape` endpoint.

Python

JavaScript

Go

Rust

cURL

Copy

```python
# pip install firecrawl-py

from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="YOUR_API_KEY")

content = app.scrape_url("https://docs.firecrawl.dev")

```

## [​](\#scraping-pdfs)  Scraping pdfs

**Firecrawl supports scraping pdfs by default.** You can use the `/scrape` endpoint to scrape a pdf link and get the text content of the pdf. You can disable this by setting `pageOptions.parsePDF` to `false`.

## [​](\#page-options)  Page Options

When using the `/scrape` endpoint, you can customize the scraping behavior with the `pageOptions` parameter. Here are the available options:

### [​](\#getting-cleaner-content-with-onlymaincontent)  Getting cleaner content with `onlyMainContent`

- **Type**: `boolean`
- **Description**: Only return the main content of the page, excluding headers, navigation bars, footers, etc.
- **Default**: `false`

### [​](\#getting-the-html-with-includehtml)  Getting the HTML with `includeHtml`

- **Type**: `boolean`
- **Description**: Include the HTML version content of the page. This will add an `html` key in the response.
- **Default**: `false`

### [​](\#getting-the-raw-html-with-includerawhtml)  Getting the raw HTML with `includeRawHtml`

- **Type**: `boolean`
- **Description**: Include the raw HTML content of the page. This will add an `rawHtml` key in the response.
- **Default**: `false`

### [​](\#getting-a-screenshot-of-the-page-with-screenshot)  Getting a screenshot of the page with `screenshot`

- **Type**: `boolean`
- **Decription**: Include a screenshot of the top of the page that you are scraping.
- **Default**: `false`

### [​](\#waiting-for-the-page-to-load-with-waitfor)  Waiting for the page to load with `waitFor`

- **Type**: `integer`
- **Description**: To be used only as a last resort. Wait for a specified amount of milliseconds for the page to load before fetching content.
- **Default**: `0`

### [​](\#example-usage)  Example Usage

```bash
curl -X POST https://api.firecrawl.dev/v0/scrape \
    -H '
    Content-Type: application/json' \
    -H 'Authorization : Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "pageOptions": {
        "onlyMainContent": true,
        "includeHtml": true,
        "includeRawHtml":true,
        "screenshot": true,
        "waitFor": 5000
      }
    }'

```

In this example, the scraper will:

- Return only the main content of the page.
- Include the raw HTML content in the response in the `html` key.
- Wait for 5000 milliseconds (5 seconds) for the page to load before fetching the content.

Here is the API Reference for it: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)

## [​](\#extractor-options)  Extractor Options

When using the `/scrape` endpoint, you can specify options for **extracting structured information** from the page content using the `extractorOptions` parameter. Here are the available options:

### [​](\#mode)  mode

- **Type**: `string`

- **Enum**: `["llm-extraction", "llm-extraction-from-raw-html"]`

- **Description**: The extraction mode to use.
  - `llm-extraction`: Extracts information from the cleaned and parsed content.
  - `llm-extraction-from-raw-html`: Extracts information directly from the raw HTML.
- **Type**: `string`

- **Description**: A prompt describing what information to extract from the page.


### [​](\#extractionschema)  extractionSchema

- **Type**: `object`
- **Description**: The schema for the data to be extracted. This defines the structure of the extracted data.

### [​](\#example-usage-2)  Example Usage

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

## [​](\#adjusting-timeout)  Adjusting Timeout

You can adjust the timeout for the scraping process using the `timeout` parameter in milliseconds.

### [​](\#example-usage-3)  Example Usage

```bash
curl -X POST https://api.firecrawl.dev/v0/scrape \
    -H '
    Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "timeout": 50000
    }'

```

## [​](\#crawling-multiple-pages)  Crawling Multiple Pages

To crawl multiple pages, you can use the `/crawl` endpoint. This endpoint allows you to specify a base URL you want to crawl and all accessible subpages will be crawled.

```bash
curl -X POST https://api.firecrawl.dev/v0/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'

```

Returns a jobId

```json
{ "jobId": "1234-5678-9101" }

```

### [​](\#check-crawl-job)  Check Crawl Job

Used to check the status of a crawl job and get its result.

```bash
curl -X GET https://api.firecrawl.dev/v0/crawl/status/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY'

```

### [​](\#crawler-options)  Crawler Options

When using the `/crawl` endpoint, you can customize the crawling behavior with the `crawlerOptions` parameter. Here are the available options:

#### [​](\#includes)  `includes`

- **Type**: `array`
- **Description**: URL patterns to include in the crawl. Only URLs matching these patterns will be crawled.
- **Example**: `["/blog/*", "/products/*"]`

#### [​](\#excludes)  `excludes`

- **Type**: `array`
- **Description**: URL patterns to exclude from the crawl. URLs matching these patterns will be skipped.
- **Example**: `["/admin/*", "/login/*"]`

#### [​](\#returnonlyurls)  `returnOnlyUrls`

- **Type**: `boolean`
- **Description**: If set to `true`, the response will only include a list of URLs instead of the full document data.
- **Default**: `false`

#### [​](\#maxdepth)  `maxDepth`

- **Type**: `integer`
- **Description**: Maximum depth to crawl relative to the entered URL. A maxDepth of 0 scrapes only the entered URL. A maxDepth of 1 scrapes the entered URL and all pages one level deep. A maxDepth of 2 scrapes the entered URL and all pages up to two levels deep. Higher values follow the same pattern.
- **Example**: `2`

#### [​](\#mode-2)  `mode`

- **Type**: `string`
- **Enum**: `["default", "fast"]`
- **Description**: The crawling mode to use. `fast` mode crawls websites without a sitemap 4x faster but may be less accurate and is not recommended for heavily JavaScript-rendered websites.
- **Default**: `default`

#### [​](\#limit)  `limit`

- **Type**: `integer`
- **Description**: Maximum number of pages to crawl.
- **Default**: `10000`

### [​](\#example-usage-4)  Example Usage

```bash
curl -X POST https://api.firecrawl.dev/v0/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization : Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "crawlerOptions": {
        "includes": ["/blog/*", "/products/*"],
        "excludes": ["/admin/*", "/login/*"],
        "returnOnlyUrls": false,
        "maxDepth": 2,
        "mode": "fast",
        "limit": 1000
      }
    }'

```

In this example, the crawler will:

- Only crawl URLs that match the patterns `/blog/*` and `/products/*`.
- Skip URLs that match the patterns `/admin/*` and `/login/*`.
- Return the full document data for each page.
- Crawl up to a maximum depth of 2.
- Use the fast crawling mode.
- Crawl a maximum of 1000 pages.

## [​](\#page-options-crawler-options)  Page Options + Crawler Options

You can combine the `pageOptions` and `crawlerOptions` parameters to customize both the full crawling behavior.

### [​](\#example-usage-5)  Example Usage

```bash
curl -X POST https://api.firecrawl.dev/v0/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "pageOptions": {
        "onlyMainContent": true,
        "includeHtml": true,
        "includeRawHtml": true,
        "screenshot": true,
        "waitFor": 5000
      },
      "crawlerOptions": {
        "includes": ["/blog/*", "/products/*"],
        "maxDepth": 2,
        "mode": "fast",
      }
    }'

```

In this example, the crawler will:

- Return only the main content for each page.
- Include the raw HTML content for each page.
- Wait for 5000 milliseconds for each page to load before fetching its content.
- Only crawl URLs that match the patterns `/blog/*` and `/products/*`.
- Crawl up to a maximum depth of 2.
- Use the fast crawling mode.

## [​](\#extractor-options-crawler-options)  Extractor Options + Crawler Options

Coming soon…

[Quickstart](/v0/introduction) [Rate Limits](/rate-limits)

On this page

- [Basic scraping with Firecrawl (/scrape)](#basic-scraping-with-firecrawl-scrape)
- [Scraping pdfs](#scraping-pdfs)
- [Page Options](#page-options)
- [Getting cleaner content with onlyMainContent](#getting-cleaner-content-with-onlymaincontent)
- [Getting the HTML with includeHtml](#getting-the-html-with-includehtml)
- [Getting the raw HTML with includeRawHtml](#getting-the-raw-html-with-includerawhtml)
- [Getting a screenshot of the page with screenshot](#getting-a-screenshot-of-the-page-with-screenshot)
- [Waiting for the page to load with waitFor](#waiting-for-the-page-to-load-with-waitfor)
- [Example Usage](#example-usage)
- [Extractor Options](#extractor-options)
- [mode](#mode)
- [extractionSchema](#extractionschema)
- [Example Usage](#example-usage-2)
- [Adjusting Timeout](#adjusting-timeout)
- [Example Usage](#example-usage-3)
- [Crawling Multiple Pages](#crawling-multiple-pages)
- [Check Crawl Job](#check-crawl-job)
- [Crawler Options](#crawler-options)
- [includes](#includes)
- [excludes](#excludes)
- [returnOnlyUrls](#returnonlyurls)
- [maxDepth](#maxdepth)
- [mode](#mode-2)
- [limit](#limit)
- [Example Usage](#example-usage-4)
- [Page Options + Crawler Options](#page-options-crawler-options)
- [Example Usage](#example-usage-5)
- [Extractor Options + Crawler Options](#extractor-options-crawler-options)

