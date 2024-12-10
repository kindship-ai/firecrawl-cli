---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:42.129Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Get Batch Scrape Status

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

GET

/

batch

/

scrape

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

The ID of the batch scrape job

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
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

The ID of the batch scrape job

#### Response

200 - application/json

status

string

The current status of the batch scrape. Can be `scraping`, `completed`, or `failed`.

total

integer

The total number of pages that were attempted to be scraped.

completed

integer

The number of pages that have been successfully scraped.

creditsUsed

integer

The number of credits used for the batch scrape.

expiresAt

string

The date and time when the batch scrape will expire.

next

string \| null

The URL to retrieve the next 10MB of data. Returned if the batch scrape is not completed or if the response is larger than 10MB.

data

object\[\]

The data of the batch scrape.

Showchild attributes

[Batch Scrape](/api-reference/endpoint/batch-scrape)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
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

