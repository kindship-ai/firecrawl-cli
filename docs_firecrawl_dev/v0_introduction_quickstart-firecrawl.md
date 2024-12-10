---
source: undefined
title: Quickstart | Firecrawl
description: Firecrawl allows you to turn entire websites into LLM-ready markdown
language: en
crawl_date: 2024-11-21T17:20:42.151Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Get Started

Quickstart

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

![Hero Light](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/hero.png)

## [​](\#welcome-to-firecrawl)  Welcome to Firecrawl

[Firecrawl](https://firecrawl.dev?ref=github) is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.

## [​](\#how-to-use-it)  How to use it?

We provide an easy to use API with our hosted version. You can find the playground and documentation [here](https://firecrawl.dev/playground). You can also self host the backend if you’d like.

Check out the following resources to get started:

- [x] **API**: [Documentation](https://docs.firecrawl.dev/api-reference/introduction)
- [x] **SDKs**: [Python](https://docs.firecrawl.dev/sdks/python), [Node](https://docs.firecrawl.dev/sdks/node), [Go](https://docs.firecrawl.dev/sdks/go), [Rust](https://docs.firecrawl.dev/sdks/rust)
- [x] **LLM Frameworks**: [Langchain (python)](https://python.langchain.com/docs/integrations/document_loaders/firecrawl/), [Langchain (js)](https://js.langchain.com/docs/integrations/document_loaders/web_loaders/firecrawl), [Llama Index](https://docs.llamaindex.ai/en/latest/examples/data_connectors/WebPageDemo/#using-firecrawl-reader), [Crew.ai](https://docs.crewai.com/), [Composio](https://composio.dev/tools/firecrawl/all), [PraisonAI](https://docs.praison.ai/firecrawl/), [Superinterface](https://superinterface.ai/docs/assistants/functions/firecrawl), [Vectorize](https://docs.vectorize.io/integrations/source-connectors/firecrawl)
- [x] **Low-code Frameworks**: [Dify](https://dify.ai/blog/dify-ai-blog-integrated-with-firecrawl), [Langflow](https://docs.langflow.org/), [Flowise AI](https://docs.flowiseai.com/integrations/langchain/document-loaders/firecrawl), [Cargo](https://docs.getcargo.io/integration/firecrawl), [Pipedream](https://pipedream.com/apps/firecrawl/)
- [x] **Others**: [Zapier](https://zapier.com/apps/firecrawl/integrations), [Pabbly Connect](https://www.pabbly.com/connect/integrations/firecrawl/)
- [ ]  Want an SDK or Integration? Let us know by opening an issue.

**Self-host:** To self-host refer to guide [here](/contributing/self-host).

### [​](\#api-key)  API Key

To use the API, you need to sign up on [Firecrawl](https://firecrawl.dev) and get an API key.

## [​](\#crawling)  Crawling

Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.

### [​](\#installation)  Installation

Python

JavaScript

Go

Rust

Copy

```bash
pip install firecrawl-py

```

### [​](\#usage)  Usage

Python

JavaScript

Go

Rust

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="YOUR_API_KEY")

crawl_result = app.crawl_url('docs.firecrawl.dev', {'crawlerOptions': {'excludes': ['blog/*']}})

# Get the markdown
for result in crawl_result:
    print(result['markdown'])

```

If you are not using the sdk or prefer to use webhook or a different polling method, you can set the `wait_until_done` to `false`.
This will return a jobId.

For cURL, /crawl will always return a jobId where you can use to check the status of the crawl.

```json
{ "jobId": "1234-5678-9101" }

```

### [​](\#check-crawl-job)  Check Crawl Job

Used to check the status of a crawl job and get its result.

Python

JavaScript

Go

Rust

cURL

Copy

```python
status = app.check_crawl_status(job_id)

```

#### [​](\#response)  Response

```json
{
  "status": "completed",
  "current": 22,
  "total": 22,
  "data": [\
    {\
      "content": "Raw Content ",\
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

## [​](\#scraping)  Scraping

To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

Python

JavaScript

Go

Rust

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="YOUR_API_KEY")

content = app.scrape_url("https://docs.firecrawl.dev")

```

### [​](\#response-2)  Response

```json
{
  "success": true,
  "data": {
    "markdown": "<string>",
    "content": "<string>",
    "html": "<string>",
    "rawHtml": "<string>",
    "metadata": {
      "title": "<string>",
      "description": "<string>",
      "language": "<string>",
      "sourceURL": "<string>",
      "<any other metadata> ": "<string>",
      "pageStatusCode": 123,
      "pageError": "<string>"
    },
    "llm_extraction": {},
    "warning": "<string>"
  }
}

```

## [​](\#extraction)  Extraction

With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:

Python

JavaScript

Go

Rust

cURL

Copy

```python
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

## [​](\#contributing)  Contributing

We love contributions! Please read our [contributing guide](https://github.com/mendableai/firecrawl/blob/main/CONTRIBUTING.md) before submitting a pull request.

[Advanced Scraping Guide](/v0/advanced-scraping-guide)

On this page

- [Welcome to Firecrawl](#welcome-to-firecrawl)
- [How to use it?](#how-to-use-it)
- [API Key](#api-key)
- [Crawling](#crawling)
- [Installation](#installation)
- [Usage](#usage)
- [Check Crawl Job](#check-crawl-job)
- [Response](#response)
- [Scraping](#scraping)
- [Response](#response-2)
- [Extraction](#extraction)
- [Contributing](#contributing)

![Hero Light](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/hero.png)

