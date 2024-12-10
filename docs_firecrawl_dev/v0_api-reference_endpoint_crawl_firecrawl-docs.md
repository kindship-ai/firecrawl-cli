---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:45.304Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v0

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Crawl

[Documentation](/v0/introduction) [SDKs](/v0/sdks/python) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/v0/api-reference/introduction)

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

crawlerOptions

object

crawlerOptions

object

includes

array

includes

array

URL patterns to include

excludes

array

excludes

array

URL patterns to exclude

generateImgAltText

boolean

Select option

generateImgAltText

boolean

Generate alt text for images using LLMs (must have a paid plan)

returnOnlyUrls

boolean

Select option

returnOnlyUrls

boolean

If true, returns only the URLs as a list on the crawl status. Attention: the return response will be a list of URLs inside the data, not a list of documents.

maxDepth

integer

maxDepth

integer

Maximum depth to crawl relative to the entered URL. A maxDepth of 0 scrapes only the entered URL. A maxDepth of 1 scrapes the entered URL and all pages one level deep. A maxDepth of 2 scrapes the entered URL and all pages up to two levels deep. Higher values follow the same pattern.

mode

enum<string>

Select option

mode

enum<string>

The crawling mode to use. Fast mode crawls 4x faster websites without sitemap, but may not be as accurate and shouldn't be used in heavy js-rendered websites.

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

Maximum number of pages to crawl

allowBackwardCrawling

boolean

Select option

allowBackwardCrawling

boolean

Enables the crawler to navigate from a specific URL to previously linked pages. For instance, from 'example.com/product/123' back to 'example.com/product'

allowExternalContentLinks

boolean

Select option

allowExternalContentLinks

boolean

Allows the crawler to follow links to external websites.

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

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v0/crawl \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "crawlerOptions": {
    "includes": [\
      "<string>"\
    ],
    "excludes": [\
      "<string>"\
    ],
    "generateImgAltText": true,
    "returnOnlyUrls": true,
    "maxDepth": 123,
    "mode": "default",
    "ignoreSitemap": true,
    "limit": 123,
    "allowBackwardCrawling": true,
    "allowExternalContentLinks": true
  },
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
  "jobId": "<string>"
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

crawlerOptions

object

Showchild attributes

pageOptions

object

Showchild attributes

#### Response

200 - application/json

jobId

string

[Search (Beta)](/v0/api-reference/endpoint/search) [Get Crawl Status](/v0/api-reference/endpoint/status)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v0/crawl \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "crawlerOptions": {
    "includes": [\
      "<string>"\
    ],
    "excludes": [\
      "<string>"\
    ],
    "generateImgAltText": true,
    "returnOnlyUrls": true,
    "maxDepth": 123,
    "mode": "default",
    "ignoreSitemap": true,
    "limit": 123,
    "allowBackwardCrawling": true,
    "allowExternalContentLinks": true
  },
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
  "jobId": "<string>"
}
```

