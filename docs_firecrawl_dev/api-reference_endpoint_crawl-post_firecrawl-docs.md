---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:43.140Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Crawl

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

POST

/

crawl

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

excludePaths

array

excludePaths

array

Specifies URL patterns to exclude from the crawl by comparing website paths against the provided regex patterns. For example, if you set "excludePaths": \["blog/\*"\] for the base URL firecrawl.dev, any results matching that pattern will be excluded, such as https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap.

includePaths

array

includePaths

array

Specifies URL patterns to include in the crawl by comparing website paths against the provided regex patterns. Only the paths that match the specified patterns will be included in the response. For example, if you set "includePaths": \["blog/\*"\] for the base URL firecrawl.dev, only results matching that pattern will be included, such as https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap.

maxDepth

integer

maxDepth

integer

Maximum depth to crawl relative to the entered URL.

ignoreSitemap

boolean

Select option

ignoreSitemap

boolean

Ignore the website sitemap when crawling

limit

integer

limit

integer

Maximum number of pages to crawl. Default limit is 10000.

allowBackwardLinks

boolean

Select option

allowBackwardLinks

boolean

Enables the crawler to navigate from a specific URL to previously linked pages.

allowExternalLinks

boolean

Select option

allowExternalLinks

boolean

Allows the crawler to follow links to external websites.

webhook

string

stringobject

webhook

string

The URL to send the webhook to. This will trigger for crawl started (crawl.started) ,every page crawled (crawl.page) and when the crawl is completed (crawl.completed or crawl.failed). The response will be the same as the `/scrape` endpoint.

scrapeOptions

object

scrapeOptions

object

formats

array

formats

array

Formats to include in the output.

headers

object

headers

object

Headers to send with the request. Can be used to send cookies, user-agent, etc.

includeTags

array

includeTags

array

Tags to include in the output.

excludeTags

array

excludeTags

array

Tags to exclude from the output.

onlyMainContent

boolean

Select option

onlyMainContent

boolean

Only return the main content of the page excluding headers, navs, footers, etc.

removeBase64Images

boolean

Select option

removeBase64Images

boolean

Remove base64 encoded images from the output

mobile

boolean

Select option

mobile

boolean

Set to true if you want to emulate scraping from a mobile device. Useful for testing responsive pages and taking mobile screenshots.

waitFor

integer

waitFor

integer

Wait x amount of milliseconds for the page to load to fetch content

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/crawl \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "excludePaths": [\
    "<string>"\
  ],
  "includePaths": [\
    "<string>"\
  ],
  "maxDepth": 123,
  "ignoreSitemap": true,
  "limit": 123,
  "allowBackwardLinks": true,
  "allowExternalLinks": true,
  "webhook": "<string>",
  "scrapeOptions": {
    "formats": [\
      "markdown"\
    ],
    "headers": {},
    "includeTags": [\
      "<string>"\
    ],
    "excludeTags": [\
      "<string>"\
    ],
    "onlyMainContent": true,
    "removeBase64Images": true,
    "mobile": true,
    "waitFor": 123
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
  "id": "<string>",
  "url": "<string>"
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

excludePaths

string\[\]

Specifies URL patterns to exclude from the crawl by comparing website paths against the provided regex patterns. For example, if you set "excludePaths": \["blog/\*"\] for the base URL firecrawl.dev, any results matching that pattern will be excluded, such as https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap.

includePaths

string\[\]

Specifies URL patterns to include in the crawl by comparing website paths against the provided regex patterns. Only the paths that match the specified patterns will be included in the response. For example, if you set "includePaths": \["blog/\*"\] for the base URL firecrawl.dev, only results matching that pattern will be included, such as https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap.

maxDepth

integer

default:2

Maximum depth to crawl relative to the entered URL.

ignoreSitemap

boolean

default:true

Ignore the website sitemap when crawling

limit

integer

default:10

Maximum number of pages to crawl. Default limit is 10000.

allowBackwardLinks

boolean

default:false

Enables the crawler to navigate from a specific URL to previously linked pages.

allowExternalLinks

boolean

default:false

Allows the crawler to follow links to external websites.

webhook

stringobject

The URL to send the webhook to. This will trigger for crawl started (crawl.started) ,every page crawled (crawl.page) and when the crawl is completed (crawl.completed or crawl.failed). The response will be the same as the `/scrape` endpoint.

scrapeOptions

object

Showchild attributes

#### Response

200 - application/json

success

boolean

id

string

url

string

[Scrape](/api-reference/endpoint/scrape) [Get Crawl Status](/api-reference/endpoint/crawl-get)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/crawl \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "excludePaths": [\
    "<string>"\
  ],
  "includePaths": [\
    "<string>"\
  ],
  "maxDepth": 123,
  "ignoreSitemap": true,
  "limit": 123,
  "allowBackwardLinks": true,
  "allowExternalLinks": true,
  "webhook": "<string>",
  "scrapeOptions": {
    "formats": [\
      "markdown"\
    ],
    "headers": {},
    "includeTags": [\
      "<string>"\
    ],
    "excludeTags": [\
      "<string>"\
    ],
    "onlyMainContent": true,
    "removeBase64Images": true,
    "mobile": true,
    "waitFor": 123
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
  "id": "<string>",
  "url": "<string>"
}
```

