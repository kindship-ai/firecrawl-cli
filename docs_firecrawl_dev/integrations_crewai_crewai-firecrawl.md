---
source: undefined
title: CrewAI | Firecrawl
description: Learn how to use Firecrawl with CrewAI
language: en
crawl_date: 2024-11-21T17:20:41.150Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Integrations

CrewAI

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#using-firecrawl-with-crewai)  Using Firecrawl with CrewAI

Firecrawl is integrated with [CrewAI, the framework for orchestrating AI agents](https://www.crewai.com/). This page introduces all of the Firecrawl tools added to the framework.

### [​](\#installing-firecrawl-tools-inside-of-crewai)  Installing Firecrawl Tools inside of CrewAI

- Get an API key from your [firecrawl.dev dashboard](https://firecrawl.dev) and set it in environment variables ( `FIRECRAWL_API_KEY`).
- Install the [Firecrawl SDK](https://github.com/mendableai/firecrawl) along with `crewai[tools]` package:

Copy

```
pip install firecrawl-py 'crewai[tools]'

```

## [​](\#tools)  Tools

### [​](\#firecrawlcrawlwebsitetool)  FirecrawlCrawlWebsiteTool

#### [​](\#example)  Example

Utilize the FirecrawlScrapeFromWebsiteTool as follows to allow your agent to load websites:

Copy

```python
from crewai_tools import FirecrawlCrawlWebsiteTool

tool = FirecrawlCrawlWebsiteTool(url='firecrawl.dev')

```

#### [​](\#arguments)  Arguments

- `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
- `url`: The base URL to start crawling from.
- `page_options`: Optional.

  - `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  - `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
- `crawler_options`: Optional. Options for controlling the crawling behavior.

  - `includes`: Optional. URL patterns to include in the crawl.
  - `exclude`: Optional. URL patterns to exclude from the crawl.
  - `generateImgAltText`: Optional. Generate alt text for images using LLMs (requires a paid plan).
  - `returnOnlyUrls`: Optional. If true, returns only the URLs as a list in the crawl status. Note: the response will be a list of URLs inside the data, not a list of documents.
  - `maxDepth`: Optional. Maximum depth to crawl. Depth 1 is the base URL, depth 2 includes the base URL and its direct children, and so on.
  - `mode`: Optional. The crawling mode to use. Fast mode crawls 4x faster on websites without a sitemap but may not be as accurate and shouldn’t be used on heavily JavaScript-rendered websites.
  - `limit`: Optional. Maximum number of pages to crawl.
  - `timeout`: Optional. Timeout in milliseconds for the crawling operation.

### [​](\#firecrawlscrapewebsitetool)  FirecrawlScrapeWebsiteTool

#### [​](\#example-2)  Example

Utilize the FirecrawlScrapeWebsiteTool as follows to allow your agent to load websites:

Copy

```python
from crewai_tools import FirecrawlScrapeWebsiteTool

tool = FirecrawlScrapeWebsiteTool(url='firecrawl.dev')

```

#### [​](\#arguments-2)  Arguments

- `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
- `url`: The URL to scrape.
- `page_options`: Optional.

  - `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  - `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
- `extractor_options`: Optional. Options for LLM-based extraction of structured information from the page content

  - `mode`: The extraction mode to use, currently supports ‘llm-extraction’
  - `extractionPrompt`: Optional. A prompt describing what information to extract from the page
  - `extractionSchema`: Optional. The schema for the data to be extracted
- `timeout`: Optional. Timeout in milliseconds for the request

### [​](\#firecrawlsearchtool)  FirecrawlSearchTool

#### [​](\#example-3)  Example

Utilize the FirecrawlSearchTool as follows to allow your agent to load websites:

Copy

```python
from crewai_tools import FirecrawlSearchTool

tool = FirecrawlSearchTool(query='what is firecrawl?')

```

#### [​](\#arguments-3)  Arguments

- `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
- `query`: The search query string to be used for searching.
- `page_options`: Optional. Options for result formatting.

  - `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  - `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
  - `fetchPageContent`: Optional. Fetch the full content of the page.
- `search_options`: Optional. Options for controlling the crawling behavior.

  - `limit`: Optional. Maximum number of pages to crawl.

[Llamaindex](/integrations/llamaindex) [Dify](/integrations/dify)

On this page

- [Using Firecrawl with CrewAI](#using-firecrawl-with-crewai)
- [Installing Firecrawl Tools inside of CrewAI](#installing-firecrawl-tools-inside-of-crewai)
- [Tools](#tools)
- [FirecrawlCrawlWebsiteTool](#firecrawlcrawlwebsitetool)
- [Example](#example)
- [Arguments](#arguments)
- [FirecrawlScrapeWebsiteTool](#firecrawlscrapewebsitetool)
- [Example](#example-2)
- [Arguments](#arguments-2)
- [FirecrawlSearchTool](#firecrawlsearchtool)
- [Example](#example-3)
- [Arguments](#arguments-3)

