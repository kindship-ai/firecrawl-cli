---
source: undefined
title: Firecrawl Docs
description: Firecrawl API Reference
language: en
crawl_date: 2024-11-21T17:20:40.897Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Using the API

Introduction

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#base-url)  Base URL

All requests contain the following base URL:

Copy

```bash
https://api.firecrawl.dev

```

## [​](\#authentication)  Authentication

For authentication, it’s required to include an Authorization header. The header should contain `Bearer fc-123456789`, where `fc-123456789` represents your API Key.

Copy

```bash
Authorization: Bearer fc-123456789

```

​

## [​](\#response-codes)  Response codes

Firecrawl employs conventional HTTP status codes to signify the outcome of your requests.

Typically, 2xx HTTP status codes denote success, 4xx codes represent failures related to the user, and 5xx codes signal infrastructure problems.

| Status | Description |
| --- | --- |
| 200 | Request was successful. |
| 400 | Verify the correctness of the parameters. |
| 401 | The API key was not provided. |
| 402 | Payment required |
| 404 | The requested resource could not be located. |
| 429 | The rate limit has been surpassed. |
| 5xx | Signifies a server error with Firecrawl. |

Refer to the Error Codes section for a detailed explanation of all potential API errors.

​

## [​](\#rate-limit)  Rate limit

The Firecrawl API has a rate limit to ensure the stability and reliability of the service. The rate limit is applied to all endpoints and is based on the number of requests made within a specific time frame.

When you exceed the rate limit, you will receive a 429 response code.

[Scrape](/api-reference/endpoint/scrape)

On this page

- [Base URL](#base-url)
- [Authentication](#authentication)
- [Response codes](#response-codes)
- [Rate limit](#rate-limit)

