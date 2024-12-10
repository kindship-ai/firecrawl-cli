---
source: undefined
title: Firecrawl Docs
description: 
language: en
crawl_date: 2024-11-21T17:20:42.123Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Endpoints

Batch Scrape

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

POST

/

batch

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

urls

array

urls

array

webhook

string

stringobject

webhook

string

The URL to send the webhook to. This will trigger for batch scrape started (batch\_scrape.started), every page scraped (batch\_scrape.page) and when the batch scrape is completed (batch\_scrape.completed or batch\_scrape.failed). The response will be the same as the `/scrape` endpoint.

formats

array

formats

array

Formats to include in the output.

onlyMainContent

boolean

Select option

onlyMainContent

boolean

Only return the main content of the page excluding headers, navs, footers, etc.

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

headers

object

headers

object

Headers to send with the request. Can be used to send cookies, user-agent, etc.

waitFor

integer

waitFor

integer

Specify a delay in milliseconds before fetching the content, allowing the page sufficient time to load.

mobile

boolean

Select option

mobile

boolean

Set to true if you want to emulate scraping from a mobile device. Useful for testing responsive pages and taking mobile screenshots.

skipTlsVerification

boolean

Select option

skipTlsVerification

boolean

Skip TLS certificate verification when making requests

timeout

integer

timeout

integer

Timeout in milliseconds for the request

extract

object

extract

object

Extract object

schema

object

schema

object

The schema to use for the extraction (Optional)

systemPrompt

string

systemPrompt

string

The system prompt to use for the extraction (Optional)

prompt

string

prompt

string

The prompt to use for the extraction without a schema (Optional)

actions

array

actions

array

Actions to perform on the page before grabbing the content

location

object

location

object

Location settings for the request. When specified, this will use an appropriate proxy if available and emulate the corresponding language and timezone settings. Defaults to 'US' if not specified.

country

string

country

string

ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP')

languages

array

languages

array

Preferred languages and locales for the request in order of priority. Defaults to the language of the specified location. See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language

removeBase64Images

boolean

Select option

removeBase64Images

boolean

Removes all base 64 images from the output, which may be overwhelmingly long. The image's alt text remains in the output, but the URL is replaced with a placeholder.

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/batch/scrape \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "urls": [\
    "<string>"\
  ],
  "webhook": "<string>",
  "formats": [\
    "markdown"\
  ],
  "onlyMainContent": true,
  "includeTags": [\
    "<string>"\
  ],
  "excludeTags": [\
    "<string>"\
  ],
  "headers": {},
  "waitFor": 123,
  "mobile": true,
  "skipTlsVerification": true,
  "timeout": 123,
  "extract": {
    "schema": {},
    "systemPrompt": "<string>",
    "prompt": "<string>"
  },
  "actions": [\
    {\
      "type": "wait",\
      "milliseconds": 2,\
      "selector": "#my-element"\
    }\
  ],
  "location": {
    "country": "<string>",
    "languages": [\
      "en-US"\
    ]
  },
  "removeBase64Images": true
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

urls

string\[\]

webhook

stringobject

The URL to send the webhook to. This will trigger for batch scrape started (batch\_scrape.started), every page scraped (batch\_scrape.page) and when the batch scrape is completed (batch\_scrape.completed or batch\_scrape.failed). The response will be the same as the `/scrape` endpoint.

formats

enum<string>\[\]

Formats to include in the output.

Available options:

`markdown`,

`html`,

`rawHtml`,

`links`,

`screenshot`,

`extract`,

`screenshot@fullPage`

onlyMainContent

boolean

default:true

Only return the main content of the page excluding headers, navs, footers, etc.

includeTags

string\[\]

Tags to include in the output.

excludeTags

string\[\]

Tags to exclude from the output.

headers

object

Headers to send with the request. Can be used to send cookies, user-agent, etc.

waitFor

integer

default:0

Specify a delay in milliseconds before fetching the content, allowing the page sufficient time to load.

mobile

boolean

default:false

Set to true if you want to emulate scraping from a mobile device. Useful for testing responsive pages and taking mobile screenshots.

skipTlsVerification

boolean

default:false

Skip TLS certificate verification when making requests

timeout

integer

default:30000

Timeout in milliseconds for the request

extract

object

Extract object

Showchild attributes

actions

object\[\]

Actions to perform on the page before grabbing the content

- Wait
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript

Showchild attributes

location

object

Location settings for the request. When specified, this will use an appropriate proxy if available and emulate the corresponding language and timezone settings. Defaults to 'US' if not specified.

Showchild attributes

removeBase64Images

boolean

Removes all base 64 images from the output, which may be overwhelmingly long. The image's alt text remains in the output, but the URL is replaced with a placeholder.

#### Response

200 - application/json

success

boolean

id

string

url

string

[Map](/api-reference/endpoint/map) [Get Batch Scrape Status](/api-reference/endpoint/batch-scrape-get)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/batch/scrape \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "urls": [\
    "<string>"\
  ],
  "webhook": "<string>",
  "formats": [\
    "markdown"\
  ],
  "onlyMainContent": true,
  "includeTags": [\
    "<string>"\
  ],
  "excludeTags": [\
    "<string>"\
  ],
  "headers": {},
  "waitFor": 123,
  "mobile": true,
  "skipTlsVerification": true,
  "timeout": 123,
  "extract": {
    "schema": {},
    "systemPrompt": "<string>",
    "prompt": "<string>"
  },
  "actions": [\
    {\
      "type": "wait",\
      "milliseconds": 2,\
      "selector": "#my-element"\
    }\
  ],
  "location": {
    "country": "<string>",
    "languages": [\
      "en-US"\
    ]
  },
  "removeBase64Images": true
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

