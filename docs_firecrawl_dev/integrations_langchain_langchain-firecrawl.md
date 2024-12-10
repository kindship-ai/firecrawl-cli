---
source: undefined
title: Langchain | Firecrawl
description: Firecrawl integrates with Langchain as a document loader.
language: en
crawl_date: 2024-11-21T17:20:42.055Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Integrations

Langchain

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

> Note: this integration is still using [v0 version of the Firecrawl API](/v0/introduction). You can install the 0.0.20 version for the Python SDK or the 0.0.36 for the Node SDK.

## [​](\#installation)  Installation

Copy

```bash
pip install firecrawl-py==0.0.20

```

## [​](\#usage)  Usage

You will need to get your own API key. See [https://firecrawl.dev](https://firecrawl.dev)

Copy

```python
from langchain_community.document_loaders import FireCrawlLoader

loader = FireCrawlLoader(
    api_key="YOUR_API_KEY", url="https://firecrawl.dev", mode="crawl"
)

docs = loader.load()

```

### [​](\#modes)  Modes

Scrape: Scrape single url and return the markdown.
Crawl: Crawl the url and all accessible sub pages and return the markdown for each one.

Copy

```python
loader = FireCrawlLoader(
    api_key="YOUR_API_KEY",
    url="https://firecrawl.dev",
    mode="scrape",
)

data = loader.load()

```

### [​](\#crawler-options)  Crawler Options

You can also pass params to the loader. This is a dictionary of options to pass to the crawler. See the FireCrawl API documentation for more information.

## [​](\#langchain-js)  Langchain JS

To use it in Langchain JS, you can install it via npm:

Copy

```bash
npm install @mendableai/firecrawl-js

```

Then, you can use it like this:

Copy

```typescript
import { FireCrawlLoader } from "langchain/document_loaders/web/firecrawl";

const loader = new FireCrawlLoader({
  url: "https://firecrawl.dev", // The URL to scrape
  apiKey: process.env.FIRECRAWL_API_KEY, // Optional, defaults to `FIRECRAWL_API_KEY` in your env.
  mode: "scrape", // The mode to run the crawler in. Can be "scrape" for single urls or "crawl" for all accessible subpages
  params: {
    // optional parameters based on Firecrawl API docs
    // For API documentation, visit https://docs.firecrawl.dev
  },
});

const docs = await loader.load();

```

[LLM Extract](/features/extract) [Llamaindex](/integrations/llamaindex)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Modes](#modes)
- [Crawler Options](#crawler-options)
- [Langchain JS](#langchain-js)

