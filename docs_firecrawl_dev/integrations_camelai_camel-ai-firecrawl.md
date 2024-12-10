---
source: undefined
title: Camel AI | Firecrawl
description: Firecrawl integrates with Camel AI as a data loader.
language: en
crawl_date: 2024-11-21T17:20:41.177Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Integrations

Camel AI

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#installation)  Installation

Copy

```bash
pip install camel-ai

```

## [​](\#usage)  Usage

With Camel AI and Firecrawl you can quickly build multi-agent systems than use data from the web.

### [​](\#using-firecrawl-to-gather-an-entire-website)  Using Firecrawl to Gather an Entire Website

Copy

```python
mock_app = MockFirecrawlApp.return_value
firecrawl = Firecrawl(
    api_key='FC_API_KEY', api_url='https://api.test.com'
)
url = 'https://example.com'
response = [{'markdown': 'Markdown content'}]
mock_app.crawl_url.return_value = respons
result = firecrawl.markdown_crawl(url)

```

### [​](\#using-firecrawl-to-gather-a-single-page)  Using Firecrawl to Gather a Single Page

Copy

```python
mock_app = MockFirecrawlApp.return_value
firecrawl = Firecrawl(
    api_key='test_api_key', api_url='https://api.test.com'
)
url = 'https://example.com'
response = 'Scraped content'
mock_app.scrape_url.return_value = response

result = firecrawl.scrape(url)

```

[Langflow](/integrations/langflow) [Open Source vs Cloud](/contributing/open-source-or-cloud)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Using Firecrawl to Gather an Entire Website](#using-firecrawl-to-gather-an-entire-website)
- [Using Firecrawl to Gather a Single Page](#using-firecrawl-to-gather-a-single-page)

