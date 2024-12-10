---
source: undefined
title: Welcome to V1 | Firecrawl
description: Firecrawl allows you to turn entire websites into LLM-ready markdown
language: en
crawl_date: 2024-11-21T17:20:41.055Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Get Started

Welcome to V1

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

Firecrawl V1 is here! With that we introduce a more reliable and developer friendly API.

Here is what’s new:

- Output Formats for `/scrape`. Choose what formats you want your output in.
- New [`/map` endpoint](/features/map) for getting most of the URLs of a webpage.
- Developer friendly API for `/crawl/{id}` status.
- 2x Rate Limits for all plans.
- [Go SDK](/sdks/go) and [Rust SDK](/sdks/rust)
- Teams support
- API Key Management in the dashboard.
- `onlyMainContent` is now default to `true`.
- `/crawl` webhooks and websocket support.

## [​](\#scrape-formats)  Scrape Formats

You can now choose what formats you want your output in. You can specify multiple output formats. Supported formats are:

- Markdown (markdown)
- HTML (html)
- Raw HTML (rawHtml) (with no modifications)
- Screenshot (screenshot or screenshot@fullPage)
- Links (links)

Output keys will match the format you choose.

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

### [​](\#response)  Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

Copy

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
## [​](\#introducing-map-alpha)  Introducing /map (Alpha)\
\
The easiest way to go from a single url to a map of the entire website.\
\
### [​](\#usage)  Usage\
\
Python\
\
Node\
\
Go\
\
Rust\
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
# Map a website:\
map_result = app.map_url('https://firecrawl.dev')\
print(map_result)\
\
```\
\
### [​](\#response-2)  Response\
\
SDKs will return the data object directly. cURL will return the payload exactly as shown below.\
\
Copy\
\
```json\
{\
  "status": "success",\
  "links": [\
    "https://firecrawl.dev",\
    "https://www.firecrawl.dev/pricing",\
    "https://www.firecrawl.dev/blog",\
    "https://www.firecrawl.dev/playground",\
    "https://www.firecrawl.dev/smart-crawl",\
    ...\
  ]\
}\
\
```\
\
## [​](\#websockets)  WebSockets\
\
To crawl a website with WebSockets, use the `Crawl URL and Watch` method.\
\
Python\
\
Node\
\
Copy\
\
```python\
# inside an async function...\
nest_asyncio.apply()\
\
# Define event handlers\
def on_document(detail):\
    print("DOC", detail)\
\
def on_error(detail):\
    print("ERR", detail['error'])\
\
def on_done(detail):\
    print("DONE", detail['status'])\
\
    # Function to start the crawl and watch process\
async def start_crawl_and_watch():\
    # Initiate the crawl job and get the watcher\
    watcher = app.crawl_url_and_watch('firecrawl.dev', { 'excludePaths': ['blog/*'], 'limit': 5 })\
\
    # Add event listeners\
    watcher.add_event_listener("document", on_document)\
    watcher.add_event_listener("error", on_error)\
    watcher.add_event_listener("done", on_done)\
\
    # Start the watcher\
    await watcher.connect()\
\
# Run the event loop\
await start_crawl_and_watch()\
\
```\
\
## [​](\#extract-format)  Extract format\
\
LLM extraction is now available in v1 under the `extract` format. To extract structured from a page, you can pass a schema to the endpoint or just provide a prompt.\
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
Copy\
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
Copy\
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
## [​](\#new-crawl-webhook)  New Crawl Webhook\
\
You can now pass a `webhook` parameter to the `/crawl` endpoint. This will send a POST request to the URL you specify when the crawl is started, updated and completed.\
\
The webhook will now trigger for every page crawled and not just the whole result at the end.\
\
cURL\
\
Copy\
\
```bash\
curl -X POST https://api.firecrawl.dev/v1/crawl \\
    -H 'Content-Type: application/json' \\
    -H 'Authorization: Bearer YOUR_API_KEY' \\
    -d '{\
      "url": "https://docs.firecrawl.dev",\
      "limit": 100,\
      "webhook": "https://example.com/webhook"\
    }'\
\
```\
\
### [​](\#webhook-events)  Webhook Events\
\
There are now 4 types of events:\
\
- `crawl.started` \- Triggered when the crawl is started.\
- `crawl.page` \- Triggered for every page crawled.\
- `crawl.completed` \- Triggered when the crawl is completed to let you know it’s done.\
- `crawl.failed` \- Triggered when the crawl fails.\
\
### [​](\#webhook-response)  Webhook Response\
\
- `success` \- If the webhook was successful in crawling the page correctly.\
- `type` \- The type of event that occurred.\
- `id` \- The ID of the crawl.\
- `data` \- The data that was scraped (Array). This will only be non empty on `crawl.page` and will contain 1 item if the page was scraped successfully. The response is the same as the `/scrape` endpoint.\
- `error` \- If the webhook failed, this will contain the error message.\
\
## [​](\#migrating-from-v0)  Migrating from V0\
\
## [​](\#scrape-endpoint)  /scrape endpoint\
\
The updated `/scrape` endpoint has been redesigned for enhanced reliability and ease of use. The structure of the new `/scrape` request body is as follows:\
\
Copy\
\
```json\
{\
  "url": "<string>",\
  "formats": ["markdown", "html", "rawHtml", "links", "screenshot"],\
  "includeTags": ["<string>"],\
  "excludeTags": ["<string>"],\
  "headers": { "<key>": "<value>" },\
  "waitFor": 123,\
  "timeout": 123\
}\
\
```\
\
### [​](\#formats)  Formats\
\
You can now choose what formats you want your output in. You can specify multiple output formats. Supported formats are:\
\
- Markdown (markdown)\
- HTML (html)\
- Raw HTML (rawHtml) (with no modifications)\
- Screenshot (screenshot or screenshot@fullPage)\
- Links (links)\
\
By default, the output will be include only the markdown format.\
\
### [​](\#details-on-the-new-request-body)  Details on the new request body\
\
The table below outlines the changes to the request body parameters for the `/scrape` endpoint in V1.\
\
| Parameter | Change | Description |\
| --- | --- | --- |\
| `onlyIncludeTags` | Moved and Renamed | Moved to root level. And renamed to `includeTags`. |\
| `removeTags` | Moved and Renamed | Moved to root level. And renamed to `excludeTags`. |\
| `onlyMainContent` | Moved | Moved to root level. `true` by default. |\
| `waitFor` | Moved | Moved to root level. |\
| `headers` | Moved | Moved to root level. |\
| `parsePDF` | Moved | Moved to root level. |\
| `extractorOptions` | No Change |  |\
| `timeout` | No Change |  |\
| `pageOptions` | Removed | No need for `pageOptions` parameter. The scrape options were moved to root level. |\
| `replaceAllPathsWithAbsolutePaths` | Removed | `replaceAllPathsWithAbsolutePaths` is not needed anymore. Every path is now default to absolute path. |\
| `includeHtml` | Removed | add `"html"` to `formats` instead. |\
| `includeRawHtml` | Removed | add `"rawHtml"` to `formats` instead. |\
| `screenshot` | Removed | add `"screenshot"` to `formats` instead. |\
| `fullPageScreenshot` | Removed | add `"screenshot@fullPage"` to `formats` instead. |\
| `extractorOptions` | Removed | Use `"extract"` format instead with `extract` object. |\
\
The new `extract` format is described in the [llm-extract](/features/extract) section.\
\
## [​](\#crawl-endpoint)  /crawl endpoint\
\
We’ve also updated the `/crawl` endpoint on `v1`. Check out the improved body request below:\
\
Copy\
\
```json\
{\
  "url": "<string>",\
  "excludePaths": ["<string>"],\
  "includePaths": ["<string>"],\
  "maxDepth": 2,\
  "ignoreSitemap": true,\
  "limit": 10,\
  "allowBackwardLinks": true,\
  "allowExternalLinks": true,\
  "scrapeOptions": {\
    // same options as in /scrape\
    "formats": ["markdown", "html", "rawHtml", "screenshot", "links"],\
    "headers": { "<key>": "<value>" },\
    "includeTags": ["<string>"],\
    "excludeTags": ["<string>"],\
    "onlyMainContent": true,\
    "waitFor": 123\
  }\
}\
\
```\
\
### [​](\#details-on-the-new-request-body-2)  Details on the new request body\
\
The table below outlines the changes to the request body parameters for the `/crawl` endpoint in V1.\
\
| Parameter | Change | Description |\
| --- | --- | --- |\
| `pageOptions` | Renamed | Renamed to `scrapeOptions`. |\
| `includes` | Moved and Renamed | Moved to root level. Renamed to `includePaths`. |\
| `excludes` | Moved and Renamed | Moved to root level. Renamed to `excludePaths`. |\
| `allowBackwardCrawling` | Moved and Renamed | Moved to root level. Renamed to `allowBackwardLinks`. |\
| `allowExternalLinks` | Moved | Moved to root level. |\
| `maxDepth` | Moved | Moved to root level. |\
| `ignoreSitemap` | Moved | Moved to root level. |\
| `limit` | Moved | Moved to root level. |\
| `crawlerOptions` | Removed | No need for `crawlerOptions` parameter. The crawl options were moved to root level. |\
| `timeout` | Removed | Use `timeout` in `scrapeOptions` instead. |\
\
[Launch Week II (New)](/launch-week) [Rate Limits](/rate-limits)\
\
On this page\
\
- [Scrape Formats](#scrape-formats)\
- [Response](#response)\
- [Introducing /map (Alpha)](#introducing-map-alpha)\
- [Usage](#usage)\
- [Response](#response-2)\
- [WebSockets](#websockets)\
- [Extract format](#extract-format)\
- [Extracting without schema (New)](#extracting-without-schema-new)\
- [New Crawl Webhook](#new-crawl-webhook)\
- [Webhook Events](#webhook-events)\
- [Webhook Response](#webhook-response)\
- [Migrating from V0](#migrating-from-v0)\
- [/scrape endpoint](#scrape-endpoint)\
- [Formats](#formats)\
- [Details on the new request body](#details-on-the-new-request-body)\
- [/crawl endpoint](#crawl-endpoint)\
- [Details on the new request body](#details-on-the-new-request-body-2)

