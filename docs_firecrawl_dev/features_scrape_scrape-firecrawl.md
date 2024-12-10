---
source: undefined
title: Scrape | Firecrawl
description: Turn any url into clean data
language: en
crawl_date: 2024-11-21T17:20:43.154Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Scrape

Scrape

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

Firecrawl converts web pages into markdown, ideal for LLM applications.

- It manages complexities: proxies, caching, rate limits, js-blocked content
- Handles dynamic content: dynamic websites, js-rendered sites, PDFs, images
- Outputs clean markdown, structured data, screenshots or html.

For details, see the [Scrape Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## [​](\#scraping-a-url-with-firecrawl)  Scraping a URL with Firecrawl

### [​](\#scrape-endpoint)  /scrape endpoint

Used to scrape a URL and get its content.

### [​](\#installation)  Installation

Python

Node

Go

Rust

Copy

```bash
pip install firecrawl-py

```

### [​](\#usage)  Usage

Python

Node

Go

Rust

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev', params={'formats': ['markdown', 'html']})
print(scrape_result)

```

For more details about the parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### [​](\#response)  Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```json
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",\
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",\
    "metadata": {\
      "title": "Home - Firecrawl",\
      "description": "Firecrawl crawls and converts any website into clean markdown.",\
      "language": "en",\
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",\
      "robots": "follow, index",\
      "ogTitle": "Firecrawl",\
      "ogDescription": "Turn any website into LLM-ready data.",\
      "ogUrl": "https://www.firecrawl.dev/",\
      "ogImage": "https://www.firecrawl.dev/og.png?123",\
      "ogLocaleAlternate": [],\
      "ogSiteName": "Firecrawl",\
      "sourceURL": "https://firecrawl.dev",\
      "statusCode": 200\
    }\
  }\
}\
\
```\
\
## [​](\#extract-structured-data)  Extract structured data\
\
### [​](\#scrape-with-extract-endpoint)  /scrape (with extract) endpoint\
\
Used to extract structured data from scraped pages.\
\
Python\
\
Node\
\
cURL\
\
Copy\
\
```python\
from firecrawl import FirecrawlApp\
from pydantic import BaseModel, Field\
\
# Initialize the FirecrawlApp with your API key\
app = FirecrawlApp(api_key='your_api_key')\
\
class ExtractSchema(BaseModel):\
    company_mission: str\
    supports_sso: bool\
    is_open_source: bool\
    is_in_yc: bool\
\
data = app.scrape_url('https://docs.firecrawl.dev/', {\
    'formats': ['extract'],\
    'extract': {\
        'schema': ExtractSchema.model_json_schema(),\
    }\
})\
print(data["extract"])\
\
```\
\
Output:\
\
JSON\
\
```json\
{\
    "success": true,\
    "data": {\
      "extract": {\
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",\
        "supports_sso": true,\
        "is_open_source": false,\
        "is_in_yc": true\
      },\
      "metadata": {\
        "title": "Mendable",\
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",\
        "robots": "follow, index",\
        "ogTitle": "Mendable",\
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",\
        "ogUrl": "https://docs.firecrawl.dev/",\
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",\
        "ogLocaleAlternate": [],\
        "ogSiteName": "Mendable",\
        "sourceURL": "https://docs.firecrawl.dev/"\
      },\
    }\
}\
\
```\
\
### [​](\#extracting-without-schema-new)  Extracting without schema (New)\
\
You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.\
\
cURL\
\
Copy\
\
```bash\
curl -X POST https://api.firecrawl.dev/v1/scrape \\
    -H 'Content-Type: application/json' \\
    -H 'Authorization: Bearer YOUR_API_KEY' \\
    -d '{\
      "url": "https://docs.firecrawl.dev/",\
      "formats": ["extract"],\
      "extract": {\
        "prompt": "Extract the company mission from the page."\
      }\
    }'\
\
```\
\
Output:\
\
JSON\
\
```json\
{\
    "success": true,\
    "data": {\
      "extract": {\
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",\
      },\
      "metadata": {\
        "title": "Mendable",\
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",\
        "robots": "follow, index",\
        "ogTitle": "Mendable",\
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",\
        "ogUrl": "https://docs.firecrawl.dev/",\
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",\
        "ogLocaleAlternate": [],\
        "ogSiteName": "Mendable",\
        "sourceURL": "https://docs.firecrawl.dev/"\
      },\
    }\
}\
\
```\
\
### [​](\#extract-object)  Extract object\
\
The `extract` object accepts the following parameters:\
\
- `schema`: The schema to use for the extraction.\
- `systemPrompt`: The system prompt to use for the extraction.\
- `prompt`: The prompt to use for the extraction without a schema.\
\
## [​](\#interacting-with-the-page-with-actions)  Interacting with the page with Actions\
\
Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.\
\
Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.\
\
It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.\
\
### [​](\#example)  Example\
\
Python\
\
Node\
\
cURL\
\
Copy\
\
```python\
from firecrawl import FirecrawlApp\
\
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")\
\
# Scrape a website:\
scrape_result = app.scrape_url('firecrawl.dev',\
    params={\
        'formats': ['markdown', 'html'],\
        'actions': [\
            {"type": "wait", "milliseconds": 2000},\
            {"type": "click", "selector": "textarea[title=\"Search\"]"},\
            {"type": "wait", "milliseconds": 2000},\
            {"type": "write", "text": "firecrawl"},\
            {"type": "wait", "milliseconds": 2000},\
            {"type": "press", "key": "ENTER"},\
            {"type": "wait", "milliseconds": 3000},\
            {"type": "click", "selector": "h3"},\
            {"type": "wait", "milliseconds": 3000},\
            {"type": "scrape"},\
            {"type": "screenshot"}\
        ]\
    }\
)\
print(scrape_result)\
\
```\
\
### [​](\#output)  Output\
\
JSON\
\
Copy\
\
```json\
{\
  "success": true,\
  "data": {\
    "markdown": "Our first Launch Week is over! [See the recap 🚀](blog/firecrawl-launch-week-1-recap)...",\
    "actions": {\
      "screenshots": [\
        "https://alttmdsdujxrfnakrkyi.supabase.co/storage/v1/object/public/media/screenshot-75ef2d87-31e0-4349-a478-fb432a29e241.png"\
      ],\
      "scrapes": [\
        {\
          "url": "https://www.firecrawl.dev/",\
          "html": "<html><body><h1>Firecrawl</h1></body></html>"\
        }\
      ]\
    },\
    "metadata": {\
      "title": "Home - Firecrawl",\
      "description": "Firecrawl crawls and converts any website into clean markdown.",\
      "language": "en",\
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",\
      "robots": "follow, index",\
      "ogTitle": "Firecrawl",\
      "ogDescription": "Turn any website into LLM-ready data.",\
      "ogUrl": "https://www.firecrawl.dev/",\
      "ogImage": "https://www.firecrawl.dev/og.png?123",\
      "ogLocaleAlternate": [],\
      "ogSiteName": "Firecrawl",\
      "sourceURL": "http://google.com",\
      "statusCode": 200\
    }\
  }\
}\
\
```\
\
For more details about the actions parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).\
\
## [​](\#location-and-language)  Location and Language\
\
Specify country and preferred languages to get relevant content based on your target location and language preferences.\
\
### [​](\#how-it-works)  How it works\
\
When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to ‘US’ if not specified.\
\
### [​](\#usage-2)  Usage\
\
To use the location and language settings, include the `location` object in your request body with the following properties:\
\
- `country`: ISO 3166-1 alpha-2 country code (e.g., ‘US’, ‘AU’, ‘DE’, ‘JP’). Defaults to ‘US’.\
- `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.\
\
Python\
\
Node\
\
cURL\
\
Copy\
\
```python\
from firecrawl import FirecrawlApp\
\
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")\
\
# Scrape a website:\
scrape_result = app.scrape_url('airbnb.com',\
    params={\
        'formats': ['markdown', 'html'],\
        'location': {\
            'country': 'BR',\
            'languages': ['pt-BR']\
        }\
    }\
)\
print(scrape_result)\
\
```\
\
## [​](\#batch-scraping-multiple-urls)  Batch scraping multiple URLs\
\
You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.\
\
### [​](\#how-it-works-2)  How it works\
\
It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.\
\
The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.\
\
### [​](\#usage-3)  Usage\
\
Python\
\
Node\
\
cURL\
\
Copy\
\
```python\
from firecrawl import FirecrawlApp\
\
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")\
\
# Scrape multiple websites:\
batch_scrape_result = app.batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], {'formats': ['markdown', 'html']})\
print(batch_scrape_result)\
\
# Or, you can use the asynchronous method:\
batch_scrape_job = app.async_batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], {'formats': ['markdown', 'html']})\
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
If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.\
\
#### [​](\#synchronous)  Synchronous\
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
[Advanced Scraping Guide](/advanced-scraping-guide) [Batch Scrape](/features/batch-scrape)\
\
On this page\
\
- [Scraping a URL with Firecrawl](#scraping-a-url-with-firecrawl)\
- [/scrape endpoint](#scrape-endpoint)\
- [Installation](#installation)\
- [Usage](#usage)\
- [Response](#response)\
- [Extract structured data](#extract-structured-data)\
- [/scrape (with extract) endpoint](#scrape-with-extract-endpoint)\
- [Extracting without schema (New)](#extracting-without-schema-new)\
- [Extract object](#extract-object)\
- [Interacting with the page with Actions](#interacting-with-the-page-with-actions)\
- [Example](#example)\
- [Output](#output)\
- [Location and Language](#location-and-language)\
- [How it works](#how-it-works)\
- [Usage](#usage-2)\
- [Batch scraping multiple URLs](#batch-scraping-multiple-urls)\
- [How it works](#how-it-works-2)\
- [Usage](#usage-3)\
- [Response](#response-2)\
- [Synchronous](#synchronous)\
- [Asynchronous](#asynchronous)

