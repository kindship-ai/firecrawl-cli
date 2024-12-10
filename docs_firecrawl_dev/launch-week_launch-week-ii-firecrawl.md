---
source: undefined
title: Launch Week II | Firecrawl
description: Check out what's new coming to Firecrawl in Launch Week II (Oct 28th - Nov 3rd)
language: en
crawl_date: 2024-11-21T17:20:40.954Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Get Started

Launch Week II (New)

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#day-7-faster-markdown-parsing)  Day 7 - Faster Markdown Parsing

We’ve rebuilt our Markdown parser from the ground up with a focus on speed and performance. This enhancement ensures that your web scraping tasks are more efficient and deliver higher-quality results.

### [​](\#whats-new)  What’s New?

- **Speed Improvements**: Experience parsing speeds up to 4 times faster than before, allowing for quicker data processing and reduced waiting times.
- **Enhanced Reliability**: Our new parser handles a wider range of HTML content more gracefully, reducing errors and improving consistency.
- **Cleaner Markdown Output**: Get cleaner and more readable Markdown, making your data easier to work with and integrate into your workflows.

## [​](\#day-6-mobile-scraping-mobile-screenshots)  Day 6 - Mobile Scraping (+ Mobile Screenshots)

Firecrawl now introduces **mobile device emulation** for both scraping and screenshots, empowering you to interact with sites as if from a mobile device. This feature is essential for testing mobile-specific content, understanding responsive design, and gaining insights from mobile-specific elements.

### [​](\#why-mobile-scraping)  Why Mobile Scraping?

Mobile-first experiences are increasingly common, and this feature enables you to:

- Take high-fidelity mobile screenshots for a more accurate representation of how a site appears on mobile.
- Test and verify mobile layouts and UI elements, ensuring the accuracy of your scraping results for responsive websites.
- Scrape mobile-only content, gaining access to information or layouts that vary from desktop versions.

### [​](\#usage)  Usage

To activate mobile scraping, simply add `"mobile": true` in your request, which will enable Firecrawl’s mobile emulation mode.

Python

Node

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_result = app.scrape_url('google.com',
    params={
        'formats': ['markdown', 'html'],
        'mobile': true
    }
)
print(scrape_result)

```

For further details, including additional configuration options, visit the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## [​](\#day-5-actions-2-new-actions)  Day 5 - Actions (2 new actions)

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

We’re excited to introduce two powerful new actions:

1. **Scrape**: Capture the current page content at any point during your interaction sequence, returning both URL and HTML.
2. **Wait for Selector**: Wait for a specific element to appear on the page before proceeding, ensuring more reliable automation.

```json
actions = [\
    {"type": "scrape"},\
    {"type": "wait", "selector": "#my-element"},\
]

```

Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, scrape the current page content, and take a screenshot.

For more precise control, you can now use `{type: "wait", selector: "#my-element"}` to wait for a specific element to appear on the page.

### [​](\#example)  Example

Python

Node

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev',
    params={
        'formats': ['markdown', 'html'],
        'actions': [\
            {"type": "wait", "milliseconds": 2000},\
            {"type": "click", "selector": "textarea[title=\"Search\"]"},\
            {"type": "wait", "milliseconds": 2000},\
            {"type": "write", "text": "firecrawl"},\
            {"type": "wait", "milliseconds": 2000},\
            {"type": "press", "key": "ENTER"},\
            {"type": "wait", "milliseconds": 3000},\
            {"type": "click", "selector": "h3"},\
            {"type": "wait", "milliseconds": 3000},\
            {"type": "scrape"},\
            {"type": "screenshot"}\
        ]
    }
)
print(scrape_result)

```

### [​](\#output)  Output

JSON

Copy

```json
{
  "success": true,
  "data": {
    "markdown": "Our first Launch Week is over! [See the recap 🚀](blog/firecrawl-launch-week-1-recap)...",
    "actions": {
      "screenshots": [\
        "https://alttmdsdujxrfnakrkyi.supabase.co/storage/v1/object/public/media/screenshot-75ef2d87-31e0-4349-a478-fb432a29e241.png"\
      ],
      "scrapes": [\
        {\
          "url": "https://www.firecrawl.dev/",\
          "html": "<html><body><h1>Firecrawl</h1></body></html>"\
        }\
      ]
    },
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "http://google.com",
      "statusCode": 200
    }
  }
}

```

For more details about the actions parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## [​](\#day-4-advanced-iframe-scraping)  Day 4 - Advanced iframe scraping

We’re excited to announce comprehensive iframe scraping support in Firecrawl. Our scraper can now seamlessly handle nested iframes, dynamically loaded content, and cross-origin frames - solving one of web scraping’s most challenging technical hurdles.

### [​](\#technical-innovation)  Technical Innovation

Firecrawl now implements:

- Recursive iframe traversal and content extraction
- Cross-origin iframe handling with proper security context management
- Smart automatic wait for iframe content to load
- Support for dynamically injected iframes
- Proper handling of sandboxed iframes

### [​](\#why-it-matters)  Why it matters

Many modern websites use iframes for:

- Embedded content and widgets
- Payment forms and secure inputs
- Third-party integrations
- Advertisement frames
- Social media embeds

Previously, these elements were often black boxes in scraping results. Now, you get complete access to iframe content just like any other part of the page.

### [​](\#usage-2)  Usage

No additional configuration needed! The iframe scraping happens automatically when you use any of our scraping or crawling endpoints. Whether you’re using `/scrape` for single pages or `/crawl` for entire websites, iframe content will be seamlessly integrated into your results.

## [​](\#day-3-credit-packs)  Day 3 - Credit Packs

Credit Packs allow you to you can easily top up your plan if your running low.
Additionally, we now offer Auto Recharge, which automatically recharges your account when you’re approaching your limit.
To enable visit the pricing page at [https://www.firecrawl.dev/pricing](https://www.firecrawl.dev/pricing)

### [​](\#credit-packs)  Credit Packs

Flexible monthly credit boosts for your projects.

- **$9/mo for 1000 credits**
- Add to any existing plan
- Choose the amount you need

### [​](\#auto-recharge-credits)  Auto Recharge Credits

Automatically top up your account when credits run low.

- **$11 per 1000 credits**
- Enable auto recharge with any subscription plan

## [​](\#day-2-geolocation)  Day 2 - Geolocation

Introducing location and language settings for scraping requests. Specify country and preferred languages to get relevant content based on your target location and language preferences.

### [​](\#how-it-works)  How it works

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to ‘US’ if not specified.

### [​](\#usage-3)  Usage

To use the location and language settings, include the `location` object in your request body with the following properties:

- `country`: ISO 3166-1 alpha-2 country code (e.g., ‘US’, ‘AU’, ‘DE’, ‘JP’). Defaults to ‘US’.
- `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

Python

Node

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_result = app.scrape_url('airbnb.com',
    params={
        'formats': ['markdown', 'html'],
        'location': {
            'country': 'BR',
            'languages': ['pt-BR']
        }
    }
)
print(scrape_result)

```

## [​](\#day-1-batch-scrape)  Day 1 - Batch Scrape

You can now scrape multiple URLs at the same time with our new batch endpoint. Ideal for when you don’t need the scraping results immediately.

### [​](\#how-it-works-2)  How it works

It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.

The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.

### [​](\#usage-4)  Usage

Python

Node

cURL

Copy

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape multiple websites:
batch_scrape_result = app.batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], {'formats': ['markdown', 'html']})
print(batch_scrape_result)

# Or, you can use the asynchronous method:
batch_scrape_job = app.async_batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], {'formats': ['markdown', 'html']})
print(batch_scrape_job)

# (async) You can then use the job ID to check the status of the batch scrape:
batch_scrape_status = app.check_batch_scrape_status(batch_scrape_job['id'])
print(batch_scrape_status)

```

### [​](\#response)  Response

If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.

#### [​](\#synchronous)  Synchronous

Completed

```json
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789?skip=26",
  "data": [\
    {\
      "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",\
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",\
      "metadata": {\
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",\
        "language": "en",\
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",\
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",\
        "ogLocaleAlternate": [],\
        "statusCode": 200\
      }\
    },\
    ...\
  ]\
}\
\
```\
\
#### [​](\#asynchronous)  Asynchronous\
\
You can then use the job ID to check the status of the batch scrape by calling the `/batch/scrape/{id}` endpoint. This endpoint is meant to be used while the job is still running or right after it has completed **as batch scrape jobs expire after 24 hours**.\
\
```json\
{\
  "success": true,\
  "id": "123-456-789",\
  "url": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789"\
}\
\
```\
\
[Quickstart](/introduction) [Welcome to V1](/v1-welcome)\
\
On this page\
\
- [Day 7 - Faster Markdown Parsing](#day-7-faster-markdown-parsing)\
- [What’s New?](#whats-new)\
- [Day 6 - Mobile Scraping (+ Mobile Screenshots)](#day-6-mobile-scraping-mobile-screenshots)\
- [Why Mobile Scraping?](#why-mobile-scraping)\
- [Usage](#usage)\
- [Day 5 - Actions (2 new actions)](#day-5-actions-2-new-actions)\
- [Example](#example)\
- [Output](#output)\
- [Day 4 - Advanced iframe scraping](#day-4-advanced-iframe-scraping)\
- [Technical Innovation](#technical-innovation)\
- [Why it matters](#why-it-matters)\
- [Usage](#usage-2)\
- [Day 3 - Credit Packs](#day-3-credit-packs)\
- [Credit Packs](#credit-packs)\
- [Auto Recharge Credits](#auto-recharge-credits)\
- [Day 2 - Geolocation](#day-2-geolocation)\
- [How it works](#how-it-works)\
- [Usage](#usage-3)\
- [Day 1 - Batch Scrape](#day-1-batch-scrape)\
- [How it works](#how-it-works-2)\
- [Usage](#usage-4)\
- [Response](#response)\
- [Synchronous](#synchronous)\
- [Asynchronous](#asynchronous)

