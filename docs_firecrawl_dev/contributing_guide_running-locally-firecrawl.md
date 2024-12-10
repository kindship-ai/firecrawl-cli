---
source: undefined
title: Running locally | Firecrawl
description: Learn how to run Firecrawl locally to run on your own and/or contribute to the project.
language: en
crawl_date: 2024-11-21T17:20:41.198Z
path: 
---

[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/dark.svg)](https://firecrawl.dev)

v1

Search or ask...

Ctrl K

Search...

Navigation

Contributing

Running locally

[Documentation](/introduction) [SDKs](/sdks/overview) [Learn](https://www.firecrawl.dev/blog/category/tutorials) [API Reference](/api-reference/introduction)

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally so you can run it on your own and contribute.

If you’re contributing, note that the process is similar to other open-source repos, i.e., fork Firecrawl, make changes, run tests, PR.

If you have any questions or would like help getting on board, join our Discord community [here](https://discord.gg/gSmWdAkdwd) for more information or submit an issue on Github [here](https://github.com/mendableai/firecrawl/issues/new/choose)!

## [​](\#running-the-project-locally)  Running the project locally

First, start by installing dependencies:

1. node.js [instructions](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)
2. pnpm [instructions](https://pnpm.io/installation)
3. redis [instructions](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)

Set environment variables in a `.env` file in the `/apps/api/` directory. You can copy over the template in `.env.example`.

To start, we won’t set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features)

Copy

```
# ./apps/api/.env

# ===== Required ENVS ======
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0

#for self-hosting using docker, use redis://redis:6379. For running locally, use redis://localhost:6379
REDIS_URL=redis://localhost:6379

#for self-hosting using docker, use redis://redis:6379. For running locally, use redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379
PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/html

## To turn on DB authentication, you need to set up supabase.
USE_DB_AUTHENTICATION=false

# ===== Optional ENVS ======

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
SUPABASE_ANON_TOKEN=
SUPABASE_URL=
SUPABASE_SERVICE_TOKEN=

# Other Optionals
# use if you've set up authentication and want to test with a real API key
TEST_API_KEY=
# set if you'd like to test the scraping rate limit
RATE_LIMIT_TEST_API_KEY_SCRAPE=
# set if you'd like to test the crawling rate limit
RATE_LIMIT_TEST_API_KEY_CRAWL=
# set if you'd like to use scraping Be to handle JS blocking
SCRAPING_BEE_API_KEY=
# add for LLM dependednt features (image alt generation, etc.)
OPENAI_API_KEY=
BULL_AUTH_KEY=@
# use if you're configuring basic logging with logtail
LOGTAIL_KEY=
# set if you have a llamaparse key you'd like to use to parse pdfs
LLAMAPARSE_API_KEY=
# set if you'd like to send slack server health status messages
SLACK_WEBHOOK_URL=
# set if you'd like to send posthog events like job logs
POSTHOG_API_KEY=
# set if you'd like to send posthog events like job logs
POSTHOG_HOST=

# set if you'd like to use the fire engine closed beta
FIRE_ENGINE_BETA_URL=

# Proxy Settings for Playwright (Alternative you can can use a proxy service like oxylabs, which rotates IPs for you on every request)
PROXY_SERVER=
PROXY_USERNAME=
PROXY_PASSWORD=
# set if you'd like to block media requests to save proxy bandwidth
BLOCK_MEDIA=

# Set this to the URL of your webhook when using the self-hosted version of FireCrawl
SELF_HOSTED_WEBHOOK_URL=

# Resend API Key for transactional emails
RESEND_API_KEY=

# LOGGING_LEVEL determines the verbosity of logs that the system will output.
# Available levels are:
# NONE - No logs will be output.
# ERROR - For logging error messages that indicate a failure in a specific operation.
# WARN - For logging potentially harmful situations that are not necessarily errors.
# INFO - For logging informational messages that highlight the progress of the application.
# DEBUG - For logging detailed information on the flow through the system, primarily used for debugging.
# TRACE - For logging more detailed information than the DEBUG level.
# Set LOGGING_LEVEL to one of the above options to control logging output.
LOGGING_LEVEL=INFO

```

### [​](\#installing-dependencies)  Installing dependencies

First, install the dependencies using pnpm.

Copy

```bash
# cd apps/api # to make sure you're in the right folder
pnpm install # make sure you have pnpm version 9+!

```

### [​](\#running-the-project)  Running the project

You’re going to need to open 3 terminals for running the services. Here is [a video guide accurate as of Oct 2024](https://youtu.be/LHqg5QNI4UY) (optional: 4 terminals for running the services and testing).

### [​](\#terminal-1-setting-up-redis)  Terminal 1 - setting up redis

Run the command anywhere within your project

Copy

```bash
redis-server

```

### [​](\#terminal-2-setting-up-workers)  Terminal 2 - setting up workers

Now, navigate to the apps/api/ directory and run:

Copy

```bash
pnpm run workers
# if you are going to use the [llm-extract feature](https://github.com/mendableai/firecrawl/pull/586/), you should also export OPENAI_API_KEY=sk-______

```

This will start the workers who are responsible for processing crawl jobs.

### [​](\#terminal-3-setting-up-the-main-server)  Terminal 3 - setting up the main server

To do this, navigate to the apps/api/ directory. If you haven’t installed pnpm already, you can do so here: [https://pnpm.io/installation](https://pnpm.io/installation)

Next, run your server with:

Copy

```bash
pnpm run start

```

### [​](\#optional-terminal-4-sending-our-first-request)  _(Optional)_ Terminal 4 - sending our first request

Alright, now let’s send our first request.

Copy

```curl
curl -X GET http://localhost:3002/test

```

This should return the response Hello, world!

If you’d like to test the crawl endpoint, you can run this

Copy

```curl
curl -X POST http://localhost:3002/v0/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'

```

## [​](\#tests)  Tests:

The best way to do this is run the test with `npm run test:local-no-auth` if you’d like to run the tests without authentication.

If you’d like to run the tests with authentication, run `npm run test:prod`

[Open Source vs Cloud](/contributing/open-source-or-cloud) [Self-hosting](/contributing/self-host)

On this page

- [Running the project locally](#running-the-project-locally)
- [Installing dependencies](#installing-dependencies)
- [Running the project](#running-the-project)
- [Terminal 1 - setting up redis](#terminal-1-setting-up-redis)
- [Terminal 2 - setting up workers](#terminal-2-setting-up-workers)
- [Terminal 3 - setting up the main server](#terminal-3-setting-up-the-main-server)
- [(Optional) Terminal 4 - sending our first request](#optional-terminal-4-sending-our-first-request)
- [Tests:](#tests)

