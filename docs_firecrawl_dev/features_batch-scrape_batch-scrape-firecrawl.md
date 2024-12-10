---
source: undefined
title: Batch Scrape | Firecrawl
description: Batch scrape multiple URLs
language: en
crawl_date: 2024-11-21T17:20:42.164Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Scrape

Batch Scrape

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#batch-scraping-multiple-urls)  Batch scraping multiple URLs

You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.

### [​](\#how-it-works)  How it works

It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.

The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.

### [​](\#usage)  Usage

Python

Node

cURL

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape multiple websites:
batch_scrape_result = app.batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], {'formats': ['markdown', 'html']})
print(batch_scrape_result)

# Or, you can use the asynchronous method:
batch_scrape_job = app.async_batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], {'formats': ['markdown', 'html']})
print(batch_scrape_job)

# (async) You can then use the job ID to check the status of the batch scrape:
batch_scrape_status = app.check_batch_scrape_status(batch_scrape_job['id'])
print(batch_scrape_status)

```

### [​](\#response)  Response

If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.

#### [​](\#synchronous)  Synchronous

Completed

```json
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789?skip=26",
  "data": [\
    {\
      "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",\
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",\
      "metadata": {\
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",\
        "language": "en",\
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",\
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",\
        "ogLocaleAlternate": [],\
        "statusCode": 200\
      }\
    },\
    ...\
  ]\
}\
\
```\
\
#### [​](\#asynchronous)  Asynchronous\
\
You can then use the job ID to check the status of the batch scrape by calling the `/batch/scrape/{id}` endpoint. This endpoint is meant to be used while the job is still running or right after it has completed **as batch scrape jobs expire after 24 hours**.\
\
```json\
{\
  "success": true,\
  "id": "123-456-789",\
  "url": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789"\
}\
\
```\
\
## [​](\#batch-scrape-with-extraction)  Batch scrape with extraction\
\
You can also use the batch scrape endpoint to extract structured data from the pages. This is useful if you want to get the same structured data from a list of URLs.\
\
Python\
\
Node\
\
cURL\
\
```python\
from firecrawl import FirecrawlApp\
\
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")\
\
# Scrape multiple websites:\
batch_scrape_result = app.batch_scrape_urls(\
    ['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'],\
    {\
        'formats': ['extract'],\
        'prompt': 'Extract the title and description from the page.',\
        'schema': {\
            'type': 'object',\
            'properties': {\
                'title': {'type': 'string'},\
                'description': {'type': 'string'}\
            },\
            'required': ['title', 'description']\
        }\
    }\
)\
print(batch_scrape_result)\
\
# Or, you can use the asynchronous method:\
batch_scrape_job = app.async_batch_scrape_urls(\
    ['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'],\
    {\
        'formats': ['extract'],\
        'prompt': 'Extract the title and description from the page.',\
        'schema': {\
            'type': 'object',\
            'properties': {\
                'title': {'type': 'string'},\
                'description': {'type': 'string'}\
            },\
            'required': ['title', 'description']\
        }\
    }\
)\
print(batch_scrape_job)\
\
# (async) You can then use the job ID to check the status of the batch scrape:\
batch_scrape_status = app.check_batch_scrape_status(batch_scrape_job['id'])\
print(batch_scrape_status)\
\
```\
\
### [​](\#response-2)  Response\
\
#### [​](\#synchronous-2)  Synchronous\
\
Completed\
\
```json\
{\
  "status": "completed",\
  "total": 36,\
  "completed": 36,\
  "creditsUsed": 36,\
  "expiresAt": "2024-00-00T00:00:00.000Z",\
  "next": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789?skip=26",\
  "data": [\
    {\
      "extract": {\
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",\
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot."\
      }\
    },\
    ...\
  ]\
}\
\
```\
\
#### [​](\#asynchronous-2)  Asynchronous\
\
```json\
{\
  "success": true,\
  "id": "123-456-789",\
  "url": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789"\
}\
\
```\
\
[Scrape](/features/scrape) [Crawl](/features/crawl)\
\
On this page\
\
- [Batch scraping multiple URLs](#batch-scraping-multiple-urls)\
- [How it works](#how-it-works)\
- [Usage](#usage)\
- [Response](#response)\
- [Synchronous](#synchronous)\
- [Asynchronous](#asynchronous)\
- [Batch scrape with extraction](#batch-scrape-with-extraction)\
- [Response](#response-2)\
- [Synchronous](#synchronous-2)\
- [Asynchronous](#asynchronous-2)

