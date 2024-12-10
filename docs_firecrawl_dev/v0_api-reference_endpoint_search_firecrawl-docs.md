---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:45.301Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Search (Beta)

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

POST

/

search

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

query

string

\*

query

Required

string

The query to search for

pageOptions

object

pageOptions

object

onlyMainContent

boolean

Select option

onlyMainContent

boolean

Only return the main content of the page excluding headers, navs, footers, etc.

fetchPageContent

boolean

Select option

fetchPageContent

boolean

Fetch the content of each page. If false, defaults to a basic fast serp API.

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

searchOptions

object

searchOptions

object

limit

integer

limit

integer

Maximum number of results. Max is 20 during beta.

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v0/search \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "query": "<string>",
  "pageOptions": {
    "onlyMainContent": true,
    "fetchPageContent": true,
    "includeHtml": true,
    "includeRawHtml": true
  },
  "searchOptions": {
    "limit": 123
  }
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
  "data": [\
    {\
      "url": "<string>",\
      "markdown": "<string>",\
      "content": "<string>",\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>"\
      }\
    }\
  ]
}
```

The search endpoint combines a search API with the power of Firecrawl to provide a powerful search experience for whatever query.

It automatically searches the web for the query and returns the most relevant results from the top pages in markdown format. The advantage of this endpoint is that it actually scrap each website on the top result so you always get the full content.

This endpoint is currently in beta and is subject to change.

#### Authorizations

Authorization

string

headerrequired

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

application/json

query

string

required

The query to search for

pageOptions

object

Showchild attributes

searchOptions

object

Showchild attributes

#### Response

200 - application/json

success

boolean

data

object\[\]

Showchild attributes

[Scrape](/v0/api-reference/endpoint/scrape) [Crawl](/v0/api-reference/endpoint/crawl)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v0/search \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "query": "<string>",
  "pageOptions": {
    "onlyMainContent": true,
    "fetchPageContent": true,
    "includeHtml": true,
    "includeRawHtml": true
  },
  "searchOptions": {
    "limit": 123
  }
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
  "data": [\
    {\
      "url": "<string>",\
      "markdown": "<string>",\
      "content": "<string>",\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>"\
      }\
    }\
  ]
}
```

