---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:45.314Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Get Crawl Status

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

GET

/

crawl

/

status

/

{jobId}

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

Path

jobId

string

\*

jobId

Required

string

ID of the crawl job

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request GET \
  --url https://api.firecrawl.dev/v0/crawl/status/{jobId} \
  --header 'Authorization: Bearer <token>'
```

200

402

429

500

Copy

```
{
  "status": "<string>",
  "current": 123,
  "total": 123,
  "data": [\
    {\
      "markdown": "<string>",\
      "content": "<string>",\
      "html": "<string>",\
      "rawHtml": "<string>",\
      "index": 123,\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>",\
        "<any other metadata> ": "<string>",\
        "pageStatusCode": 123,\
        "pageError": "<string>"\
      }\
    }\
  ],
  "partial_data": [\
    {\
      "markdown": "<string>",\
      "content": "<string>",\
      "html": "<string>",\
      "rawHtml": "<string>",\
      "index": 123,\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>",\
        "<any other metadata> ": "<string>",\
        "pageStatusCode": 123,\
        "pageError": "<string>"\
      }\
    }\
  ]
}
```

This endpoint retrieves the status of a crawl job. If the job is not completed, the response includes content within `partial_data`. Once the job is completed, the content is available under `data`.

**We recommend keeping track of the crawl jobs yourself as the crawl status results can expire after 24 hours.**

#### Authorizations

Authorization

string

headerrequired

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

jobId

string

required

ID of the crawl job

#### Response

200 - application/json

status

string

Status of the job (completed, active, failed, paused)

current

integer

Current page number

total

integer

Total number of pages

data

object\[\]

Data returned from the job (null when it is in progress)

Showchild attributes

partial\_data

object\[\]

Partial documents returned as it is being crawled (streaming). **This feature is currently in alpha - expect breaking changes** When a page is ready, it will append to the partial\_data array, so there is no need to wait for the entire website to be crawled. When the crawl is done, partial\_data will become empty and the result will be available in `data`. There is a max of 50 items in the array response. The oldest item (top of the array) will be removed when the new item is added to the array.

Showchild attributes

[Crawl](/v0/api-reference/endpoint/crawl) [Cancel Crawl Job](/v0/api-reference/endpoint/crawl-cancel)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request GET \
  --url https://api.firecrawl.dev/v0/crawl/status/{jobId} \
  --header 'Authorization: Bearer <token>'
```

200

402

429

500

Copy

```
{
  "status": "<string>",
  "current": 123,
  "total": 123,
  "data": [\
    {\
      "markdown": "<string>",\
      "content": "<string>",\
      "html": "<string>",\
      "rawHtml": "<string>",\
      "index": 123,\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>",\
        "<any other metadata> ": "<string>",\
        "pageStatusCode": 123,\
        "pageError": "<string>"\
      }\
    }\
  ],
  "partial_data": [\
    {\
      "markdown": "<string>",\
      "content": "<string>",\
      "html": "<string>",\
      "rawHtml": "<string>",\
      "index": 123,\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>",\
        "<any other metadata> ": "<string>",\
        "pageStatusCode": 123,\
        "pageError": "<string>"\
      }\
    }\
  ]
}
```

