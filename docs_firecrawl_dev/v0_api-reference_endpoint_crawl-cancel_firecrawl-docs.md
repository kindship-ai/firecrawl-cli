---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:45.315Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Cancel Crawl Job

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

DELETE

/

crawl

/

cancel

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
curl --request DELETE \
  --url https://api.firecrawl.dev/v0/crawl/cancel/{jobId} \
  --header 'Authorization: Bearer <token>'
```

200

402

429

500

Copy

```
{
  "status": "<string>"
}
```

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

Returns cancelled.

[Get Crawl Status](/v0/api-reference/endpoint/status)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v0/crawl/cancel/{jobId} \
  --header 'Authorization: Bearer <token>'
```

200

402

429

500

Copy

```
{
  "status": "<string>"
}
```

