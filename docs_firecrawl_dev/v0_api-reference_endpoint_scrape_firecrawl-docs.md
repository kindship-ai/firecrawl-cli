---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:45.297Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Scrape

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

POST

/

scrape

Send

Authorization

Authorization

string

\*

Bearer

Authorization

Required

string

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

Body

object

\*

url

string

\*

url

Required

string

The URL to scrape

pageOptions

object

pageOptions

object

headers

object

headers

object

Headers to send with the request. Can be used to send cookies, user-agent, etc.

includeHtml

boolean

Select option

includeHtml

boolean

Include the HTML version of the content on page. Will output a html key in the response.

includeRawHtml

boolean

Select option

includeRawHtml

boolean

Include the raw HTML content of the page. Will output a rawHtml key in the response.

onlyIncludeTags

array

onlyIncludeTags

array

Only include tags, classes and ids from the page in the final output. Use comma separated values. Example: 'script, .ad, #footer'

onlyMainContent

boolean

Select option

onlyMainContent

boolean

Only return the main content of the page excluding headers, navs, footers, etc.

removeTags

array

removeTags

array

Tags, classes and ids to remove from the page. Use comma separated values. Example: 'script, .ad, #footer'

replaceAllPathsWithAbsolutePaths

boolean

Select option

replaceAllPathsWithAbsolutePaths

boolean

Replace all relative paths with absolute paths for images and links

screenshot

boolean

Select option

screenshot

boolean

Include a screenshot of the top of the page that you are scraping.

fullPageScreenshot

boolean

Select option

fullPageScreenshot

boolean

Include a full page screenshot of the page that you are scraping.

waitFor

integer

waitFor

integer

Wait x amount of milliseconds for the page to load to fetch content

extractorOptions

object

extractorOptions

object

Options for extraction of structured information from the page content. Note: LLM-based extraction is not performed by default and only occurs when explicitly configured. The 'markdown' mode simply returns the scraped markdown and is the default mode for scraping.

mode

enum<string>

Select option

mode

enum<string>

The extraction mode to use. 'markdown': Returns the scraped markdown content, does not perform LLM extraction. 'llm-extraction': Extracts information from the cleaned and parsed content using LLM. 'llm-extraction-from-raw-html': Extracts information directly from the raw HTML using LLM. 'llm-extraction-from-markdown': Extracts information from the markdown content using LLM.

extractionPrompt

string

extractionPrompt

string

A prompt describing what information to extract from the page, applicable for LLM extraction modes.

extractionSchema

object

extractionSchema

object

The schema for the data to be extracted, required only for LLM extraction modes.

timeout

integer

timeout

integer

Timeout in milliseconds for the request

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v0/scrape \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "pageOptions": {
    "headers": {},
    "includeHtml": true,
    "includeRawHtml": true,
    "onlyIncludeTags": [\
      "<string>"\
    ],
    "onlyMainContent": true,
    "removeTags": [\
      "<string>"\
    ],
    "replaceAllPathsWithAbsolutePaths": true,
    "screenshot": true,
    "fullPageScreenshot": true,
    "waitFor": 123
  },
  "extractorOptions": {
    "mode": "markdown",
    "extractionPrompt": "<string>",
    "extractionSchema": {}
  },
  "timeout": 123
}'
```

200

402

429

500

Copy

```
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

#### Authorizations

Authorization

string

headerrequired

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

application/json

url

string

required

The URL to scrape

pageOptions

object

Showchild attributes

extractorOptions

object

Options for extraction of structured information from the page content. Note: LLM-based extraction is not performed by default and only occurs when explicitly configured. The 'markdown' mode simply returns the scraped markdown and is the default mode for scraping.

Showchild attributes

timeout

integer

default:30000

Timeout in milliseconds for the request

#### Response

200 - application/json

success

boolean

data

object

Showchild attributes

[Introduction](/v0/api-reference/introduction) [Search (Beta)](/v0/api-reference/endpoint/search)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v0/scrape \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "pageOptions": {
    "headers": {},
    "includeHtml": true,
    "includeRawHtml": true,
    "onlyIncludeTags": [\
      "<string>"\
    ],
    "onlyMainContent": true,
    "removeTags": [\
      "<string>"\
    ],
    "replaceAllPathsWithAbsolutePaths": true,
    "screenshot": true,
    "fullPageScreenshot": true,
    "waitFor": 123
  },
  "extractorOptions": {
    "mode": "markdown",
    "extractionPrompt": "<string>",
    "extractionSchema": {}
  },
  "timeout": 123
}'
```

200

402

429

500

Copy

```
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

