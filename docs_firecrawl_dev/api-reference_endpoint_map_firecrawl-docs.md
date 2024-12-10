---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:42.100Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Map

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

POST

/

map

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

The base URL to start crawling from

search

string

search

string

Search query to use for mapping. During the Alpha phase, the 'smart' part of the search functionality is limited to 1000 search results. However, if map finds more results, there is no limit applied.

ignoreSitemap

boolean

Select option

ignoreSitemap

boolean

Ignore the website sitemap when crawling.

sitemapOnly

boolean

Select option

sitemapOnly

boolean

Only return links found in the website sitemap

includeSubdomains

boolean

Select option

includeSubdomains

boolean

Include subdomains of the website

limit

integer

limit

integer

Maximum number of links to return

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/map \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "search": "<string>",
  "ignoreSitemap": true,
  "sitemapOnly": true,
  "includeSubdomains": true,
  "limit": 123
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
  "links": [\
    "<string>"\
  ]
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

The base URL to start crawling from

search

string

Search query to use for mapping. During the Alpha phase, the 'smart' part of the search functionality is limited to 1000 search results. However, if map finds more results, there is no limit applied.

ignoreSitemap

boolean

default:true

Ignore the website sitemap when crawling.

sitemapOnly

boolean

default:false

Only return links found in the website sitemap

includeSubdomains

boolean

default:false

Include subdomains of the website

limit

integer

default:5000

Maximum number of links to return

Required range: `x < 5000`

#### Response

200 - application/json

success

boolean

links

string\[\]

[Cancel Crawl](/api-reference/endpoint/crawl-delete) [Batch Scrape](/api-reference/endpoint/batch-scrape)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/map \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "search": "<string>",
  "ignoreSitemap": true,
  "sitemapOnly": true,
  "includeSubdomains": true,
  "limit": 123
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
  "links": [\
    "<string>"\
  ]
}
```

