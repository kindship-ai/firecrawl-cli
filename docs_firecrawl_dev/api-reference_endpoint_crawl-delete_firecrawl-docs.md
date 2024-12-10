---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:42.093Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Cancel Crawl

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

DELETE

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
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'
```

200

404

500

Copy

```
{
  "success": true,
  "message": "Crawl job successfully cancelled."
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

success

boolean

message

string

[Get Crawl Status](/api-reference/endpoint/crawl-get) [Map](/api-reference/endpoint/map)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'
```

200

404

500

Copy

```
{
  "success": true,
  "message": "Crawl job successfully cancelled."
}
```

