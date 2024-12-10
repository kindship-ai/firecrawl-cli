---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:42.091Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Get Crawl Status

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

GET

/

crawl

/

{id}

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

id

string

\*

id

Required

string

The ID of the crawl job

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
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
  "total": 123,
  "completed": 123,
  "creditsUsed": 123,
  "expiresAt": "2023-11-07T05:31:56Z",
  "next": "<string>",
  "data": [\
    {\
      "markdown": "<string>",\
      "html": "<string>",\
      "rawHtml": "<string>",\
      "links": [\
        "<string>"\
      ],\
      "screenshot": "<string>",\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>",\
        "<any other metadata> ": "<string>",\
        "statusCode": 123,\
        "error": "<string>"\
      }\
    }\
  ]
}
```

#### Authorizations

Authorization

string

headerrequired

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

id

string

required

The ID of the crawl job

#### Response

200 - application/json

status

string

The current status of the crawl. Can be `scraping`, `completed`, or `failed`.

total

integer

The total number of pages that were attempted to be crawled.

completed

integer

The number of pages that have been successfully crawled.

creditsUsed

integer

The number of credits used for the crawl.

expiresAt

string

The date and time when the crawl will expire.

next

string \| null

The URL to retrieve the next 10MB of data. Returned if the crawl is not completed or if the response is larger than 10MB.

data

object\[\]

The data of the crawl.

Showchild attributes

[Crawl](/api-reference/endpoint/crawl-post) [Cancel Crawl](/api-reference/endpoint/crawl-delete)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
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
  "total": 123,
  "completed": 123,
  "creditsUsed": 123,
  "expiresAt": "2023-11-07T05:31:56Z",
  "next": "<string>",
  "data": [\
    {\
      "markdown": "<string>",\
      "html": "<string>",\
      "rawHtml": "<string>",\
      "links": [\
        "<string>"\
      ],\
      "screenshot": "<string>",\
      "metadata": {\
        "title": "<string>",\
        "description": "<string>",\
        "language": "<string>",\
        "sourceURL": "<string>",\
        "<any other metadata> ": "<string>",\
        "statusCode": 123,\
        "error": "<string>"\
      }\
    }\
  ]
}
```

