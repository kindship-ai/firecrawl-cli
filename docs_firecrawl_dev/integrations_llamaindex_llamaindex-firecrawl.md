---
source: undefined
title: Llamaindex | Firecrawl
description: Firecrawl integrates with LlamaIndex as a document reader.
language: en
crawl_date: 2024-11-21T17:20:41.143Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Integrations

Llamaindex

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

> Note: this integration is still using [v0 version of the Firecrawl API](/v0/introduction). You can install the 0.0.20 version for the Python SDK or the 0.0.36 for the Node SDK.

## [​](\#installation)  Installation

Copy

```bash
pip install firecrawl-py==0.0.20 llama_index llama-index llama-index-readers-web

```

## [​](\#usage)  Usage

### [​](\#using-firecrawl-to-gather-an-entire-website)  Using FireCrawl to Gather an Entire Website

Copy

```python
from llama_index.readers.web import FireCrawlWebReader
from llama_index.core import SummaryIndex
import os

# Initialize FireCrawlWebReader to crawl a website
firecrawl_reader = FireCrawlWebReader(
    api_key="<your_api_key>",  # Replace with your actual API key from https://www.firecrawl.dev/
    mode="scrape",  # Choose between "crawl" and "scrape" for single page scraping
    params={"additional": "parameters"}  # Optional additional parameters
)

# Set the environment variable for the virtual key
os.environ["OPENAI_API_KEY"] = "<OPENAI_API_KEY>"

# Load documents from a single page URL
documents = firecrawl_reader.load_data(url="http://paulgraham.com/")
index = SummaryIndex.from_documents(documents)

# Set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

```

### [​](\#using-firecrawl-to-gather-a-single-page)  Using FireCrawl to Gather a Single Page

Copy

```python
from llama_index.readers.web import FireCrawlWebReader

# Initialize the FireCrawlWebReader with your API key and desired mode
firecrawl_reader = FireCrawlWebReader(
    api_key="<your_api_key>",  # Replace with your actual API key from https://www.firecrawl.dev/
    mode="scrape",  # Choose between "crawl" and "scrape"
    params={"additional": "parameters"}  # Optional additional parameters
)

# Load documents from a specified URL
documents = firecrawl_reader.load_data(url="http://paulgraham.com/worked.html")
index = SummaryIndex.from_documents(documents)

# Set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

```

[Langchain](/integrations/langchain) [CrewAI](/integrations/crewai)

On this page

- [Installation](#installation)
- [Usage](#usage)
- [Using FireCrawl to Gather an Entire Website](#using-firecrawl-to-gather-an-entire-website)
- [Using FireCrawl to Gather a Single Page](#using-firecrawl-to-gather-a-single-page)

