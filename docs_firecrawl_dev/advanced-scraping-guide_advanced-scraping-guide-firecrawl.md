---
source: undefined
title: Advanced Scraping Guide | Firecrawl
description: Learn how to improve your Firecrawl scraping with advanced options.
language: en
crawl_date: 2024-11-21T17:20:42.038Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Get Started

Advanced Scraping Guide

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

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

## [​](\#scraping-pdfs)  Scraping PDFs

**Firecrawl supports scraping PDFs by default.** You can use the `/scrape` endpoint to scrape a PDF link and get the text content of the PDF. You can disable this by setting `parsePDF` to `false`.

## [​](\#scrape-options)  Scrape Options

When using the `/scrape` endpoint, you can customize the scraping behavior with many parameters. Here are the available options:

### [​](\#setting-the-content-formats-on-response-with-formats)  Setting the content formats on response with `formats`

- **Type**: `array`
- **Enum**: `["markdown", "links", "html", "rawHtml", "screenshot"]`
- **Description**: Specify the formats to include in the response. Options include:

  - `markdown`: Returns the scraped content in Markdown format.
  - `links`: Includes all hyperlinks found on the page.
  - `html`: Provides the content in HTML format.
  - `rawHtml`: Delivers the raw HTML content, without any processing.
  - `screenshot`: Includes a screenshot of the page as it appears in the browser.
  - `extract`: Extracts structured information from the page using the LLM.
- **Default**: `["markdown"]`

### [​](\#getting-the-full-page-content-as-markdown-with-onlymaincontent)  Getting the full page content as markdown with `onlyMainContent`

- **Type**: `boolean`
- **Description**: By default, the scraper will only return the main content of the page, excluding headers, navigation bars, footers, etc. Set this to `false` to return the full page content.
- **Default**: `true`

### [​](\#setting-the-tags-to-include-with-includetags)  Setting the tags to include with `includeTags`

- **Type**: `array`
- **Description**: Specify the HTML tags, classes and ids to include in the response.
- **Default**: undefined

### [​](\#setting-the-tags-to-exclude-with-excludetags)  Setting the tags to exclude with `excludeTags`

- **Type**: `array`
- **Description**: Specify the HTML tags, classes and ids to exclude from the response.
- **Default**: undefined

### [​](\#waiting-for-the-page-to-load-with-waitfor)  Waiting for the page to load with `waitFor`

- **Type**: `integer`
- **Description**: To be used only as a last resort. Wait for a specified amount of milliseconds for the page to load before fetching content.
- **Default**: `0`

### [​](\#setting-the-maximum-timeout)  Setting the maximum `timeout`

- **Type**: `integer`
- **Description**: Set the maximum duration in milliseconds that the scraper will wait for the page to respond before aborting the operation.
- **Default**: `30000` (30 seconds)

### [​](\#example-usage)  Example Usage

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
    -H '
    Content-Type: application/json' \
    -H 'Authorization : Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats": ["markdown", "links", "html", "rawHtml", "screenshot"],
      "includeTags": ["h1", "p", "a", ".main-content"],
      "excludeTags": ["#ad", "#footer"],
      "onlyMainContent": false,
      "waitFor": 1000,
      "timeout": 15000
    }'

```

In this example, the scraper will:

- Return the full page content as markdown.
- Include the markdown, raw HTML, HTML, links and screenshot in the response.
- The response will include only the HTML tags `<h1>`, `<p>`, `<a>`, and elements with the class `.main-content`, while excluding any elements with the IDs `#ad` and `#footer`.
- Wait for 1000 milliseconds (1 second) for the page to load before fetching the content.
- Set the maximum duration of the scrape request to 15000 milliseconds (15 seconds).

Here is the API Reference for it: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)

## [​](\#extractor-options)  Extractor Options

When using the `/scrape` endpoint, you can specify options for **extracting structured information** from the page content using the `extract` parameter. Here are the available options:

### [​](\#using-the-llm-extraction)  Using the LLM Extraction

### [​](\#schema)  schema

- **Type**: `object`
- **Required**: False if prompt is provided
- **Description**: The schema for the data to be extracted. This defines the structure of the extracted data.

### [​](\#system-prompt)  system prompt

- **Type**: `string`
- **Required**: False
- **Description**: System prompt for the LLM.

### [​](\#prompt)  prompt

- **Type**: `string`
- **Required**: False if schema is provided
- **Description**: A prompt for the LLM to extract the data in the correct structure.
- **Example**: `"Extract the features of the product"`

### [​](\#example-usage-2)  Example Usage

```bash
curl -X POST https://api.firecrawl.dev/v0/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["markdown", "extract"],
      "extract": {
        "prompt": "Extract the features of the product"
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
      "sourceURL": "https://docs.firecrawl.dev/",
      "statusCode": 200
    },
    "extract": {
      "product": "Firecrawl",
      "features": {
        "general": {
          "description": "Turn websites into LLM-ready data.",
          "openSource": true,
          "freeCredits": 500,
          "useCases": [\
            "AI applications",\
            "Data science",\
            "Market research",\
            "Content aggregation"\
          ]
        },
        "crawlingAndScraping": {
          "crawlAllAccessiblePages": true,
          "noSitemapRequired": true,
          "dynamicContentHandling": true,
          "dataCleanliness": {
            "process": "Advanced algorithms",
            "outputFormat": "Markdown"
          }
        },
        ...
      }
    }
  }
}

```

## [​](\#actions)  Actions

When using the `/scrape` endpoint, Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

### [​](\#available-actions)  Available Actions

#### [​](\#wait)  wait

- **Type**: `object`
- **Description**: Wait for a specified amount of milliseconds.
- **Properties**:

  - `type`: `"wait"`
  - `milliseconds`: Number of milliseconds to wait.
- **Example**:







```json
{
    "type": "wait",
    "milliseconds": 2000
}

```


#### [​](\#screenshot)  screenshot

- **Type**: `object`
- **Description**: Take a screenshot.
- **Properties**:

  - `type`: `"screenshot"`
  - `fullPage`: Should the screenshot be full-page or viewport sized? (default: `false`)
- **Example**:







```json
{
    "type": "screenshot",
    "fullPage": true
}

```


#### [​](\#click)  click

- **Type**: `object`
- **Description**: Click on an element.
- **Properties**:

  - `type`: `"click"`
  - `selector`: Query selector to find the element by.
- **Example**:







```json
{
    "type": "click",
    "selector": "#load-more-button"
}

```


#### [​](\#write)  write

- **Type**: `object`
- **Description**: Write text into an input field.
- **Properties**:

  - `type`: `"write"`
  - `text`: Text to type.
  - `selector`: Query selector for the input field.
- **Example**:







```json
{
    "type": "write",
    "text": "Hello, world!",
    "selector": "#search-input"
}

```


#### [​](\#press)  press

- **Type**: `object`
- **Description**: Press a key on the page.
- **Properties**:

  - `type`: `"press"`
  - `key`: Key to press.
- **Example**:







```json
{
    "type": "press",
    "key": "Enter"
}

```


#### [​](\#scroll)  scroll

- **Type**: `object`
- **Description**: Scroll the page.
- **Properties**:

  - `type`: `"scroll"`
  - `direction`: Direction to scroll ( `"up"` or `"down"`).
  - `amount`: Amount to scroll in pixels.
- **Example**:







```json
{
    "type": "scroll",
    "direction": "down",
    "amount": 500
}

```


For more details about the actions parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## [​](\#crawling-multiple-pages)  Crawling Multiple Pages

To crawl multiple pages, you can use the `/crawl` endpoint. This endpoint allows you to specify a base URL you want to crawl and all accessible subpages will be crawled.

```bash
curl -X POST https://api.firecrawl.dev/v1/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'

```

Returns a id

```json
{ "id": "1234-5678-9101" }

```

### [​](\#check-crawl-job)  Check Crawl Job

Used to check the status of a crawl job and get its result.

```bash
curl -X GET https://api.firecrawl.dev/v1/crawl/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY'

```

#### [​](\#pagination-next-url)  Pagination/Next URL

If the content is larger than 10MB or if the crawl job is still running, the response will include a `next` parameter. This parameter is a URL to the next page of results. You can use this parameter to get the next page of results.

### [​](\#crawler-options)  Crawler Options

When using the `/crawl` endpoint, you can customize the crawling behavior with request body parameters. Here are the available options:

#### [​](\#includepaths)  `includePaths`

- **Type**: `array`
- **Description**: URL patterns to include in the crawl. Only URLs matching these patterns will be crawled.
- **Example**: `["/blog/*", "/products/*"]`

#### [​](\#excludepaths)  `excludePaths`

- **Type**: `array`
- **Description**: URL patterns to exclude from the crawl. URLs matching these patterns will be skipped.
- **Example**: `["/admin/*", "/login/*"]`

#### [​](\#maxdepth)  `maxDepth`

- **Type**: `integer`
- **Description**: Maximum depth to crawl relative to the entered URL. A maxDepth of 0 scrapes only the entered URL. A maxDepth of 1 scrapes the entered URL and all pages one level deep. A maxDepth of 2 scrapes the entered URL and all pages up to two levels deep. Higher values follow the same pattern.
- **Example**: `2`

#### [​](\#limit)  `limit`

- **Type**: `integer`
- **Description**: Maximum number of pages to crawl.
- **Default**: `10000`

#### [​](\#allowbackwardlinks)  `allowBackwardLinks`

- **Type**: `boolean`
- **Description**: This option permits the crawler to navigate to URLs that are higher in the directory structure than the base URL. For instance, if the base URL is `example.com/blog/topic`, enabling this option allows crawling to pages like `example.com/blog` or `example.com`, which are backward in the path hierarchy relative to the base URL.
- **Default**: `false`

### [​](\#allowexternallinks)  `allowExternalLinks`

- **Type**: `boolean`
- **Description**: This option allows the crawler to follow links that point to external domains. Be careful with this option, as it can cause the crawl to stop only based only on the `limit` and `maxDepth` values.
- **Default**: `false`

#### [​](\#scrapeoptions)  scrapeOptions

As part of the crawler options, you can also specify the `scrapeOptions` parameter. This parameter allows you to customize the scraping behavior for each page.

- **Type**: `object`
- **Description**: Options for the scraper.
- **Example**: `{"formats": ["markdown", "links", "html", "rawHtml", "screenshot"], "includeTags": ["h1", "p", "a", ".main-content"], "excludeTags": ["#ad", "#footer"], "onlyMainContent": false, "waitFor": 1000, "timeout": 15000}`
- **Default**: `{ "formats": ["markdown"] }`
- **See**: [Scrape Options](/advanced-scraping-guide#setting-the-content-formats-on-response-with-formats)

### [​](\#example-usage-3)  Example Usage

```bash
curl -X POST https://api.firecrawl.dev/v1/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization : Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "includePaths": ["/blog/*", "/products/*"],
      "excludePaths": ["/admin/*", "/login/*"],
      "maxDepth": 2,
      "limit": 1000
    }'

```

In this example, the crawler will:

- Only crawl URLs that match the patterns `/blog/*` and `/products/*`.
- Skip URLs that match the patterns `/admin/*` and `/login/*`.
- Return the full document data for each page.
- Crawl up to a maximum depth of 2.
- Crawl a maximum of 1000 pages.

## [​](\#mapping-website-links-with-map)  Mapping Website Links with `/map`

The `/map` endpoint is adept at identifying URLs that are contextually related to a given website. This feature is crucial for understanding a site’s contextual link environment, which can greatly aid in strategic site analysis and navigation planning.

### [​](\#usage)  Usage

To use the `/map` endpoint, you need to send a GET request with the URL of the page you want to map. Here is an example using `curl`:

```bash
curl -X POST https://api.firecrawl.dev/v1/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'

```

This will return a JSON object containing links contextually related to the url.

### [​](\#example-response)  Example Response

```json
  {
    "success":true,
    "links":[\
      "https://docs.firecrawl.dev",\
      "https://docs.firecrawl.dev/api-reference/endpoint/crawl-delete",\
      "https://docs.firecrawl.dev/api-reference/endpoint/crawl-get",\
      "https://docs.firecrawl.dev/api-reference/endpoint/crawl-post",\
      "https://docs.firecrawl.dev/api-reference/endpoint/map",\
      "https://docs.firecrawl.dev/api-reference/endpoint/scrape",\
      "https://docs.firecrawl.dev/api-reference/introduction",\
      "https://docs.firecrawl.dev/articles/search-announcement",\
      ...\
    ]
  }

```

### [​](\#map-options)  Map Options

- **Type**: `string`
- **Description**: Search for links containing specific text.
- **Example**: `"blog"`

#### [​](\#limit-2)  `limit`

- **Type**: `integer`
- **Description**: Maximum number of links to return.
- **Default**: `100`

#### [​](\#ignoresitemap)  `ignoreSitemap`

- **Type**: `boolean`
- **Description**: Ignore the website sitemap when crawling
- **Default**: `true`

#### [​](\#includesubdomains)  `includeSubdomains`

- **Type**: `boolean`
- **Description**: Include subdomains of the website
- **Default**: `false`

Here is the API Reference for it: [Map Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)

[Integrations](/integrations) [Scrape](/features/scrape)

On this page

- [Basic scraping with Firecrawl (/scrape)](#basic-scraping-with-firecrawl-scrape)
- [Scraping PDFs](#scraping-pdfs)
- [Scrape Options](#scrape-options)
- [Setting the content formats on response with formats](#setting-the-content-formats-on-response-with-formats)
- [Getting the full page content as markdown with onlyMainContent](#getting-the-full-page-content-as-markdown-with-onlymaincontent)
- [Setting the tags to include with includeTags](#setting-the-tags-to-include-with-includetags)
- [Setting the tags to exclude with excludeTags](#setting-the-tags-to-exclude-with-excludetags)
- [Waiting for the page to load with waitFor](#waiting-for-the-page-to-load-with-waitfor)
- [Setting the maximum timeout](#setting-the-maximum-timeout)
- [Example Usage](#example-usage)
- [Extractor Options](#extractor-options)
- [Using the LLM Extraction](#using-the-llm-extraction)
- [schema](#schema)
- [system prompt](#system-prompt)
- [prompt](#prompt)
- [Example Usage](#example-usage-2)
- [Actions](#actions)
- [Available Actions](#available-actions)
- [wait](#wait)
- [screenshot](#screenshot)
- [click](#click)
- [write](#write)
- [press](#press)
- [scroll](#scroll)
- [Crawling Multiple Pages](#crawling-multiple-pages)
- [Check Crawl Job](#check-crawl-job)
- [Pagination/Next URL](#pagination-next-url)
- [Crawler Options](#crawler-options)
- [includePaths](#includepaths)
- [excludePaths](#excludepaths)
- [maxDepth](#maxdepth)
- [limit](#limit)
- [allowBackwardLinks](#allowbackwardlinks)
- [allowExternalLinks](#allowexternallinks)
- [scrapeOptions](#scrapeoptions)
- [Example Usage](#example-usage-3)
- [Mapping Website Links with /map](#mapping-website-links-with-map)
- [Usage](#usage)
- [Example Response](#example-response)
- [Map Options](#map-options)
- [search](#search)
- [limit](#limit-2)
- [ignoreSitemap](#ignoresitemap)
- [includeSubdomains](#includesubdomains)

