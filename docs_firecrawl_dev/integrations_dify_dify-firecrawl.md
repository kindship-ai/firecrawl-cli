---
source: undefined
title: Dify | Firecrawl
description: Learn how to use Firecrawl on Dify
language: en
crawl_date: 2024-11-21T17:20:41.154Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Integrations

Dify

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

## [​](\#sync-data-from-websites-for-dify-workflows)  Sync Data from Websites for Dify workflows

Firecrawl can be used inside of [Dify the LLM workflow builder](https://cloud.dify.ai/). This page introduces how to scrape data from a web page, parse it into Markdown, and import it into the Dify knowledge base using their Firecrawl integration.

### [​](\#configuring-firecrawl)  Configuring Firecrawl

First, you need to configure Firecrawl credentials in the Data Source section of the Settings page.

![Configure Firecrawl key](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/fc_dify_config.avif)

Log in to your Firecrawl account and get your API Key, and then enter and save it in Dify.

![Save Firecrawl key](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/fc_dify_savekey.png)

### [​](\#scrape-target-webpage)  Scrape target webpage

Now comes the fun part, scraping and crawling. On the knowledge base creation page, select Sync from website and enter the URL to be scraped.

![Scraping setup](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/fc_dify_webscrape.webp)

The configuration options include: Whether to crawl sub-pages, Page crawling limit, Page scraping max depth, Excluded paths, Include only paths, and Content extraction scope. After completing the configuration, click Run to preview the parsed pages.

![Set Firecrawl configuration](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/fc_dify_fcoptions.webp)

### [​](\#review-import-results)  Review import results

After importing the parsed text from the webpage, it is stored in the knowledge base documents. View the import results and click Add URL to continue importing new web pages.

![See results of the Firecrawl scrape](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/fc_dify_results.webp)

[CrewAI](/integrations/crewai) [Flowise](/integrations/flowise)

On this page

- [Sync Data from Websites for Dify workflows](#sync-data-from-websites-for-dify-workflows)
- [Configuring Firecrawl](#configuring-firecrawl)
- [Scrape target webpage](#scrape-target-webpage)
- [Review import results](#review-import-results)

![Save Firecrawl key](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/fc_dify_savekey.png)

![Configure Firecrawl key](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/images/fc_dify_config.avif)

