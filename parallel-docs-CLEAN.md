# Parallel AI API — Technical Reference
> Source: docs.parallel.ai | Cleaned: duplicates removed, non-content removed, English only
> Original: 1.79MB → Cleaned: see below

---

# Search - Parallel

**URL:** https://docs.parallel.ai/api-reference/search-beta/search

[Skip to main content](https://docs.parallel.ai/api-reference/search-beta/search#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Search (Beta)

Search

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

search = client.beta.search(
    objective="What was the GDP of France in 2023?"
)
print(search.results)
```

200

422

Copy

Ask AI

```
{
  "search_id": "search_fcb2b4f3-c75e-4186-87bc-caa1a8381331",
  "results": [\
    {\
      "url": "https://www.example.com",\
      "title": "Sample webpage title",\
      "publish_date": "2024-01-15",\
      "excerpts": [\
        "Sample excerpt 1",\
        "Sample excerpt 2"\
      ]\
    }\
  ]
}
```

POST

/

v1beta

/

search

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

search = client.beta.search(
    objective="What was the GDP of France in 2023?"
)
print(search.results)
```

200

422

Copy

Ask AI

```
{
  "search_id": "search_fcb2b4f3-c75e-4186-87bc-caa1a8381331",
  "results": [\
    {\
      "url": "https://www.example.com",\
      "title": "Sample webpage title",\
      "publish_date": "2024-01-15",\
      "excerpts": [\
        "Sample excerpt 1",\
        "Sample excerpt 2"\
      ]\
    }\
  ]
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/search-beta/search#authorization-x-api-key)

x-api-key

string

header

required

#### Body

application/json

Request to Search API.

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-mode-one-of-0)

mode

enum<string> \| null

default:one-shot

Presets default values for parameters for different use cases.

- `one-shot` returns more comprehensive results and longer excerpts to answer questions from a single response
- `agentic` returns more concise, token-efficient results for use in an agentic loop
- `fast` trades some quality for lower latency, with best results when used with concise and high-quality objective and keyword queries

Available options:

`one-shot`,

`agentic`,

`fast`

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-objective-one-of-0)

objective

string \| null

Natural-language description of what the web search is trying to find. May include guidance about preferred sources or freshness. At least one of objective or search\_queries must be provided.

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-search-queries-one-of-0)

search\_queries

string\[\] \| null

Optional list of traditional keyword search queries to guide the search. May contain search operators. At least one of objective or search\_queries must be provided.

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-processor-one-of-0)

processor

enum<string> \| null

deprecated

DEPRECATED: use `mode` instead.

Available options:

`base`,

`pro`

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-max-results-one-of-0)

max\_results

integer \| null

default:10

Upper bound on the number of results to return. Defaults to 10 if not provided.

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-max-chars-per-result-one-of-0)

max\_chars\_per\_result

integer \| null

deprecated

DEPRECATED: Use `excerpts.max_chars_per_result` instead.

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-excerpts)

excerpts

ExcerptSettings · object

Optional settings to configure excerpt generation.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-source-policy-one-of-0)

source\_policy

SourcePolicy · object

Optional source policy governing domain and date preferences in search results.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/search-beta/search#body-fetch-policy-one-of-0)

fetch\_policy

FetchPolicy · object

Fetch policy: determines when to return cached content from the index (faster) vs fetching live content (fresher). Default is to disable live fetch and return cached content from the index.

Showchild attributes

#### Response

200

application/json

Successful Response

Output for the Search API.

[​](https://docs.parallel.ai/api-reference/search-beta/search#response-search-id)

search\_id

string

required

Search ID. Example: `search_cad0a6d2dec046bd95ae900527d880e7`

[​](https://docs.parallel.ai/api-reference/search-beta/search#response-results)

results

WebSearchResult · object\[\]

required

A list of WebSearchResult objects, ordered by decreasing relevance.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/search-beta/search#response-warnings-one-of-0)

warnings

Warning · object\[\] \| null

Warnings for the search request, if any.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/search-beta/search#response-usage-one-of-0)

usage

UsageItem · object\[\] \| null

Usage metrics for the search request.

Showchild attributes

[Extract](https://docs.parallel.ai/api-reference/extract-beta/extract) [List Monitors](https://docs.parallel.ai/api-reference/monitor/list-monitors)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Add Enrichment to FindAll Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Add Enrichment to FindAll Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

class CompanyEnrichment(BaseModel):
    ceo_name: str = Field(
        description="Name of the CEO"
    )
    founding_year: str = Field(
        description="Year the company was founded"
    )

run = client.beta.findall.enrich(
    findall_id="findall_40e0ab8c10754be0b7a16477abb38a2f",
    processor="core",
    output_schema=CompanyEnrichment
)

print(f"FindAll run {run.findall_id} enriched: {run.model_dump_json(indent=2)}")
```

200

404

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    }\
  ],
  "enrichments": [\
    {\
      "processor": "core",\
      "output_schema": {\
        "json_schema": {\
          "type": "object",\
          "properties": {\
            "ceo_name": {\
              "type": "string",\
              "description": "Name of the current CEO of the company. If the CEO is not publicly known, provide the name of the highest-ranking executive or founder. If no information is available, return null."\
            }\
          }\
        },\
        "type": "json"\
      }\
    }\
  ],
  "generator": "core",
  "match_limit": 50
}
```

POST

/

v1beta

/

findall

/

runs

/

{findall\_id}

/

enrich

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

class CompanyEnrichment(BaseModel):
    ceo_name: str = Field(
        description="Name of the CEO"
    )
    founding_year: str = Field(
        description="Year the company was founded"
    )

run = client.beta.findall.enrich(
    findall_id="findall_40e0ab8c10754be0b7a16477abb38a2f",
    processor="core",
    output_schema=CompanyEnrichment
)

print(f"FindAll run {run.findall_id} enriched: {run.model_dump_json(indent=2)}")
```

200

404

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    }\
  ],
  "enrichments": [\
    {\
      "processor": "core",\
      "output_schema": {\
        "json_schema": {\
          "type": "object",\
          "properties": {\
            "ceo_name": {\
              "type": "string",\
              "description": "Name of the current CEO of the company. If the CEO is not publicly known, provide the name of the highest-ranking executive or founder. If no information is available, return null."\
            }\
          }\
        },\
        "type": "json"\
      }\
    }\
  ],
  "generator": "core",
  "match_limit": 50
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#parameter-findall-id)

findall\_id

string

required

#### Body

application/json

Input model for FindAll enrich.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#body-output-schema)

output\_schema

JsonSchema · object

required

JSON schema for the enrichment output schema for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#body-processor)

processor

string

default:core

Processor to use for the task.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#body-mcp-servers-one-of-0)

mcp\_servers

McpServer · object\[\] \| null

List of MCP servers to use for the task.

Showchild attributes

#### Response

200

application/json

Successful Response

Response model for FindAll ingest.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#response-objective)

objective

string

required

Natural language objective of the FindAll run.

Example:

`"Find all AI companies that raised Series A funding in 2024"`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#response-entity-type)

entity\_type

string

required

Type of the entity for the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#response-match-conditions)

match\_conditions

MatchCondition · object\[\]

required

List of match conditions for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#response-enrichments-one-of-0)

enrichments

FindAllEnrichInput · object\[\] \| null

List of enrichment inputs for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#response-generator)

generator

enum<string>

default:core

The generator of the FindAll run.

Available options:

`base`,

`core`,

`pro`,

`preview`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run#response-match-limit-one-of-0)

match\_limit

integer \| null

Max number of candidates to evaluate

[Extend FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run) [Cancel FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve Event Group - Parallel

**URL:** https://docs.parallel.ai/api-reference/monitor/retrieve-event-group

[Skip to main content](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

Retrieve Event Group

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Retrieve Event Group

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}/event_groups/{event_group_id}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "events": [\
    {\
      "type": "event",\
      "event_group_id": "mevtgrp_b0079f70195e4258eab1e7284340f1a9ec3a8033ed236a24",\
      "output": "New product launch announced",\
      "event_date": "2025-01-15",\
      "source_urls": [\
        "https://example.com/news"\
      ],\
      "result": {\
        "type": "text",\
        "content": "New product launch announced"\
      }\
    }\
  ]
}
```

GET

/

v1alpha

/

monitors

/

{monitor\_id}

/

event\_groups

/

{event\_group\_id}

Try it

Retrieve Event Group

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}/event_groups/{event_group_id}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "events": [\
    {\
      "type": "event",\
      "event_group_id": "mevtgrp_b0079f70195e4258eab1e7284340f1a9ec3a8033ed236a24",\
      "output": "New product launch announced",\
      "event_date": "2025-01-15",\
      "source_urls": [\
        "https://example.com/news"\
      ],\
      "result": {\
        "type": "text",\
        "content": "New product launch announced"\
      }\
    }\
  ]
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group#parameter-monitor-id)

monitor\_id

string

required

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group#parameter-event-group-id)

event\_group\_id

string

required

#### Response

200

application/json

Successful Response

Response containing monitor execution history.

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group#response-events)

events

(MonitorEventDetail · object \| MonitorExecutionError · object \| MonitorCompletion · object)\[\]

required

List of execution events for the monitor.

Event response for a material change detected by a monitor.

- MonitorEventDetail

- MonitorExecutionError

- MonitorCompletion

Showchild attributes

[Delete Monitor](https://docs.parallel.ai/api-reference/monitor/delete-monitor) [List Events](https://docs.parallel.ai/api-reference/monitor/list-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# LangChain - Parallel

**URL:** https://docs.parallel.ai/integrations/langchain

[Skip to main content](https://docs.parallel.ai/integrations/langchain#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

LangChain

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features](https://docs.parallel.ai/integrations/langchain#features)
- [Installation](https://docs.parallel.ai/integrations/langchain#installation)
- [Setup](https://docs.parallel.ai/integrations/langchain#setup)
- [Chat Models](https://docs.parallel.ai/integrations/langchain#chat-models)
- [ChatParallelWeb](https://docs.parallel.ai/integrations/langchain#chatparallelweb)
- [Basic Usage](https://docs.parallel.ai/integrations/langchain#basic-usage)
- [Streaming Responses](https://docs.parallel.ai/integrations/langchain#streaming-responses)
- [Async Operations](https://docs.parallel.ai/integrations/langchain#async-operations)
- [Conversation Context](https://docs.parallel.ai/integrations/langchain#conversation-context)
- [Configuration Options](https://docs.parallel.ai/integrations/langchain#configuration-options)
- [Real-Time Web Research](https://docs.parallel.ai/integrations/langchain#real-time-web-research)
- [Integration with LangChain](https://docs.parallel.ai/integrations/langchain#integration-with-langchain)
- [Chains](https://docs.parallel.ai/integrations/langchain#chains)
- [Agents](https://docs.parallel.ai/integrations/langchain#agents)
- [Search API](https://docs.parallel.ai/integrations/langchain#search-api)
- [ParallelWebSearchTool](https://docs.parallel.ai/integrations/langchain#parallelwebsearchtool)
- [Search API Configuration](https://docs.parallel.ai/integrations/langchain#search-api-configuration)
- [Search with Specific Queries](https://docs.parallel.ai/integrations/langchain#search-with-specific-queries)
- [Tool Usage in Agents](https://docs.parallel.ai/integrations/langchain#tool-usage-in-agents)
- [Extract API](https://docs.parallel.ai/integrations/langchain#extract-api)
- [ParallelExtractTool](https://docs.parallel.ai/integrations/langchain#parallelextracttool)
- [Extract with Search Objective and Advanced Options](https://docs.parallel.ai/integrations/langchain#extract-with-search-objective-and-advanced-options)
- [Extract with Search Queries](https://docs.parallel.ai/integrations/langchain#extract-with-search-queries)
- [Content Length Control](https://docs.parallel.ai/integrations/langchain#content-length-control)
- [Extract API Configuration](https://docs.parallel.ai/integrations/langchain#extract-api-configuration)
- [Extract Error Handling](https://docs.parallel.ai/integrations/langchain#extract-error-handling)
- [Async Extract](https://docs.parallel.ai/integrations/langchain#async-extract)
- [Error Handling](https://docs.parallel.ai/integrations/langchain#error-handling)
- [Examples](https://docs.parallel.ai/integrations/langchain#examples)

Add Parallel’s search and extract tools and search-powered chat model to your LangChain applications.

View the complete repository for this integration [here](https://github.com/parallel-web/langchain-parallel)

## [​](https://docs.parallel.ai/integrations/langchain\#features)  Features

- **Chat Models**: `ChatParallelWeb` \- Real-time web research chat completions
- **Search Tools**: `ParallelWebSearchTool` \- Direct access to Parallel’s Search API
- **Extract Tools**: `ParallelExtractTool` \- Clean content extraction from web pages
- **Streaming Support**: Real-time response streaming
- **Async/Await**: Full asynchronous operation support
- **OpenAI Compatible**: Uses familiar OpenAI SDK patterns
- **LangChain Integration**: Seamless integration with LangChain ecosystem

## [​](https://docs.parallel.ai/integrations/langchain\#installation)  Installation

Copy

Ask AI

```
pip install langchain-parallel
```

## [​](https://docs.parallel.ai/integrations/langchain\#setup)  Setup

1. Get your API key from [Parallel](https://platform.parallel.ai/)
2. Set your API key as an environment variable:

Copy

Ask AI

```
export PARALLEL_API_KEY="your-api-key-here"
```

## [​](https://docs.parallel.ai/integrations/langchain\#chat-models)  Chat Models

### [​](https://docs.parallel.ai/integrations/langchain\#chatparallelweb)  ChatParallelWeb

The `ChatParallelWeb` class provides access to Parallel’s Chat API, which combines language models with real-time web research capabilities.

#### [​](https://docs.parallel.ai/integrations/langchain\#basic-usage)  Basic Usage

Copy

Ask AI

```
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_parallel.chat_models import ChatParallelWeb

# Initialize the chat model
chat = ChatParallelWeb(
    model="speed",  # Parallel's chat model
    temperature=0.7,  # Optional: ignored by Parallel
    max_tokens=None,  # Optional: ignored by Parallel
)

# Create messages
messages = [\
    SystemMessage(content="You are a helpful assistant with access to real-time web information."),\
    HumanMessage(content="What are the latest developments in artificial intelligence?")\
]

# Get response
response = chat.invoke(messages)
print(response.content)
```

#### [​](https://docs.parallel.ai/integrations/langchain\#streaming-responses)  Streaming Responses

Copy

Ask AI

```
# Stream responses for real-time output
for chunk in chat.stream(messages):
    if chunk.content:
        print(chunk.content, end="", flush=True)
```

#### [​](https://docs.parallel.ai/integrations/langchain\#async-operations)  Async Operations

Copy

Ask AI

```
import asyncio

async def main():
    # Async invoke
    response = await chat.ainvoke(messages)
    print(response.content)

    # Async streaming
    async for chunk in chat.astream(messages):
        if chunk.content:
            print(chunk.content, end="", flush=True)

asyncio.run(main())
```

#### [​](https://docs.parallel.ai/integrations/langchain\#conversation-context)  Conversation Context

Copy

Ask AI

```
# Maintain conversation history
messages = [\
    SystemMessage(content="You are a helpful assistant.")\
]

# First turn
messages.append(HumanMessage(content="What is machine learning?"))
response = chat.invoke(messages)
messages.append(response)  # Add assistant response

# Example: Current events
messages = [\
    SystemMessage(content="You are a research assistant with access to real-time web data."),\
    HumanMessage(content="What happened in the stock market today?")\
]

response = chat.invoke(messages)
print(response.content)  # Gets real-time market information
```

### [​](https://docs.parallel.ai/integrations/langchain\#integration-with-langchain)  Integration with LangChain

#### [​](https://docs.parallel.ai/integrations/langchain\#chains)  Chains

Copy

Ask AI

```
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Create a chain
prompt = ChatPromptTemplate.from_messages([\
    ("system", "You are a helpful research assistant with access to real-time web information."),\
    ("human", "{question}")\
])

chain = prompt | chat | StrOutputParser()

# Use the chain
result = chain.invoke({"question": "What are the latest AI breakthroughs?"})
print(result)
```

#### [​](https://docs.parallel.ai/integrations/langchain\#agents)  Agents

Copy

Ask AI

```
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

# Create an agent with web research capabilities
prompt = ChatPromptTemplate.from_messages([\
    ("system", "You are a helpful assistant with access to real-time web information."),\
    ("human", "{input}"),\
    ("placeholder", "{agent_scratchpad}"),\
])

# Use with tools for additional capabilities
# agent = create_openai_functions_agent(chat, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools)
```

## [​](https://docs.parallel.ai/integrations/langchain\#search-api)  Search API

The Search API provides direct access to Parallel’s web search capabilities, returning structured, compressed excerpts optimized for LLM consumption.

### [​](https://docs.parallel.ai/integrations/langchain\#parallelwebsearchtool)  ParallelWebSearchTool

The search tool provides direct access to Parallel’s Search API:

Copy

Ask AI

```
from langchain_parallel import ParallelWebSearchTool

# Initialize the search tool
search_tool = ParallelWebSearchTool()

# {
#     "search_id": "search_123...",
#     "results": [\
#         {\
#             "url": "https://example.com/renewable-energy",\
#             "title": "Latest Renewable Energy Developments",\
#             "excerpts": [\
#                 "Solar energy has seen remarkable growth...",\
#                 "Wind power capacity increased by 15%..."\
#             ]\
#         }\
#     ]
# Search with specific queries
result = search_tool.invoke({
    "search_queries": [\
        "renewable energy 2024",\
        "solar power developments",\
        "wind energy statistics"\
    ],
    "mode": "fast"
})
```

#### [​](https://docs.parallel.ai/integrations/langchain\#tool-usage-in-agents)  Tool Usage in Agents

The search tool works seamlessly with LangChain agents:

Copy

Ask AI

```
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

# Create agent with search capabilities
tools = [search_tool]

prompt = ChatPromptTemplate.from_messages([\
    ("system", "You are a research assistant. Use the search tool to find current information."),\
    ("human", "{input}"),\
    ("placeholder", "{agent_scratchpad}"),\
])

agent = create_openai_functions_agent(chat, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Run the agent
result = agent_executor.invoke({
    "input": "What are the latest developments in artificial intelligence?"
})
print(result["output"])
```

## [​](https://docs.parallel.ai/integrations/langchain\#extract-api)  Extract API

The Extract API provides clean content extraction from web pages, returning structured markdown-formatted content optimized for LLM consumption.

### [​](https://docs.parallel.ai/integrations/langchain\#parallelextracttool)  ParallelExtractTool

The extract tool extracts clean, structured content from web pages:

Copy

Ask AI

```
from langchain_parallel import ParallelExtractTool

# Initialize the extract tool
extract_tool = ParallelExtractTool()

# Extract from a single URL
result = extract_tool.invoke({
    "urls": ["https://en.wikipedia.org/wiki/Artificial_intelligence"]
})

print(result)
# [\
#     {\
#         "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",\
#         "title": "Artificial intelligence - Wikipedia",\
#         "content": "# Artificial intelligence\n\nMain content in markdown...",\
#         "publish_date": "2024-01-15"  # Optional\
#     }\
# ]
```

#### [​](https://docs.parallel.ai/integrations/langchain\#extract-with-search-objective-and-advanced-options)  Extract with Search Objective and Advanced Options

Focus extraction on specific topics using search objectives, with control over excerpts and fetch policy:

Copy

Ask AI

```
# Extract content focused on a specific objective with excerpt settings
result = extract_tool.invoke({
    "urls": ["https://en.wikipedia.org/wiki/Artificial_intelligence"],
    "search_objective": "What are the main applications and ethical concerns of AI?",
    "excerpts": {"max_chars_per_result": 2000},
    "full_content": False,
    "fetch_policy": {
        "max_age_seconds": 86400,
        "timeout_seconds": 60,
        "disable_cache_fallback": False
    }
})

# Returns relevant excerpts focused on the objective
print(result[0]["excerpts"])  # List of relevant text excerpts
```

#### [​](https://docs.parallel.ai/integrations/langchain\#extract-with-search-queries)  Extract with Search Queries

Extract content relevant to specific search queries:

Copy

Ask AI

```
# Extract content focused on specific queries
result = extract_tool.invoke({
    "urls": [\
        "https://en.wikipedia.org/wiki/Machine_learning",\
        "https://en.wikipedia.org/wiki/Deep_learning"\
    ],
    "search_queries": ["neural networks", "training algorithms", "applications"],
    "excerpts": True
})

for item in result:
    print(f"Title: {item['title']}")
    print(f"Relevant excerpts: {len(item['excerpts'])}")
    print()
```

#### [​](https://docs.parallel.ai/integrations/langchain\#content-length-control)  Content Length Control

Copy

Ask AI

```
# Mix of valid and invalid URLs
result = extract_tool.invoke({
    "urls": [\
        "https://en.wikipedia.org/wiki/Python_(programming_language)",\
        "https://this-domain-does-not-exist-12345.com/"\
    ]
})

for item in result:
    if "error_type" in item:
        print(f"Failed: {item['url']} - {item['content']}")
    else:
        print(f"Success: {item['url']} - {len(item['content'])} chars")
```

#### [​](https://docs.parallel.ai/integrations/langchain\#async-extract)  Async Extract

Copy

Ask AI

```
import asyncio

async def extract_async():
    result = await extract_tool.ainvoke({
        "urls": ["https://en.wikipedia.org/wiki/Artificial_intelligence"]
    })
    return result

# Run async extraction
result = asyncio.run(extract_async())
```

## [​](https://docs.parallel.ai/integrations/langchain\#error-handling)  Error Handling

Copy

Ask AI

```
try:
    response = chat.invoke(messages)
    print(response.content)
except ValueError as e:
    if "API key not found" in str(e):
        print("Please set your PARALLEL_API_KEY environment variable")
    else:
        print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## [​](https://docs.parallel.ai/integrations/langchain\#examples)  Examples

See the `examples/` and `docs/` directories for complete working examples:

- `examples/chat_example.py` \- Chat model usage examples
- `docs/search_tool.ipynb` \- Search tool examples and tutorials
- `docs/extract_tool.ipynb` \- Extract tool examples and tutorials

Examples include:

- Basic synchronous usage
- Streaming responses
- Async operations
- Conversation management
- Tool usage in agents

[Google Vertex AI](https://docs.parallel.ai/integrations/google-vertex) [n8n](https://docs.parallel.ai/integrations/n8n)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Get FindAll Run Schema - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Get FindAll Run Schema

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

schema = client.beta.findall.schema(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {schema.findall_id} schema: {schema.model_dump_json(indent=2)}")
```

200

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    }\
  ],
  "enrichments": [\
    {\
      "processor": "core",\
      "output_schema": {\
        "json_schema": {\
          "type": "object",\
          "properties": {\
            "ceo_name": {\
              "type": "string",\
              "description": "Name of the current CEO of the company. If the CEO is not publicly known, provide the name of the highest-ranking executive or founder. If no information is available, return null."\
            }\
          }\
        },\
        "type": "json"\
      }\
    }\
  ],
  "generator": "core",
  "match_limit": 50
}
```

GET

/

v1beta

/

findall

/

runs

/

{findall\_id}

/

schema

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

schema = client.beta.findall.schema(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {schema.findall_id} schema: {schema.model_dump_json(indent=2)}")
```

200

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    }\
  ],
  "enrichments": [\
    {\
      "processor": "core",\
      "output_schema": {\
        "json_schema": {\
          "type": "object",\
          "properties": {\
            "ceo_name": {\
              "type": "string",\
              "description": "Name of the current CEO of the company. If the CEO is not publicly known, provide the name of the highest-ranking executive or founder. If no information is available, return null."\
            }\
          }\
        },\
        "type": "json"\
      }\
    }\
  ],
  "generator": "core",
  "match_limit": 50
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#parameter-findall-id)

findall\_id

string

required

#### Response

200

application/json

Successful Response

Response model for FindAll ingest.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#response-objective)

objective

string

required

Natural language objective of the FindAll run.

Example:

`"Find all AI companies that raised Series A funding in 2024"`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#response-entity-type)

entity\_type

string

required

Type of the entity for the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#response-match-conditions)

match\_conditions

MatchCondition · object\[\]

required

List of match conditions for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#response-enrichments-one-of-0)

enrichments

FindAllEnrichInput · object\[\] \| null

List of enrichment inputs for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#response-generator)

generator

enum<string>

default:core

The generator of the FindAll run.

Available options:

`base`,

`core`,

`pro`,

`preview`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema#response-match-limit-one-of-0)

match\_limit

integer \| null

Max number of candidates to evaluate

[Cancel FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Update Monitor - Parallel

**URL:** https://docs.parallel.ai/api-reference/monitor/update-monitor

[Skip to main content](https://docs.parallel.ai/api-reference/monitor/update-monitor#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

Update Monitor

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Update Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}"

payload = {}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",
  "query": "Extract recent news about AI",
  "status": "active",
  "cadence": "daily",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "https://example.com/webhook",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "created_at": "2025-04-23T20:21:48.037943Z"
}
```

POST

/

v1alpha

/

monitors

/

{monitor\_id}

Try it

Update Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}"

payload = {}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",
  "query": "Extract recent news about AI",
  "status": "active",
  "cadence": "daily",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "https://example.com/webhook",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "created_at": "2025-04-23T20:21:48.037943Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#parameter-monitor-id)

monitor\_id

string

required

#### Body

application/json

Request to update a monitor's configuration.

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#body-query-one-of-0)

query

string \| null

Updated search query for the monitor. Use this for minor updates to prompts and instructions only. Major changes to the query may lead to unexpected results in change detection, as the monitor compares new results with what was previously seen.

Example:

`"Extract recent news about AI"`

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#body-cadence-one-of-0)

cadence

enum<string> \| null

Updated cadence of the monitor.

Available options:

`daily`,

`weekly`,

`hourly`,

`every_two_weeks`

Example:

`"daily"`

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#body-webhook-one-of-0)

webhook

MonitorWebhook · object

Updated webhook configuration.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#body-metadata-one-of-0)

metadata

Metadata · object

Updated user-provided metadata. This field is returned in webhook notifications, enabling you to map responses to corresponding objects in your application.

Showchild attributes

Example:

```
{
  "slack_thread_id": "1234567890.123456",
  "user_id": "U123ABC"
}
```

#### Response

200

application/json

Successful Response

Response object for a monitor, including its status, cadence and metadata.

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-monitor-id)

monitor\_id

string

required

ID of the monitor.

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-query)

query

string

required

The query being monitored.

Example:

`"Recent news about LLM models."`

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-status)

status

enum<string>

required

Status of the monitor.

Available options:

`active`,

`canceled`

Examples:

`"active"`

`"canceled"`

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-cadence)

cadence

enum<string>

required

Cadence of the monitor.

Available options:

`daily`,

`weekly`,

`hourly`,

`every_two_weeks`

Examples:

`"daily"`

`"weekly"`

`"hourly"`

`"every_two_weeks"`

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-created-at)

created\_at

string<date-time>

required

Timestamp of the creation of the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the monitor.

Showchild attributes

Example:

```
{ "key": "value" }
```

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-webhook-one-of-0)

webhook

MonitorWebhook · object

Webhook configuration for the monitor.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-output-schema-one-of-0)

output\_schema

JsonSchema · object

Output schema for the monitor event.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/update-monitor#response-last-run-at-one-of-0)

last\_run\_at

string \| null

Timestamp of the last run for the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[Retrieve Monitor](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor) [Delete Monitor](https://docs.parallel.ai/api-reference/monitor/delete-monitor)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Claude Code Plugin Marketplace - Parallel

**URL:** https://docs.parallel.ai/integrations/claude-code-marketplace

[Skip to main content](https://docs.parallel.ai/integrations/claude-code-marketplace#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Claude Code Plugin Marketplace

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features](https://docs.parallel.ai/integrations/claude-code-marketplace#features)
- [Prerequisites](https://docs.parallel.ai/integrations/claude-code-marketplace#prerequisites)
- [Installation](https://docs.parallel.ai/integrations/claude-code-marketplace#installation)
- [Slash Commands](https://docs.parallel.ai/integrations/claude-code-marketplace#slash-commands)
- [Usage](https://docs.parallel.ai/integrations/claude-code-marketplace#usage)
- [Learn More](https://docs.parallel.ai/integrations/claude-code-marketplace#learn-more)

The Parallel plugin for Claude Code gives your coding agent access to live web search, content extraction, deep research, and data enrichment — all available as slash commands and automatic skills directly inside Claude Code.

View the complete repository for this plugin [here](https://github.com/parallel-web/parallel-agent-skills)

## [​](https://docs.parallel.ai/integrations/claude-code-marketplace\#features)  Features

- **Web Search**: Fast, real-time search for current events, documentation lookups, and fact-checking
- **Content Extraction**: Clean content extraction from any URL, including JavaScript-heavy sites and PDFs
- **Deep Research**: Exhaustive, multi-source research reports with configurable depth and processing power
- **Data Enrichment**: Bulk enrichment of companies, people, or products with web-sourced fields like CEO names, funding, and contact info

## [​](https://docs.parallel.ai/integrations/claude-code-marketplace\#prerequisites)  Prerequisites

1

[Navigate to header](https://docs.parallel.ai/integrations/claude-code-marketplace#)

Install the Parallel CLI

Copy

Ask AI

```
curl -fsSL https://parallel.ai/install.sh | bash
```

2

[Navigate to header](https://docs.parallel.ai/integrations/claude-code-marketplace#)

Get your API key

Get your API key from [Parallel](https://platform.parallel.ai/) and set it as an environment variable:

Copy

Ask AI

```
export PARALLEL_API_KEY="your-api-key"
```

## [​](https://docs.parallel.ai/integrations/claude-code-marketplace\#installation)  Installation

Install the plugin from the Claude Code Plugin Marketplace:

Copy

Ask AI

```
/plugin marketplace add parallel-web/parallel-agent-skills
/plugin install parallel
```

Then run the setup command to verify the CLI is installed and authenticated:

Copy

Ask AI

```
/parallel:setup
```

## [​](https://docs.parallel.ai/integrations/claude-code-marketplace\#slash-commands)  Slash Commands

Once installed, the following commands are available in Claude Code:

| Command | Description |
| --- | --- |
| `/parallel:search <query>` | Search the web for current information |
| `/parallel:extract <url>` | Extract content from a URL |
| `/parallel:research <topic>` | Run a deep research task |
| `/parallel:enrich <data>` | Enrich a list of entities with web data |
| `/parallel:status <run_id>` | Check the status of a research task |
| `/parallel:result <run_id>` | Get the results of a completed research task |
| `/parallel:setup` | Install CLI and authenticate |

## [​](https://docs.parallel.ai/integrations/claude-code-marketplace\#usage)  Usage

Beyond slash commands, the plugin also installs skills that Claude Code uses automatically based on context:

- Ask a question that needs current information and Claude will search the web
- Paste a URL and ask Claude to read it — it will extract the content
- Ask for exhaustive research on a topic and Claude will run a deep research task
- Give Claude a list of companies and ask it to find their CEOs — it will use data enrichment

## [​](https://docs.parallel.ai/integrations/claude-code-marketplace\#learn-more)  Learn More

For detailed documentation, skill definitions, and contribution guidelines, see the [parallel-agent-skills repository on GitHub](https://github.com/parallel-web/parallel-agent-skills).For Agent Skills support with other coding agents (Cursor, Cline, Copilot, etc.), see the [Agent Skills](https://docs.parallel.ai/integrations/agent-skills) integration.

[Browser Use](https://docs.parallel.ai/integrations/browseruse) [Google Sheets](https://docs.parallel.ai/integrations/gsuite)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Chat Completions - Parallel

**URL:** https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions

[Skip to main content](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Chat API (Beta)

Chat Completions

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Chat Completions

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1beta/chat/completions"

payload = {
    "model": "<string>",
    "messages": [\
        {\
            "role": "system",\
            "content": "<string>",\
            "name": "<string>"\
        }\
    ]
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

200

422

Copy

Ask AI

```
{
  "id": "<string>",
  "choices": [\
    {\
      "delta": {\
        "content": "<string>",\
        "function_call": {\
          "arguments": "<string>",\
          "name": "<string>"\
        },\
        "refusal": "<string>",\
        "role": "developer",\
        "tool_calls": [\
          {\
            "index": 123,\
            "id": "<string>",\
            "function": {\
              "arguments": "<string>",\
              "name": "<string>"\
            },\
            "type": "<string>"\
          }\
        ]\
      },\
      "index": 123,\
      "finish_reason": "stop",\
      "logprobs": {\
        "content": [\
          {\
            "token": "<string>",\
            "logprob": 123,\
            "top_logprobs": [\
              {\
                "token": "<string>",\
                "logprob": 123,\
                "bytes": [\
                  123\
                ]\
              }\
            ],\
            "bytes": [\
              123\
            ]\
          }\
        ],\
        "refusal": [\
          {\
            "token": "<string>",\
            "logprob": 123,\
            "top_logprobs": [\
              {\
                "token": "<string>",\
                "logprob": 123,\
                "bytes": [\
                  123\
                ]\
              }\
            ],\
            "bytes": [\
              123\
            ]\
          }\
        ]\
      }\
    }\
  ],
  "created": 123,
  "model": "<string>",
  "object": "<string>",
  "service_tier": "auto",
  "system_fingerprint": "<string>",
  "usage": {
    "completion_tokens": 123,
    "prompt_tokens": 123,
    "total_tokens": 123,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 123,
      "audio_tokens": 123,
      "reasoning_tokens": 123,
      "rejected_prediction_tokens": 123
    },
    "prompt_tokens_details": {
      "audio_tokens": 123,
      "cached_tokens": 123
    }
  },
  "basis": []
}
```

POST

/

v1beta

/

chat

/

completions

Try it

Chat Completions

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1beta/chat/completions"

payload = {
    "model": "<string>",
    "messages": [\
        {\
            "role": "system",\
            "content": "<string>",\
            "name": "<string>"\
        }\
    ]
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

200

422

Copy

Ask AI

```
{
  "id": "<string>",
  "choices": [\
    {\
      "delta": {\
        "content": "<string>",\
        "function_call": {\
          "arguments": "<string>",\
          "name": "<string>"\
        },\
        "refusal": "<string>",\
        "role": "developer",\
        "tool_calls": [\
          {\
            "index": 123,\
            "id": "<string>",\
            "function": {\
              "arguments": "<string>",\
              "name": "<string>"\
            },\
            "type": "<string>"\
          }\
        ]\
      },\
      "index": 123,\
      "finish_reason": "stop",\
      "logprobs": {\
        "content": [\
          {\
            "token": "<string>",\
            "logprob": 123,\
            "top_logprobs": [\
              {\
                "token": "<string>",\
                "logprob": 123,\
                "bytes": [\
                  123\
                ]\
              }\
            ],\
            "bytes": [\
              123\
            ]\
          }\
        ],\
        "refusal": [\
          {\
            "token": "<string>",\
            "logprob": 123,\
            "top_logprobs": [\
              {\
                "token": "<string>",\
                "logprob": 123,\
                "bytes": [\
                  123\
                ]\
              }\
            ],\
            "bytes": [\
              123\
            ]\
          }\
        ]\
      }\
    }\
  ],
  "created": 123,
  "model": "<string>",
  "object": "<string>",
  "service_tier": "auto",
  "system_fingerprint": "<string>",
  "usage": {
    "completion_tokens": 123,
    "prompt_tokens": 123,
    "total_tokens": 123,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 123,
      "audio_tokens": 123,
      "reasoning_tokens": 123,
      "rejected_prediction_tokens": 123
    },
    "prompt_tokens_details": {
      "audio_tokens": 123,
      "cached_tokens": 123
    }
  },
  "basis": []
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#authorization-x-api-key)

x-api-key

string

header

required

#### Body

application/json

Request for the chat completions endpoint.

Note that all parameters except for `model`, `stream`, and `response_format`
are ignored.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-model)

model

string

required

The model to use for chat completions.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-messages)

messages

ChatMessage · object\[\]

required

The messages to use for chat completions.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-stream-one-of-0)

stream

boolean \| null

Whether to stream the chat completions.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-response-format)

response\_format

ResponseFormatText · object

The response format to use for chat completions. OpenAI compatible.

- ResponseFormatText

- ResponseFormatJSONSchema

- ResponseFormatJSONObject

Showchild attributes

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-max-tokens-one-of-0)

max\_tokens

integer \| null

The maximum number of tokens to generate. Unsupported.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-temperature-one-of-0)

temperature

number \| null

The temperature to use for chat completions. Unsupported.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-top-p-one-of-0)

top\_p

number \| null

The top p to use for chat completions. Unsupported.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-n-one-of-0)

n

integer \| null

The number of chat completions to generate. Unsupported.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-presence-penalty-one-of-0)

presence\_penalty

number \| null

The presence penalty to use for chat completions. Unsupported.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#body-frequency-penalty-one-of-0)

frequency\_penalty

number \| null

The frequency penalty to use for chat completions. Unsupported.

#### Response

200

application/json

Returns a ChatCompletion object for non-streaming requests (application/json), or a stream of ChatCompletionResponseChunk objects for streaming requests (text/event-stream) when `stream=true` is set in the request.

Chat completion response.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-id)

id

string

required

The id of the chat completion.

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-choices)

choices

Choice · object\[\]

required

Showchild attributes

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-created)

created

integer

required

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-model)

model

string

required

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-object)

object

string

required

Allowed value: `"chat.completion"`

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-service-tier-one-of-0)

service\_tier

enum<string> \| null

Available options:

`auto`,

`default`,

`flex`,

`scale`,

`priority`

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-system-fingerprint-one-of-0)

system\_fingerprint

string \| null

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-usage-one-of-0)

usage

CompletionUsage · object

Showchild attributes

[​](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions#response-basis)

basis

FieldBasis · object\[\]

Basis for the chat completion, including citations and reasoning supporting the output.

Showchild attributes

[Extract](https://docs.parallel.ai/api-reference/extract-beta/extract)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Create FindAll Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Create FindAll Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run_input = {
    "objective": ingest.objective,
    "entity_type": ingest.entity_type,
    "match_conditions": ingest.match_conditions,
    "generator": "base",
    "match_limit": 10,
    "metadata": {
        "run_id": "123",
    },
}

run = client.beta.findall.create(run_input)

print(f"FindAll run {run.findall_id} created, response:")
print(run.model_dump_json(indent=2))
```

200

402

422

429

Copy

Ask AI

```
{
  "findall_id": "findall_56ccc4d188fb41a0803a935cf485c774",
  "status": {
    "status": "queued",
    "is_active": true,
    "metrics": {
      "generated_candidates_count": 0,
      "matched_candidates_count": 0
    }
  },
  "generator": "base",
  "metadata": {},
  "created_at": "2025-09-10T21:02:08.626446Z",
  "modified_at": "2025-09-10T21:02:08.627376Z"
}
```

POST

/

v1beta

/

findall

/

runs

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run_input = {
    "objective": ingest.objective,
    "entity_type": ingest.entity_type,
    "match_conditions": ingest.match_conditions,
    "generator": "base",
    "match_limit": 10,
    "metadata": {
        "run_id": "123",
    },
}

run = client.beta.findall.create(run_input)

print(f"FindAll run {run.findall_id} created, response:")
print(run.model_dump_json(indent=2))
```

200

402

422

429

Copy

Ask AI

```
{
  "findall_id": "findall_56ccc4d188fb41a0803a935cf485c774",
  "status": {
    "status": "queued",
    "is_active": true,
    "metrics": {
      "generated_candidates_count": 0,
      "matched_candidates_count": 0
    }
  },
  "generator": "base",
  "metadata": {},
  "created_at": "2025-09-10T21:02:08.626446Z",
  "modified_at": "2025-09-10T21:02:08.627376Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#parameter-one-of-0)

parallel-beta

string \| null

#### Body

application/json

Input model for FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-objective)

objective

string

required

Natural language objective of the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-entity-type)

entity\_type

string

required

Type of the entity for the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-match-conditions)

match\_conditions

MatchCondition · object\[\]

required

List of match conditions for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-generator)

generator

enum<string>

required

Generator for the FindAll run. One of base, core, pro, preview.

Available options:

`base`,

`core`,

`pro`,

`preview`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-match-limit)

match\_limit

integer

required

Maximum number of matches to find for this FindAll run. Must be between 5 and 1000 (inclusive).

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-exclude-list-one-of-0)

exclude\_list

ExcludeCandidate · object\[\] \| null

List of entity names/IDs to exclude from results.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-metadata-one-of-0)

metadata

Metadata · object

Metadata for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-webhook-one-of-0)

webhook

Webhook · object

Webhook for the FindAll run.

Showchild attributes

#### Response

200

application/json

Successful Response

FindAll run object with status and metadata.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#response-findall-id)

findall\_id

string

required

ID of the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#response-status)

status

FindAllRunStatus · object

required

Status object for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#response-generator)

generator

enum<string>

required

Generator for the FindAll run.

Available options:

`base`,

`core`,

`pro`,

`preview`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#response-metadata-one-of-0)

metadata

Metadata · object

Metadata for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#response-created-at-one-of-0)

created\_at

string \| null

Timestamp of the creation of the run, in RFC 3339 format.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#response-modified-at-one-of-0)

modified\_at

string \| null

Timestamp of the latest modification to the FindAll run result, in RFC 3339 format.

[Ingest FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run) [Retrieve FindAll Run Status](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Create Task Group - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-beta/create-task-group

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks (Beta)

Create Task Group

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group = client.beta.task_group.create(metadata={"key": "value"})
print(task_group.task_group_id)
```

200

422

Copy

Ask AI

```
{
  "taskgroup_id": "<string>",
  "status": {
    "num_task_runs": 123,
    "task_run_status_counts": {},
    "is_active": true,
    "status_message": "<string>",
    "modified_at": "2025-04-24T18:56:22.513132Z"
  },
  "created_at": "2025-04-24T18:56:22.513132Z",
  "metadata": {}
}
```

POST

/

v1beta

/

tasks

/

groups

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group = client.beta.task_group.create(metadata={"key": "value"})
print(task_group.task_group_id)
```

200

422

Copy

Ask AI

```
{
  "taskgroup_id": "<string>",
  "status": {
    "num_task_runs": 123,
    "task_run_status_counts": {},
    "is_active": true,
    "status_message": "<string>",
    "modified_at": "2025-04-24T18:56:22.513132Z"
  },
  "created_at": "2025-04-24T18:56:22.513132Z",
  "metadata": {}
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group#authorization-x-api-key)

x-api-key

string

header

required

#### Body

application/json

Request to create a task group.

[​](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group#body-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the task group.

Showchild attributes

#### Response

200

application/json

Successful Response

Response object for a task group, including its status and metadata.

[​](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group#response-taskgroup-id)

taskgroup\_id

string

required

ID of the group.

[​](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group#response-status)

status

TaskGroupStatus · object

required

Status of the group.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group#response-created-at-one-of-0)

created\_at

string \| null

required

Timestamp of the creation of the group, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the group.

Showchild attributes

[Stream Task Run Events](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events) [Retrieve Task Group](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# List Events - Parallel

**URL:** https://docs.parallel.ai/api-reference/monitor/list-events

[Skip to main content](https://docs.parallel.ai/api-reference/monitor/list-events#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

List Events

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

List Events

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}/events?lookback_period=10d"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "events": [\
    {\
      "type": "event",\
      "event_group_id": "mevtgrp_b0079f70195e4258eab1e7284340f1a9ec3a8033ed236a24",\
      "output": "New product launch announced",\
      "event_date": "2025-01-15",\
      "source_urls": [\
        "https://example.com/news"\
      ],\
      "result": {\
        "type": "text",\
        "content": "New product launch announced"\
      }\
    },\
    {\
      "type": "completion",\
      "monitor_ts": "completed_2025-01-15T10:30:00Z"\
    },\
    {\
      "type": "error",\
      "error": "Error occurred while processing the event",\
      "id": "error_2025-01-15T10:30:00Z",\
      "date": "2025-01-15T10:30:00Z"\
    }\
  ]
}
```

GET

/

v1alpha

/

monitors

/

{monitor\_id}

/

events

Try it

List Events

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}/events?lookback_period=10d"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "events": [\
    {\
      "type": "event",\
      "event_group_id": "mevtgrp_b0079f70195e4258eab1e7284340f1a9ec3a8033ed236a24",\
      "output": "New product launch announced",\
      "event_date": "2025-01-15",\
      "source_urls": [\
        "https://example.com/news"\
      ],\
      "result": {\
        "type": "text",\
        "content": "New product launch announced"\
      }\
    },\
    {\
      "type": "completion",\
      "monitor_ts": "completed_2025-01-15T10:30:00Z"\
    },\
    {\
      "type": "error",\
      "error": "Error occurred while processing the event",\
      "id": "error_2025-01-15T10:30:00Z",\
      "date": "2025-01-15T10:30:00Z"\
    }\
  ]
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/monitor/list-events#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/monitor/list-events#parameter-monitor-id)

monitor\_id

string

required

#### Query Parameters

[​](https://docs.parallel.ai/api-reference/monitor/list-events#parameter-lookback-period)

lookback\_period

string

default:10d

Lookback period to fetch events from. Sample values: `10d`, `1w`. A minimum of 1 day is supported and with one day increments. Use `d` for days, `w` for weeks.

#### Response

200

application/json

Successful Response

Response containing monitor execution history.

[​](https://docs.parallel.ai/api-reference/monitor/list-events#response-events)

events

(MonitorEventDetail · object \| MonitorExecutionError · object \| MonitorCompletion · object)\[\]

required

List of execution events for the monitor.

Event response for a material change detected by a monitor.

- MonitorEventDetail

- MonitorExecutionError

- MonitorCompletion

Showchild attributes

[Retrieve Event Group](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group) [Simulate Event](https://docs.parallel.ai/api-reference/monitor/simulate-event)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve Task Run Result - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks v1

Retrieve Task Run Result

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Beta params

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

# If task run has beta output fields
task_run_result = client.beta.task_run.result(
    run_id="run_id",
    betas=["mcp-server-2025-07-17"]
)
print(task_run_result.output)
```

200

401

404

408

422

Copy

Ask AI

```
{
  "run": {
    "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
    "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
    "status": "completed",
    "is_active": false,
    "processor": "core",
    "metadata": {
      "my_key": "my_value"
    },
    "created_at": "2025-04-23T20:21:48.037943Z",
    "modified_at": "2025-04-23T20:21:48.037943Z"
  },
  "output": {
    "basis": [],
    "type": "json",
    "content": {
      "gdp": "$3.1 trillion (2023)"
    }
  }
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result#parameter-run-id)

run\_id

string

required

#### Query Parameters

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result#parameter-timeout)

timeout

integer

default:600

#### Response

200

application/json

Successful Response

- TaskRunResult

- BetaTaskRunResult

Result of a task run.

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result#response-one-of-0-run)

run

TaskRun · object

required

Task run object with status 'completed'.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result#response-one-of-0-output)

output

TaskRunTextOutput · object

required

Output from a task that returns text.

- TaskRunTextOutput

- TaskRunJsonOutput

Showchild attributes

[Retrieve Task Run Input](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input) [Stream Task Run Events](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Generators - Parallel

**URL:** https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing

[Skip to main content](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Generators

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Generators](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#generators)
- [How to Choose](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#how-to-choose)
- [1\. Start with Preview](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#1-start-with-preview)
- [2\. Choosing the Right Generator](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#2-choosing-the-right-generator)
- [Enrichments](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#enrichments)
- [Additional Notes](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#additional-notes)
- [Related Topics](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing#related-topics)

FindAll offers different generators that determine the quality and thoroughness of FindAll run results. See [Pricing](https://docs.parallel.ai/getting-started/pricing) for generator costs and all API rates.

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing\#generators)  Generators

| Generator | Best For | Candidate Pool | Expected Match Rate |
| --- | --- | --- | --- |
| `preview` | Testing queries before committing to a full run | ~10 candidates evaluated | Varies — use to validate schema |
| `base` | Broad, common queries where you expect many matches | Moderate pool | Higher (broad criteria match more candidates) |
| `core` | Specific queries with moderate expected matches | Large pool | Moderate (balanced breadth and depth) |
| `pro` | Highly specific queries with rare or hard-to-find matches | Largest pool | Lower per candidate (thorough search for rare matches) |

**Candidate pool size matters**: Each generator evaluates a different number of candidates. `preview` evaluates ~10, while `pro` searches the most thoroughly. If you’re getting 0 matches, try upgrading to a stronger generator before modifying your query — the issue may be pool size, not query quality.

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing\#how-to-choose)  How to Choose

### [​](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing\#1-start-with-preview)  1\. Start with Preview

Always test your query with `preview` first to validate your approach and get a sense of how many matches to expect. See [Preview](https://docs.parallel.ai/findall-api/features/findall-preview).

### [​](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing\#2-choosing-the-right-generator)  2\. Choosing the Right Generator

Based on your preview results and query characteristics:**Choose `base` when:**

- You expect many matches (e.g., “companies in healthcare”)
- Your query has broad criteria that are common
- You’re searching for fewer than 20 matches where the low fixed cost matters most

**Choose `core` when:**

- You expect a moderate number of matches (e.g., “healthcare companies using AI for diagnostics”)
- Your query is fairly specific but not extremely rare
- You need between 20-50 matches

**Choose `pro` when:**

- You expect few matches or very specific criteria (e.g., “Series A healthcare AI companies with FDA-approved products”)
- Your query requires the most thorough and comprehensive search
- The higher per-match cost is acceptable for your use case

**Note:** For match counts above 50, the per-match cost becomes more significant than the fixed cost in your total bill. When using enrichments, consider that enrichment costs also scale with the number of matches.

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing\#enrichments)  Enrichments

When adding [enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich) to extract additional data from your matches, each enrichment adds its own per-match cost based on the [Task API processor](https://docs.parallel.ai/task-api/guides/choose-a-processor) you choose. Since enrichments run on every match and you can add multiple enrichments, they can significantly impact your total costs for high-match queries. Choose enrichment processors based on the complexity of data extraction needed.

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing\#additional-notes)  Additional Notes

- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Fixed cost is not charged again, only per-match costs for new matches. If enrichments are present, they also run on new matches at the same enrichment processor cost.
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Enrichments are charged based on Task API processor pricing × number of matches. You can add multiple enrichments using different processors, and each enrichment’s cost is calculated separately.
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: You’re charged for work completed before cancellation, including any enrichments that finished.

**Tip:** If a run terminates early, consider using a more advanced generator (like `pro` instead of `base`) or refining your query criteria to be more achievable.

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing\#related-topics)  Related Topics

- **[Pricing](https://docs.parallel.ai/getting-started/pricing)**: Consolidated pricing for all Parallel APIs
- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Task API Processors](https://docs.parallel.ai/task-api/guides/choose-a-processor)**: Understand processor options for enrichments
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and how to cancel runs
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#body-generator)**: Complete endpoint documentation

[Quickstart](https://docs.parallel.ai/findall-api/findall-quickstart) [Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Cancel FindAll Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Cancel FindAll Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run = client.beta.findall.cancel(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {run.findall_id} cancelled: {run.model_dump_json(indent=2)}")
```

404

409

422

Copy

Ask AI

```
{
  "type": "error",
  "error": {
    "ref_id": "fcb2b4f3-c75e-4186-87bc-caa1a8381331",
    "message": "FindAll run not found"
  }
}
```

POST

/

v1beta

/

findall

/

runs

/

{findall\_id}

/

cancel

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run = client.beta.findall.cancel(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {run.findall_id} cancelled: {run.model_dump_json(indent=2)}")
```

404

409

422

Copy

Ask AI

```
{
  "type": "error",
  "error": {
    "ref_id": "fcb2b4f3-c75e-4186-87bc-caa1a8381331",
    "message": "FindAll run not found"
  }
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run#parameter-findall-id)

findall\_id

string

required

#### Response

200

application/json

Successful Response

[Add Enrichment to FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run) [Get FindAll Run Schema](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Apache Spark - Parallel

**URL:** https://docs.parallel.ai/data-integrations/spark

[Skip to main content](https://docs.parallel.ai/data-integrations/spark#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Data Integrations

Apache Spark

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features](https://docs.parallel.ai/data-integrations/spark#features)
- [Installation](https://docs.parallel.ai/data-integrations/spark#installation)
- [Setup](https://docs.parallel.ai/data-integrations/spark#setup)
- [Configuration Options](https://docs.parallel.ai/data-integrations/spark#configuration-options)
- [Basic Usage](https://docs.parallel.ai/data-integrations/spark#basic-usage)
- [UDF Parameters](https://docs.parallel.ai/data-integrations/spark#udf-parameters)
- [Parsing Results](https://docs.parallel.ai/data-integrations/spark#parsing-results)
- [Including Basis/Citations](https://docs.parallel.ai/data-integrations/spark#including-basis%2Fcitations)
- [Processor Selection](https://docs.parallel.ai/data-integrations/spark#processor-selection)
- [Best Practices](https://docs.parallel.ai/data-integrations/spark#best-practices)

This integration is ideal for data engineers who need to enrich large datasets with web intelligence directly in their Spark pipelines—without leaving SQL or building custom API integrations.Parallel provides SQL-native User Defined Functions (UDFs) for Apache Spark that enable data enrichment directly in your SQL queries. The UDFs process rows concurrently within each partition for optimal performance.

View the complete demo notebooks:

- [Spark Enrichment Demo](https://github.com/parallel-web/parallel-web-tools/blob/main/notebooks/spark_enrichment_demo.ipynb)
- [Spark Streaming Demo](https://github.com/parallel-web/parallel-web-tools/blob/main/notebooks/spark_streaming_demo.ipynb)

## [​](https://docs.parallel.ai/data-integrations/spark\#features)  Features

- **SQL-Native**: Use `parallel_enrich()` directly in Spark SQL queries
- **Concurrent Processing**: All rows in each partition are processed concurrently using asyncio
- **Configurable Processors**: Choose from lite-fast to ultra for speed vs thoroughness tradeoffs
- **Structured Output**: Returns JSON that can be parsed with Spark’s `from_json()`

## [​](https://docs.parallel.ai/data-integrations/spark\#installation)  Installation

Copy

Ask AI

```
pip install parallel-web-tools[spark]
```

## [​](https://docs.parallel.ai/data-integrations/spark\#setup)  Setup

1. Get your API key from [Parallel](https://platform.parallel.ai/)
2. Register the UDFs with your Spark session:

Copy

Ask AI

```
from pyspark.sql import SparkSession
from parallel_web_tools.integrations.spark import register_parallel_udfs

# Create Spark session
spark = SparkSession.builder.appName("parallel-enrichment").getOrCreate()

# Register UDFs (uses PARALLEL_API_KEY env var by default)
register_parallel_udfs(spark)

# Or pass API key explicitly
register_parallel_udfs(spark, api_key="your-api-key")
```

### [​](https://docs.parallel.ai/data-integrations/spark\#configuration-options)  Configuration Options

Copy

Ask AI

```
register_parallel_udfs(
    spark,
    api_key="your-api-key",      # Optional: defaults to PARALLEL_API_KEY env var
    processor="lite-fast",        # Processor tier (default: lite-fast)
    timeout=300,                  # Timeout per API call in seconds (default: 300)
    include_basis=False,          # Include citations in response (default: False)
    udf_name="parallel_enrich",   # Custom UDF name (default: parallel_enrich)
)
```

## [​](https://docs.parallel.ai/data-integrations/spark\#basic-usage)  Basic Usage

Once registered, use `parallel_enrich()` in any SQL query:

Copy

Ask AI

```
# Create sample data
spark.sql("""
    CREATE OR REPLACE TEMP VIEW companies AS
    SELECT 'Google' as company_name, 'https://google.com' as website
    UNION ALL
    SELECT 'Apple', 'https://apple.com'
""")

# Enrich with Parallel
result = spark.sql("""
    SELECT
        company_name,
        parallel_enrich(
            map('company_name', company_name, 'website', website),
            array('CEO name', 'company description', 'founding year')
        ) as enriched_data
    FROM companies
""")

result.show(truncate=False)
```

Output:

Copy

Ask AI

```
+------------+-------------------------------------------------------------------------------------------------------------+
|company_name|enriched_data                                                                                                |
+------------+-------------------------------------------------------------------------------------------------------------+
|Google      |{"ceo_name": "Sundar Pichai", "founding_year": "1998", "company_description": "Google is an American..."}    |
|Apple       |{"ceo_name": "Tim Cook", "founding_year": "1976", "company_description": "Apple Inc. is an American..."}     |
+------------+-------------------------------------------------------------------------------------------------------------+
```

### [​](https://docs.parallel.ai/data-integrations/spark\#udf-parameters)  UDF Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `input_data` | `map<string, string>` | Key-value pairs of input data for enrichment |
| `output_columns` | `array<string>` | Descriptions of the columns you want to enrich |

### [​](https://docs.parallel.ai/data-integrations/spark\#parsing-results)  Parsing Results

The UDF returns JSON strings. Field names are converted to snake\_case (e.g., “CEO name” → `ceo_name`).Use `get_json_object()` to extract individual fields:

Copy

Ask AI

```
from pyspark.sql.functions import get_json_object

result = spark.sql("""
    SELECT
        company_name,
        get_json_object(enriched_data, '$.ceo_name') as ceo,
        get_json_object(enriched_data, '$.founding_year') as founded
    FROM (
        SELECT
            company_name,
            parallel_enrich(
                map('company_name', company_name),
                array('CEO name', 'founding year')
            ) as enriched_data
        FROM companies
    )
""")

result.show()
```

Output:

Copy

Ask AI

```
+------------+-------------+-------+
|company_name|          ceo|founded|
+------------+-------------+-------+
|      Google|Sundar Pichai|   1998|
|       Apple|     Tim Cook|   1976|
+------------+-------------+-------+
```

Or use `from_json()` with a schema for structured parsing:

Copy

Ask AI

```
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType

schema = StructType([\
    StructField("ceo_name", StringType()),\
    StructField("founding_year", StringType()),\
])

parsed = result.withColumn("parsed", from_json(col("enriched_data"), schema))
parsed.select("company_name", "parsed.*").show()
```

Output:

Copy

Ask AI

```
+------------+-------------+-------------+
|company_name|     ceo_name|founding_year|
+------------+-------------+-------------+
|      Google|Sundar Pichai|         1998|
|       Apple|     Tim Cook|         1976|
+------------+-------------+-------------+
```

## [​](https://docs.parallel.ai/data-integrations/spark\#including-basis/citations)  Including Basis/Citations

To include source citations in your enrichment results, set `include_basis=True`:

Copy

Ask AI

```
register_parallel_udfs(
    spark,
    include_basis=True,
    udf_name="parallel_enrich_with_basis",
)

result = spark.sql("""
    SELECT parallel_enrich_with_basis(
        map('company_name', company_name),
        array('CEO name')
    ) as enriched
    FROM companies
""")

result.show(truncate=False)
```

Output (truncated):

Copy

Ask AI

```
+---------------------------------------------------------------------------------------------+
|enriched                                                                                     |
+---------------------------------------------------------------------------------------------+
|{"ceo_name": "Sundar Pichai", "_basis": [{"field": "ceo_name", "citations": [...]}]}         |
|{"ceo_name": "Tim Cook", "_basis": [{"field": "ceo_name", "citations": [...]}]}              |
+---------------------------------------------------------------------------------------------+
```

When enabled, each result includes a `_basis` field with citations:

Copy

Ask AI

```
{
  "ceo_name": "Sundar Pichai",
  "_basis": [\
    {\
      "field": "ceo_name",\
      "citations": [\
        {"url": "https://...", "excerpts": ["..."]}\
      ]\
    }\
  ]
}
```

## [​](https://docs.parallel.ai/data-integrations/spark\#processor-selection)  Processor Selection

Choose a processor based on your speed vs thoroughness requirements. See [Choose a Processor](https://docs.parallel.ai/task-api/guides/choose-a-processor) for detailed guidance and [Pricing](https://docs.parallel.ai/resources/pricing) for cost information.Use the `parallel_enrich_with_processor` UDF to override per query:

Copy

Ask AI

```
SELECT parallel_enrich_with_processor(
    map('company_name', company_name),
    array('CEO name'),
    'pro-fast'  -- Override processor
) as enriched
FROM companies
LIMIT 1
```

Output:

Copy

Ask AI

```
+-----------------------------+
|enriched                     |
+-----------------------------+
|{"ceo_name": "Sundar Pichai"}|
+-----------------------------+
```

## [​](https://docs.parallel.ai/data-integrations/spark\#best-practices)  Best Practices

Partition sizing

The UDF processes all rows in a partition concurrently. For optimal performance:

- Use `repartition()` to control partition sizes
- Aim for 10-100 rows per partition for balanced concurrency

Error handling

Failed enrichments return JSON with an `error` field:

Copy

Ask AI

```
{"error": "error message here"}
```

Filter these in your downstream processing.

Rate limits

Concurrent processing respects Parallel’s rate limits. For large datasets, consider:

- Reducing partition sizes
- Using slower processors that have higher rate limits

[Overview](https://docs.parallel.ai/data-integrations/overview) [DuckDB](https://docs.parallel.ai/data-integrations/duckdb)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Data Integrations - Parallel

**URL:** https://docs.parallel.ai/data-integrations/overview

[Skip to main content](https://docs.parallel.ai/data-integrations/overview#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Data Integrations

Data Integrations

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [How it works](https://docs.parallel.ai/data-integrations/overview#how-it-works)
- [Available integrations](https://docs.parallel.ai/data-integrations/overview#available-integrations)
- [Choosing an integration](https://docs.parallel.ai/data-integrations/overview#choosing-an-integration)
- [Installation](https://docs.parallel.ai/data-integrations/overview#installation)
- [Common patterns](https://docs.parallel.ai/data-integrations/overview#common-patterns)
- [Input column mapping](https://docs.parallel.ai/data-integrations/overview#input-column-mapping)
- [Output column descriptions](https://docs.parallel.ai/data-integrations/overview#output-column-descriptions)
- [Next steps](https://docs.parallel.ai/data-integrations/overview#next-steps)

Parallel’s data integrations let you enrich datasets with web intelligence without leaving your existing data workflows. Whether you’re working with DataFrames in Python, SQL queries in a data warehouse, or analytics databases, there’s an integration that fits your stack.

## [​](https://docs.parallel.ai/data-integrations/overview\#how-it-works)  How it works

All data integrations follow the same pattern:

1. **Define inputs**: Specify which columns contain the data to research (company name, website, etc.)
2. **Define outputs**: Describe what information you want to extract (“CEO name”, “Founding year”, etc.)
3. **Choose a processor**: Select speed vs thoroughness based on your needs
4. **Get enriched data**: Receive structured results with optional citations

## [​](https://docs.parallel.ai/data-integrations/overview\#available-integrations)  Available integrations

[**Apache Spark** \\
\\
Distributed enrichment for large-scale data processing with PySpark UDFs](https://docs.parallel.ai/data-integrations/spark) [**Google BigQuery** \\
\\
SQL-native remote functions for enrichment directly in BigQuery queries](https://docs.parallel.ai/data-integrations/bigquery) [**Snowflake** \\
\\
SQL-native UDTF with batched processing via External Access Integration](https://docs.parallel.ai/data-integrations/snowflake) [**DuckDB** \\
\\
Batch processing and SQL UDFs for local analytics databases](https://docs.parallel.ai/data-integrations/duckdb) [**Polars** \\
\\
DataFrame-native enrichment with batch processing and LazyFrame support](https://docs.parallel.ai/data-integrations/polars) [**Supabase** \\
\\
Edge Functions for enrichment in Supabase applications](https://docs.parallel.ai/data-integrations/supabase)

## [​](https://docs.parallel.ai/data-integrations/overview\#choosing-an-integration)  Choosing an integration

| Integration | Best for | Processing model |
| --- | --- | --- |
| **Spark** | Large-scale distributed processing | UDF with concurrent processing per partition |
| **BigQuery** | Google Cloud data warehouses | Remote function with batched API calls |
| **Snowflake** | Snowflake data warehouses | Batched UDTF (partition-based) |
| **DuckDB** | Local analytics, embedded databases | Batch processing (recommended) or SQL UDF |
| **Polars** | Python DataFrame workflows | Batch processing |
| **Supabase** | PostgreSQL/Supabase applications | Edge Function |

## [​](https://docs.parallel.ai/data-integrations/overview\#installation)  Installation

All Python-based integrations are available via the `parallel-web-tools` package:

Copy

Ask AI

```
# Install with specific integration
pip install parallel-web-tools[polars]
pip install parallel-web-tools[duckdb]
pip install parallel-web-tools[spark]

# Install with all integrations
pip install parallel-web-tools[all]
```

For BigQuery and Snowflake, additional deployment steps are required to set up cloud functions and permissions. See the individual integration guides for details.

## [​](https://docs.parallel.ai/data-integrations/overview\#common-patterns)  Common patterns

### [​](https://docs.parallel.ai/data-integrations/overview\#input-column-mapping)  Input column mapping

All integrations use the same input mapping format—a dictionary where keys describe the data semantically and values reference your actual column names:

Copy

Ask AI

```
input_columns = {
    "company_name": "name",      # "name" is the column in your data
    "website": "domain",         # "domain" is the column in your data
    "headquarters": "location",  # "location" is the column in your data
}
```

### [​](https://docs.parallel.ai/data-integrations/overview\#output-column-descriptions)  Output column descriptions

Describe what you want to extract in plain language. Column names are automatically converted to valid identifiers:

Copy

Ask AI

```
output_columns = [\
    "CEO name",                           # → ceo_name\
    "Founding year (YYYY format)",        # → founding_year\
    "Annual revenue (USD, most recent)",  # → annual_revenue\
]
```

## [​](https://docs.parallel.ai/data-integrations/overview\#next-steps)  Next steps

[**Choose a Processor** \\
\\
Select the right processor based on speed vs thoroughness requirements](https://docs.parallel.ai/task-api/guides/choose-a-processor) [**Task API** \\
\\
Learn about the underlying Task API that powers all data integrations](https://docs.parallel.ai/task-api/task-enrichment) [**Pricing** \\
\\
View detailed pricing for all processors and API endpoints](https://docs.parallel.ai/resources/pricing)

[Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp) [Apache Spark](https://docs.parallel.ai/data-integrations/spark)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Overview - Parallel

**URL:** https://docs.parallel.ai/getting-started/overview

[Skip to main content](https://docs.parallel.ai/getting-started/overview#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Getting started

Overview

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [API products](https://docs.parallel.ai/getting-started/overview#api-products)
- [Web Tools](https://docs.parallel.ai/getting-started/overview#web-tools)
- [Web Agents](https://docs.parallel.ai/getting-started/overview#web-agents)
- [Choosing the right API](https://docs.parallel.ai/getting-started/overview#choosing-the-right-api)
- [Getting started](https://docs.parallel.ai/getting-started/overview#getting-started)
- [Step 1: Get your API key](https://docs.parallel.ai/getting-started/overview#step-1-get-your-api-key)
- [Step 2: Install the SDK](https://docs.parallel.ai/getting-started/overview#step-2-install-the-sdk)
- [Step 3: Make your first request](https://docs.parallel.ai/getting-started/overview#step-3-make-your-first-request)
- [Next steps](https://docs.parallel.ai/getting-started/overview#next-steps)

Parallel provides a suite of APIs that combine AI inference with live web data to power research, enrichment, and automation workflows. Whether you need to search the web, extract content from pages, enrich datasets, discover entities, or monitor changes—Parallel handles the complexity so you can focus on building.

## [​](https://docs.parallel.ai/getting-started/overview\#api-products)  API products

Parallel offers two categories of APIs: **Web Tools** for direct web access and **Web Agents** for AI-powered research workflows.

### [​](https://docs.parallel.ai/getting-started/overview\#web-tools)  Web Tools

Low-latency, synchronous APIs for direct web access.

[**Search API** \\
\\
Execute natural language web searches and retrieve LLM-optimized excerpts. Replace multiple keyword searches with a single call for broad or complex queries.](https://docs.parallel.ai/search/search-quickstart) [**Extract API** \\
\\
Convert any public URL into clean, LLM-optimized markdown. Handles JavaScript-heavy pages and PDFs with focused excerpts or full page content.](https://docs.parallel.ai/extract/extract-quickstart)

### [​](https://docs.parallel.ai/getting-started/overview\#web-agents)  Web Agents

AI-powered APIs that combine inference with web research for complex workflows.

[**Task API** \\
\\
Transform complex research tasks into programmable, repeatable operations. Define what you need in plain language or JSON, and get structured outputs with citations and confidence levels.](https://docs.parallel.ai/task-api/task-quickstart) [**Chat API** \\
\\
Build low-latency web research applications with OpenAI-compatible streaming chat completions. Choose from speed-optimized or research-grade models.](https://docs.parallel.ai/chat-api/chat-quickstart) [**FindAll API** \\
\\
Discover and enrich entities from the web using natural language queries. Turn queries like “FindAll AI companies that raised Series A” into structured, enriched databases.](https://docs.parallel.ai/findall-api/findall-quickstart) [**Monitor API** \\
\\
Track web changes continuously with scheduled queries and webhook notifications. Set up once and receive updates when relevant changes occur.](https://docs.parallel.ai/monitor-api/monitor-quickstart)

## [​](https://docs.parallel.ai/getting-started/overview\#choosing-the-right-api)  Choosing the right API

| Use case | Recommended API | Why |
| --- | --- | --- |
| Search the web for information | [Search API](https://docs.parallel.ai/search/search-quickstart) | Fast, synchronous results with LLM-optimized excerpts |
| Extract content from specific URLs | [Extract API](https://docs.parallel.ai/extract/extract-quickstart) | Clean markdown from any page, including JS-heavy sites |
| Enrich CRM or database records | [Task API](https://docs.parallel.ai/task-api/task-enrichment) | Structured input/output with web research |
| Generate research reports | [Task API](https://docs.parallel.ai/task-api/task-deep-research) | Deep research with citations and confidence levels |
| Build a grounded chatbot | [Chat API](https://docs.parallel.ai/chat-api/chat-quickstart) | OpenAI-compatible with web-grounded responses |
| Build lists of companies, people, or products | [FindAll API](https://docs.parallel.ai/findall-api/findall-quickstart) | Entity discovery with automatic validation |
| Track news or changes over time | [Monitor API](https://docs.parallel.ai/monitor-api/monitor-quickstart) | Scheduled monitoring with webhook delivery |

## [​](https://docs.parallel.ai/getting-started/overview\#getting-started)  Getting started

### [​](https://docs.parallel.ai/getting-started/overview\#step-1-get-your-api-key)  Step 1: Get your API key

Sign up at [platform.parallel.ai](https://platform.parallel.ai/) to generate your API key.

### [​](https://docs.parallel.ai/getting-started/overview\#step-2-install-the-sdk)  Step 2: Install the SDK

Use our Python or TypeScript SDK for the best developer experience.

Python

TypeScript

Copy

Ask AI

```
pip install parallel-web
export PARALLEL_API_KEY="your-api-key"
```

### [​](https://docs.parallel.ai/getting-started/overview\#step-3-make-your-first-request)  Step 3: Make your first request

Try a simple search to verify your setup.

Python

TypeScript

Copy

Ask AI

```
from parallel import Parallel

client = Parallel()

search = client.beta.search(
    objective="What is Parallel Web Systems?",
    search_queries=["Parallel Web Systems company"],
    mode="fast",
)

print(search.results)
```

## [​](https://docs.parallel.ai/getting-started/overview\#next-steps)  Next steps

- **[Pricing](https://docs.parallel.ai/getting-started/pricing)**: Understand costs for each API
- **[Rate limits](https://docs.parallel.ai/getting-started/rate-limits)**: Default quotas and how to request increases
- **[Glossary](https://docs.parallel.ai/getting-started/glossary)**: Key terms and concepts used throughout the docs

[Pricing](https://docs.parallel.ai/getting-started/pricing)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Agent Skills - Parallel

**URL:** https://docs.parallel.ai/integrations/agent-skills

[Skip to main content](https://docs.parallel.ai/integrations/agent-skills#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Agent Skills

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Available Skills](https://docs.parallel.ai/integrations/agent-skills#available-skills)
- [Prerequisites](https://docs.parallel.ai/integrations/agent-skills#prerequisites)
- [Installation](https://docs.parallel.ai/integrations/agent-skills#installation)
- [Usage](https://docs.parallel.ai/integrations/agent-skills#usage)
- [Supported Agents](https://docs.parallel.ai/integrations/agent-skills#supported-agents)
- [Learn More](https://docs.parallel.ai/integrations/agent-skills#learn-more)

Agent Skills let you add Parallel’s capabilities to AI coding agents like Cursor, Cline, GitHub Copilot, Windsurf, and 30+ other tools via the [Agent Skills CLI](https://github.com/agentskills/agentskills). Skills are lightweight, declarative integrations that give your agent access to live web data without writing any code.

View the complete repository for this integration [here](https://github.com/parallel-web/parallel-agent-skills)

## [​](https://docs.parallel.ai/integrations/agent-skills\#available-skills)  Available Skills

| Skill | Description |
| --- | --- |
| `parallel-web-search` | Fast web search for current events, fact-checking, and lookups |
| `parallel-web-extract` | Extract clean content from URLs, including JavaScript-heavy sites and PDFs |
| `parallel-deep-research` | Exhaustive, multi-source research reports with configurable depth |
| `parallel-data-enrichment` | Bulk enrichment of companies, people, or products with web-sourced data |

## [​](https://docs.parallel.ai/integrations/agent-skills\#prerequisites)  Prerequisites

1

[Navigate to header](https://docs.parallel.ai/integrations/agent-skills#)

Install the Parallel CLI

Copy

Ask AI

```
curl -fsSL https://parallel.ai/install.sh | bash
```

2

[Navigate to header](https://docs.parallel.ai/integrations/agent-skills#)

Get your API key

Get your API key from [Parallel](https://platform.parallel.ai/) and set it as an environment variable:

Copy

Ask AI

```
export PARALLEL_API_KEY="your-api-key"
```

3

[Navigate to header](https://docs.parallel.ai/integrations/agent-skills#)

Authenticate the CLI

Copy

Ask AI

```
parallel-cli login
```

## [​](https://docs.parallel.ai/integrations/agent-skills\#installation)  Installation

Install all skills globally so they’re available in every project:

Copy

Ask AI

```
npx skills add parallel-web/parallel-agent-skills --all --global
```

Or install a specific skill:

Copy

Ask AI

```
npx skills add parallel-web/parallel-agent-skills --skill parallel-web-search
```

To see all available skills before installing:

Copy

Ask AI

```
npx skills add parallel-web/parallel-agent-skills --list
```

## [​](https://docs.parallel.ai/integrations/agent-skills\#usage)  Usage

Once installed, skills are automatically available to your agent. No additional configuration is needed — your agent will use them when appropriate based on your prompts.

- **Web search** is used by default for any research, lookup, or question needing current information
- **Extract** is used when your agent needs to fetch content from a specific URL
- **Deep research** is triggered when you explicitly request exhaustive or comprehensive research
- **Data enrichment** is used for bulk enrichment of lists of companies, people, or products

## [​](https://docs.parallel.ai/integrations/agent-skills\#supported-agents)  Supported Agents

Agent Skills work with any tool that supports the Vercel Skills CLI, including:

- Cursor
- Cline
- GitHub Copilot
- Windsurf
- And [30+ other agents](https://github.com/agentskills/agentskills)

For Claude Code, you can also use the [Claude Code Plugin Marketplace](https://docs.parallel.ai/integrations/claude-code-marketplace) integration.

## [​](https://docs.parallel.ai/integrations/agent-skills\#learn-more)  Learn More

For detailed skill documentation, configuration options, and local development instructions, see the [parallel-agent-skills repository on GitHub](https://github.com/parallel-web/parallel-agent-skills).

[Supabase](https://docs.parallel.ai/data-integrations/supabase) [AWS Marketplace](https://docs.parallel.ai/integrations/aws-marketplace)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Quickstart - Parallel

**URL:** https://docs.parallel.ai/integrations/mcp/quickstart

[Skip to main content](https://docs.parallel.ai/integrations/mcp/quickstart#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

MCP

Quickstart

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [When to use Parallel MCPs?](https://docs.parallel.ai/integrations/mcp/quickstart#when-to-use-parallel-mcps)
- [Available MCP Servers](https://docs.parallel.ai/integrations/mcp/quickstart#available-mcp-servers)
- [Search MCP](https://docs.parallel.ai/integrations/mcp/quickstart#search-mcp)
- [Task MCP](https://docs.parallel.ai/integrations/mcp/quickstart#task-mcp)
- [Quick Installation](https://docs.parallel.ai/integrations/mcp/quickstart#quick-installation)
- [Quick Install Links](https://docs.parallel.ai/integrations/mcp/quickstart#quick-install-links)

## [​](https://docs.parallel.ai/integrations/mcp/quickstart\#when-to-use-parallel-mcps)  When to use Parallel MCPs?

Our MCP servers are the best way to explore what’s possible with our APIs, as it using complex APIs without prior knowledge, and comparing results.The Parallel MCP Servers expose Parallel APIs to AI assistants and large language model (LLM) workflows, delivering high-quality, relevant results from the web while optimizing for the price-performance balance your AI applications need at scale.As can be seen in the following table, our MCPs can be useful for quick experimentation with deep research and task groups, or for daily use.

| Use Case | What |
| --- | --- |
| Agentic applications where low-latency search is a tool call | **[Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp)** |
| Daily use for everyday deep-research tasks in chat-based clients | **[Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp)** |
| Enriching a dataset (eg. a CSV) with web data via chat-based clients | **[Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp)** |
| Running benchmarks on Parallel processors across a series of queries | **[Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp)** |
| Building high-scale production apps that integrate with Parallel APIs | **[Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) and [Tasks](https://docs.parallel.ai/task-api/task-quickstart)** |

## [​](https://docs.parallel.ai/integrations/mcp/quickstart\#available-mcp-servers)  Available MCP Servers

Parallel offers two MCP servers that can be installed in any MCP client. They can also be [used programmatically](https://docs.parallel.ai/integrations/mcp/programmatic-use) by providing your Parallel API key in the Authorization header as a Bearer token.

Looking for help with Parallel documentation? Try our [Docs MCP](https://docs.parallel.ai/mcp) to get AI-assisted answers about Parallel’s documentation. This is for navigating our docs only—it does not provide access to Parallel APIs.

### [​](https://docs.parallel.ai/integrations/mcp/quickstart\#search-mcp)  [Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp)

The Search MCP provides drop-in web search capabilities for any MCP-aware model. It invokes the [Search API](https://docs.parallel.ai/search/search-quickstart) endpoint with an `agentic` mode optimized for agent workflows.**Server URL:**`https://search-mcp.parallel.ai/mcp`[View Search MCP Documentation →](https://docs.parallel.ai/integrations/mcp/search-mcp)

* * *

### [​](https://docs.parallel.ai/integrations/mcp/quickstart\#task-mcp)  [Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp)

The Task MCP enables deep research tasks and data enrichment workflows. It provides access to the [Task API](https://docs.parallel.ai/task-api/task-quickstart) for generating comprehensive reports and transforming datasets with web intelligence.**Server URL:**`https://task-mcp.parallel.ai/mcp`[View Task MCP Documentation →](https://docs.parallel.ai/integrations/mcp/task-mcp)

* * *

## [​](https://docs.parallel.ai/integrations/mcp/quickstart\#quick-installation)  Quick Installation

Both MCPs can be installed in popular AI assistants and IDEs. For detailed installation instructions for your specific platform, visit:

- **[Search MCP Installation Guide →](https://docs.parallel.ai/integrations/mcp/search-mcp#installation)**
- **[Task MCP Installation Guide →](https://docs.parallel.ai/integrations/mcp/task-mcp#installation)**

### [​](https://docs.parallel.ai/integrations/mcp/quickstart\#quick-install-links)  Quick Install Links

For Cursor and VS Code users, you can use these deep links for one-click installation:**Cursor:**

- [🔗 Install Search MCP](https://cursor.com/en/install-mcp?name=Parallel%20Search%20MCP&config=eyJ1cmwiOiJodHRwczovL3NlYXJjaC1tY3AucGFyYWxsZWwuYWkvbWNwIn0=)
- [🔗 Install Task MCP](https://cursor.com/en/install-mcp?name=Parallel%20Task%20MCP&config=eyJ1cmwiOiJodHRwczovL3Rhc2stbWNwLnBhcmFsbGVsLmFpL21jcCJ9)

**VS Code:**

- [🔗 Install Search MCP](https://insiders.vscode.dev/redirect/mcp/install?name=Parallel%20Search%20MCP&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fsearch-mcp.parallel.ai%2Fmcp%22%7D)
- [🔗 Install Task MCP](https://insiders.vscode.dev/redirect/mcp/install?name=Parallel%20Task%20MCP&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Ftask-mcp.parallel.ai%2Fmcp%22%7D)

[Simulate Event](https://docs.parallel.ai/monitor-api/monitor-simulate-event) [Programmatic Use](https://docs.parallel.ai/integrations/mcp/programmatic-use)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Cancel - Parallel

**URL:** https://docs.parallel.ai/findall-api/features/findall-cancel

[Skip to main content](https://docs.parallel.ai/findall-api/features/findall-cancel#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Cancel

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [How Cancellation Works](https://docs.parallel.ai/findall-api/features/findall-cancel#how-cancellation-works)
- [Common Use Cases](https://docs.parallel.ai/findall-api/features/findall-cancel#common-use-cases)
- [Related Topics](https://docs.parallel.ai/findall-api/features/findall-cancel#related-topics)

Stop a running FindAll search when you have enough matches or need to control costs. Results found before cancellation are preserved.

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X POST \
  https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/cancel \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15" \
  -H "Content-Type: application/json"
```

## [​](https://docs.parallel.ai/findall-api/features/findall-cancel\#how-cancellation-works)  How Cancellation Works

Cancellation is a **signal**, not instant:

- Active work units finish gracefully, no new work is scheduled
- Matches found so far are preserved and accessible
- You’re charged for work completed during cancellation
- After cancellation, the run transitions to `cancelled` status (see **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**)

Cancelled runs **cannot be extended or enriched**. Cancellation is irreversible—you’ll need to create a new run to continue searching.

## [​](https://docs.parallel.ai/findall-api/features/findall-cancel\#common-use-cases)  Common Use Cases

- Control costs when a run takes longer than expected
- Stop after finding enough matches (monitor via [webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook) or [SSE](https://docs.parallel.ai/findall-api/features/findall-sse))
- Iterate quickly with refined queries instead of waiting for completion

## [​](https://docs.parallel.ai/findall-api/features/findall-cancel\#related-topics)  Related Topics

- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/cancel-findall-run)**: Complete endpoint documentation

[Extend](https://docs.parallel.ai/findall-api/features/findall-extend) [Refresh Runs](https://docs.parallel.ai/findall-api/features/findall-refresh)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Supabase - Parallel

**URL:** https://docs.parallel.ai/data-integrations/supabase

[Skip to main content](https://docs.parallel.ai/data-integrations/supabase#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Data Integrations

Supabase

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Getting Started](https://docs.parallel.ai/data-integrations/supabase#getting-started)
- [Example Usage](https://docs.parallel.ai/data-integrations/supabase#example-usage)

Enrich your Supabase data with live web intelligence using [Supabase Edge Functions](https://supabase.com/docs/guides/functions) and Parallel’s Task API.

Check out the [Parallel integration on Supabase](https://supabase.com/partners/integrations/parallel) for more information.

## [​](https://docs.parallel.ai/data-integrations/supabase\#getting-started)  Getting Started

We provide a complete cookbook with Supabase Edge Functions, a Next.js frontend, and step-by-step setup instructions. [**Supabase + Parallel Cookbook** \\
\\
Complete working example showing how to build a data enrichment pipeline with Supabase and Parallel.](https://github.com/parallel-web/parallel-cookbook/tree/main/typescript-recipes/parallel-supabase-enrichment) The cookbook includes:

- **Supabase Edge Functions** that call Parallel’s Task API
- **Next.js frontend** with live updates via Supabase Realtime
- **SQL schemas** for storing enrichment data
- **Polling pattern** for handling long-running enrichments

## [​](https://docs.parallel.ai/data-integrations/supabase\#example-usage)  Example Usage

The Edge Function uses the `parallel-web` SDK to call Parallel’s Task API:

Copy

Ask AI

```
import Parallel from "npm:parallel-web@0.2.4";

const parallel = new Parallel({ apiKey: Deno.env.get("PARALLEL_API_KEY") });

const taskRun = await parallel.taskRun.create({
  input: {
    company_name: "Stripe",
    website: "stripe.com",
  },
  processor: "base-fast",
  task_spec: {
    output_schema: {
      type: "json",
      json_schema: {
        type: "object",
        properties: {
          industry: { type: "string" },
          employee_count: { type: "string" },
          headquarters: { type: "string" },
          description: { type: "string" },
        },
      },
    },
  },
});

const result = await parallel.taskRun.result(taskRun.run_id, { timeout: 30 });
```

For detailed configuration and advanced features, see the [Task API Quickstart](https://docs.parallel.ai/task-api/task-quickstart).**Links:**

- [Supabase + Parallel Cookbook](https://github.com/parallel-web/parallel-cookbook/tree/main/typescript-recipes/parallel-supabase-enrichment)
- [Parallel on Supabase Integrations](https://supabase.com/partners/integrations/parallel)
- [parallel-web npm package](https://www.npmjs.com/package/parallel-web)

[Snowflake](https://docs.parallel.ai/data-integrations/snowflake) [Agent Skills](https://docs.parallel.ai/integrations/agent-skills)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Snowflake - Parallel

**URL:** https://docs.parallel.ai/data-integrations/snowflake

[Skip to main content](https://docs.parallel.ai/data-integrations/snowflake#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Data Integrations

Snowflake

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features](https://docs.parallel.ai/data-integrations/snowflake#features)
- [Installation](https://docs.parallel.ai/data-integrations/snowflake#installation)
- [Deployment](https://docs.parallel.ai/data-integrations/snowflake#deployment)
- [Prerequisites](https://docs.parallel.ai/data-integrations/snowflake#prerequisites)
- [Finding Your Account Identifier](https://docs.parallel.ai/data-integrations/snowflake#finding-your-account-identifier)
- [Deploy with CLI](https://docs.parallel.ai/data-integrations/snowflake#deploy-with-cli)
- [Basic Usage](https://docs.parallel.ai/data-integrations/snowflake#basic-usage)
- [Function Parameters](https://docs.parallel.ai/data-integrations/snowflake#function-parameters)
- [Return Values](https://docs.parallel.ai/data-integrations/snowflake#return-values)
- [Custom Processor](https://docs.parallel.ai/data-integrations/snowflake#custom-processor)
- [Batching with PARTITION BY](https://docs.parallel.ai/data-integrations/snowflake#batching-with-partition-by)
- [All Rows in One Batch](https://docs.parallel.ai/data-integrations/snowflake#all-rows-in-one-batch)
- [Batch by Column](https://docs.parallel.ai/data-integrations/snowflake#batch-by-column)
- [Fixed Batch Sizes](https://docs.parallel.ai/data-integrations/snowflake#fixed-batch-sizes)
- [Choosing a Partition Strategy](https://docs.parallel.ai/data-integrations/snowflake#choosing-a-partition-strategy)
- [Processor Selection](https://docs.parallel.ai/data-integrations/snowflake#processor-selection)
- [Best Practices](https://docs.parallel.ai/data-integrations/snowflake#best-practices)
- [Security](https://docs.parallel.ai/data-integrations/snowflake#security)

This integration is ideal for data engineers who need to enrich large datasets with web intelligence directly in their Snowflake pipelines—without leaving SQL or building custom API integrations.Parallel provides a SQL-native User Defined Table Function (UDTF) for Snowflake that enables data enrichment directly in your SQL queries. The integration uses Snowflake’s External Access feature to securely connect to the Parallel API, and batches all rows in a partition into a single API call for efficient processing.

View the complete demo notebook:

- [Snowflake Enrichment Demo](https://github.com/parallel-web/parallel-web-tools/blob/main/notebooks/snowflake_enrichment_demo.ipynb)

## [​](https://docs.parallel.ai/data-integrations/snowflake\#features)  Features

- **SQL-Native**: Use `parallel_enrich()` directly in Snowflake SQL queries
- **Batched Processing**: All rows in a partition are sent in a single API call using `end_partition()`
- **Secure**: API key stored as Snowflake Secret, accessed via External Access Integration
- **Configurable Processors**: Choose from lite-fast to pro for speed vs thoroughness tradeoffs
- **Structured Output**: Returns VARIANT columns for input and enriched data

## [​](https://docs.parallel.ai/data-integrations/snowflake\#installation)  Installation

Copy

Ask AI

```
pip install parallel-web-tools[snowflake]
```

The standalone `parallel-cli` binary does not include deployment commands. You must install via pip with the `[snowflake]` extra to deploy the Snowflake integration.

## [​](https://docs.parallel.ai/data-integrations/snowflake\#deployment)  Deployment

The Snowflake integration requires a one-time deployment step to set up the External Access Integration, secrets, and UDTF in your Snowflake account.

### [​](https://docs.parallel.ai/data-integrations/snowflake\#prerequisites)  Prerequisites

1. **Snowflake Account** \- Paid account required (trial accounts don’t support External Access)
2. **ACCOUNTADMIN Role** \- Required for creating External Access Integrations
3. **Parallel API Key** from [Parallel](https://platform.parallel.ai/)

### [​](https://docs.parallel.ai/data-integrations/snowflake\#finding-your-account-identifier)  Finding Your Account Identifier

Your Snowflake account identifier is in your Snowsight URL:

Copy

Ask AI

```
https://app.snowflake.com/ORGNAME/ACCOUNTNAME/worksheets
                         └───────┬───────────┘
                     Account: ORGNAME-ACCOUNTNAME
```

### [​](https://docs.parallel.ai/data-integrations/snowflake\#deploy-with-cli)  Deploy with CLI

Copy

Ask AI

```
parallel-cli enrich deploy --system snowflake \
    --account ORGNAME-ACCOUNTNAME \
    --user your-username \
    --password "your-password" \
    --warehouse COMPUTE_WH
```

If your account requires MFA:

Copy

Ask AI

```
parallel-cli enrich deploy --system snowflake \
    --account ORGNAME-ACCOUNTNAME \
    --user your-username \
    --password "your-password" \
    --authenticator username_password_mfa \
    --passcode 123456 \
    --warehouse COMPUTE_WH
```

This creates:

- Database: `PARALLEL_INTEGRATION`
- Schema: `ENRICHMENT`
- Network rule for `api.parallel.ai`
- Secret with your API key
- External Access Integration
- `parallel_enrich()` UDTF (batched table function)
- Roles: `PARALLEL_DEVELOPER` and `PARALLEL_USER`

For manual deployment options (useful if you don’t have ACCOUNTADMIN), troubleshooting, MFA setup, and cleanup instructions, see the [complete Snowflake setup guide](https://github.com/parallel-web/parallel-web-tools/blob/main/docs/snowflake-setup.md).

## [​](https://docs.parallel.ai/data-integrations/snowflake\#basic-usage)  Basic Usage

The `parallel_enrich()` function is a table function (UDTF) that requires the `TABLE(...) OVER (PARTITION BY ...)` syntax:

Copy

Ask AI

```
WITH companies AS (
    SELECT * FROM (VALUES
        ('Google', 'google.com'),
        ('Anthropic', 'anthropic.com'),
        ('Apple', 'apple.com')
    ) AS t(company_name, website)
)
SELECT
    e.input:company_name::STRING AS company_name,
    e.input:website::STRING AS website,
    e.enriched:ceo_name::STRING AS ceo_name,
    e.enriched:founding_year::STRING AS founding_year
FROM companies t,
     TABLE(PARALLEL_INTEGRATION.ENRICHMENT.parallel_enrich(
         TO_JSON(OBJECT_CONSTRUCT('company_name', t.company_name, 'website', t.website)),
         ARRAY_CONSTRUCT('CEO name', 'Founding year')
     ) OVER (PARTITION BY 1)) e;
```

Output:

| company\_name | website | ceo\_name | founding\_year |
| --- | --- | --- | --- |
| Google | google.com | Sundar Pichai | 1998 |
| Anthropic | anthropic.com | Dario Amodei | 2021 |
| Apple | apple.com | Tim Cook | 1976 |

### [​](https://docs.parallel.ai/data-integrations/snowflake\#function-parameters)  Function Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `input_json` | `VARCHAR` | JSON string via `TO_JSON(OBJECT_CONSTRUCT(...))` |
| `output_columns` | `ARRAY` | Array of descriptions for columns you want to enrich |
| `processor` | `VARCHAR` | (Optional) Processor to use (default: `lite-fast`) |

### [​](https://docs.parallel.ai/data-integrations/snowflake\#return-values)  Return Values

The function returns a table with two VARIANT columns:

| Column | Description |
| --- | --- |
| `input` | Original input data as VARIANT |
| `enriched` | Enrichment results including `basis` citations |

The `enriched` column contains:

Copy

Ask AI

```
{
  "ceo_name": "Sundar Pichai",
  "founding_year": "1998",
  "basis": [{"field": "ceo_name", "citations": [...], "confidence": "high"}]
}
```

Field names are automatically converted to snake\_case (e.g., “CEO name” → `ceo_name`).

### [​](https://docs.parallel.ai/data-integrations/snowflake\#custom-processor)  Custom Processor

Override the default processor by adding a third parameter:

Copy

Ask AI

```
SELECT
    e.input:company_name::STRING AS company_name,
    e.enriched:ceo_name::STRING AS ceo_name
FROM companies t,
     TABLE(PARALLEL_INTEGRATION.ENRICHMENT.parallel_enrich(
         TO_JSON(OBJECT_CONSTRUCT('company_name', t.company_name)),
         ARRAY_CONSTRUCT('CEO name'),
         'base-fast'  -- processor option
     ) OVER (PARTITION BY 1)) e;
```

## [​](https://docs.parallel.ai/data-integrations/snowflake\#batching-with-partition-by)  Batching with PARTITION BY

The `PARTITION BY` clause controls how rows are batched into API calls. All rows in the same partition are sent together in a single API request.

### [​](https://docs.parallel.ai/data-integrations/snowflake\#all-rows-in-one-batch)  All Rows in One Batch

Copy

Ask AI

```
-- Single API call for all rows (fastest for small datasets)
TABLE(parallel_enrich(...) OVER (PARTITION BY 1))
```

### [​](https://docs.parallel.ai/data-integrations/snowflake\#batch-by-column)  Batch by Column

Copy

Ask AI

```
-- One API call per region
SELECT
    e.input:company_name::STRING AS company_name,
    e.enriched:ceo_name::STRING AS ceo_name
FROM companies t,
     TABLE(PARALLEL_INTEGRATION.ENRICHMENT.parallel_enrich(
         TO_JSON(OBJECT_CONSTRUCT('company_name', t.company_name, 'region', t.region)),
         ARRAY_CONSTRUCT('CEO name')
     ) OVER (PARTITION BY t.region)) e;
```

### [​](https://docs.parallel.ai/data-integrations/snowflake\#fixed-batch-sizes)  Fixed Batch Sizes

Copy

Ask AI

```
-- Process in batches of 100 rows
WITH numbered AS (
    SELECT *, CEIL(ROW_NUMBER() OVER (ORDER BY company_name) / 100.0) AS batch_id
    FROM companies
)
SELECT
    e.input:company_name::STRING AS company_name,
    e.enriched:ceo_name::STRING AS ceo_name
FROM numbered t,
     TABLE(PARALLEL_INTEGRATION.ENRICHMENT.parallel_enrich(
         TO_JSON(OBJECT_CONSTRUCT('company_name', t.company_name)),
         ARRAY_CONSTRUCT('CEO name')
     ) OVER (PARTITION BY t.batch_id)) e;
```

### [​](https://docs.parallel.ai/data-integrations/snowflake\#choosing-a-partition-strategy)  Choosing a Partition Strategy

| Pattern | Use Case |
| --- | --- |
| `PARTITION BY 1` | Small datasets (under 1000 rows), fastest for few rows |
| `PARTITION BY column` | Large datasets, natural groupings, incremental processing |
| `PARTITION BY batch_id` | Fixed batch sizes for very large datasets |

## [​](https://docs.parallel.ai/data-integrations/snowflake\#processor-selection)  Processor Selection

Choose a processor based on your speed vs thoroughness requirements. See [Choose a Processor](https://docs.parallel.ai/task-api/guides/choose-a-processor) for detailed guidance and [Pricing](https://docs.parallel.ai/resources/pricing) for cost information.

| Processor | Speed | Best For |
| --- | --- | --- |
| `lite-fast` | Fastest | Basic metadata, high volume |
| `base-fast` | Fast | Standard enrichments |
| `core-fast` | Medium | Cross-referenced data |
| `pro-fast` | Slower | Deep research |

## [​](https://docs.parallel.ai/data-integrations/snowflake\#best-practices)  Best Practices

Use PARTITION BY 1 for small datasets

For smaller datasets, batch all rows together for maximum efficiency:

Copy

Ask AI

```
TABLE(parallel_enrich(...) OVER (PARTITION BY 1))
```

Use specific descriptions

Be specific in your output column descriptions for better results:

Copy

Ask AI

```
ARRAY_CONSTRUCT(
    'CEO name (current CEO or equivalent leader)',
    'Founding year (YYYY format)'
)
```

Cache results

Store enriched results in a table to avoid re-processing:

Copy

Ask AI

```
CREATE TABLE enriched_companies AS
SELECT
    e.input:company_name::STRING AS company_name,
    e.enriched:ceo_name::STRING AS ceo_name,
    e.enriched:founding_year::STRING AS founding_year
FROM companies t,
     TABLE(PARALLEL_INTEGRATION.ENRICHMENT.parallel_enrich(
         TO_JSON(OBJECT_CONSTRUCT('company_name', t.company_name)),
         ARRAY_CONSTRUCT('CEO name', 'Founding year')
     ) OVER (PARTITION BY 1)) e;
```

Incremental processing

Process new records daily using date partitioning:

Copy

Ask AI

```
SELECT e.*
FROM companies t,
     TABLE(PARALLEL_INTEGRATION.ENRICHMENT.parallel_enrich(
         TO_JSON(OBJECT_CONSTRUCT('company_name', t.company_name)),
         ARRAY_CONSTRUCT('CEO name')
     ) OVER (PARTITION BY DATE_TRUNC('day', t.created_at))) e
WHERE t.created_at >= CURRENT_DATE;
```

## [​](https://docs.parallel.ai/data-integrations/snowflake\#security)  Security

The integration uses Snowflake’s security features:

1. **Network Rule**: Only allows egress to `api.parallel.ai:443`
2. **Secret**: API key stored encrypted (not visible in SQL)
3. **External Access Integration**: Combines network rule and secret
4. **Roles**: `PARALLEL_USER` for query access, `PARALLEL_DEVELOPER` for UDF management

Grant access to users:

Copy

Ask AI

```
GRANT ROLE PARALLEL_USER TO USER analyst_user;
```

[Polars](https://docs.parallel.ai/data-integrations/polars) [Supabase](https://docs.parallel.ai/data-integrations/supabase)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Enrichments - Parallel

**URL:** https://docs.parallel.ai/findall-api/features/findall-enrich

[Skip to main content](https://docs.parallel.ai/findall-api/features/findall-enrich#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Enrichments

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Overview](https://docs.parallel.ai/findall-api/features/findall-enrich#overview)
- [Match Conditions vs. Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich#match-conditions-vs-enrichments)
- [Why This Separation Matters](https://docs.parallel.ai/findall-api/features/findall-enrich#why-this-separation-matters)
- [Adding Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich#adding-enrichments)
- [Creating Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich#creating-enrichments)
- [Quick Example](https://docs.parallel.ai/findall-api/features/findall-enrich#quick-example)
- [Retrieving Enrichment Results](https://docs.parallel.ai/findall-api/features/findall-enrich#retrieving-enrichment-results)
- [Related Topics](https://docs.parallel.ai/findall-api/features/findall-enrich#related-topics)
- [Task API Foundation](https://docs.parallel.ai/findall-api/features/findall-enrich#task-api-foundation)
- [FindAll Features](https://docs.parallel.ai/findall-api/features/findall-enrich#findall-features)

**Built on Task API**: FindAll enrichments are powered by our [Task API](https://docs.parallel.ai/task-api/task-quickstart). All Task API concepts—including [task specifications](https://docs.parallel.ai/task-api/guides/specify-a-task), [processors](https://docs.parallel.ai/task-api/guides/choose-a-processor), [output schemas](https://docs.parallel.ai/task-api/guides/specify-a-task#output-schema), and pricing—apply directly to enrichments. We handle the orchestration automatically, running tasks on each matched candidate.

## [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#overview)  Overview

FindAll enrichments allow you to extract additional non-boolean information about candidates that should not be used as filters for matches. For example, if you’re finding companies, you might want to extract the CEO name as pure enrichment data—something you want to know about each match, but not something that should affect whether a candidate matches your criteria.

## [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#match-conditions-vs-enrichments)  Match Conditions vs. Enrichments

Understanding the distinction between match conditions and enrichments is fundamental to using FindAll effectively.

|  | **Match Conditions** | **Enrichments** |
| --- | --- | --- |
| **Purpose** | Required criteria that determine whether a candidate is a match | Additional data fields extracted only for matched candidates |
| **When Executed** | During FindAll generation and evaluation process | **Only on matched candidates** using the Task API |
| **Output format** | Boolean (yes/no) + extracted value | String values (by default) |
| **Type of Criteria** | Must be boolean/filterable (yes/no questions) | Can be any type of data extraction |
| **Affects Matching?** | ✅ Yes - determines which candidates reach `matched` status | ❌ No - does not affect which candidates match |
| **When to Add** | Must be defined when creating the run | Can be added when creating the run, or multiple times after |
| **Example Questions** | • “Is the company founded after 2020?”<br>• “Has the company raised Series A funding?”<br>• “Is the company in the healthcare industry?” | • “What is the CEO’s name?”<br>• “What is the company’s revenue?”<br>• “What products does the company offer?” |

### [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#why-this-separation-matters)  Why This Separation Matters

This two-stage approach is efficient and cost-effective:

1. **Filter first**: Match conditions quickly narrow down candidates to relevant matches
2. **Enrich selectively**: Extract detailed data only from the matches that matter

This means you don’t pay to enrich hundreds of candidates that won’t match your criteria.

## [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#adding-enrichments)  Adding Enrichments

Enrichments can be added anytime after a FindAll run is created, even for completed runs. Once added:

- Enrichments will run on **all matches** (both ones that exist when the request is made and all future matches)
- If enrichments are present, **extend** will also perform the same set of enrichments on all extended matches

## [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#creating-enrichments)  Creating Enrichments

**Task API Concepts Apply Here**: Enrichments use the same [task spec](https://docs.parallel.ai/task-api/guides/specify-a-task) structure as Task API runs. You’ll define:

- **[Processors](https://docs.parallel.ai/task-api/guides/choose-a-processor)**: Choose from `base`, `advanced`, or `auto` (same as Task API)
- **[Output Schema](https://docs.parallel.ai/task-api/guides/specify-a-task#output-schema)**: Define structured JSON output (same format as Task API)
- **[Pricing](https://docs.parallel.ai/task-api/guides/execute-task-run#pricing)**: Charged according to Task API processor pricing

The only difference: you don’t need to define `input_schema`—it’s automatically set to the candidate’s `name`, `url`, and `description`.

### [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#quick-example)  Quick Example

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/enrich" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15" \
  -H "Content-Type: application/json" \
  -d '{
    "processor": "core",
    "output_schema": {
      "type": "json",
      "json_schema": {
        "type": "object",
        "properties": {
          "ceo_name": {
            "type": "string",
            "description": "Name of the CEO"
          },
          "founding_year": {
            "type": "string",
            "description": "Year the company was founded"
          }
        },
        "required": ["ceo_name", "founding_year"],
        "additionalProperties": false
      }
    }
  }'
```

## [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#retrieving-enrichment-results)  Retrieving Enrichment Results

You can access enrichment results through multiple methods:

- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)** (`/events`): Enrichment results stream in real-time as they complete
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Subscribe to `findall.candidate.enriched` events to receive enrichment results via HTTP callbacks
- **Result endpoint** (`/result`): Enrichment data is included when fetching the final results of a FindAll run

Enrichment data is added to the candidate’s `output` object with `type: "enrichment"`. See [Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates) for details on how enrichments appear in the candidate structure.

## [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#related-topics)  Related Topics

### [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#task-api-foundation)  Task API Foundation

Enrichments are built on Task API, so these guides will help you understand how they work:

- **[Task API Quickstart](https://docs.parallel.ai/task-api/task-quickstart)**: Learn the Task API that powers enrichments
- **[Specify a Task](https://docs.parallel.ai/task-api/guides/specify-a-task)**: Master task\_spec structure and best practices
- **[Choose a Task Processor](https://docs.parallel.ai/task-api/guides/choose-a-processor)**: Understand Task API processor options
- **[Execute Task Runs](https://docs.parallel.ai/task-api/guides/execute-task-run)**: Learn about pricing and execution patterns

### [​](https://docs.parallel.ai/findall-api/features/findall-enrich\#findall-features)  FindAll Features

- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and how to cancel runs
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run)**: Complete endpoint documentation

[Preview](https://docs.parallel.ai/findall-api/features/findall-preview) [Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# OpenAI SDK Compatibility - Parallel

**URL:** https://docs.parallel.ai/chat-api/sdk-compatibility

[Skip to main content](https://docs.parallel.ai/chat-api/sdk-compatibility#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Chat

OpenAI SDK Compatibility

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Important OpenAI Compatibility Limitations](https://docs.parallel.ai/chat-api/sdk-compatibility#important-openai-compatibility-limitations)
- [API Behavior](https://docs.parallel.ai/chat-api/sdk-compatibility#api-behavior)
- [Detailed OpenAI Compatible API Support](https://docs.parallel.ai/chat-api/sdk-compatibility#detailed-openai-compatible-api-support)
- [Request Fields](https://docs.parallel.ai/chat-api/sdk-compatibility#request-fields)
- [Simple Fields](https://docs.parallel.ai/chat-api/sdk-compatibility#simple-fields)
- [Tools / Functions Fields](https://docs.parallel.ai/chat-api/sdk-compatibility#tools-%2F-functions-fields)
- [Messages Array Fields](https://docs.parallel.ai/chat-api/sdk-compatibility#messages-array-fields)
- [Response Fields](https://docs.parallel.ai/chat-api/sdk-compatibility#response-fields)
- [Parallel-Specific Response Fields](https://docs.parallel.ai/chat-api/sdk-compatibility#parallel-specific-response-fields)
- [Error Message Compatibility](https://docs.parallel.ai/chat-api/sdk-compatibility#error-message-compatibility)
- [Header Compatibility](https://docs.parallel.ai/chat-api/sdk-compatibility#header-compatibility)

**Research Basis via OpenAI SDK**: When using task processors (`lite`, `base`, `core`) with the Chat API, the response includes a `basis` field with citations, reasoning, and confidence levels. Access it via `response.basis` in Python or `(response as any).basis` in TypeScript. See [Basis documentation](https://docs.parallel.ai/task-api/guides/access-research-basis) for details.

## [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#important-openai-compatibility-limitations)  Important OpenAI Compatibility Limitations

### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#api-behavior)  API Behavior

Here are the most substantial differences from using OpenAI:

- Multimodal input (images/audio) is not supported and will be ignored.
- Prompt caching is not supported.
- Most unsupported fields are silently ignored rather than producing errors. These are all documented below.

## [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#detailed-openai-compatible-api-support)  Detailed OpenAI Compatible API Support

### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#request-fields)  Request Fields

#### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#simple-fields)  Simple Fields

| Field | Support Status |
| --- | --- |
| model | Use `speed`, `lite`, `base`, or `core` |
| response\_format | Fully supported |
| stream | Fully supported |
| max\_tokens | Ignored |
| max\_completion\_tokens | Ignored |
| stream\_options | Ignored |
| top\_p | Ignored |
| parallel\_tool\_calls | Ignored |
| stop | Ignored |
| temperature | Ignored |
| n | Ignored |
| logprobs | Ignored |
| metadata | Ignored |
| prediction | Ignored |
| presence\_penalty | Ignored |
| frequency\_penalty | Ignored |
| seed | Ignored |
| service\_tier | Ignored |
| audio | Ignored |
| logit\_bias | Ignored |
| store | Ignored |
| user | Ignored |
| modalities | Ignored |
| top\_logprobs | Ignored |
| reasoning\_effort | Ignored |

#### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#tools-/-functions-fields)  Tools / Functions Fields

Tools are ignored.

#### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#messages-array-fields)  Messages Array Fields

| Field | Support Status |
| --- | --- |
| messages\[\].role | Fully supported |
| messages\[\].content | String only |
| messages\[\].name | Fully supported |
| messages\[\].tool\_calls | Ignored |
| messages\[\].tool\_call\_id | Ignored |
| messages\[\].function\_call | Ignored |
| messages\[\].audio | Ignored |
| messages\[\].modalities | Ignored |

The `content` field only supports string values. Structured content arrays (e.g., for multimodal inputs with text and image parts) are not supported.

### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#response-fields)  Response Fields

| Field | Support Status |
| --- | --- |
| id | Always empty |
| choices\[\] | Will always have a length of 1 |
| choices\[\].finish\_reason | Always empty |
| choices\[\].index | Fully supported |
| choices\[\].message.role | Fully supported |
| choices\[\].message.content | Fully supported |
| choices\[\].message.tool\_calls | Always empty |
| object | Always empty |
| created | Fully supported |
| model | Always empty |
| finish\_reason | Always empty |
| content | Fully supported |
| usage.completion\_tokens | Always empty |
| usage.prompt\_tokens | Always empty |
| usage.total\_tokens | Always empty |
| usage.completion\_tokens\_details | Always empty |
| usage.prompt\_tokens\_details | Always empty |
| choices\[\].message.refusal | Always empty |
| choices\[\].message.audio | Always empty |
| logprobs | Always empty |
| service\_tier | Always empty |
| system\_fingerprint | Always empty |

#### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#parallel-specific-response-fields)  Parallel-Specific Response Fields

The following fields are Parallel extensions not present in the OpenAI API:

| Field | Support Status |
| --- | --- |
| basis | Supported with task processors (`lite`, `base`, `core`) |

### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#error-message-compatibility)  Error Message Compatibility

The compatibility layer maintains approximately the same error formats as the OpenAI API.

### [​](https://docs.parallel.ai/chat-api/sdk-compatibility\#header-compatibility)  Header Compatibility

While the OpenAI SDK automatically manages headers, here is the complete list of headers supported by Parallel’s API for developers who need to work with them directly.

| Field | Support Status |
| --- | --- |
| authorization | Fully supported |
| x-ratelimit-limit-requests | Ignored |
| x-ratelimit-limit-tokens | Ignored |
| x-ratelimit-remaining-requests | Ignored |
| x-ratelimit-remaining-tokens | Ignored |
| x-ratelimit-reset-requests | Ignored |
| x-ratelimit-reset-tokens | Ignored |
| retry-after | Ignored |
| x-request-id | Ignored |
| openai-version | Ignored |
| openai-processing-ms | Ignored |

[Quickstart](https://docs.parallel.ai/chat-api/chat-quickstart) [Quickstart](https://docs.parallel.ai/findall-api/findall-quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Google Vertex AI - Parallel

**URL:** https://docs.parallel.ai/integrations/google-vertex

[Skip to main content](https://docs.parallel.ai/integrations/google-vertex#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Google Vertex AI

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Use cases](https://docs.parallel.ai/integrations/google-vertex#use-cases)
- [Example](https://docs.parallel.ai/integrations/google-vertex#example)
- [Supported models](https://docs.parallel.ai/integrations/google-vertex#supported-models)
- [Before you begin](https://docs.parallel.ai/integrations/google-vertex#before-you-begin)
- [Ground Gemini responses with Parallel Search](https://docs.parallel.ai/integrations/google-vertex#ground-gemini-responses-with-parallel-search)
- [Quota](https://docs.parallel.ai/integrations/google-vertex#quota)
- [Billing](https://docs.parallel.ai/integrations/google-vertex#billing)

The Parallel Search API is available in Google Vertex AI as an external grounding provider. Use it to ground Gemini model responses with up‑to‑date context from the public web.Read Vertex AI’s official documentation [here](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-parallel).

## [​](https://docs.parallel.ai/integrations/google-vertex\#use-cases)  Use cases

- Using web data for information completion or enrichment.
- Multi-hop agents that require deeper web searches for complex questions.
- Building APIs that integrate web search data.
- Employee-facing assistants for up-to-date analysis and reporting.
- Consumer apps (retail, travel) supporting informed purchase decisions.
- Automated agents (e.g., news analysis, KYC checks).
- Vertical agents (sales, coding, finance) fetching the latest context from the web.

## [​](https://docs.parallel.ai/integrations/google-vertex\#example)  Example

Who won the 2025 Las Vegas F1 Grand Prix?

| Without Grounding | With Grounding |
| --- | --- |
| The 2025 Las Vegas Grand Prix has not happened yet. The race is scheduled to take place on the weekend of November 20-22, 2025. Therefore, the winner is currently unknown. | The winner of the 2025 Las Vegas F1 Grand Prix was Max Verstappen of Red Bull Racing. The race took place on November 22, 2025. Sources: domain1.com, domain2.com, … |

## [​](https://docs.parallel.ai/integrations/google-vertex\#supported-models)  Supported models

The following models support Grounding with Parallel web search:

- Gemini 3 Flash preview
- Gemini 3 Pro preview
- Gemini 3 Pro Image preview
- Gemini 2.5 Pro
- Gemini 2.5 Flash preview
- Gemini 2.5 Flash-Lite preview
- Gemini 2.5 Flash
- Gemini 2.5 Flash-Lite
- Gemini 2.5 Flash with Gemini Live API native audio
- Gemini 2.5 Flash with Live API native audio (Preview) preview
- Gemini 2.0 Flash with Live API preview
- Gemini 2.0 Flash

## [​](https://docs.parallel.ai/integrations/google-vertex\#before-you-begin)  Before you begin

Get a Parallel API key from [Platform](https://platform.parallel.ai/). This API key is used in your request to Gemini.

## [​](https://docs.parallel.ai/integrations/google-vertex\#ground-gemini-responses-with-parallel-search)  Ground Gemini responses with Parallel Search

Request grounded responses from Gemini using the REST API. For best performance, use default settings for optional parameters unless you strictly require non‑default values. For guidance on crafting objectives, queries, and modes, see [Search API Best Practices](https://docs.parallel.ai/search/best-practices).Set up an HTTP method and URL with the following fields:

- `LOCATION`: The region to process the request. To use the global endpoint, exclude the location from the endpoint name and configure the resource location to `global`.
- `PROJECT_ID`: Your Google Cloud project ID.
- `MODEL_ID`: The ID of the Gemini model to use.

Copy

Ask AI

```
POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_ID:generateContent
```

Create your Gemini request JSON body with a grounding call to Parallel Search:

Copy

Ask AI

```
{
  "contents": [{\
    "role": "user",\
    "parts": [{\
      "text": "MODEL_PROMPT_TEXT"\
    }]\
  }],
  "tools": [{\
    "parallelAiSearch": {\
      "api_key": "PARALLEL_API_KEY",\
      "customConfigs": {\
        "source_policy": {\
          "exclude_domains": ["EXCLUDE_DOMAINS"],\
          "include_domains": ["INCLUDE_DOMAINS"]\
        },\
        "excerpts": {\
          "max_chars_per_result": MAX_CHARS_PER_RESULT,\
          "max_chars_total": MAX_CHARS_TOTAL\
        },\
        "mode": "fast"\
      }\
    }\
  }],
  "model": "projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_ID"
}
```

Execute your request:

Copy

Ask AI

```
curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d @request.json \
     "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_ID:generateContent"
```

You should receive a JSON response with the model’s grounded output and associated metadata.

For a complete working example, see the [Vertex AI demo](https://github.com/parallel-web/parallel-cookbook/tree/main/python-recipes/vertex_ai_demo) in the Parallel Cookbook.

## [​](https://docs.parallel.ai/integrations/google-vertex\#quota)  Quota

The default quota is 60 prompts per minute. If you need higher rate limits, contact `support@parallel.ai` and your Google account team with your use case and requirements.

## [​](https://docs.parallel.ai/integrations/google-vertex\#billing)  Billing

Using Gemini with Parallel incurs charges from both Gemini token consumption and use of [Parallel’s Search API](https://docs.parallel.ai/resources/pricing).

[Google Sheets](https://docs.parallel.ai/integrations/gsuite) [LangChain](https://docs.parallel.ai/integrations/langchain)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Preview - Parallel

**URL:** https://docs.parallel.ai/findall-api/features/findall-preview

[Skip to main content](https://docs.parallel.ai/findall-api/features/findall-preview#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Preview

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [How Preview Works](https://docs.parallel.ai/findall-api/features/findall-preview#how-preview-works)
- [Preview vs. Full Run](https://docs.parallel.ai/findall-api/features/findall-preview#preview-vs-full-run)
- [Key Characteristics](https://docs.parallel.ai/findall-api/features/findall-preview#key-characteristics)
- [Quick Example](https://docs.parallel.ai/findall-api/features/findall-preview#quick-example)
- [Best Practices](https://docs.parallel.ai/findall-api/features/findall-preview#best-practices)
- [Related Topics](https://docs.parallel.ai/findall-api/features/findall-preview#related-topics)

Preview mode lets you quickly and inexpensively test your FindAll queries with a small sample of candidates before committing to a full run. It’s ideal for validating your match conditions and enrichments.**When to use preview:**

- Test query structure before running on large datasets
- Validate match conditions work as expected
- Iterate quickly on FindAll schema and descriptions

## [​](https://docs.parallel.ai/findall-api/features/findall-preview\#how-preview-works)  How Preview Works

Preview mode uses the same API endpoint as regular FindAll runs, but with `generator: "preview"`. It generates approximately 10 evaluated candidates (both matched and unmatched) to give you a representative sample of results.

## [​](https://docs.parallel.ai/findall-api/features/findall-preview\#preview-vs-full-run)  Preview vs. Full Run

| Feature | Preview Mode | Full Run |
| --- | --- | --- |
| **Generator** | `preview` | `base`, `core`, `pro` |
| **Candidates Generated** | ~10 evaluated | Until `match_limit` matches found |
| **Match Limit** | Up to 10 | 5 to 1000 (inclusive) |
| **Speed** | Fast (minutes) | Slower (varies by generator) |
| **Cost** | Flat, cheap | Variable, higher |
| **Outputs** | Full | Full |
| **Enrichments** | ❌ No | ✅ Yes |
| **Can Extend** | ❌ No | ✅ Yes |
| **Can Cancel** | ❌ No | ✅ Yes |

### [​](https://docs.parallel.ai/findall-api/features/findall-preview\#key-characteristics)  Key Characteristics

- **Fast & Cost-Effective**: Much faster and cheaper than full runs
- **Sample Size**: Generates ~10 evaluated candidates with no guarantee of match rate
- **Full Outputs**: Candidates include full match outputs, reasoning, and citations (just like regular runs)
- **Capped Limit**: `match_limit` is capped at 10 and interpreted as candidates to evaluate, not matches to find
- **No Modifications**: Cannot be extended or cancelled after creation

Preview candidates follow the same structure as full run candidates. See [Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates) for details on candidate object structure and fields.

## [​](https://docs.parallel.ai/findall-api/features/findall-preview\#quick-example)  Quick Example

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/findall/runs" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15" \
  -H "Content-Type: application/json" \
  -d '{
    "objective": "FindAll portfolio companies of Khosla Ventures founded after 2020",
    "entity_type": "companies",
    "match_conditions": [\
      {\
        "name": "khosla_ventures_portfolio_check",\
        "description": "Company must be a portfolio company of Khosla Ventures."\
      },\
      {\
        "name": "founded_after_2020_check",\
        "description": "Company must have been founded after 2020."\
      }\
    ],
    "generator": "preview",
    "match_limit": 10
  }'
```

## [​](https://docs.parallel.ai/findall-api/features/findall-preview\#best-practices)  Best Practices

1. **Always Preview First**: Run preview to validate match conditions before committing to full searches
2. **Review Both Results**: Check matched and unmatched candidates to refine your query logic
3. **Test Enrichments Early**: Validate enrichment outputs in preview before running at scale
4. **Examine Reasoning**: Review the `basis` field to understand how matches were determined
5. **Iterate Quickly**: Use preview’s fast feedback loop to refine queries before full runs

## [​](https://docs.parallel.ai/findall-api/features/findall-preview\#related-topics)  Related Topics

- **[Quickstart Guide](https://docs.parallel.ai/findall-api/findall-quickstart)**: Get started with FindAll API
- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and how to cancel runs
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run)**: Complete endpoint documentation

[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle) [Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# DuckDB - Parallel

**URL:** https://docs.parallel.ai/data-integrations/duckdb

[Skip to main content](https://docs.parallel.ai/data-integrations/duckdb#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Data Integrations

DuckDB

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features](https://docs.parallel.ai/data-integrations/duckdb#features)
- [Installation](https://docs.parallel.ai/data-integrations/duckdb#installation)
- [Basic Usage - Batch Processing](https://docs.parallel.ai/data-integrations/duckdb#basic-usage-batch-processing)
- [Function Parameters](https://docs.parallel.ai/data-integrations/duckdb#function-parameters)
- [Return Value](https://docs.parallel.ai/data-integrations/duckdb#return-value)
- [Column Name Mapping](https://docs.parallel.ai/data-integrations/duckdb#column-name-mapping)
- [SQL Query as Source](https://docs.parallel.ai/data-integrations/duckdb#sql-query-as-source)
- [Creating Permanent Tables](https://docs.parallel.ai/data-integrations/duckdb#creating-permanent-tables)
- [Progress Tracking](https://docs.parallel.ai/data-integrations/duckdb#progress-tracking)
- [SQL UDF Usage](https://docs.parallel.ai/data-integrations/duckdb#sql-udf-usage)
- [Including Citations](https://docs.parallel.ai/data-integrations/duckdb#including-citations)
- [Processor Selection](https://docs.parallel.ai/data-integrations/duckdb#processor-selection)
- [Best Practices](https://docs.parallel.ai/data-integrations/duckdb#best-practices)

This integration is ideal for data engineers and analysts who work with DuckDB and need to enrich data with web intelligence directly in their SQL or Python workflows.Parallel provides a native DuckDB integration with two approaches: batch processing for efficiency, and SQL UDFs for flexibility.

View the complete demo notebook:

- [DuckDB Enrichment Demo](https://github.com/parallel-web/parallel-web-tools/blob/main/notebooks/duckdb_enrichment_demo.ipynb)

## [​](https://docs.parallel.ai/data-integrations/duckdb\#features)  Features

- **Batch Processing**: Process all rows in parallel with a single API call (recommended)
- **SQL UDF**: Use `parallel_enrich()` directly in SQL queries
- **Progress Callbacks**: Track enrichment progress for large datasets
- **Permanent Tables**: Optionally save results to a new table

## [​](https://docs.parallel.ai/data-integrations/duckdb\#installation)  Installation

Copy

Ask AI

```
pip install parallel-web-tools[duckdb]
```

Or with all dependencies:

Copy

Ask AI

```
pip install parallel-web-tools[all]
```

## [​](https://docs.parallel.ai/data-integrations/duckdb\#basic-usage-batch-processing)  Basic Usage - Batch Processing

Batch processing is the recommended approach for enriching multiple rows efficiently.

Copy

Ask AI

```
import duckdb
from parallel_web_tools.integrations.duckdb import enrich_table

# Create a connection and sample data
conn = duckdb.connect()
conn.execute("""
    CREATE TABLE companies AS SELECT * FROM (VALUES
        ('Google', 'google.com'),
        ('Microsoft', 'microsoft.com'),
        ('Apple', 'apple.com')
    ) AS t(name, website)
""")

# Enrich the table
result = enrich_table(
    conn,
    source_table="companies",
    input_columns={
        "company_name": "name",
        "website": "website",
    },
    output_columns=[\
        "CEO name",\
        "Founding year",\
        "Headquarters city",\
    ],
)

# Query the permanent table later
conn.execute("SELECT * FROM enriched_companies").fetchall()
```

## [​](https://docs.parallel.ai/data-integrations/duckdb\#progress-tracking)  Progress Tracking

Track progress for large enrichment jobs:

Copy

Ask AI

```
def on_progress(completed: int, total: int):
    print(f"Progress: {completed}/{total} ({100*completed/total:.0f}%)")

result = enrich_table(
    conn,
    source_table="companies",
    input_columns={"company_name": "name"},
    output_columns=["CEO name"],
    progress_callback=on_progress,
)
```

## [​](https://docs.parallel.ai/data-integrations/duckdb\#sql-udf-usage)  SQL UDF Usage

For flexibility in SQL queries, you can register a `parallel_enrich()` function:

Copy

Ask AI

```
import duckdb
import json
from parallel_web_tools.integrations.duckdb import register_parallel_functions

conn = duckdb.connect()
conn.execute("CREATE TABLE companies AS SELECT 'Google' as name")

# Register the UDF
register_parallel_functions(conn, processor="lite-fast")

# Use in SQL
results = conn.execute("""
    SELECT
        name,
        parallel_enrich(
            json_object('company_name', name),
            json_array('CEO name', 'Founding year')
        ) as enriched
    FROM companies
""").fetchall()

# Parse the JSON result
for name, enriched_json in results:
    data = json.loads(enriched_json)
    print(f"{name}: CEO = {data.get('ceo_name')}")
```

The SQL UDF processes rows individually. For better performance with multiple rows, use batch processing with `enrich_table()`.

## [​](https://docs.parallel.ai/data-integrations/duckdb\#including-citations)  Including Citations

Copy

Ask AI

```
result = enrich_table(
    conn,
    source_table="companies",
    input_columns={"company_name": "name"},
    output_columns=["CEO name"],
    include_basis=True,
)

# Recommended - processes all rows in parallel
result = enrich_table(conn, "companies", ...)

# Slower - one API call per row
conn.execute("SELECT *, parallel_enrich(...) FROM companies")
```

Use specific descriptions

Be specific in your output column descriptions for better results:

Copy

Ask AI

```
output_columns = [\
    "CEO name (current CEO or equivalent leader)",\
    "Founding year (YYYY format)",\
    "Annual revenue (USD, most recent fiscal year)",\
]
```

Handle errors gracefully

Errors don’t stop processing - partial results are returned:

Copy

Ask AI

```
result = enrich_table(conn, ...)

if result.error_count > 0:
    print(f"Failed rows: {result.error_count}")
    for error in result.errors:
        print(f"  Row {error['row']}: {error['error']}")

# Errors appear as NULL in the result
df = result.relation.fetchdf()
successful = df[df['ceo_name'].notna()]
```

Cost management

- Use `lite-fast` for high-volume, basic enrichments
- Test with small batches before processing large tables
- Store results in permanent tables to avoid re-enriching

[Apache Spark](https://docs.parallel.ai/data-integrations/spark) [Google BigQuery](https://docs.parallel.ai/data-integrations/bigquery)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Extend - Parallel

**URL:** https://docs.parallel.ai/findall-api/features/findall-extend

[Skip to main content](https://docs.parallel.ai/findall-api/features/findall-extend#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Extend

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Overview](https://docs.parallel.ai/findall-api/features/findall-extend#overview)
- [How Extend Works](https://docs.parallel.ai/findall-api/features/findall-extend#how-extend-works)
- [Limitations](https://docs.parallel.ai/findall-api/features/findall-extend#limitations)
- [Related Topics](https://docs.parallel.ai/findall-api/features/findall-extend#related-topics)

## [​](https://docs.parallel.ai/findall-api/features/findall-extend\#overview)  Overview

Extend allows you to increase the `match_limit` of an existing FindAll run to get more results using the same evaluation criteria—without paying the fixed cost again. Start with a small limit (10-20) to validate your criteria, then extend to get more matches.

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/extend" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15" \
  -H "Content-Type: application/json" \
  -d '{ "additional_match_limit": 40 }'
```

### [​](https://docs.parallel.ai/findall-api/features/findall-extend\#how-extend-works)  How Extend Works

- **Increases match limit:** The `additional_match_limit` you set is the **incremental** number of matches to add (not the total). For example, to go from 10 to 50 matches, set `additional_match_limit: 40`, not `50`.
- **Continues the same evaluation:** All other parameters— **generator**, **filters**, **enrichments**, and **match conditions**—stay exactly the same as the original run.
- **Handles run status automatically:**
  - If the run is _active_, it continues seamlessly up to the new match limit.
  - If the run is _completed_, it automatically “respawns” and resumes until reaching the new limit.
- **Pricing:** Extending has **no fixed cost—you only pay for the additional matches beyond the original run**. For example, extending from 10 to 100 matches means paying for 90 additional matches (plus evaluation costs).

### [​](https://docs.parallel.ai/findall-api/features/findall-extend\#limitations)  Limitations

- **Preview runs:** Cannot be extended. Use a full generator (`base`, `core`, or `pro`) if you plan to extend.
- **Fixed parameters:** Cannot modify processor, filters, enrichments, or match conditions. Start a new run to change criteria.nerator
- **Candidate reuse:** May process previously evaluated candidates before finding new ones. Start a new run for time-sensitive searches.

## [​](https://docs.parallel.ai/findall-api/features/findall-extend\#related-topics)  Related Topics

- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and how to cancel runs
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run)**: Complete endpoint documentation

[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook) [Cancel](https://docs.parallel.ai/findall-api/features/findall-cancel)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Stream Task Group Events - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks (Beta)

Stream Task Group Events

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group_events = client.beta.task_group.events("taskgroup_id")
for event in task_group_events:
    print(event)
```

200

404

422

Copy

Ask AI

```
{
  "type": "task_group_status",
  "event_id": "123",
  "status": {
    "num_task_runs": 1,
    "task_run_status_counts": {
      "completed": 1
    },
    "is_active": false,
    "status_message": "",
    "modified_at": "2025-04-23T20:21:48.037943Z"
  }
}
```

GET

/

v1beta

/

tasks

/

groups

/

{taskgroup\_id}

/

events

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group_events = client.beta.task_group.events("taskgroup_id")
for event in task_group_events:
    print(event)
```

200

404

422

Copy

Ask AI

```
{
  "type": "task_group_status",
  "event_id": "123",
  "status": {
    "num_task_runs": 1,
    "task_run_status_counts": {
      "completed": 1
    },
    "is_active": false,
    "status_message": "",
    "modified_at": "2025-04-23T20:21:48.037943Z"
  }
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#parameter-taskgroup-id)

taskgroup\_id

string

required

#### Query Parameters

[​](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#parameter-one-of-0)

last\_event\_id

string \| null

[​](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#parameter-one-of-0)

timeout

number \| null

#### Response

200

text/event-stream

Successful Response

- TaskGroupStatusEvent

- TaskRunEvent

- ErrorEvent

Event indicating an update to group status.

[​](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#response-one-of-0-type)

type

string

required

Event type; always 'task\_group\_status'.

Allowed value: `"task_group_status"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#response-one-of-0-event-id)

event\_id

string

required

Cursor to resume the event stream.

[​](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events#response-one-of-0-status)

status

TaskGroupStatus · object

required

Task group status object.

Showchild attributes

[Add Runs to Task Group](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group) [Retrieve Task Group Run](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve Task Group - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks (Beta)

Retrieve Task Group

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group = client.beta.task_group.retrieve("taskgroup_id")
print(task_group.status)
```

200

422

Copy

Ask AI

```
{
  "taskgroup_id": "<string>",
  "status": {
    "num_task_runs": 123,
    "task_run_status_counts": {},
    "is_active": true,
    "status_message": "<string>",
    "modified_at": "2025-04-24T18:56:22.513132Z"
  },
  "created_at": "2025-04-24T18:56:22.513132Z",
  "metadata": {}
}
```

GET

/

v1beta

/

tasks

/

groups

/

{taskgroup\_id}

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group = client.beta.task_group.retrieve("taskgroup_id")
print(task_group.status)
```

200

422

Copy

Ask AI

```
{
  "taskgroup_id": "<string>",
  "status": {
    "num_task_runs": 123,
    "task_run_status_counts": {},
    "is_active": true,
    "status_message": "<string>",
    "modified_at": "2025-04-24T18:56:22.513132Z"
  },
  "created_at": "2025-04-24T18:56:22.513132Z",
  "metadata": {}
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group#parameter-taskgroup-id)

taskgroup\_id

string

required

#### Response

200

application/json

Successful Response

Response object for a task group, including its status and metadata.

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group#response-taskgroup-id)

taskgroup\_id

string

required

ID of the group.

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group#response-status)

status

TaskGroupStatus · object

required

Status of the group.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group#response-created-at-one-of-0)

created\_at

string \| null

required

Timestamp of the creation of the group, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the group.

Showchild attributes

[Create Task Group](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group) [Fetch Task Group Runs](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Add Runs to Task Group - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks (Beta)

Add Runs to Task Group

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Beta params

Copy

Ask AI

```
from parallel import Parallel
from parallel.types.beta import McpServerParam
from parallel.types.beta.beta_run_input_param import BetaRunInputParam

client = Parallel(api_key="API Key")
group_status = client.beta.task_group.add_runs(
    "taskgroup_id",
    inputs=[\
        BetaRunInputParam(\
            input="What was the GDP of France in 2023?",\
            processor="base",\
            mcp_servers=[McpServerParam(\
                type="url",\
                name="parallel_web_search",\
                url="https://mcp.parallel.ai/v1beta/search_mcp",\
                headers={"x-api-key": "API Key"}\
            )]\
        )\
    ],
    betas=["mcp-server-2025-07-17"]
)
print(group_status.status)
```

200

422

Copy

Ask AI

```
{
  "status": {
    "num_task_runs": 123,
    "task_run_status_counts": {},
    "is_active": true,
    "status_message": "<string>",
    "modified_at": "2025-04-24T18:56:22.513132Z"
  },
  "run_ids": [\
    "<string>"\
  ],
  "run_cursor": "<string>",
  "event_cursor": "<string>"
}
```

POST

/

v1beta

/

tasks

/

groups

/

{taskgroup\_id}

/

runs

Try it

Python

Beta params

Copy

Ask AI

```
from parallel import Parallel
from parallel.types.beta import McpServerParam
from parallel.types.beta.beta_run_input_param import BetaRunInputParam

client = Parallel(api_key="API Key")
group_status = client.beta.task_group.add_runs(
    "taskgroup_id",
    inputs=[\
        BetaRunInputParam(\
            input="What was the GDP of France in 2023?",\
            processor="base",\
            mcp_servers=[McpServerParam(\
                type="url",\
                name="parallel_web_search",\
                url="https://mcp.parallel.ai/v1beta/search_mcp",\
                headers={"x-api-key": "API Key"}\
            )]\
        )\
    ],
    betas=["mcp-server-2025-07-17"]
)
print(group_status.status)
```

200

422

Copy

Ask AI

```
{
  "status": {
    "num_task_runs": 123,
    "task_run_status_counts": {},
    "is_active": true,
    "status_message": "<string>",
    "modified_at": "2025-04-24T18:56:22.513132Z"
  },
  "run_ids": [\
    "<string>"\
  ],
  "run_cursor": "<string>",
  "event_cursor": "<string>"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#parameter-taskgroup-id)

taskgroup\_id

string

required

#### Body

application/json

Request to initiate new task runs in a task group.

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#body-inputs)

inputs

BetaTaskRunInput · object\[\]

required

List of task runs to execute. Up to 1,000 runs can be specified per request. If you'd like to add more runs, split them across multiple TaskGroup POST requests.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#body-default-task-spec-one-of-0)

default\_task\_spec

TaskSpec · object

Default task spec to use for the runs. If task\_spec is specified in a run, it overrides this default.

Showchild attributes

#### Response

200

application/json

Successful Response

Response from adding new task runs to a task group.

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#response-status)

status

TaskGroupStatus · object

required

Status of the group.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#response-run-ids)

run\_ids

string\[\]

required

IDs of the newly created runs.

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#response-run-cursor-one-of-0)

run\_cursor

string \| null

required

Cursor for these runs in the run stream at taskgroup/runs?last\_event\_id=<run\_cursor>. Empty for the first runs in the group.

[​](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group#response-event-cursor-one-of-0)

event\_cursor

string \| null

required

Cursor for these runs in the event stream at taskgroup/events?last\_event\_id=<event\_cursor>. Empty for the first runs in the group.

[Fetch Task Group Runs](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs) [Stream Task Group Events](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve Monitor - Parallel

**URL:** https://docs.parallel.ai/api-reference/monitor/retrieve-monitor

[Skip to main content](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

Retrieve Monitor

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Retrieve Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",
  "query": "Extract recent news about AI",
  "status": "active",
  "cadence": "daily",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "https://example.com/webhook",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "created_at": "2025-04-23T20:21:48.037943Z"
}
```

GET

/

v1alpha

/

monitors

/

{monitor\_id}

Try it

Retrieve Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",
  "query": "Extract recent news about AI",
  "status": "active",
  "cadence": "daily",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "https://example.com/webhook",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "created_at": "2025-04-23T20:21:48.037943Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#parameter-monitor-id)

monitor\_id

string

required

#### Response

200

application/json

Successful Response

Response object for a monitor, including its status, cadence and metadata.

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-monitor-id)

monitor\_id

string

required

ID of the monitor.

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-query)

query

string

required

The query being monitored.

Example:

`"Recent news about LLM models."`

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-status)

status

enum<string>

required

Status of the monitor.

Available options:

`active`,

`canceled`

Examples:

`"active"`

`"canceled"`

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-cadence)

cadence

enum<string>

required

Cadence of the monitor.

Available options:

`daily`,

`weekly`,

`hourly`,

`every_two_weeks`

Examples:

`"daily"`

`"weekly"`

`"hourly"`

`"every_two_weeks"`

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-created-at)

created\_at

string<date-time>

required

Timestamp of the creation of the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the monitor.

Showchild attributes

Example:

```
{ "key": "value" }
```

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-webhook-one-of-0)

webhook

MonitorWebhook · object

Webhook configuration for the monitor.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-output-schema-one-of-0)

output\_schema

JsonSchema · object

Output schema for the monitor event.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor#response-last-run-at-one-of-0)

last\_run\_at

string \| null

Timestamp of the last run for the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[Create Monitor](https://docs.parallel.ai/api-reference/monitor/create-monitor) [Update Monitor](https://docs.parallel.ai/api-reference/monitor/update-monitor)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Stream FindAll Events - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Stream FindAll Events

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

events = client.beta.findall.events(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {events.findall_id} events: {events.model_dump_json(indent=2)}")
```

200

404

422

Copy

Ask AI

```
{
  "type": "findall.candidate.generated",
  "timestamp": "2025-09-10T21:02:08.626446Z",
  "event_id": "56cee734dbc84172bfc491327f2a0183",
  "data": {
    "candidate_id": "candidate_52e1e30b-4e0a-49d8-82eb-79e64e0ed015",
    "name": "Pika",
    "url": "pika.art",
    "description": "Pika is an AI video generation platform that creates and edits videos from text prompts or images.",
    "match_status": "generated"
  }
}
```

GET

/

v1beta

/

findall

/

runs

/

{findall\_id}

/

events

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

events = client.beta.findall.events(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {events.findall_id} events: {events.model_dump_json(indent=2)}")
```

200

404

422

Copy

Ask AI

```
{
  "type": "findall.candidate.generated",
  "timestamp": "2025-09-10T21:02:08.626446Z",
  "event_id": "56cee734dbc84172bfc491327f2a0183",
  "data": {
    "candidate_id": "candidate_52e1e30b-4e0a-49d8-82eb-79e64e0ed015",
    "name": "Pika",
    "url": "pika.art",
    "description": "Pika is an AI video generation platform that creates and edits videos from text prompts or images.",
    "match_status": "generated"
  }
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#parameter-findall-id)

findall\_id

string

required

#### Query Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#parameter-one-of-0)

last\_event\_id

string \| null

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#parameter-one-of-0)

timeout

number \| null

#### Response

200

text/event-stream

Successful Response

- FindAllSchemaUpdatedEvent

- FindAllRunStatusEvent

- FindAllCandidateMatchStatusEvent

- ErrorEvent

Event containing full snapshot of FindAll run state.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#response-one-of-0-type)

type

enum<string>

required

Event type; always 'findall.schema.updated'.

Available options:

`findall.schema.updated`

Allowed value: `"findall.schema.updated"`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#response-one-of-0-timestamp)

timestamp

string<date-time>

required

Timestamp of the event.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#response-one-of-0-event-id)

event\_id

string

required

Unique event identifier for the event.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events#response-one-of-0-data)

data

FindAllSchema · object

required

Updated FindAll schema.

Showchild attributes

[Retrieve FindAll Run Status](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status) [FindAll Run Result](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# FindAll Run Result - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

FindAll Run Result

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run_result = client.beta.findall.result(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {run_result.run.findall_id} result: {run_result.model_dump_json(indent=2)}")
```

200

422

Copy

Ask AI

```
{
  "run": {
    "findall_id": "findall_56ccc4d188fb41a0803a935cf485c774",
    "status": {
      "status": "running",
      "is_active": true,
      "metrics": {
        "generated_candidates_count": 1,
        "matched_candidates_count": 1
      }
    },
    "generator": "base",
    "metadata": {},
    "created_at": "2025-09-10T21:02:08.626446Z",
    "modified_at": "2025-09-10T21:02:08.627376Z"
  },
  "candidates": [\
    {\
      "candidate_id": "candidate_7594eb7c-4f4a-487f-9d0c-9d1e63ec240c",\
      "name": "Cognition AI",\
      "url": "cognition.ai",\
      "match_status": "matched",\
      "output": {\
        "developing_ai_products_check": "yes",\
        "raised_series_a_2024_check": "yes"\
      },\
      "basis": [\
        {\
          "field": "developing_ai_products_check",\
          "citations": [\
            {\
              "title": "Cognition - Devin and Cognition AI",\
              "url": "https://cognition.ai/",\
              "excerpts": [\
                "We're the makers of Devin, a collaborative AI teammate that helps ambitious engineering teams achieve more.",\
                "An applied AI lab building the future of software engineering",\
                "Cognition"\
              ]\
            }\
          ],\
          "reasoning": "The search results repeatedly state that Cognition AI is an 'applied AI lab building the future of software engineering' and that they developed 'Devin AI', described as the 'world's first AI software engineer'. This directly confirms they are developing AI products.",\
          "confidence": "high"\
        },\
        {\
          "field": "raised_series_a_2024_check",\
          "citations": [\
            {\
              "title": "Cognition Labs Raises $21 Million Series A to Support AI Coding Products",\
              "url": "https://voicebot.ai/2024/04/25/cognition-labs-raises-21-million-series-a-to-support-ai-coding-products/",\
              "excerpts": [\
                "Cognition Labs Raises $21 Million Series A to Support AI Coding Products"\
              ]\
            }\
          ],\
          "reasoning": "The article from voicebot.ai, dated April 25, 2024, states that Founders Fund led a \"$21 million Series A investment\" for Cognition Labs. This confirms that Series A funding was raised in 2024.",\
          "confidence": "low"\
        }\
      ]\
    }\
  ]
}
```

GET

/

v1beta

/

findall

/

runs

/

{findall\_id}

/

result

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run_result = client.beta.findall.result(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {run_result.run.findall_id} result: {run_result.model_dump_json(indent=2)}")
```

200

422

Copy

Ask AI

```
{
  "run": {
    "findall_id": "findall_56ccc4d188fb41a0803a935cf485c774",
    "status": {
      "status": "running",
      "is_active": true,
      "metrics": {
        "generated_candidates_count": 1,
        "matched_candidates_count": 1
      }
    },
    "generator": "base",
    "metadata": {},
    "created_at": "2025-09-10T21:02:08.626446Z",
    "modified_at": "2025-09-10T21:02:08.627376Z"
  },
  "candidates": [\
    {\
      "candidate_id": "candidate_7594eb7c-4f4a-487f-9d0c-9d1e63ec240c",\
      "name": "Cognition AI",\
      "url": "cognition.ai",\
      "match_status": "matched",\
      "output": {\
        "developing_ai_products_check": "yes",\
        "raised_series_a_2024_check": "yes"\
      },\
      "basis": [\
        {\
          "field": "developing_ai_products_check",\
          "citations": [\
            {\
              "title": "Cognition - Devin and Cognition AI",\
              "url": "https://cognition.ai/",\
              "excerpts": [\
                "We're the makers of Devin, a collaborative AI teammate that helps ambitious engineering teams achieve more.",\
                "An applied AI lab building the future of software engineering",\
                "Cognition"\
              ]\
            }\
          ],\
          "reasoning": "The search results repeatedly state that Cognition AI is an 'applied AI lab building the future of software engineering' and that they developed 'Devin AI', described as the 'world's first AI software engineer'. This directly confirms they are developing AI products.",\
          "confidence": "high"\
        },\
        {\
          "field": "raised_series_a_2024_check",\
          "citations": [\
            {\
              "title": "Cognition Labs Raises $21 Million Series A to Support AI Coding Products",\
              "url": "https://voicebot.ai/2024/04/25/cognition-labs-raises-21-million-series-a-to-support-ai-coding-products/",\
              "excerpts": [\
                "Cognition Labs Raises $21 Million Series A to Support AI Coding Products"\
              ]\
            }\
          ],\
          "reasoning": "The article from voicebot.ai, dated April 25, 2024, states that Founders Fund led a \"$21 million Series A investment\" for Cognition Labs. This confirms that Series A funding was raised in 2024.",\
          "confidence": "low"\
        }\
      ]\
    }\
  ]
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result#parameter-findall-id)

findall\_id

string

required

#### Response

200

application/json

Successful Response

Complete FindAll search results.

Represents a snapshot of a FindAll run, including run metadata and a list of
candidate entities with their match status and details at the time the snapshot was
taken.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result#response-run)

run

FindAllRun · object

required

FindAll run object.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result#response-candidates)

candidates

FindAllCandidate · object\[\]

required

All evaluated candidates at the time of the snapshot.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result#response-last-event-id-one-of-0)

last\_event\_id

string \| null

ID of the last event of the run at the time of the request. This can be used to resume streaming from the last event.

[Stream FindAll Events](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events) [Extend FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Extract API Quickstart - Parallel

**URL:** https://docs.parallel.ai/extract/extract-quickstart

[Skip to main content](https://docs.parallel.ai/extract/extract-quickstart#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Extract

Extract API Quickstart

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [1\. Set up Prerequisites](https://docs.parallel.ai/extract/extract-quickstart#1-set-up-prerequisites)
- [2\. Extract API Example](https://docs.parallel.ai/extract/extract-quickstart#2-extract-api-example)
- [Response Structure](https://docs.parallel.ai/extract/extract-quickstart#response-structure)
- [Sample Response](https://docs.parallel.ai/extract/extract-quickstart#sample-response)
- [Next Steps](https://docs.parallel.ai/extract/extract-quickstart#next-steps)

The **Extract API** converts any public URL into clean markdown, including
JavaScript-heavy pages and PDFs. It returns focused excerpts aligned to your objective,
or full page content if requested.

**Beta Notice**: The Search and Extract APIs are currently in beta and subject to change. Usage is
limited to 600 requests per minute.

See [Pricing](https://docs.parallel.ai/getting-started/pricing) for a detailed schedule of rates.

## [​](https://docs.parallel.ai/extract/extract-quickstart\#1-set-up-prerequisites)  1\. Set up Prerequisites

Generate your API key on [Platform](https://platform.parallel.ai/). Then, set up with the TypeScript SDK, Python SDK or with cURL:

cURL

Python

TypeScript

Copy

Ask AI

```
echo "Install curl and jq via brew, apt, or your favorite package manager"
export PARALLEL_API_KEY="PARALLEL_API_KEY"
```

## [​](https://docs.parallel.ai/extract/extract-quickstart\#2-extract-api-example)  2\. Extract API Example

Extract clean markdown content from specific URLs. This example retrieves content from
the UN’s history page with excerpts focused on the founding:

cURL

Python

TypeScript

Copy

Ask AI

```
curl https://api.parallel.ai/v1beta/extract \
  -H "Content-Type: application/json" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: search-extract-2025-10-10" \
  -d '{
    "urls": ["https://www.un.org/en/about-us/history-of-the-un"],
    "objective": "When was the United Nations established?",
    "excerpts": true,
    "full_content": false
  }'
```

## [​](https://docs.parallel.ai/extract/extract-quickstart\#response-structure)  Response Structure

Each result in the `results` array contains:

| Field | Type | Description |
| --- | --- | --- |
| `url` | string | The URL that was extracted. |
| `title` | string? | Page title, if available. |
| `publish_date` | string? | Publish date in `YYYY-MM-DD` format, if available. |
| `excerpts` | string\[\]? | Relevant excerpts formatted as markdown, if `excerpts` was enabled. |
| `full_content` | string? | Full page content formatted as markdown, if `full_content` was enabled. |

Both `excerpts` and `full_content` return content formatted as markdown. This includes links as `[text](url)`, headings, lists, and other markup. If you need plain text, strip the markdown formatting in your application.

### [​](https://docs.parallel.ai/extract/extract-quickstart\#sample-response)  Sample Response

Copy

Ask AI

```
{
  "extract_id": "extract_470002358ec147e8a40cb70d0d82627e",
  "results": [\
    {\
      "url": "https://www.un.org/en/about-us/history-of-the-un",\
      "title": "History of the United Nations | United Nations",\
      "publish_date": "2001-01-01",\
      "excerpts": [\
        "[Skip to main content]()\nToggle navigation [Welcome to the United Nations](/)\n[العربية](/ar/about-us/history-of-the-un \"تاريخ الأمم المتحدة\")\n[中文](/zh/about-us/history-of-the-un \"联合国历史\")\nNederlands\n[English](/en/about-us/history-of-the-un \"History of the United Nations\")\n[Français](/fr/about-us/history-of-the-un \"L'histoire des Nations Unies\")\nKreyòl\nहिन्दी\nBahasa Indonesia\nPolski\nPortuguês\n[Русский](/ru/about-us/history-of-the-un \"История Организации Объединенных Наций\")\n[Español](/es/about-us/history-of-the-un \"Historia de las Naciones Unidas\")\nKiswahili\nTürkçe\nУкраїнська\n[](/en \"United Nations\") Peace, dignity and equality  \non a healthy planet\n\nSection Title: History of the United Nations\nContent:\nThe UN Secretariat building (at left) under construction in New York City in 1949. At right, the Secretariat and General Assembly buildings four decades later in 1990. UN Photo: MB (L) ; UN Photo (R)\nAs World War II was about to end in 1945, nations were in ruins, and the world wanted peace. Representatives of 50 countries gathered at the United Nations Conference on International Organization in San Francisco, California from 25 April to 26 June 1945. For the next two months, they proceeded to draft and then sign the UN Charter, which created a new international organization, the United Nations, which, it was hoped, would prevent another world war like the one they had just lived through.\nFour months after the San Francisco Conference ended, the United Nations officially began, on 24 October 1945, when it came into existence after its Charter had been ratified by China, France, the Soviet Union, the United Kingdom, the United States and by a majority of other signatories.\nNow, more than 75 years later, the United Nations is still working to maintain international peace and security, give humanitarian assistance to those in need, protect human rights, and uphold international law.\n\nSection Title: History of the United Nations\nContent:\nAt the same time, the United Nations is doing new work not envisioned for it in 1945 by its founders. The United Nations has set [sustainable development goals](http://www.un.org/sustainabledevelopment/sustainable-development-goals/) for 2030, in order to achieve a better and more sustainable future for us all. UN Member States have also agreed to [climate action](http://www.un.org/en/climatechange) to limit global warming.\nWith many achievements now in its past, the United Nations is looking to the future, to new achievements.\nThe history of the United Nations is still being written.\n\nSection Title: History of the United Nations > [Milestones in UN History](https://www.un.org/en/about-us/history-of-the-un/1941-1950)\nContent:\n[](https://www.un.org/en/about-us/history-of-the-un/1941-1950)\nTimelines by decade highlighting key UN milestones\n\nSection Title: History of the United Nations > [The San Francisco Conference](https://www.un.org/en/about-us/history-of-the-un/san-francisco-conference)\nContent:\n[](https://www.un.org/en/about-us/history-of-the-un/san-francisco-conference)\nThe story of the 1945 San Francisco Conference\n\nSection Title: History of the United Nations > [Preparatory Years: UN Charter History](https://www.un.org/en/about-us/history-of-the-un/preparatory-years)\nContent:\n[](https://www.un.org/en/about-us/history-of-the-un/preparatory-years)\nThe steps that led to the signing of the UN Charter in 1945\n\nSection Title: History of the United Nations > [Predecessor: The League of Nations](https://www.un.org/en/about-us/history-of-the-un/predecessor)\nContent:\n[](https://www.un.org/en/about-us/history-of-the-un/predecessor)\nThe UN's predecessor and other earlier international organizations\n[](https://www.addtoany.com/share)\n"\
      ],\
      "full_content": null\
    }\
  ],
  "errors": [],
  "warnings": null,
  "usage": [\
    {\
      "name": "sku_extract_excerpts",\
      "count": 1\
    }\
  ]
}
```

## [​](https://docs.parallel.ai/extract/extract-quickstart\#next-steps)  Next Steps

- **[Best Practices](https://docs.parallel.ai/extract/best-practices)** — learn about objectives, fetch policies, and excerpt settings
- **[API Reference](https://docs.parallel.ai/api-reference/extract-beta/extract)** — full parameter specifications, constraints, and response schema
- **[Rate Limits](https://docs.parallel.ai/getting-started/rate-limits)** — default quotas per product

[Search MCP](https://docs.parallel.ai/search/search-mcp) [Best Practices](https://docs.parallel.ai/extract/best-practices)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve Task Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks v1

Retrieve Task Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_run = client.task_run.retrieve("run_id")
print(task_run.status)
```

200

401

404

422

Copy

Ask AI

```
{
  "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "status": "running",
  "is_active": true,
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "created_at": "2025-04-23T20:21:48.037943Z",
  "modified_at": "2025-04-23T20:21:48.037943Z"
}
```

GET

/

v1

/

tasks

/

runs

/

{run\_id}

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_run = client.task_run.retrieve("run_id")
print(task_run.status)
```

200

401

404

422

Copy

Ask AI

```
{
  "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "status": "running",
  "is_active": true,
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "created_at": "2025-04-23T20:21:48.037943Z",
  "modified_at": "2025-04-23T20:21:48.037943Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#parameter-run-id)

run\_id

string

required

#### Response

200

application/json

Successful Response

Status of a task run.

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-run-id)

run\_id

string

required

ID of the task run.

Example:

`"trun_e0083b6aac0544eb8686e8d2a76533d2"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-interaction-id)

interaction\_id

string

required

Identifier for this interaction. Pass this value as `previous_interaction_id` to reuse context for a future request.

Example:

`"trun_e0083b6aac0544eb8686e8d2a76533d2"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-status)

status

enum<string>

required

Status of the run.

Available options:

`queued`,

`action_required`,

`running`,

`completed`,

`failed`,

`cancelling`,

`cancelled`

Examples:

`"queued"`

`"action_required"`

`"running"`

`"completed"`

`"failed"`

`"cancelling"`

`"cancelled"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-is-active)

is\_active

boolean

required

Whether the run is currently active, i.e. status is one of {'cancelling', 'queued', 'running'}.

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-processor)

processor

string

required

Processor used for the run.

Example:

`"base"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-created-at-one-of-0)

created\_at

string \| null

required

Timestamp of the creation of the task, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-modified-at-one-of-0)

modified\_at

string \| null

required

Timestamp of the last modification to the task, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-warnings-one-of-0)

warnings

Warning · object\[\] \| null

Warnings for the run, if any.

Showchild attributes

Example:

```
[]
```

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-error-one-of-0)

error

Error · object

Error for the run, present only if status is 'failed'.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the run.

Showchild attributes

Example:

```
{}
```

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run#response-taskgroup-id-one-of-0)

taskgroup\_id

string \| null

ID of the taskgroup to which the run belongs.

[Create Task Run](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run) [Retrieve Task Run Input](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# List Monitors - Parallel

**URL:** https://docs.parallel.ai/api-reference/monitor/list-monitors

[Skip to main content](https://docs.parallel.ai/api-reference/monitor/list-monitors#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

List Monitors

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

List Monitors

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

422

Copy

Ask AI

```
[\
  {\
    "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",\
    "query": "Extract recent news about AI",\
    "status": "active",\
    "cadence": "daily",\
    "metadata": {\
      "key": "value"\
    },\
    "webhook": {\
      "url": "https://example.com/webhook",\
      "event_types": [\
        "monitor.event.detected"\
      ]\
    },\
    "created_at": "2025-04-23T20:21:48.037943Z"\
  },\
  {\
    "monitor_id": "monitor_b0179f70195e4258a3b982c1b6d8bd3a",\
    "query": "Extract recent news about AI",\
    "status": "canceled",\
    "cadence": "daily",\
    "metadata": {\
      "key": "value"\
    },\
    "webhook": {\
      "url": "https://example.com/webhook",\
      "event_types": [\
        "monitor.event.detected"\
      ]\
    },\
    "created_at": "2025-04-23T20:21:48.037943Z"\
  }\
]
```

GET

/

v1alpha

/

monitors

Try it

List Monitors

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

422

Copy

Ask AI

```
[\
  {\
    "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",\
    "query": "Extract recent news about AI",\
    "status": "active",\
    "cadence": "daily",\
    "metadata": {\
      "key": "value"\
    },\
    "webhook": {\
      "url": "https://example.com/webhook",\
      "event_types": [\
        "monitor.event.detected"\
      ]\
    },\
    "created_at": "2025-04-23T20:21:48.037943Z"\
  },\
  {\
    "monitor_id": "monitor_b0179f70195e4258a3b982c1b6d8bd3a",\
    "query": "Extract recent news about AI",\
    "status": "canceled",\
    "cadence": "daily",\
    "metadata": {\
      "key": "value"\
    },\
    "webhook": {\
      "url": "https://example.com/webhook",\
      "event_types": [\
        "monitor.event.detected"\
      ]\
    },\
    "created_at": "2025-04-23T20:21:48.037943Z"\
  }\
]
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#authorization-x-api-key)

x-api-key

string

header

required

#### Query Parameters

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#parameter-one-of-0)

monitor\_id

string \| null

Monitor ID to start listing after (for pagination). Returns monitors starting with this ID in lexicographic order.

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#parameter-one-of-0)

limit

integer \| null

Maximum number of monitors to return. Defaults to returning all monitors.

Required range: `1 <= x <= 10000`

#### Response

200

application/json

Successful Response

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-monitor-id)

monitor\_id

string

required

ID of the monitor.

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-query)

query

string

required

The query being monitored.

Example:

`"Recent news about LLM models."`

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-status)

status

enum<string>

required

Status of the monitor.

Available options:

`active`,

`canceled`

Examples:

`"active"`

`"canceled"`

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-cadence)

cadence

enum<string>

required

Cadence of the monitor.

Available options:

`daily`,

`weekly`,

`hourly`,

`every_two_weeks`

Examples:

`"daily"`

`"weekly"`

`"hourly"`

`"every_two_weeks"`

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-created-at)

created\_at

string<date-time>

required

Timestamp of the creation of the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the monitor.

Showchild attributes

Example:

```
{ "key": "value" }
```

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-webhook-one-of-0)

webhook

MonitorWebhook · object

Webhook configuration for the monitor.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-output-schema-one-of-0)

output\_schema

JsonSchema · object

Output schema for the monitor event.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/list-monitors#response-items-last-run-at-one-of-0)

last\_run\_at

string \| null

Timestamp of the last run for the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[Search](https://docs.parallel.ai/api-reference/search-beta/search) [Create Monitor](https://docs.parallel.ai/api-reference/monitor/create-monitor)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Create Monitor - Parallel

**URL:** https://docs.parallel.ai/api-reference/monitor/create-monitor

[Skip to main content](https://docs.parallel.ai/api-reference/monitor/create-monitor#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

Create Monitor

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Create Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors"

payload = {
    "query": "<string>",
    "cadence": "daily"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

201

401

422

Copy

Ask AI

```
{
  "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",
  "query": "Extract recent news about AI",
  "status": "active",
  "cadence": "daily",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "https://example.com/webhook",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "created_at": "2025-04-23T20:21:48.037943Z"
}
```

POST

/

v1alpha

/

monitors

Try it

Create Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors"

payload = {
    "query": "<string>",
    "cadence": "daily"
}
headers = {
    "x-api-key": "<api-key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

201

401

422

Copy

Ask AI

```
{
  "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",
  "query": "Extract recent news about AI",
  "status": "active",
  "cadence": "daily",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "https://example.com/webhook",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "created_at": "2025-04-23T20:21:48.037943Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#authorization-x-api-key)

x-api-key

string

header

required

#### Body

application/json

Request to create a monitor.

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#body-query)

query

string

required

Search query to monitor for material changes.

Example:

`"Extract recent news about AI"`

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#body-cadence)

cadence

enum<string>

required

Cadence of the monitor.

Available options:

`daily`,

`weekly`,

`hourly`,

`every_two_weeks`

Examples:

`"daily"`

`"weekly"`

`"hourly"`

`"every_two_weeks"`

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#body-webhook-one-of-0)

webhook

MonitorWebhook · object

Webhook to receive notifications about the monitor's execution.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#body-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the monitor. This field is returned in webhook notifications and GET requests, enabling you to map responses to corresponding objects in your application. For example, if you are building a Slackbot that monitors changes, you could store the Slack thread ID here to properly route webhook responses back to the correct conversation thread.

Showchild attributes

Example:

```
{
  "slack_thread_id": "1234567890.123456",
  "user_id": "U123ABC"
}
```

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#body-output-schema-one-of-0)

output\_schema

JsonSchema · object

Output schema for the monitor event.

Showchild attributes

#### Response

201

application/json

Successful Response

Response object for a monitor, including its status, cadence and metadata.

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-monitor-id)

monitor\_id

string

required

ID of the monitor.

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-query)

query

string

required

The query being monitored.

Example:

`"Recent news about LLM models."`

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-status)

status

enum<string>

required

Status of the monitor.

Available options:

`active`,

`canceled`

Examples:

`"active"`

`"canceled"`

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-cadence)

cadence

enum<string>

required

Cadence of the monitor.

Available options:

`daily`,

`weekly`,

`hourly`,

`every_two_weeks`

Examples:

`"daily"`

`"weekly"`

`"hourly"`

`"every_two_weeks"`

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-created-at)

created\_at

string<date-time>

required

Timestamp of the creation of the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the monitor.

Showchild attributes

Example:

```
{ "key": "value" }
```

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-webhook-one-of-0)

webhook

MonitorWebhook · object

Webhook configuration for the monitor.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-output-schema-one-of-0)

output\_schema

JsonSchema · object

Output schema for the monitor event.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/create-monitor#response-last-run-at-one-of-0)

last\_run\_at

string \| null

Timestamp of the last run for the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[List Monitors](https://docs.parallel.ai/api-reference/monitor/list-monitors) [Retrieve Monitor](https://docs.parallel.ai/api-reference/monitor/retrieve-monitor)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Fetch Task Group Runs - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks (Beta)

Fetch Task Group Runs

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group_runs = client.beta.task_group.get_runs("taskgroup_id")
for run in task_group_runs:
    print(run)
```

200

404

422

Copy

Ask AI

```
{
  "type": "task_run.state",
  "event_id": "123",
  "input": {
    "processor": "core",
    "metadata": {
      "my_key": "my_value"
    },
    "input": {
      "country": "France",
      "year": 2023
    }
  },
  "run": {
    "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
    "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
    "status": "completed",
    "is_active": false,
    "processor": "core",
    "metadata": {
      "my_key": "my_value"
    },
    "created_at": "2025-04-23T20:21:48.037943Z",
    "modified_at": "2025-04-23T20:21:48.037943Z"
  }
}
```

GET

/

v1beta

/

tasks

/

groups

/

{taskgroup\_id}

/

runs

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_group_runs = client.beta.task_group.get_runs("taskgroup_id")
for run in task_group_runs:
    print(run)
```

200

404

422

Copy

Ask AI

```
{
  "type": "task_run.state",
  "event_id": "123",
  "input": {
    "processor": "core",
    "metadata": {
      "my_key": "my_value"
    },
    "input": {
      "country": "France",
      "year": 2023
    }
  },
  "run": {
    "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
    "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
    "status": "completed",
    "is_active": false,
    "processor": "core",
    "metadata": {
      "my_key": "my_value"
    },
    "created_at": "2025-04-23T20:21:48.037943Z",
    "modified_at": "2025-04-23T20:21:48.037943Z"
  }
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#parameter-taskgroup-id)

taskgroup\_id

string

required

#### Query Parameters

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#parameter-one-of-0)

last\_event\_id

string \| null

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#parameter-one-of-0)

status

enum<string> \| null

Available options:

`queued`,

`action_required`,

`running`,

`completed`,

`failed`,

`cancelling`,

`cancelled`

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#parameter-include-input)

include\_input

boolean

default:false

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#parameter-include-output)

include\_output

boolean

default:false

#### Response

200

text/event-stream

Successful Response

- TaskRunEvent

- ErrorEvent

Event when a task run transitions to a non-active status.

May indicate completion, cancellation, or failure.

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#response-one-of-0-type)

type

string

required

Event type; always 'task\_run.state'.

Allowed value: `"task_run.state"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#response-one-of-0-event-id-one-of-0)

event\_id

string \| null

required

Cursor to resume the event stream. Always empty for non Task Group runs.

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#response-one-of-0-run)

run

TaskRun · object

required

Task run object.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#response-one-of-0-input-one-of-0)

input

BetaTaskRunInput · object

Input to the run; included only if requested.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-beta/fetch-task-group-runs#response-one-of-0-output)

output

TaskRunTextOutput · object

Output from a task that returns text.

- TaskRunTextOutput

- TaskRunJsonOutput

Showchild attributes

[Retrieve Task Group](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group) [Add Runs to Task Group](https://docs.parallel.ai/api-reference/tasks-beta/add-runs-to-task-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# OAuth Provider - Parallel

**URL:** https://docs.parallel.ai/integrations/oauth-provider

[Skip to main content](https://docs.parallel.ai/integrations/oauth-provider#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

OAuth Provider

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Provider URL](https://docs.parallel.ai/integrations/oauth-provider#provider-url)
- [Quick Start](https://docs.parallel.ai/integrations/oauth-provider#quick-start)
- [1\. Start Authorization Flow](https://docs.parallel.ai/integrations/oauth-provider#1-start-authorization-flow)
- [2\. Handle Callback & Exchange Code](https://docs.parallel.ai/integrations/oauth-provider#2-handle-callback-%26-exchange-code)
- [3\. Use the API Key](https://docs.parallel.ai/integrations/oauth-provider#3-use-the-api-key)
- [Authentication Flow](https://docs.parallel.ai/integrations/oauth-provider#authentication-flow)
- [Features](https://docs.parallel.ai/integrations/oauth-provider#features)
- [MCP Compatibility](https://docs.parallel.ai/integrations/oauth-provider#mcp-compatibility)

Parallel provides an OAuth 2.0 provider that allows applications to securely access user API keys with explicit user consent. This enables building applications that can make API calls to Parallel on behalf of users without requiring them to manually share their API keys.

## [​](https://docs.parallel.ai/integrations/oauth-provider\#provider-url)  Provider URL

**[https://platform.parallel.ai](https://platform.parallel.ai/)**

## [​](https://docs.parallel.ai/integrations/oauth-provider\#quick-start)  Quick Start

### [​](https://docs.parallel.ai/integrations/oauth-provider\#1-start-authorization-flow)  1\. Start Authorization Flow

Copy

Ask AI

```
// Generate PKCE parameters
function generatePKCE() {
  const codeVerifier = btoa(crypto.getRandomValues(new Uint8Array(32))).replace(
    /[+/=]/g,
    (m) => ({ "+": "-", "/": "_", "=": "" }[m])
  );

  return crypto.subtle
    .digest("SHA-256", new TextEncoder().encode(codeVerifier))
    .then((hash) => ({
      codeVerifier,
      codeChallenge: btoa(String.fromCharCode(...new Uint8Array(hash))).replace(
        /[+/=]/g,
        (m) => ({ "+": "-", "/": "_", "=": "" }[m])
      ),
    }));
}

// Redirect user to authorization
const { codeVerifier, codeChallenge } = await generatePKCE();
localStorage.setItem("code_verifier", codeVerifier);

const authUrl = new URL("https://platform.parallel.ai/getKeys/authorize");
authUrl.searchParams.set("client_id", "yourapp.com");
authUrl.searchParams.set("redirect_uri", "https://yourapp.com/callback");
authUrl.searchParams.set("response_type", "code");
authUrl.searchParams.set("scope", "key:read");
authUrl.searchParams.set("code_challenge", codeChallenge);
authUrl.searchParams.set("code_challenge_method", "S256");
authUrl.searchParams.set("state", "random-state-value");

window.location.href = authUrl.toString();
```

### [​](https://docs.parallel.ai/integrations/oauth-provider\#2-handle-callback-&-exchange-code)  2\. Handle Callback & Exchange Code

Copy

Ask AI

```
// On your callback page
const urlParams = new URLSearchParams(window.location.search);
const code = urlParams.get("code");
const codeVerifier = localStorage.getItem("code_verifier");

const response = await fetch("https://platform.parallel.ai/getKeys/token", {
  method: "POST",
  headers: { "Content-Type": "application/x-www-form-urlencoded" },
  body: new URLSearchParams({
    grant_type: "authorization_code",
    code: code,
    client_id: "yourapp.com",
    redirect_uri: "https://yourapp.com/callback",
    code_verifier: codeVerifier,
  }),
});

const { access_token } = await response.json();
// access_token is the user's Parallel API key
```

### [​](https://docs.parallel.ai/integrations/oauth-provider\#3-use-the-api-key)  3\. Use the API Key

Copy

Ask AI

```
const response = await fetch("https://api.parallel.ai/v1/tasks/runs", {
  method: "POST",
  headers: {
    "x-api-key": access_token,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    input: "What was the GDP of France in 2023?",
    processor: "base",
  }),
});

const taskRun = await response.json();
console.log(taskRun.run_id);
```

## [​](https://docs.parallel.ai/integrations/oauth-provider\#authentication-flow)  Authentication Flow

The OAuth flow follows these steps:

1. **Authorization Request**: Redirect user to Parallel’s authorization endpoint
2. **User Consent**: User sees your application hostname and grants permission
3. **API Key Selection**: User selects an existing API key or generates a new one
4. **Authorization Code**: User is redirected back with an authorization code
5. **Token Exchange**: Exchange the code for the user’s API key using PKCE

## [​](https://docs.parallel.ai/integrations/oauth-provider\#features)  Features

- **PKCE Required**: Code challenge/verifier mandatory for all clients
- **No Client Secret**: Public client design - no secrets to manage
- **User Consent**: Users explicitly approve each application by hostname
- **One-Time Codes**: Authorization codes can only be used once
- **Direct Access**: The `access_token` returned is the user’s actual Parallel API key

## [​](https://docs.parallel.ai/integrations/oauth-provider\#mcp-compatibility)  MCP Compatibility

This OAuth provider is fully compatible with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) specification for authorization. MCP clients can discover and use this OAuth provider automatically through the well-known endpoints at `/.well-known/oauth-authorization-server`.You can see an example of this OAuth provider being used in practice in the [Parallel Tasks SSE recipe](https://github.com/parallel-web/parallel-cookbook/blob/main/typescript-recipes/parallel-tasks-sse/index.html).

[n8n](https://docs.parallel.ai/integrations/n8n) [OpenAI Tool Calling](https://docs.parallel.ai/integrations/openai-tool-calling)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# n8n - Parallel

**URL:** https://docs.parallel.ai/integrations/n8n

[Skip to main content](https://docs.parallel.ai/integrations/n8n#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

n8n

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Installation](https://docs.parallel.ai/integrations/n8n#installation)
- [Available Nodes](https://docs.parallel.ai/integrations/n8n#available-nodes)
- [Common Use Cases](https://docs.parallel.ai/integrations/n8n#common-use-cases)

Integrate Parallel’s AI-powered web research directly into your n8n workflows with our community node package.

## [​](https://docs.parallel.ai/integrations/n8n\#installation)  Installation

Install the community node directly in n8n through the Community Nodes section in your n8n settings.**Links:**

- [NPM Package](https://www.npmjs.com/package/n8n-nodes-parallel)
- [n8n Integration Hub](https://n8n.io/integrations/parallel/)

## [​](https://docs.parallel.ai/integrations/n8n\#available-nodes)  Available Nodes

| Node | Operation | Description | Use Case |
| --- | --- | --- | --- |
| **Parallel Node** | Sync Web Enrichment | Execute tasks synchronously (up to 5 minutes) | Lead enrichment, competitive analysis, content research |
| **Parallel Node** | Async Web Enrichment | Long-running research tasks (up to 30 minutes) | Complex multi-source research, deep competitive intelligence |
| **Parallel Node** | Web Search | AI-powered web search with domain filtering | Natural language search with structured results and citations |
| **Parallel Node** | Web Chat | Real-time web-informed AI responses (< 5 seconds) | Current events queries, fact-checking, research-backed conversations |
| **Parallel Task Run Completion Trigger** | Webhook Trigger | Automatically trigger workflows when async tasks complete | Use with Async Web Enrichment - paste trigger webhook URL into the async node’s “Webhook URL” field |

## [​](https://docs.parallel.ai/integrations/n8n\#common-use-cases)  Common Use Cases

- **Sales**: Lead scoring, account research, contact discovery
- **Marketing**: Content research, trend analysis, competitor monitoring
- **Operations**: Vendor research, risk assessment, due diligence
- **Support**: Real-time information lookup, documentation generation

For detailed configuration and advanced features, see the [Task API guide](https://docs.parallel.ai/task-api/task-quickstart).

[LangChain](https://docs.parallel.ai/integrations/langchain) [OAuth Provider](https://docs.parallel.ai/integrations/oauth-provider)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Superhuman - Parallel

**URL:** https://docs.parallel.ai/integrations/superhuman

[Skip to main content](https://docs.parallel.ai/integrations/superhuman#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Superhuman

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Installation](https://docs.parallel.ai/integrations/superhuman#installation)
- [Available Skills](https://docs.parallel.ai/integrations/superhuman#available-skills)
- [Tips](https://docs.parallel.ai/integrations/superhuman#tips)

Integrate Parallel’s AI-powered web intelligence with Superhuman to bring real-time web data
into your writing.

## [​](https://docs.parallel.ai/integrations/superhuman\#installation)  Installation

- Search for Parallel on the Superhuman agent store and install.
- Or install the agent integration directly [here](https://superhuman.com/store/agents/parallel-web-intelligence-45397).

## [​](https://docs.parallel.ai/integrations/superhuman\#available-skills)  Available Skills

- **Verify claims and suggest modifications**: verify any claims made in your writing and have the agent suggest modifications
inplace.
- **Generate citations**: for any text, ask the agent to generate citations that you can use to establish
authenticity and provenance
- **Write or extend a report**: for any topic or a partial report, ask the agent to write a report or if the report is already
partially complete, complete it

## [​](https://docs.parallel.ai/integrations/superhuman\#tips)  Tips

- Keep the context small and verify claims as you go instead of verifying claims for a long text at once.
- Ask the agent to verify claims to trigger the claim verification skill
- To get the agent to generate citations, ask it to generate citations in the Superhuman chat box.

[OpenAI Tool Calling](https://docs.parallel.ai/integrations/openai-tool-calling) [Vercel](https://docs.parallel.ai/integrations/vercel)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Vercel - Parallel

**URL:** https://docs.parallel.ai/integrations/vercel

[Skip to main content](https://docs.parallel.ai/integrations/vercel#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Vercel

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Vercel AI Gateway](https://docs.parallel.ai/integrations/vercel#vercel-ai-gateway)
- [Vercel AI SDK](https://docs.parallel.ai/integrations/vercel#vercel-ai-sdk)
- [Sample Code](https://docs.parallel.ai/integrations/vercel#sample-code)
- [Vercel Marketplace](https://docs.parallel.ai/integrations/vercel#vercel-marketplace)
- [Getting started](https://docs.parallel.ai/integrations/vercel#getting-started)
- [Example application](https://docs.parallel.ai/integrations/vercel#example-application)

Use Parallel Search in the Vercel AI SDK. Get started quickly by installing Parallel in the Vercel Agent Marketplace.

## [​](https://docs.parallel.ai/integrations/vercel\#vercel-ai-gateway)  Vercel AI Gateway

Parallel Search is available as a built-in tool in [Vercel AI Gateway](https://vercel.com/docs/ai-gateway). AI Gateway provides a unified API to access hundreds of models through a single endpoint, with built-in web search capabilities.The `parallelSearch` tool can be used with any model regardless of the model provider. When the model needs current information, it calls the tool and AI Gateway routes the request to Parallel’s Search API.

streamText

generateText

Copy

Ask AI

```
import { gateway, streamText } from 'ai';

export async function POST(request: Request) {
  const { prompt } = await request.json();

  const result = streamText({
    model: 'anthropic/claude-sonnet-4.5', // Works with any model
    prompt,
    tools: {
      parallel_search: gateway.tools.parallelSearch(),
    },
  });

  return result.toDataStreamResponse();
}
```

You can configure additional parameters to tune the search behavior, such as `maxResults`, `country`, `searchDomainFilter`, and more. See the [Parallel parameters documentation](https://vercel.com/docs/ai-gateway/capabilities/web-search#parallel-parameters) for the full list of options.For more details, see the [Vercel AI Gateway Web Search documentation](https://vercel.com/docs/ai-gateway/capabilities/web-search#using-parallel-search).

## [​](https://docs.parallel.ai/integrations/vercel\#vercel-ai-sdk)  Vercel AI SDK

Easily drop in Parallel Search API or Extract API with any Vercel AI SDK compatible model provider.

- **Search API**: Given a semantic search objective and optional keywords, Parallel returns ranked URLs with compressed excerpts
- **Extract API**: Given a URL and an optional objective, Parallel returns compressed excerpts or full page contents

**Links:**

- [NPM Package](https://www.npmjs.com/package/@parallel-web/ai-sdk-tools)
- [Vercel AI SDK Toolkit](https://ai-sdk.dev/docs/foundations/tools#ready-to-use-tool-packages)
- [Vercel AI SDK Web Search Agent Cookbook](https://ai-sdk.dev/cookbook/node/web-search-agent#parallel-web)

### [​](https://docs.parallel.ai/integrations/vercel\#sample-code)  Sample Code

Parallel search and extract tools can be used with any Vercel AI SDK compatible model provider.

Search

Extract

Copy

Ask AI

```
import { openai } from '@ai-sdk/openai';
import { streamText, type Tool } from 'ai';
import { searchTool } from '@parallel-web/ai-sdk-tools';

const result = streamText({
  model: openai('gpt-5'),
  messages: [\
    { role: 'user', content: 'What are the latest developments in AI?' }\
  ],
  tools: {
    'web-search': searchTool as Tool,
  },
  toolChoice: 'auto',
});

// Stream the response
return result.toUIMessageStreamResponse();
```

## [​](https://docs.parallel.ai/integrations/vercel\#vercel-marketplace)  Vercel Marketplace

Parallel is available on the [Vercel Marketplace](https://vercel.com/marketplace/parallel). Install the integration to get a Parallel API key that you can use directly in your Vercel apps, with billing managed through Vercel.

### [​](https://docs.parallel.ai/integrations/vercel\#getting-started)  Getting started

1. Install the [Parallel integration](https://vercel.com/marketplace/parallel) from the Vercel Marketplace
2. Once installed, you’ll receive a Parallel API key automatically provisioned for your account
3. Use the API key in your Vercel applications to access Parallel Search and Extract APIs

### [​](https://docs.parallel.ai/integrations/vercel\#example-application)  Example application

See the [Parallel Vercel Template](https://parallel-vercel-template-cookbook.vercel.app/) for a working example, with source code available in the [cookbook repository](https://github.com/parallel-web/parallel-cookbook/tree/main/typescript-recipes/parallel-vercel-template).

[Superhuman](https://docs.parallel.ai/integrations/superhuman) [Zapier](https://docs.parallel.ai/integrations/zapier)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Source Policy - Parallel

**URL:** https://docs.parallel.ai/resources/source-policy

[Skip to main content](https://docs.parallel.ai/resources/source-policy#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Additional Resources

Source Policy

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Configuration](https://docs.parallel.ai/resources/source-policy#configuration)
- [Domain Limit](https://docs.parallel.ai/resources/source-policy#domain-limit)
- [Example](https://docs.parallel.ai/resources/source-policy#example)
- [Best Practices](https://docs.parallel.ai/resources/source-policy#best-practices)

The Source Policy feature allows you to precisely control which domains Parallel processors can
access during web research and to apply a freshness constraint. It’s available for both Tasks and
Web Tools and lets you tailor search results by specifying domains to include or exclude and by
setting a start date so results are limited to recent content.

## [​](https://docs.parallel.ai/resources/source-policy\#configuration)  Configuration

You can configure source control by setting the following parameters:

| Parameter | Type | Supported | Description |
| --- | --- | --- | --- |
| `include_domains` | array\[string\] | Task API, Search API | List of domains to **allow**. Only sources from these domains will be included in results. Maximum 10 domains. |
| `exclude_domains` | array\[string\] | Task API, Search API | List of domains to **block**. Sources from these domains will be excluded from results. Maximum 10 domains. |
| `after_date` | string<date> | Search API | Optional start date for filtering results. Results are limited to content published on or after this date. Provided as an RFC 3339 date string (`YYYY-MM-DD`). |

Specifying an apex domain such as `example.com` will automatically include all its
subdomains (e.g., `www.example.com`, `blog.example.com`, `api.example.com`).

### [​](https://docs.parallel.ai/resources/source-policy\#domain-limit)  Domain Limit

**Hard limit: 10 domains per request.** You can specify up to 10 domains total in either `include_domains` or `exclude_domains`. Exceeding this limit will raise a validation error. This limit applies to each array separately—you cannot combine them to exceed 10 domains per policy type.

## [​](https://docs.parallel.ai/resources/source-policy\#example)  Example

Task API

Search API

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1/tasks/runs" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "input": "How many employees does Parallel Web Systems have?",
      "processor": "core",
      "source_policy": {
        "include_domains": ["linkedin.com"]
      }
    }'
```

## [​](https://docs.parallel.ai/resources/source-policy\#best-practices)  Best Practices

- Use either `include_domains` or `exclude_domains` in a single query. Specifying `exclude_domains` is redundant when `include_domains` is set, as only `include_domains` will be applied.
- List each domain in its apex form (e.g., `example.com`). Do not include schemes (`http://`, `https://`) or subdomain prefixes (such as `www.`).
- Wildcards can be used in domain specifications, for example, to research only “.org” domains. However, paths, for example “example.com/blog”, are not yet supported.
- Although there is a maximum limit of 10 domains, carefully using specific and targeted domains will give better results.

[Zapier](https://docs.parallel.ai/integrations/zapier) [Warnings and Errors](https://docs.parallel.ai/resources/warnings-and-errors)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Crawler - Parallel

**URL:** https://docs.parallel.ai/resources/crawler

[Skip to main content](https://docs.parallel.ai/resources/crawler#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Additional Resources

Crawler

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [ShapBot](https://docs.parallel.ai/resources/crawler#shapbot)
- [Contact & Support](https://docs.parallel.ai/resources/crawler#contact-%26-support)
- [Changes to This Documentation](https://docs.parallel.ai/resources/crawler#changes-to-this-documentation)

## [​](https://docs.parallel.ai/resources/crawler\#shapbot)  ShapBot

ShapBot helps discover and index websites for Parallel’s web APIs. To maximize your site’s visibility in search results, we suggest allowing ShapBot access in your robots.txt configuration and permitting connections from our designated IP ranges.Full user-agent string: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ShapBot/0.1.0For the complete list of ShapBot IPs, see [shapbot.json](https://docs.parallel.ai/resources/shapbot.json).

## [​](https://docs.parallel.ai/resources/crawler\#contact-&-support)  Contact & Support

If you have questions about our crawlers or need assistance, please contact us at [support@parallel.ai](mailto:support@parallel.ai)

## [​](https://docs.parallel.ai/resources/crawler\#changes-to-this-documentation)  Changes to This Documentation

We may update this documentation periodically to reflect changes in our crawler behavior or policies. Please check back regularly for updates.

[FindAll Migration Guide](https://docs.parallel.ai/findall-api/findall-migration-guide) [Status Page](https://docs.parallel.ai/resources/status)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Structured Outputs - Parallel

**URL:** https://docs.parallel.ai/monitor-api/monitor-structured-outputs

[Skip to main content](https://docs.parallel.ai/monitor-api/monitor-structured-outputs#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Structured Outputs

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Defining an Output Schema](https://docs.parallel.ai/monitor-api/monitor-structured-outputs#defining-an-output-schema)
- [Retrieving Structured Events](https://docs.parallel.ai/monitor-api/monitor-structured-outputs#retrieving-structured-events)
- [Best Practices](https://docs.parallel.ai/monitor-api/monitor-structured-outputs#best-practices)
- [Related Topics](https://docs.parallel.ai/monitor-api/monitor-structured-outputs#related-topics)

Structured outputs enable you to define a JSON schema for monitor events. Each detected event conforms to the specified schema, returning data in a consistent, machine-readable format suitable for downstream processing in databases, analytics pipelines, or automation workflows.

**Schema Complexity**: Output schemas are currently limited to the complexity supported by the core processor. Use flat schemas with a small number of clearly defined fields.

## [​](https://docs.parallel.ai/monitor-api/monitor-structured-outputs\#defining-an-output-schema)  Defining an Output Schema

Include an [`output_schema`](https://docs.parallel.ai/api-reference/monitor/create-monitor#body-output-schema-one-of-0) field when creating a monitor:

Copy

Ask AI

```
curl --request POST \
  --url https://api.parallel.ai/v1alpha/monitors \
  --header 'Content-Type: application/json' \
  --header "x-api-key: $PARALLEL_API_KEY" \
  --data '{
    "query": "monitor ai news",
    "frequency": "1d",
    "output_schema": {
      "type": "json",
      "json_schema": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "description": "Name of the company the news is about, NA if not company-specific"
          },
          "sentiment": {
            "type": "string",
            "description": "Sentiment of the news: positive or negative"
          },
          "description": {
            "type": "string",
            "description": "Brief description of the news"
          }
        }
      }
    }
  }'
```

**Response:**

Copy

Ask AI

```
{
  "monitor_id": "monitor_da7460cdc958453ea092ce6bbbd7fd4b",
  "query": "monitor ai news",
  "status": "active",
  "frequency": "1d",
  "created_at": "2025-12-03T17:49:54.077782Z"
}
```

## [​](https://docs.parallel.ai/monitor-api/monitor-structured-outputs\#retrieving-structured-events)  Retrieving Structured Events

Events from monitors configured with structured outputs include a `result` field containing the parsed JSON object:

Copy

Ask AI

```
curl --request GET \
  --url "https://api.parallel.ai/v1alpha/monitors/<monitor_id>/events" \
  --header "x-api-key: $PARALLEL_API_KEY"
```

**Response:**

Copy

Ask AI

```
{
  "events": [\
    {\
      "type": "event",\
      "event_group_id": "mevtgrp_f9727e22dd4a42ba5e7fdcaa36b2b8ea2ef7c11f15fb4061",\
      "event_date": "2025-12-02",\
      "source_urls": [\
        "https://www.cnbc.com/2025/12/02/youtube-ai-biometric-data-creator-deepfake.html"\
      ],\
      "result": {\
        "type": "json",\
        "content": {\
          "company_name": "YouTube/Google",\
          "sentiment": "negative",\
          "description": "YouTube expanded a likeness detection deepfake tracking tool; experts warn the sign-up requires government ID and a biometric video."\
        }\
      }\
    },\
    {\
      "type": "event",\
      "event_group_id": "mevtgrp_f9727e22dd4a42ba5e7fdcaa36b2b8ea2ef7c11f15fb4061",\
      "event_date": "2025-12-02",\
      "source_urls": [\
        "https://fox59.com/business/press-releases/globenewswire/9595236/kloudfuse-launches-kloudfuse-3-5"\
      ],\
      "result": {\
        "type": "json",\
        "content": {\
          "company_name": "Kloudfuse",\
          "sentiment": "positive",\
          "description": "Kloudfuse announced version 3.5 with AI-native observability features including LLM observability integrated into APM."\
        }\
      }\
    }\
  ]
}
```

## [​](https://docs.parallel.ai/monitor-api/monitor-structured-outputs\#best-practices)  Best Practices

- **Include property descriptions**: Provide clear `description` fields for each property to improve extraction accuracy
- **Use primitive types**: Limit properties to `string` and `enum` types for reliable parsing
- **Maintain flat schemas**: Use 3–5 properties with a single-level object structure
- **Define edge case handling**: Specify how missing or inapplicable values should be represented

## [​](https://docs.parallel.ai/monitor-api/monitor-structured-outputs\#related-topics)  Related Topics

- **[Quickstart](https://docs.parallel.ai/monitor-api/monitor-quickstart)**: Monitor API setup and configuration
- **[Events](https://docs.parallel.ai/monitor-api/monitor-events)**: Event model and event groups
- **[Webhooks](https://docs.parallel.ai/monitor-api/monitor-webhooks)**: Real-time notification delivery

[Quickstart](https://docs.parallel.ai/monitor-api/monitor-quickstart) [Events and Event Groups](https://docs.parallel.ai/monitor-api/monitor-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Simulate Event - Parallel

**URL:** https://docs.parallel.ai/monitor-api/monitor-simulate-event

[Skip to main content](https://docs.parallel.ai/monitor-api/monitor-simulate-event#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Simulate Event

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Endpoint](https://docs.parallel.ai/monitor-api/monitor-simulate-event#endpoint)
- [Query Parameters](https://docs.parallel.ai/monitor-api/monitor-simulate-event#query-parameters)
- [Response](https://docs.parallel.ai/monitor-api/monitor-simulate-event#response)
- [Errors](https://docs.parallel.ai/monitor-api/monitor-simulate-event#errors)
- [Usage](https://docs.parallel.ai/monitor-api/monitor-simulate-event#usage)
- [Test Event Groups](https://docs.parallel.ai/monitor-api/monitor-simulate-event#test-event-groups)
- [Related Topics](https://docs.parallel.ai/monitor-api/monitor-simulate-event#related-topics)

The simulate event endpoint allows you to test your webhook integration without waiting for a scheduled monitor run.

## [​](https://docs.parallel.ai/monitor-api/monitor-simulate-event\#endpoint)  Endpoint

Copy

Ask AI

```
POST /v1alpha/monitors/{monitor_id}/simulate_event
```

### [​](https://docs.parallel.ai/monitor-api/monitor-simulate-event\#query-parameters)  Query Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `event_type` | string | `monitor.event.detected` | Event type to simulate. One of: `monitor.event.detected`, `monitor.execution.completed`, `monitor.execution.failed` |

### [​](https://docs.parallel.ai/monitor-api/monitor-simulate-event\#response)  Response

Returns `204 No Content` on success.

### [​](https://docs.parallel.ai/monitor-api/monitor-simulate-event\#errors)  Errors

| Status | Description |
| --- | --- |
| 400 | Webhook not configured for this monitor |
| 404 | Monitor not found |

## [​](https://docs.parallel.ai/monitor-api/monitor-simulate-event\#usage)  Usage

Copy

Ask AI

```
curl --request POST \
  --url "https://api.parallel.ai/v1alpha/monitors/<monitor_id>/simulate_event?event_type=monitor.event.detected" \
  --header "x-api-key: $PARALLEL_API_KEY"
```

## [​](https://docs.parallel.ai/monitor-api/monitor-simulate-event\#test-event-groups)  Test Event Groups

When you simulate a `monitor.event.detected` event, the webhook payload includes a test `event_group_id`. You can retrieve this test event group using the standard endpoint:

Copy

Ask AI

```
GET /v1alpha/monitors/{monitor_id}/event_groups/{event_group_id}
```

Test event group IDs return dummy event data, allowing you to verify your full webhook processing pipeline—from receiving the webhook to fetching event details.

Copy

Ask AI

```
curl --request GET \
  --url "https://api.parallel.ai/v1alpha/monitors/<monitor_id>/event_groups/<test_event_group_id>" \
  --header "x-api-key: $PARALLEL_API_KEY"
```

**Response:**

No Structured Output

Structured Output

Copy

Ask AI

```
{
    "events": [\
        {\
            "type": "event",\
            "event_group_id": "test_abc",\
            "output": "",\
            "event_date": "2025-12-05",\
            "source_urls": [\
                "https://test.example.com"\
            ],\
            "result": {\
                "type": "text",\
                "content": "This is a test event."\
            }\
        }\
    ]
}
```

## [​](https://docs.parallel.ai/monitor-api/monitor-simulate-event\#related-topics)  Related Topics

- **[Webhooks](https://docs.parallel.ai/monitor-api/monitor-webhooks)**: Configure webhooks and understand event payloads
- **[Events](https://docs.parallel.ai/monitor-api/monitor-events)**: Event types and event groups

[Slack](https://docs.parallel.ai/monitor-api/monitor-slack) [Quickstart](https://docs.parallel.ai/integrations/mcp/quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Search MCP - Parallel

**URL:** https://docs.parallel.ai/integrations/mcp/search-mcp

[Skip to main content](https://docs.parallel.ai/integrations/mcp/search-mcp#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

MCP

Search MCP

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Use Cases](https://docs.parallel.ai/integrations/mcp/search-mcp#use-cases)
- [Installation](https://docs.parallel.ai/integrations/mcp/search-mcp#installation)
- [Cursor](https://docs.parallel.ai/integrations/mcp/search-mcp#cursor)
- [VS Code](https://docs.parallel.ai/integrations/mcp/search-mcp#vs-code)
- [Claude Desktop / Claude.ai](https://docs.parallel.ai/integrations/mcp/search-mcp#claude-desktop-%2F-claude-ai)
- [Claude Code](https://docs.parallel.ai/integrations/mcp/search-mcp#claude-code)
- [Windsurf](https://docs.parallel.ai/integrations/mcp/search-mcp#windsurf)
- [Cline](https://docs.parallel.ai/integrations/mcp/search-mcp#cline)
- [Gemini CLI](https://docs.parallel.ai/integrations/mcp/search-mcp#gemini-cli)
- [ChatGPT](https://docs.parallel.ai/integrations/mcp/search-mcp#chatgpt)
- [OpenAI Codex CLI](https://docs.parallel.ai/integrations/mcp/search-mcp#openai-codex-cli)
- [Amp](https://docs.parallel.ai/integrations/mcp/search-mcp#amp)
- [Kiro](https://docs.parallel.ai/integrations/mcp/search-mcp#kiro)
- [Google Antigravity](https://docs.parallel.ai/integrations/mcp/search-mcp#google-antigravity)
- [Best practices](https://docs.parallel.ai/integrations/mcp/search-mcp#best-practices)
- [Filtering by date or domain](https://docs.parallel.ai/integrations/mcp/search-mcp#filtering-by-date-or-domain)
- [Troubleshooting](https://docs.parallel.ai/integrations/mcp/search-mcp#troubleshooting)
- [Common Installation Issues](https://docs.parallel.ai/integrations/mcp/search-mcp#common-installation-issues)

The Parallel Search MCP Server provides drop-in web search and content extraction capabilities for any MCP-aware model. The tools invoke the [Search API](https://docs.parallel.ai/search/search-quickstart) endpoint but present a simpler interface to ensure effective use by agents. The tools use the Search API in `agentic` mode, which returns more concise results than the default `one-shot` mode.The Search MCP comprises two tools:

- **web\_search** \- Search the web for information and retrieve relevant results
- **web\_fetch** \- Extract and retrieve content from specific URLs

## [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#use-cases)  Use Cases

The Search MCP is suited for any application where real-world information is needed as part of an AI agent’s reasoning loop. Common use cases include:

- Real-time fact checking and verification during conversations
- Gathering current information to answer user questions
- Researching topics that require recent or live data
- Retrieving content from specific URLs to analyze or summarize
- Competitive intelligence and market research

## [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#installation)  Installation

The Search MCP can be installed in any MCP client. The server URL is:**`https://search-mcp.parallel.ai/mcp`**The Search MCP can also be [used programmatically](https://docs.parallel.ai/integrations/mcp/programmatic-use) by providing your Parallel API key in the Authorization header as a Bearer token.

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#cursor)  Cursor

Add to `~/.cursor/mcp.json` or `.cursor/mcp.json` (project-specific):

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "url": "https://search-mcp.parallel.ai/mcp"
    }
  }
}
```

**Deep Link:** [🔗 Install Search MCP](https://cursor.com/en/install-mcp?name=Parallel%20Search%20MCP&config=eyJ1cmwiOiJodHRwczovL3NlYXJjaC1tY3AucGFyYWxsZWwuYWkvbWNwIn0=)For more details, see the [Cursor MCP documentation](https://cursor.com/docs/context/mcp).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#vs-code)  VS Code

Add to `settings.json` in VS Code:

Copy

Ask AI

```
{
  "mcp": {
    "servers": {
      "Parallel Search MCP": {
        "type": "http",
        "url": "https://search-mcp.parallel.ai/mcp"
      }
    }
  }
}
```

**Deep Link:** [🔗 Install Search MCP](https://insiders.vscode.dev/redirect/mcp/install?name=Parallel%20Search%20MCP&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fsearch-mcp.parallel.ai%2Fmcp%22%7D)For more details, see the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#claude-desktop-/-claude-ai)  Claude Desktop / Claude.ai

Go to Settings → Connectors → Add Custom Connector, and fill in:

Copy

Ask AI

```
Name: Parallel Search MCP
URL: https://search-mcp.parallel.ai/mcp
```

If you are part of an organization, you may not have access to custom connectors. Contact your organization administrator for assistance.If you are not an admin, go to Settings → Developer → Edit Config and add the following JSON after retrieving your API key from [Platform](https://platform.parallel.ai/):

Copy

Ask AI

```
"Parallel Search MCP": {
  "command": "npx",
  "args": [\
    "-y",\
    "mcp-remote",\
    "https://search-mcp.parallel.ai/mcp",\
    "--header", "authorization: Bearer YOUR-PARALLEL-API-KEY"\
  ]
}
```

For more details, see the [Claude remote MCP documentation](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#claude-code)  Claude Code

Run this command in your terminal:

Copy

Ask AI

```
claude mcp add --transport http "Parallel-Search-MCP" https://search-mcp.parallel.ai/mcp
```

In Claude code, use the command:

Copy

Ask AI

```
/mcp
```

Then follow the steps in your browser to login.For more details, see the [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#windsurf)  Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "serverUrl": "https://search-mcp.parallel.ai/mcp"
    }
  }
}
```

For more details, see the [Windsurf MCP documentation](https://docs.windsurf.com/windsurf/cascade/mcp).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#cline)  Cline

Go to MCP Servers → Remote Servers → Edit Configuration:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "url": "https://search-mcp.parallel.ai/mcp",
      "type": "streamableHttp"
    }
  }
}
```

For more details, see the [Cline MCP documentation](https://docs.cline.bot/mcp/configuring-mcp-servers).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#gemini-cli)  Gemini CLI

Add to `~/.gemini/settings.json`:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "httpUrl": "https://search-mcp.parallel.ai/mcp"
    }
  }
}
```

For more details, see the [Gemini CLI MCP documentation](https://geminicli.com/docs/tools/mcp-server/).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#chatgpt)  ChatGPT

**WARNING:** Please note that [Developer Mode](https://platform.openai.com/docs/guides/developer-mode) must be enabled, and this feature may not be available to everyone. Additionally, MCPs in ChatGPT are experimental and may not work reliably.First, go to Settings → Connectors → Advanced Settings, and turn on Developer Mode.Then, in connector settings, click Create and fill in:

Copy

Ask AI

```
Name: Parallel Search MCP
URL: https://search-mcp.parallel.ai/mcp
Authentication: OAuth
```

In a new chat, ensure Developer Mode is turned on with the connector(s) selected.For more details, see the [ChatGPT Developer Mode documentation](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#openai-codex-cli)  OpenAI Codex CLI

Add to `~/.codex/config.toml`:

Copy

Ask AI

```
[mcp_servers.parallel-search]
url = "https://search-mcp.parallel.ai/mcp"
```

Alternatively, run this in your terminal. This should start the OAuth flow:

Copy

Ask AI

```
codex mcp add parallel-search --url https://search-mcp.parallel.ai/mcp
```

For more details, see the [Codex MCP documentation](https://developers.openai.com/codex/mcp/).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#amp)  Amp

Run this command in your terminal:

Copy

Ask AI

```
amp mcp add "Parallel-Search-MCP" https://search-mcp.parallel.ai/mcp
```

The OAuth flow will start when you start Amp.For more details, see the [Amp MCP documentation](https://ampcode.com/manual#mcp-oauth).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#kiro)  Kiro

Add to `.kiro/settings/mcp.json` (workspace) or `~/.kiro/settings/mcp.json` (global):

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "url": "https://search-mcp.parallel.ai/mcp"
    }
  }
}
```

For more details, see the [Kiro MCP documentation](https://kiro.dev/docs/mcp/configuration/).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#google-antigravity)  Google Antigravity

In the Antigravity Agent pane, click the menu (⋮) → MCP Servers → Manage MCP Servers → View raw config, then add:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel-Search-MCP": {
      "serverUrl": "https://search-mcp.parallel.ai/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

For more details, see the [Antigravity MCP documentation](https://antigravity.google/docs/mcp).

* * *

## [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#best-practices)  Best practices

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#filtering-by-date-or-domain)  Filtering by date or domain

To filter search results by date or domain, include these constraints directly in your search query or objective rather than expecting separate parameters. For example:

- “Latest AI research papers from 2025”
- “News about climate change from nytimes.com”
- “Product announcements from apple.com in the last month”

If date or domain filtering is important for your task, prompt the agent explicitly to include these details when using the tool.

We have experimented with adding dedicated date and domain parameters to the Search MCP tools, but found they harm quality overall—LLMs tend to overuse them, which overconstrains search results.

## [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#troubleshooting)  Troubleshooting

### [​](https://docs.parallel.ai/integrations/mcp/search-mcp\#common-installation-issues)  Common Installation Issues

Cline: 'Authorization Error redirect\_uri must be https'

This error occurs when Cline attempts OAuth authentication but the redirect URI isn’t using HTTPS.**Solution:** Use the API key approach instead of OAuth:

1. Get your API key from [platform.parallel.ai](https://platform.parallel.ai/)
2. Configure Cline with the bearer token method:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "command": "npx",
      "args": [\
        "-y",\
        "mcp-remote",\
        "https://search-mcp.parallel.ai/mcp",\
        "--header",\
        "authorization: Bearer YOUR-PARALLEL-API-KEY"\
      ]
    }
  }
}
```

Replace `YOUR-PARALLEL-API-KEY` with your actual API key.

Gemini CLI: Where to provide API key

Gemini CLI uses HTTP MCPs and authenticates via OAuth. If OAuth isn’t working, you can provide your API key directly.**Solution:** Use environment variables or the `mcp-remote` proxy:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "command": "npx",
      "args": [\
        "-y",\
        "mcp-remote",\
        "https://search-mcp.parallel.ai/mcp",\
        "--header",\
        "authorization: Bearer YOUR-PARALLEL-API-KEY"\
      ]
    }
  }
}
```

Add this to `~/.gemini/settings.json` and replace `YOUR-PARALLEL-API-KEY` with your key from [platform.parallel.ai](https://platform.parallel.ai/).

VS Code: Incorrect configuration format

VS Code requires a specific configuration format. Common mistakes include using the wrong property names.**Incorrect (Cursor format):**

Copy

Ask AI

```
{
  "mcpServers": {
    "parallel-search": {
      "url": "https://search-mcp.parallel.ai/mcp"
    }
  }
}
```

**Correct (VS Code format):**

Copy

Ask AI

```
{
  "mcp": {
    "servers": {
      "Parallel Search MCP": {
        "type": "http",
        "url": "https://search-mcp.parallel.ai/mcp"
      }
    }
  }
}
```

Note: VS Code uses `mcp.servers` (not `mcpServers`) and requires the `type: "http"` field.

Windsurf: Configuration location and format

Windsurf uses a different configuration format than Cursor.**Correct Windsurf configuration:**

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Search MCP": {
      "serverUrl": "https://search-mcp.parallel.ai/mcp"
    }
  }
}
```

Note: Windsurf uses `serverUrl` instead of `url`. Add this to your Windsurf MCP configuration file.

Connection timeout or 'server unavailable' errors

If you’re getting connection errors:

1. **Check your network:** Ensure you can reach `https://search-mcp.parallel.ai`
2. **Verify API key:** Make sure your key is valid at [platform.parallel.ai](https://platform.parallel.ai/)
3. **Check balance:** A 402 error means insufficient credits—add funds to your account
4. **Restart your IDE:** Some clients cache MCP connections

Tools not appearing in the IDE

If the MCP installs but tools don’t show up:

1. **Restart your IDE** completely (not just reload)
2. **Check configuration syntax:** Ensure valid JSON with no trailing commas
3. **Verify the server URL:** Must be exactly `https://search-mcp.parallel.ai/mcp`
4. **Check IDE logs:** Look for MCP-related errors in your IDE’s output/debug panel

[Programmatic Use](https://docs.parallel.ai/integrations/mcp/programmatic-use) [Task MCP](https://docs.parallel.ai/integrations/mcp/task-mcp)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# FAQs - Parallel

**URL:** https://docs.parallel.ai/resources/faqs

[Skip to main content](https://docs.parallel.ai/resources/faqs#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Additional Resources

FAQs

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Platform](https://docs.parallel.ai/resources/faqs#platform)
- [APIs](https://docs.parallel.ai/resources/faqs#apis)
- [Billing & Payments](https://docs.parallel.ai/resources/faqs#billing-%26-payments)
- [Security & Compliance](https://docs.parallel.ai/resources/faqs#security-%26-compliance)

## [​](https://docs.parallel.ai/resources/faqs\#platform)  Platform

Where do I get an API key?

A default API key is generated when you signup to
[Platform](https://platform.parallel.ai/). You can create and manage keys via
Settings.

How can I track usage and costs?

Go to **Platform > Usage** for real-time request counts, and spend.

How do I add teammates?

Owners can invite users under **Settings** in
[Platform](https://platform.parallel.ai/). Choose “Admin” or “Member” roles.

Can I use Parallel for commercial use?

Subject to our [Terms of Service](https://www.parallel.ai/customer-terms) -
you own the output you create with Parallel, including the right to reprint,
sell, and merchandise.

## [​](https://docs.parallel.ai/resources/faqs\#apis)  APIs

Can I chain several Tasks together in the Task API?

Yes — Task Run Results from one execution can map to Task Run Input fields in
another execution. For example, in one Task Run, you can identify the address
of a business using a simple processor. Then, in the next Task Run you
identify additional details about the business, given business name and
address.

Can I limit my query to specific sources only?

Yes, you can do this with [Source Policy](https://docs.parallel.ai/search/source-policy). This is
available for the Task API and the Search API today.

Can Parallel fetch data that sits behind a login?

Parallel is focused on reasoning and retrieval over the public web. For now,
we only access what can be reached on the public web without authentication
(e.g. signing in with credentials).

Is Parallel multi‑modal?

Our strength is reasoning and retrieval over text. We can recognize some
on‑page images (e.g. detect customer logos), but we don’t accept images as
inputs or return them as outputs yet.

Are there rate limits?

| **API** | **Default Rate Limit** |
| --- | --- |
| Tasks | 2000 per min |
| Web Tools | 600 per min |
| Chat | 300 per min |
| FindAll | 300 per hour |
| Monitor | 300 per min |

How recent is the web research you provide?

With the Task API, our web research is up to date to the current day. We are
able to access live web links at the time of your query to ensure data is as
real time as possible. For lower end processors in the Search API and Chat
API, our systems prioritize reduced latency over freshness.

Can you include data from internal sources as part of your search?

Parallel focuses on public web information. You can pass private data into a
task as an input variable or post‑process the output on your side, but we
don’t pull it natively.

## [​](https://docs.parallel.ai/resources/faqs\#billing-&-payments)  Billing & Payments

How is pricing calculated?

Parallel Processors incorporate usage-based pricing. All pricing details for
API and Processor are available [here](https://parallel.ai/pricing).

## [​](https://docs.parallel.ai/resources/faqs\#security-&-compliance)  Security & Compliance

Are you SOC-II compliant?

Yes. Parallel is SOC-II Type 1 and Type II certified as of April 2025. Email
us at [partnerships@parallel.ai](mailto:partnerships@parallel.ai) to request
access to our full report in Trust Center.

Where is Parallel data stored?

All data is encrypted in transit (TLS 1.2+) and at rest in US-based data
centers.

Do you access or store my private data?

No. Parallel focuses on public web information. You can pass private data into
a task as an input variable or post‑process the output on your side, but we
don’t pull it natively. In the future we plan on building tools that will
allow you to more easily point Parallel to your own sources.

Can I run Parallel inside my VPC?

Private‑cloud and on‑prem options are available for qualified enterprise
customers—ask our team at
[partnerships@parallel.ai](mailto:partnerships@parallel.ai).

Will you train models on my data?

Never. Inputs and outputs remain yours. We do not use customer data to train
any models. See our [Terms of Service](https://www.parallel.ai/customer-terms)
for details.

[Status Page](https://docs.parallel.ai/resources/status)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Research Basis - Parallel

**URL:** https://docs.parallel.ai/task-api/guides/access-research-basis

[Skip to main content](https://docs.parallel.ai/task-api/guides/access-research-basis#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Research Basis

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Terminology](https://docs.parallel.ai/task-api/guides/access-research-basis#terminology)
- [Task Run Result](https://docs.parallel.ai/task-api/guides/access-research-basis#task-run-result)
- [Research Basis Structure](https://docs.parallel.ai/task-api/guides/access-research-basis#research-basis-structure)
- [The FieldBasis object](https://docs.parallel.ai/task-api/guides/access-research-basis#the-fieldbasis-object)
- [Citations](https://docs.parallel.ai/task-api/guides/access-research-basis#citations)
- [Reasoning](https://docs.parallel.ai/task-api/guides/access-research-basis#reasoning)
- [Confidence Levels](https://docs.parallel.ai/task-api/guides/access-research-basis#confidence-levels)
- [Per-element Basis (beta)](https://docs.parallel.ai/task-api/guides/access-research-basis#per-element-basis-beta)
- [Examples](https://docs.parallel.ai/task-api/guides/access-research-basis#examples)
- [Output with Research Basis](https://docs.parallel.ai/task-api/guides/access-research-basis#output-with-research-basis)
- [High vs. Low Confidence Outputs](https://docs.parallel.ai/task-api/guides/access-research-basis#high-vs-low-confidence-outputs)
- [Per-Element Basis](https://docs.parallel.ai/task-api/guides/access-research-basis#per-element-basis)

When you execute a task using the Task API, the response includes both the generated output and its corresponding research basis—a structured explanation detailing the reasoning and evidence behind each result. This transparency enables you to understand how the system arrived at its conclusions and to assess the reliability of the output.

## [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#terminology)  Terminology

To avoid confusion, this document uses the following terminology:

- **Research Basis**: The overall feature that provides transparency into how Task API results are generated
- **Basis**: The `basis` field in the API response, which contains an array of field-specific evidence
- **FieldBasis**: The specific object type that contains citations, reasoning, and confidence for individual output fields

## [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#task-run-result)  Task Run Result

Every Task Run Result object contains the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `run` | object | Task Run object with status and id, detailed above. |
| `output` | TaskRunOutput object or null | Output from the task conforming to the output schema. Present iff run.status == completed. |

A TaskRunOutput object can be one of two types:

- TaskRunTextOutput
- TaskRunJsonOutput

Both have the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `content` | string | JSON or plain text according to the output schema. |
| `basis` | array\[FieldBasis\] | Array of FieldBasis objects, one for each top-level output field. See FieldBasis object below. |
| `type` | string | Always `text` |

## [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#research-basis-structure)  Research Basis Structure

The `basis` field contains an array of FieldBasis objects that correspond to each top-level field in your output. This allows you to trace exactly which sources on the web contributed to each specific piece of information in your result.

Task Run Result

Task Run Output

Output Content

Output Basis

Company: Microsoft

Founded: 1975

Basis for Company

Basis for Founded

Citations + Reasoning

Citations + Reasoning

## [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#the-fieldbasis-object)  The FieldBasis object

Each FieldBasis object has these components:

| Field | Type | Description |
| --- | --- | --- |
| `field` | string | Name of the corresponding output field |
| `citations` | array\[Citation\] | List of web sources supporting the output field |
| `reasoning` | string | Explanation of how the system processed the information |
| `confidence` | string or null | Reliability rating for each output field |

### [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#citations)  Citations

Citations provide the exact URLs where information was found. Each citation includes excerpts from the source that contributed to the output:

| Field | Type | Description |
| --- | --- | --- |
| `url` | string | The source URL |
| `excerpts` | array\[string\] or null | Relevant text from the source |

Having multiple citations for an output field often indicates stronger evidence, as the information was verified across multiple sources.

### [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#reasoning)  Reasoning

The reasoning field explains how the system evaluated, compared, and synthesized information from different sources. This is particularly valuable when:

- Information from different sources needed to be reconciled
- Calculations or conversions were performed
- The system needed to make judgments about conflicting data

### [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#confidence-levels)  Confidence Levels

All processors include a confidence rating for each output field:

- **High**: Strong evidence from multiple authoritative sources with consistent information
- **Medium**: Adequate evidence but with some inconsistencies or from less authoritative sources
- **Low**: Limited or conflicting evidence, or information from less reliable sources

### [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#per-element-basis-beta)  Per-element Basis (beta)

By default, `basis` entries are emitted only for the top-level fields in your output schema.
If a top-level field is an array and you need citations for each element, opt in to the **field-basis** beta header:

Copy

Ask AI

```
parallel-beta: field-basis-2025-11-25
```

When this header is present on task creation requests:

- The Task API still returns top-level FieldBasis objects.
- Each element of a Top-level field with an array value gains an additional FieldBasis and it’s own `field` which follows the pydash-style dot notation (e.g., `key_executives.0`, `key_executives.1`).
- No other schema changes are required; you simply read the expanded `basis` array.

## [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#examples)  Examples

### [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#output-with-research-basis)  Output with Research Basis

Here’s an example of a complete Task Run output that includes research basis information:

Copy

Ask AI

```
{
  "content": "{\"company\":\"Microsoft\",\"founded\":\"1975\",\"headquarters\":\"Redmond, Washington, USA\"}",
  "basis": [\
    {\
      "field": "company",\
      "citations": [\
        {\
          "url": "https://www.microsoft.com/en-us/about",\
          "excerpts": ["Microsoft Corporation is an American multinational technology corporation headquartered in Redmond, Washington."]\
        }\
      ],\
      "reasoning": "The company name is clearly identified on the official corporate website.",\
      "confidence": "high"\
    },\
    {\
      "field": "founded",\
      "citations": [\
        {\
          "url": "https://www.microsoft.com/en-us/about/company",\
          "excerpts": ["Founded in 1975, Microsoft (Nasdaq "MSFT") enables digital transformation for the era of an intelligent cloud and an intelligent edge."]\
        },\
        {\
          "url": "https://en.wikipedia.org/wiki/Microsoft",\
          "excerpts": ["Microsoft Corporation was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800."]\
        }\
      ],\
      "reasoning": "Multiple authoritative sources consistently state 1975 as the founding year. The official company website and Wikipedia both confirm this date, with Wikipedia providing the specific day (April 4).",\
      "confidence": "high"\
    },\
    {\
      "field": "headquarters",\
      "citations": [\
        {\
          "url": "https://www.microsoft.com/en-us/about/company",\
          "excerpts": ["Headquartered in Redmond, Washington, Microsoft has offices in over 100 countries."]\
        }\
      ],\
      "reasoning": "The official company website explicitly states the headquarters location as Redmond, Washington, USA.",\
      "confidence": "high"\
    }\
  ],
  "type": "json"
}
```

### [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#high-vs-low-confidence-outputs)  High vs. Low Confidence Outputs

- High Confidence

- Low Confidence

Copy

Ask AI

```
{
  "field": "revenue",
  "citations": [\
    {\
      "url": "https://www.microsoft.com/en-us/Investor/earnings/FY-2023-Q4/press-release-webcast",\
      "excerpts": ["Microsoft reported fiscal year 2023 revenue of $211.9 billion, an increase of 7% compared to the previous fiscal year."]\
    },\
    {\
      "url": "https://www.sec.gov/Archives/edgar/data/789019/000095017023014837/msft-20230630.htm",\
      "excerpts": ["Revenue was $211.9 billion for fiscal year 2023, up 7% compared to $198.3 billion for fiscal year 2022."]\
    }\
  ],
  "reasoning": "The revenue figure is consistent across both the company's investor relations page and their official SEC filing. Both sources explicitly state the fiscal year 2023 revenue as $211.9 billion, representing a 7% increase over the previous year.",
  "confidence": "high"
}
```

Copy

Ask AI

```
{
  "field": "crm_system",
  "citations": [\
    {\
      "url": "https://www.linkedin.com/jobs/view/sales-representative-microsoft-dynamics-365-at-contoso-inc-3584271",\
      "excerpts": ["Looking for sales professionals with experience in Microsoft Dynamics 365 CRM to join our growing team."]\
    }\
  ],
  "reasoning": "There is limited direct evidence about which CRM system the company uses internally. The job posting suggests they work with Microsoft Dynamics 365, but it's not explicitly stated whether this is their primary internal CRM or simply a product they sell/support. No official company documentation confirming their internal CRM system was found.",
  "confidence": "low"
}
```

### [​](https://docs.parallel.ai/task-api/guides/access-research-basis\#per-element-basis)  Per-Element Basis

When working with arrays in your output, the research basis can provide granular citations for individual elements. Here’s an example showing how basis information is provided for both the parent array and individual elements:

Copy

Ask AI

```
{
  "content": "{\"company\":\"OpenAI\",\"key_executives\":[{\"name\":\"Sam Altman\",\"title\":\"CEO\"},{\"name\":\"Greg Brockman\",\"title\":\"President\"}]}",
  "basis": [\
    {\
      "field": "company",\
      "citations": [\
        {\
          "url": "https://openai.com/about",\
          "excerpts": ["OpenAI is headquartered in San Francisco, California."]\
        }\
      ],\
      "reasoning": "The company name is taken from the official about page.",\
      "confidence": "high"\
    },\
    {\
      "field": "key_executives",\
      "citations": [\
        {\
          "url": "https://openai.com/leadership",\
          "excerpts": ["Key executives include Sam Altman and Greg Brockman."]\
        }\
      ],\
      "reasoning": "The leadership page lists each executive explicitly.",\
      "confidence": "high"\
    },\
    {\
      "field": "key_executives.0",\
      "citations": [\
        {\
          "url": "https://openai.com/leadership",\
          "excerpts": ["Sam Altman serves as the CEO of OpenAI."]\
        }\
      ],\
      "reasoning": "Same source, filtered down to the first list element.",\
      "confidence": "high"\
    },\
    {\
      "field": "key_executives.1",\
      "citations": [\
        {\
          "url": "https://openai.com/leadership",\
          "excerpts": ["Greg Brockman serves as President."]\
        }\
      ],\
      "reasoning": "Same source, filtered down to the second list element.",\
      "confidence": "high"\
    }\
  ],
  "type": "json"
}
```

[Task Runs Lifecycle](https://docs.parallel.ai/task-api/guides/execute-task-run) [Webhooks](https://docs.parallel.ai/task-api/webhooks)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Streaming Events - Parallel

**URL:** https://docs.parallel.ai/task-api/task-sse

[Skip to main content](https://docs.parallel.ai/task-api/task-sse#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Streaming Events

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Overview](https://docs.parallel.ai/task-api/task-sse#overview)
- [Enabling Events Streaming](https://docs.parallel.ai/task-api/task-sse#enabling-events-streaming)
- [Stream Behavior](https://docs.parallel.ai/task-api/task-sse#stream-behavior)
- [For Running Tasks](https://docs.parallel.ai/task-api/task-sse#for-running-tasks)
- [For Completed Tasks](https://docs.parallel.ai/task-api/task-sse#for-completed-tasks)
- [Reconnection Behavior](https://docs.parallel.ai/task-api/task-sse#reconnection-behavior)
- [Supported Events](https://docs.parallel.ai/task-api/task-sse#supported-events)
- [Differences Between Task Group Events and Task Run Events](https://docs.parallel.ai/task-api/task-sse#differences-between-task-group-events-and-task-run-events)

This feature is currently in beta and requires the
`parallel-beta: events-sse-2025-07-24` header when using the Task API.

## [​](https://docs.parallel.ai/task-api/task-sse\#overview)  Overview

Task Runs support Server-Sent Events (SSE) at the run level, allowing you to receive real-time
updates on ongoing research conducted by our processors during execution.For streaming events related to Task Groups, see the [streaming endpoints on the Task Group API](https://docs.parallel.ai/task-api/group-api#stream-group-results).
Task Group events provide aggregate updates at the group level, while Task Run events represent updates for individual task runs.
For a more comprehensive list of differences, [see here.](https://docs.parallel.ai/task-api/task-sse#differences-between-task-group-events-and-task-run-events)

### [​](https://docs.parallel.ai/task-api/task-sse\#enabling-events-streaming)  Enabling Events Streaming

To enable periodic event publishing for a task run, set the `enable_events` flag to `true`
when creating the task run. If not specified, events may still be available, but frequent updates are not guaranteed.Create a Task Run with events aggregation enabled explicitly:

Task API

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1/tasks/runs" \
  -H "x-api-key: ${PARALLEL_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "parallel-beta: events-sse-2025-07-24" \
  --data '{
  "input": "What is the latest in AI research?",
  "processor": "lite",
  "enable_events": true
}'
```

To access the event stream for a specific run, use the `/v1beta/tasks/runs/{run_id}/events` endpoint:

Access event stream

Copy

Ask AI

```

curl -X GET "https://api.parallel.ai/v1beta/tasks/runs/trun_6eb64c73e4324b15af2a351bef6d0190/events"
\ -H "x-api-key: ${PARALLEL_API_KEY}" \ -H "Content-Type: text/event-stream"
```

This is what a sample stream looks like:

Event stream

Copy

Ask AI

```

event: task_run.state
data: {"type":"task_run.state","event_id":null,"input":null,"run":{"run_id":"trun_aa9c7a780c9d4d4b9aa0ca064f61a6f7","status":"running","is_active":true,"warnings":null,"error":null,"processor":"pro","metadata":{},"taskgroup_id":null,"created_at":"2025-08-06T00:52:58.619503Z","modified_at":"2025-08-06T00:52:59.495063Z"},"output":null}

event: task_run.progress_msg.exec_status
data: {"type":"task_run.progress_msg.exec_status","message":"Starting research","timestamp":"2025-08-06T00:52:59.786126Z"}

event: task_run.progress_msg.plan
data: {"type":"task_run.progress_msg.plan","message":"I'm working on gathering information about Google's hiring in 2024, including where most jobs were created and any official announcements. I'll review recent news, reports, and Google's own statements to provide a comprehensive answer.","timestamp":"2025-08-06T00:53:19.281306Z"}

event: task_run.progress_msg.tool
data: {"type":"task_run.progress_msg.tool","message":"I've looked into Google's hiring activity in 2024, focusing on locations and official statements. I'll compile the findings and share a clear update with you shortly.","timestamp":"2025-08-06T00:53:28.282905Z"}

event: task_run.progress_stats
data: {"type":"task_run.progress_stats","source_stats":{"num_sources_considered":223,"num_sources_read":22,"sources_read_sample":["http://stcloudlive.com/business/19-layoffs-coming-in-mid-march-at-st-cloud-arctic-cat-facility-company-says","http://snowgoer.com/snowmobiles/arctic-cat-sleds/putting-the-arctic-cat-layoffs-production-stop-in-context/32826","http://25newsnow.com/2024/07/26/cat-deere-cyclical-layoff-mode-say-industry-experts","http://citizen.org/article/big-tech-lobbying-update","http://businessalabama.com/women-in-tech-23-for-23","http://itif.org/publications/2019/10/28/policymakers-guide-techlash","http://distributech.com/","http://newyorker.com/magazine/2019/09/30/four-years-in-startups"]}}

...
```

**Notes:**

- All [Task API processors](https://docs.parallel.ai/task-api/guides/choose-a-processor) starting from `pro` and above have event streaming enabled by default.
- Event streams remain open for 570 seconds. After this period, the stream is closed.

## [​](https://docs.parallel.ai/task-api/task-sse\#stream-behavior)  Stream Behavior

When a stream is started, some earlier events are also re-sent in addition to new updates. This allows developers to build stateless applications more easily, since the API can be relied on without persisting every streamed update. It also supports scenarios where clients can disconnect and later reconnect without missing important events.

### [​](https://docs.parallel.ai/task-api/task-sse\#for-running-tasks)  For Running Tasks

When connecting to a stream for a task that is still running:

- **Complete reasoning trace:** You receive all reasoning messages (`task_run.progress_msg.*`) from the beginning of the task execution, regardless of when you connect to the stream
- **Latest progress stats:** You receive only the current aggregate state via `task_run.progress_stats` events, not historical progress snapshots
- **Real-time updates:** As the task continues, you’ll receive new reasoning messages and updated progress statistics
- **Final result:** The stream concludes with a `task_run.state` event containing the complete task output when execution finishes

### [​](https://docs.parallel.ai/task-api/task-sse\#for-completed-tasks)  For Completed Tasks

When connecting to a stream for a task that has already completed:

- **Complete reasoning trace:** You receive the full sequence of reasoning messages that occurred during the original execution
- **Final progress stats:** You receive the final aggregate statistics from when the task completed
- **Immediate result:** The stream ends with a `task_run.state` event that includes the complete task output in the `output` field. This is useful so you don’t also need to use the result endpoint.

### [​](https://docs.parallel.ai/task-api/task-sse\#reconnection-behavior)  Reconnection Behavior

- Event streams are **not resumable** \- there are no sequence numbers or cursors to resume from a specific point
- If you disconnect and reconnect to the same task:
- **Running tasks:** You get the complete reasoning trace again plus current progress stats
- **Completed tasks:** You get the same complete sequence as the first connection
- Every connection starts with a `task_run.state` event indicating the current status

### [​](https://docs.parallel.ai/task-api/task-sse\#supported-events)  Supported Events

Currently, four types of events are supported:

- **Run Status Events (`task_run.state`):** Indicate the current status of the run. These are sent at the beginning of every stream and when the run transitions to a non-active status.
- **Progress Statistics Events (`task_run.progress_stats`):** Provide point-in-time updates on the number of sources considered and other aggregate statistics. Only the current state is provided, not historical snapshots.
- **Message Events (`task_run.progress_msg.*`):** Communicate reasoning at various stages of task run execution. The complete sequence from the beginning of execution is always provided. Note that this might not be available for `lite` and `base` processors.
- **Error Events (`error`):** Report errors that occur during execution.

**Additional Notes:**

- Event streams always start with a status event and end with a status event (for completed tasks)
- The final status event for completed tasks always includes the complete output in the `output` field
- Events within the reasoning trace maintain their original timestamps, allowing you to understand the execution timeline
- After the event has completed, reasoning traces may not get streamed anymore.

For the full specification of each event, see the examples above.

### [​](https://docs.parallel.ai/task-api/task-sse\#differences-between-task-group-events-and-task-run-events)  Differences Between Task Group Events and Task Run Events

Currently, the events returned by Task Groups is not a strict superset of events returned by Task Runs. See the list of differences below:

|  | Task Run Events | Task Group Events |
| --- | --- | --- |
| **Purpose** | Events for a single Task Run. | Events for an entire Task Group. |
| **Run-level events** | Progress updates, messages, status changes. | Only run status changes. |
| **Resumable streams** | No | Yes, using `event_id`. |
| **Events supported** | Progress updates, messages, status changes for an individual run. | Group status and run terminations. |
| **Reasoning trace** | Complete trace always provided when connecting. | Not available. |
| **Final results** | Always included in final status event. | Available through separate API. |

[Ingest API](https://docs.parallel.ai/task-api/ingest-api) [MCP Tool Calling](https://docs.parallel.ai/task-api/mcp-tool-call)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Task API Quickstart - Parallel

**URL:** https://docs.parallel.ai/task-api/task-quickstart

[Skip to main content](https://docs.parallel.ai/task-api/task-quickstart#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Task

Task API Quickstart

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [What you can build](https://docs.parallel.ai/task-api/task-quickstart#what-you-can-build)
- [Prerequisites](https://docs.parallel.ai/task-api/task-quickstart#prerequisites)
- [Quick start](https://docs.parallel.ai/task-api/task-quickstart#quick-start)
- [Core concepts](https://docs.parallel.ai/task-api/task-quickstart#core-concepts)
- [Output schema types](https://docs.parallel.ai/task-api/task-quickstart#output-schema-types)
- [Input and output patterns](https://docs.parallel.ai/task-api/task-quickstart#input-and-output-patterns)
- [Question in → Answer out](https://docs.parallel.ai/task-api/task-quickstart#question-in-%E2%86%92-answer-out)
- [Question in → Report out](https://docs.parallel.ai/task-api/task-quickstart#question-in-%E2%86%92-report-out)
- [Question in → Auto-structured output](https://docs.parallel.ai/task-api/task-quickstart#question-in-%E2%86%92-auto-structured-output)
- [Structured input → Structured output](https://docs.parallel.ai/task-api/task-quickstart#structured-input-%E2%86%92-structured-output)
- [Use cases](https://docs.parallel.ai/task-api/task-quickstart#use-cases)
- [Next steps](https://docs.parallel.ai/task-api/task-quickstart#next-steps)
- [Rate limits](https://docs.parallel.ai/task-api/task-quickstart#rate-limits)

The **Task API** combines AI inference with web search and live crawling to turn complex research tasks into repeatable workflows. Define what you need in plain language or JSON, and the Task API handles the research, synthesis, and structured output—complete with citations and confidence levels.

See [Pricing](https://docs.parallel.ai/getting-started/pricing) for a detailed schedule of rates.

## [​](https://docs.parallel.ai/task-api/task-quickstart\#what-you-can-build)  What you can build

The Task API is designed for maximum extensibility. Create a task spec for any research need:

- **Data enrichment**: Enhance CRM records, company databases, or contact lists with web intelligence
- **Market research**: Generate comprehensive reports on industries, competitors, or trends
- **Due diligence**: Automate compliance checks, background research, and verification workflows
- **Content generation**: Create research-backed reports, summaries, and analyses

## [​](https://docs.parallel.ai/task-api/task-quickstart\#prerequisites)  Prerequisites

Generate your API key on [Platform](https://platform.parallel.ai/). Then, set up with the TypeScript SDK, Python SDK or with cURL:

cURL

Python

TypeScript

Copy

Ask AI

```
echo "Install curl and jq via brew, apt, or your favorite package manager"
export PARALLEL_API_KEY="PARALLEL_API_KEY"
```

## [​](https://docs.parallel.ai/task-api/task-quickstart\#quick-start)  Quick start

Every Task API workflow follows three steps: **create** a task run, **wait** for completion, and **retrieve** the result.

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="PARALLEL_API_KEY")

# 1. Create a task run
task_run = client.task_run.create(
    input="Stripe",
    task_spec={"output_schema": "The founding year and total funding raised"},
    processor="base"
)

# Output: "10-1945"
```

### [​](https://docs.parallel.ai/task-api/task-quickstart\#question-in-%E2%86%92-report-out)  Question in → Report out

Generate comprehensive markdown reports with inline citations.

Copy

Ask AI

```
from parallel.types import TaskSpecParam, TextSchemaParam

task_run = client.task_run.create(
    input="Create a market research report on the HVAC industry in the USA",
    processor="ultra",
    task_spec=TaskSpecParam(output_schema=TextSchemaParam())
)
# Output: Multi-page markdown report with citations
```

### [​](https://docs.parallel.ai/task-api/task-quickstart\#question-in-%E2%86%92-auto-structured-output)  Question in → Auto-structured output

Let the processor automatically determine the best output structure.

Copy

Ask AI

```
task_run = client.task_run.create(
    input="Research the top 5 AI infrastructure companies and their recent funding",
    processor="ultra"
)
# Output: Automatically structured JSON with company profiles, funding details, etc.
```

### [​](https://docs.parallel.ai/task-api/task-quickstart\#structured-input-%E2%86%92-structured-output)  Structured input → Structured output

Define explicit input and output schemas for precise control over data enrichment.

Copy

Ask AI

```
task_run = client.task_run.create(
    input={"company_name": "Stripe", "website": "stripe.com"},
    task_spec={
        "input_schema": {
            "type": "json",
            "json_schema": {
                "type": "object",
                "properties": {
                    "company_name": {"type": "string"},
                    "website": {"type": "string"}
                }
            }
        },
        "output_schema": {
            "type": "json",
            "json_schema": {
                "type": "object",
                "properties": {
                    "founding_year": {"type": "string"},
                    "employee_count": {"type": "string"},
                    "total_funding": {"type": "string"}
                }
            }
        }
    },
    processor="core"
)
```

## [​](https://docs.parallel.ai/task-api/task-quickstart\#use-cases)  Use cases

[**Enrichment** \\
\\
Enhance structured data with web intelligence. Start with a spreadsheet or database, add new columns with researched data.](https://docs.parallel.ai/task-api/task-enrichment) [**Deep Research** \\
\\
Conduct open-ended research without structured input. Generate comprehensive reports on any topic.](https://docs.parallel.ai/task-api/task-deep-research)

## [​](https://docs.parallel.ai/task-api/task-quickstart\#next-steps)  Next steps

- [**Enrichment quickstart:**](https://docs.parallel.ai/task-api/task-enrichment) Learn how to enrich structured data at scale
- [**Deep Research quickstart:**](https://docs.parallel.ai/task-api/task-deep-research) Generate comprehensive research reports
- [**Task Groups:**](https://docs.parallel.ai/task-api/group-api) Run multiple tasks concurrently with batch tracking
- [**Streaming Events:**](https://docs.parallel.ai/task-api/task-sse) Monitor long-running tasks with real-time progress updates
- [**Webhooks:**](https://docs.parallel.ai/task-api/webhooks) Configure HTTP callbacks for task completion notifications
- [**API Reference:**](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run) Complete endpoint documentation

## [​](https://docs.parallel.ai/task-api/task-quickstart\#rate-limits)  Rate limits

See [Rate Limits](https://docs.parallel.ai/resources/rate-limits) for default quotas and how to request higher limits.

[Best Practices](https://docs.parallel.ai/extract/best-practices) [Enrichment](https://docs.parallel.ai/task-api/task-enrichment)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Define task specification as a variable
TASK_SPEC='{
  "input_schema": {
    "json_schema": {
      "type": "object",
      "properties": {
        "company_name": {
          "type": "string",
          "description": "Name of the company"
        },
        "company_website": {
          "type": "string",
          "description": "Company website URL"
        }
      },
      "required": ["company_name", "company_website"]
    }
  },
  "output_schema": {
    "json_schema": {
      "type": "object",
      "properties": {
        "key_insights": {
          "type": "array",
          "items": {"type": "string"},
          "description": "Key business insights"
        },
        "market_position": {
          "type": "string",
          "description": "Market positioning analysis"
        }
      },
      "required": ["key_insights", "market_position"]
    }
  }
}'
```

### [​](https://docs.parallel.ai/task-api/group-api\#2-create-a-task-group)  2\. Create a Task Group

cURL

Python

TypeScript

Copy

Ask AI

```
# Create task group and capture the ID
response=$(curl --request POST \
  --url https://api.parallel.ai/v1beta/tasks/groups \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: ${PARALLEL_API_KEY}' \
  --data '{}')

# Extract taskgroup_id from response
TASKGROUP_ID=$(echo $response | jq -r '.taskgroup_id')
echo "Created task group: $TASKGROUP_ID"
```

### [​](https://docs.parallel.ai/task-api/group-api\#3-add-tasks-to-the-group)  3\. Add Tasks to the Group

cURL

Python

TypeScript

Copy

Ask AI

```
curl --request POST \
  --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID}/runs \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: ${PARALLEL_API_KEY}' \
  --data '{
  "default_task_spec": '$TASK_SPEC',
  "inputs": [\
    {\
      "input": {\
        "company_name": "Acme Corp",\
        "company_website": "https://acme.com"\
      },\
      "processor": "pro"\
    },\
    {\
      "input": {\
        "company_name": "TechStart",\
        "company_website": "https://techstart.io"\
      },\
      "processor": "pro"\
    }\
  ]
}'
```

### [​](https://docs.parallel.ai/task-api/group-api\#4-monitor-progress)  4\. Monitor Progress

cURL

Python

TypeScript

Copy

Ask AI

```
# Get status of the group
curl --request GET \
  --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID} \
  --header 'x-api-key: ${PARALLEL_API_KEY}'

# Get status of all runs in the group
curl --request GET \
  --no-buffer \
  --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID}/runs \
  --header 'x-api-key: ${PARALLEL_API_KEY}'
```

### [​](https://docs.parallel.ai/task-api/group-api\#5-retrieve-results)  5\. Retrieve Results

The `getRuns` endpoint returns a **Server-Sent Events stream**, not a simple JSON response. Each event in the stream has:

- `type`: Either `"task_run.state"` (a run reached a non-active status: completed, failed, or cancelled) or `"error"`
- `event_id`: Cursor for resuming the stream via the `last_event_id` parameter
- `run`: The `TaskRun` object with `run_id`, `status`, and `is_active`
- `input`: The original input (only included when `include_input=true`)
- `output`: The result output (only included when `include_output=true` **and** the run completed successfully)

cURL

Python

TypeScript

Copy

Ask AI

```
curl --request GET \
  --no-buffer \
  --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID}/events \
  --header 'x-api-key: ${PARALLEL_API_KEY}'
```

## [​](https://docs.parallel.ai/task-api/group-api\#batch-processing-pattern)  Batch Processing Pattern

For large datasets, process Tasks in batches to optimize performance:

Python

TypeScript

Copy

Ask AI

```
async def process_companies_in_batches(
    client: AsyncParallel,
    taskgroup_id: str,
    companies: list[dict[str, str]],
    batch_size: int = 500,
) -> None:
    total_created = 0

    for i in range(0, len(companies), batch_size):
        batch = companies[i : i + batch_size]

        # Create run inputs for this batch
        run_inputs = [\
            BetaRunInputParam(\
                input=CompanyInput(**company).model_dump(),\
                processor="pro",\
            )\
            for company in batch\
        ]

        # Add batch to group
        response = await client.beta.task_group.add_runs(
            taskgroup_id,
            inputs=run_inputs,
            default_task_spec=task_spec,
        )
        total_created += len(response.run_ids)

        print(f"Processed {i + len(batch)} companies. Created {total_created} Tasks.")
```

## [​](https://docs.parallel.ai/task-api/group-api\#error-handling)  Error Handling

The Group API provides robust error handling:

Python

TypeScript

Copy

Ask AI

```
async def process_with_error_handling(client: AsyncParallel, taskgroup_id: str):
    successful_results = []
    failed_results = []

    run_stream = await client.beta.task_group.get_runs(
        taskgroup_id,
        include_input=True,
        include_output=True,
    )

    async for event in run_stream:
        if isinstance(event, ErrorEvent):
            failed_results.append(event)
            continue

        if isinstance(event, TaskRunEvent) and event.output:
            try:
                # Validate the result
                company_output = CompanyOutput.model_validate(event.output.content)
                successful_results.append(event)
            except Exception as e:
                print(f"Validation error: {e}")
                failed_results.append(event)
        elif isinstance(event, TaskRunEvent):
            # Run failed or was cancelled (no output)
            failed_results.append(event)

    print(f"Success: {len(successful_results)}, Failed: {len(failed_results)}")
    return successful_results, failed_results
```

## [​](https://docs.parallel.ai/task-api/group-api\#complete-example)  Complete Example

Here’s a complete script that demonstrates the full workflow, including all of
the setup code above.

Python

TypeScript

Copy

Ask AI

```
import asyncio
import pydantic
from parallel import AsyncParallel
from parallel.types import TaskSpecParam, JsonSchemaParam
from parallel.types.beta.beta_run_input_param import BetaRunInputParam
from parallel.types.beta.task_run_event import TaskRunEvent
from parallel.types.beta.error_event import ErrorEvent

# Define your input and output models
class CompanyInput(pydantic.BaseModel):
    company_name: str = pydantic.Field(description="Name of the company")
    company_website: str = pydantic.Field(description="Company website URL")

class CompanyOutput(pydantic.BaseModel):
    key_insights: list[str] = pydantic.Field(description="Key business insights")
    market_position: str = pydantic.Field(description="Market positioning analysis")

# Create reusable task specification
task_spec = TaskSpecParam(
    input_schema=JsonSchemaParam(json_schema=CompanyInput.model_json_schema()),
    output_schema=JsonSchemaParam(json_schema=CompanyOutput.model_json_schema()),
)

async def wait_for_completion(client: AsyncParallel, taskgroup_id: str) -> None:
    while True:
        task_group = await client.beta.task_group.retrieve(taskgroup_id)

        status = task_group.status
        print(f"Status: {status.task_run_status_counts}")

        if not status.is_active:
            print("All tasks completed!")
            break

        await asyncio.sleep(10)

async def get_all_results(client: AsyncParallel, taskgroup_id: str):
    results = []

    run_stream = await client.beta.task_group.get_runs(
        taskgroup_id,
        include_input=True,
        include_output=True,
    )

    async for event in run_stream:
        if isinstance(event, TaskRunEvent) and event.output:
            company_output = CompanyOutput.model_validate(event.output.content)

            results.append(
                {
                    "company": event.input.input["company_name"],
                    "insights": company_output.key_insights,
                    "market_position": company_output.market_position,
                }
            )
        elif isinstance(event, ErrorEvent):
            print(f"Error: {event.error}")

    return results

async def batch_company_research():
    client = AsyncParallel(api_key="PARALLEL_API_KEY")

    # Create task group
    task_group = await client.beta.task_group.create()
    taskgroup_id = task_group.task_group_id
    print(f"Created taskgroup id {taskgroup_id}")

    # Define companies to research
    companies = [\
        {"company_name": "Stripe", "company_website": "https://stripe.com"},\
        {"company_name": "Shopify", "company_website": "https://shopify.com"},\
        {"company_name": "Salesforce", "company_website": "https://salesforce.com"},\
    ]

    # Add Tasks to group
    run_inputs = [\
        BetaRunInputParam(\
            input=CompanyInput(**company).model_dump(),\
            processor="pro",\
        )\
        for company in companies\
    ]

    response = await client.beta.task_group.add_runs(
        taskgroup_id,
        inputs=run_inputs,
        default_task_spec=task_spec,
    )
    print(f"Added {len(response.run_ids)} runs to taskgroup {taskgroup_id}")

    # Wait for completion and get results
    await wait_for_completion(client, taskgroup_id)
    results = await get_all_results(client, taskgroup_id)
    print(f"Successfully processed {len(results)} companies")
    return results

# Run the batch job
results = asyncio.run(batch_company_research())
```

See all 106 lines

[Webhooks](https://docs.parallel.ai/task-api/webhooks) [Ingest API](https://docs.parallel.ai/task-api/ingest-api)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve Task Run Input - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks v1

Retrieve Task Run Input

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Retrieve Task Run Input

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1/tasks/runs/{run_id}/input"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "task_spec": {
    "output_schema": {
      "json_schema": {
        "type": "object",
        "properties": {
          "gdp": {
            "type": "string",
            "description": "GDP in USD for the year, formatted like '$3.1 trillion (2023)'"
          }
        },
        "required": [\
          "gdp"\
        ],
        "additionalProperties": false
      },
      "type": "json"
    },
    "input_schema": {
      "json_schema": {
        "type": "object",
        "properties": {
          "country": {
            "type": "string"
          },
          "year": {
            "type": "integer"
          }
        },
        "required": [\
          "country",\
          "year"\
        ],
        "additionalProperties": false
      },
      "type": "json"
    }
  },
  "input": {
    "country": "France",
    "year": 2023
  }
}
```

GET

/

v1

/

tasks

/

runs

/

{run\_id}

/

input

Try it

Retrieve Task Run Input

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1/tasks/runs/{run_id}/input"

headers = {"x-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "task_spec": {
    "output_schema": {
      "json_schema": {
        "type": "object",
        "properties": {
          "gdp": {
            "type": "string",
            "description": "GDP in USD for the year, formatted like '$3.1 trillion (2023)'"
          }
        },
        "required": [\
          "gdp"\
        ],
        "additionalProperties": false
      },
      "type": "json"
    },
    "input_schema": {
      "json_schema": {
        "type": "object",
        "properties": {
          "country": {
            "type": "string"
          },
          "year": {
            "type": "integer"
          }
        },
        "required": [\
          "country",\
          "year"\
        ],
        "additionalProperties": false
      },
      "type": "json"
    }
  },
  "input": {
    "country": "France",
    "year": 2023
  }
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#parameter-run-id)

run\_id

string

required

#### Response

200

application/json

Successful Response

Request to run a task.

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#response-processor)

processor

string

required

Processor to use for the task.

Example:

`"base"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#response-input-one-of-0)

input

stringInput · objectstringInput · object

required

Input to the task, either text or a JSON object.

Example:

`"What was the GDP of France in 2023?"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the run. Keys and values must be strings with a maximum length of 16 and 512 characters respectively.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#response-source-policy-one-of-0)

source\_policy

SourcePolicy · object

Optional source policy governing preferred and disallowed domains in web search results.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#response-task-spec-one-of-0)

task\_spec

TaskSpec · object

Task specification. If unspecified, defaults to auto output schema.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-input#response-previous-interaction-id-one-of-0)

previous\_interaction\_id

string \| null

Interaction ID to use as context for this request.

[Retrieve Task Run](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run) [Retrieve Task Run Result](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Delete Monitor - Parallel

**URL:** https://docs.parallel.ai/api-reference/monitor/delete-monitor

[Skip to main content](https://docs.parallel.ai/api-reference/monitor/delete-monitor#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

Delete Monitor

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Delete Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}"

headers = {"x-api-key": "<api-key>"}

response = requests.delete(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "monitor_id": "<string>",
  "query": "<string>",
  "status": "active",
  "cadence": "daily",
  "created_at": "2023-11-07T05:31:56Z",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "<string>",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "output_schema": {
    "json_schema": {},
    "type": "json"
  },
  "last_run_at": "2025-01-15T10:30:00Z"
}
```

DELETE

/

v1alpha

/

monitors

/

{monitor\_id}

Try it

Delete Monitor

Python

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1alpha/monitors/{monitor_id}"

headers = {"x-api-key": "<api-key>"}

response = requests.delete(url, headers=headers)

print(response.text)
```

200

401

404

422

Copy

Ask AI

```
{
  "monitor_id": "<string>",
  "query": "<string>",
  "status": "active",
  "cadence": "daily",
  "created_at": "2023-11-07T05:31:56Z",
  "metadata": {
    "key": "value"
  },
  "webhook": {
    "url": "<string>",
    "event_types": [\
      "monitor.event.detected"\
    ]
  },
  "output_schema": {
    "json_schema": {},
    "type": "json"
  },
  "last_run_at": "2025-01-15T10:30:00Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#parameter-monitor-id)

monitor\_id

string

required

#### Response

200

application/json

Successful Response

Response object for a monitor, including its status, cadence and metadata.

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-monitor-id)

monitor\_id

string

required

ID of the monitor.

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-query)

query

string

required

The query being monitored.

Example:

`"Recent news about LLM models."`

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-status)

status

enum<string>

required

Status of the monitor.

Available options:

`active`,

`canceled`

Examples:

`"active"`

`"canceled"`

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-cadence)

cadence

enum<string>

required

Cadence of the monitor.

Available options:

`daily`,

`weekly`,

`hourly`,

`every_two_weeks`

Examples:

`"daily"`

`"weekly"`

`"hourly"`

`"every_two_weeks"`

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-created-at)

created\_at

string<date-time>

required

Timestamp of the creation of the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the monitor.

Showchild attributes

Example:

```json
{ "key": "value" }
```

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-webhook-one-of-0)

webhook

MonitorWebhook · object

Webhook configuration for the monitor.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-output-schema-one-of-0)

output\_schema

JsonSchema · object

Output schema for the monitor event.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/monitor/delete-monitor#response-last-run-at-one-of-0)

last\_run\_at

string \| null

Timestamp of the last run for the monitor.

Example:

`"2025-01-15T10:30:00Z"`

[Update Monitor](https://docs.parallel.ai/api-reference/monitor/update-monitor) [Retrieve Event Group](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Google BigQuery - Parallel

**URL:** https://docs.parallel.ai/data-integrations/bigquery

[Skip to main content](https://docs.parallel.ai/data-integrations/bigquery#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Data Integrations

Google BigQuery

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features](https://docs.parallel.ai/data-integrations/bigquery#features)
- [Installation](https://docs.parallel.ai/data-integrations/bigquery#installation)
- [Deployment](https://docs.parallel.ai/data-integrations/bigquery#deployment)
- [Prerequisites](https://docs.parallel.ai/data-integrations/bigquery#prerequisites)
- [Deploy with CLI](https://docs.parallel.ai/data-integrations/bigquery#deploy-with-cli)
- [Basic Usage](https://docs.parallel.ai/data-integrations/bigquery#basic-usage)
- [Function Parameters](https://docs.parallel.ai/data-integrations/bigquery#function-parameters)
- [Parsing Results](https://docs.parallel.ai/data-integrations/bigquery#parsing-results)
- [Company Convenience Function](https://docs.parallel.ai/data-integrations/bigquery#company-convenience-function)
- [Processor Selection](https://docs.parallel.ai/data-integrations/bigquery#processor-selection)
- [Best Practices](https://docs.parallel.ai/data-integrations/bigquery#best-practices)

This integration is ideal for data engineers who need to enrich large datasets with web intelligence directly in their BigQuery pipelines—without leaving SQL or building custom API integrations.Parallel provides SQL-native remote functions for Google BigQuery that enable data enrichment directly in your SQL queries. The integration uses Cloud Functions to securely connect BigQuery to the Parallel API.

View the complete demo notebook:

- [BigQuery Enrichment Demo](https://github.com/parallel-web/parallel-web-tools/blob/main/notebooks/bigquery_enrichment_demo.ipynb)

## [​](https://docs.parallel.ai/data-integrations/bigquery\#features)  Features

- **SQL-Native**: Use `parallel_enrich()` directly in BigQuery SQL queries
- **Secure**: API key stored in Secret Manager, accessed via Cloud Functions
- **Configurable Processors**: Choose from lite-fast to ultra for speed vs thoroughness tradeoffs
- **Structured Output**: Returns JSON that can be parsed with BigQuery’s `JSON_EXTRACT_SCALAR()`

## [​](https://docs.parallel.ai/data-integrations/bigquery\#installation)  Installation

Copy

Ask AI

```
pip install parallel-web-tools
```

The standalone `parallel-cli` binary does not include deployment commands. You must install via pip to deploy the BigQuery integration.

## [​](https://docs.parallel.ai/data-integrations/bigquery\#deployment)  Deployment

Unlike Spark, the BigQuery integration requires a one-time deployment step to set up Cloud Functions and remote function definitions in your GCP project.

### [​](https://docs.parallel.ai/data-integrations/bigquery\#prerequisites)  Prerequisites

1. **Google Cloud Project** with billing enabled
2. **Parallel API Key** from [Parallel](https://platform.parallel.ai/)
3. **Google Cloud SDK** installed and authenticated:

Copy

Ask AI

```
gcloud auth login
gcloud auth application-default login
```

### [​](https://docs.parallel.ai/data-integrations/bigquery\#deploy-with-cli)  Deploy with CLI

Copy

Ask AI

```
parallel-cli enrich deploy --system bigquery \
    --project=your-gcp-project \
    --region=us-central1 \
    --api-key=your-parallel-api-key
```

This creates:

- Secret in Secret Manager for your API key
- Cloud Function (Gen2) that handles enrichment requests
- BigQuery Connection for remote function calls
- BigQuery Dataset (`parallel_functions`)
- Remote functions: `parallel_enrich()` and `parallel_enrich_company()`

For manual deployment options, troubleshooting, and cleanup instructions, see the [complete BigQuery setup guide](https://github.com/parallel-web/parallel-web-tools/blob/main/docs/bigquery-setup.md).

## [​](https://docs.parallel.ai/data-integrations/bigquery\#basic-usage)  Basic Usage

Once deployed, use `parallel_enrich()` in any BigQuery SQL query:

Copy

Ask AI

```
SELECT
    name,
    `your-project.parallel_functions.parallel_enrich`(
        JSON_OBJECT('company_name', name, 'website', website),
        JSON_ARRAY('CEO name', 'Founding year', 'Brief description')
    ) as enriched_data
FROM your_dataset.companies
LIMIT 10;
```

Output:

Copy

Ask AI

```
+--------+----------------------------------------------------------------------------------------------------------------------+
| name   | enriched_data                                                                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------+
| Google | {"ceo_name": "Sundar Pichai", "founding_year": "1998", "brief_description": "Google is an American...", "basis": []} |
| Apple  | {"ceo_name": "Tim Cook", "founding_year": "1976", "brief_description": "Apple Inc. is an American...", "basis": []}  |
+--------+----------------------------------------------------------------------------------------------------------------------+
```

### [​](https://docs.parallel.ai/data-integrations/bigquery\#function-parameters)  Function Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `input_data` | `JSON` | JSON object with key-value pairs of input data for enrichment |
| `output_columns` | `JSON` | JSON array of descriptions for columns you want to enrich |

### [​](https://docs.parallel.ai/data-integrations/bigquery\#parsing-results)  Parsing Results

The function returns JSON strings. Field names are converted to snake\_case (e.g., “CEO name” → `ceo_name`).Use `JSON_EXTRACT_SCALAR()` to extract individual fields:

Copy

Ask AI

```
WITH enriched AS (
    SELECT
        name,
        `your-project.parallel_functions.parallel_enrich`(
            JSON_OBJECT('company_name', name),
            JSON_ARRAY('CEO name', 'Industry', 'Headquarters')
        ) as info
    FROM your_dataset.companies
)
SELECT
    name,
    JSON_EXTRACT_SCALAR(info, '$.ceo_name') as ceo,
    JSON_EXTRACT_SCALAR(info, '$.industry') as industry,
    JSON_EXTRACT_SCALAR(info, '$.headquarters') as hq
FROM enriched;
```

Output:

Copy

Ask AI

```
+--------+-------------+------------+---------------+
| name   | ceo         | industry   | hq            |
+--------+-------------+------------+---------------+
| Google | Sundar Pichai| Technology | Mountain View |
| Apple  | Tim Cook    | Technology | Cupertino     |
+--------+-------------+------------+---------------+
```

### [​](https://docs.parallel.ai/data-integrations/bigquery\#company-convenience-function)  Company Convenience Function

For common company enrichment use cases:

Copy

Ask AI

```
SELECT
    `your-project.parallel_functions.parallel_enrich_company`(
        'Google',
        'google.com',
        JSON_ARRAY('CEO name', 'Employee count', 'Stock ticker')
    ) as company_info;
```

## [​](https://docs.parallel.ai/data-integrations/bigquery\#processor-selection)  Processor Selection

Choose a processor based on your speed vs thoroughness requirements. See [Choose a Processor](https://docs.parallel.ai/task-api/guides/choose-a-processor) for detailed guidance and [Pricing](https://docs.parallel.ai/resources/pricing) for cost information.To use a different processor, create a custom remote function with the desired processor in the `user_defined_context`:

Copy

Ask AI

```
CREATE OR REPLACE FUNCTION `your-project.parallel_functions.parallel_enrich_pro`(
    input_data STRING,
    output_columns STRING
)
RETURNS STRING
REMOTE WITH CONNECTION `your-project.us-central1.parallel-connection`
OPTIONS (
    endpoint = 'YOUR_FUNCTION_URL',
    user_defined_context = [("processor", "pro-fast")]
);
```

## [​](https://docs.parallel.ai/data-integrations/bigquery\#best-practices)  Best Practices

Batch sizing

Process data in batches to manage costs and avoid timeouts:

Copy

Ask AI

```
SELECT parallel_enrich(...) FROM companies LIMIT 100;
```

Error handling

Failed enrichments return JSON with an `error` field:

Copy

Ask AI

```
{"error": "error message here"}
```

Filter these in your downstream processing.

Cost management

- Use `lite-fast` for high-volume, basic enrichments
- Test with small batches before processing large tables
- Store results to avoid re-enriching the same data

[DuckDB](https://docs.parallel.ai/data-integrations/duckdb) [Polars](https://docs.parallel.ai/data-integrations/polars)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Extend FindAll Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Extend FindAll Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run = client.beta.findall.extend(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
    additional_match_limit=10,
)

print(f"FindAll run {run.findall_id} extended: {run.model_dump_json(indent=2)}")
```

200

404

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    }\
  ],
  "enrichments": [\
    {\
      "processor": "core",\
      "output_schema": {\
        "json_schema": {\
          "type": "object",\
          "properties": {\
            "ceo_name": {\
              "type": "string",\
              "description": "Name of the current CEO of the company. If the CEO is not publicly known, provide the name of the highest-ranking executive or founder. If no information is available, return null."\
            }\
          }\
        },\
        "type": "json"\
      }\
    }\
  ],
  "generator": "core",
  "match_limit": 50
}
```

POST

/

v1beta

/

findall

/

runs

/

{findall\_id}

/

extend

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run = client.beta.findall.extend(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
    additional_match_limit=10,
)

print(f"FindAll run {run.findall_id} extended: {run.model_dump_json(indent=2)}")
```

200

404

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    }\
  ],
  "enrichments": [\
    {\
      "processor": "core",\
      "output_schema": {\
        "json_schema": {\
          "type": "object",\
          "properties": {\
            "ceo_name": {\
              "type": "string",\
              "description": "Name of the current CEO of the company. If the CEO is not publicly known, provide the name of the highest-ranking executive or founder. If no information is available, return null."\
            }\
          }\
        },\
        "type": "json"\
      }\
    }\
  ],
  "generator": "core",
  "match_limit": 50
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#parameter-findall-id)

findall\_id

string

required

#### Body

application/json

Input model for FindAll extend.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#body-additional-match-limit)

additional\_match\_limit

integer

required

Additional number of matches to find for this FindAll run. This value will be added to the current match limit to determine the new total match limit. Must be greater than 0.

#### Response

200

application/json

Successful Response

Response model for FindAll ingest.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#response-objective)

objective

string

required

Natural language objective of the FindAll run.

Example:

`"Find all AI companies that raised Series A funding in 2024"`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#response-entity-type)

entity\_type

string

required

Type of the entity for the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#response-match-conditions)

match\_conditions

MatchCondition · object\[\]

required

List of match conditions for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#response-enrichments-one-of-0)

enrichments

FindAllEnrichInput · object\[\] \| null

List of enrichment inputs for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#response-generator)

generator

enum<string>

default:core

The generator of the FindAll run.

Available options:

`base`,

`core`,

`pro`,

`preview`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/extend-findall-run#response-match-limit-one-of-0)

match\_limit

integer \| null

Max number of candidates to evaluate

[FindAll Run Result](https://docs.parallel.ai/api-reference/findall-api-beta/findall-run-result) [Add Enrichment to FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/add-enrichment-to-findall-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve FindAll Run Status - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Retrieve FindAll Run Status

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run = client.beta.findall.retrieve(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {run.findall_id} status: {run.status.status}")
```

200

422

Copy

Ask AI

```
{
  "findall_id": "<string>",
  "status": {
    "status": "queued",
    "is_active": true,
    "metrics": {
      "generated_candidates_count": 0,
      "matched_candidates_count": 0
    },
    "termination_reason": "low_match_rate"
  },
  "generator": "base",
  "metadata": {},
  "created_at": "<string>",
  "modified_at": "<string>"
}
```

GET

/

v1beta

/

findall

/

runs

/

{findall\_id}

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

run = client.beta.findall.retrieve(
    findall_id="findall_56ccc4d188fb41a0803a935cf485c774",
)

print(f"FindAll run {run.findall_id} status: {run.status.status}")
```

200

422

Copy

Ask AI

```
{
  "findall_id": "<string>",
  "status": {
    "status": "queued",
    "is_active": true,
    "metrics": {
      "generated_candidates_count": 0,
      "matched_candidates_count": 0
    },
    "termination_reason": "low_match_rate"
  },
  "generator": "base",
  "metadata": {},
  "created_at": "<string>",
  "modified_at": "<string>"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#parameter-one-of-0)

parallel-beta

string \| null

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#parameter-findall-id)

findall\_id

string

required

#### Response

200

application/json

Successful Response

FindAll run object with status and metadata.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#response-findall-id)

findall\_id

string

required

ID of the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#response-status)

status

FindAllRunStatus · object

required

Status object for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#response-generator)

generator

enum<string>

required

Generator for the FindAll run.

Available options:

`base`,

`core`,

`pro`,

`preview`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#response-metadata-one-of-0)

metadata

Metadata · object

Metadata for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#response-created-at-one-of-0)

created\_at

string \| null

Timestamp of the creation of the run, in RFC 3339 format.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/retrieve-findall-run-status#response-modified-at-one-of-0)

modified\_at

string \| null

Timestamp of the latest modification to the FindAll run result, in RFC 3339 format.

[Create FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run) [Stream FindAll Events](https://docs.parallel.ai/api-reference/findall-api-beta/stream-findall-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Ingest API - Parallel

**URL:** https://docs.parallel.ai/task-api/ingest-api

[Skip to main content](https://docs.parallel.ai/task-api/ingest-api#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Ingest API

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [API Overview](https://docs.parallel.ai/task-api/ingest-api#api-overview)
- [Endpoints](https://docs.parallel.ai/task-api/ingest-api#endpoints)
- [Suggest Task](https://docs.parallel.ai/task-api/ingest-api#suggest-task)
- [Request Parameters](https://docs.parallel.ai/task-api/ingest-api#request-parameters)
- [Response Schema](https://docs.parallel.ai/task-api/ingest-api#response-schema)
- [Example Request](https://docs.parallel.ai/task-api/ingest-api#example-request)
- [Example Response](https://docs.parallel.ai/task-api/ingest-api#example-response)
- [Suggest Processor](https://docs.parallel.ai/task-api/ingest-api#suggest-processor)
- [Suggest Processor Request Parameters](https://docs.parallel.ai/task-api/ingest-api#suggest-processor-request-parameters)
- [Suggest Processor Example Request](https://docs.parallel.ai/task-api/ingest-api#suggest-processor-example-request)
- [Suggest Processor Response Schema](https://docs.parallel.ai/task-api/ingest-api#suggest-processor-response-schema)
- [Suggest Processor Example Response](https://docs.parallel.ai/task-api/ingest-api#suggest-processor-example-response)
- [How Processor Suggestion Works](https://docs.parallel.ai/task-api/ingest-api#how-processor-suggestion-works)
- [Examples](https://docs.parallel.ai/task-api/ingest-api#examples)
- [Select Input Columns from a Predefined Set](https://docs.parallel.ai/task-api/ingest-api#select-input-columns-from-a-predefined-set)
- [End-to-End Ingest to Task Execution](https://docs.parallel.ai/task-api/ingest-api#end-to-end-ingest-to-task-execution)

## [​](https://docs.parallel.ai/task-api/ingest-api\#api-overview)  API Overview

The Parallel Ingest API provides endpoints for creating intelligent task runs that can perform web research and data extraction. The API is built around a stateful architecture where task creation and result retrieval are separate operations.

## [​](https://docs.parallel.ai/task-api/ingest-api\#endpoints)  Endpoints

### [​](https://docs.parallel.ai/task-api/ingest-api\#suggest-task)  Suggest Task

`POST /v1beta/tasks/suggest`Generate a task specification based on user intent. This endpoint helps you create properly structured tasks by analyzing your requirements and suggesting appropriate schemas.

#### [​](https://docs.parallel.ai/task-api/ingest-api\#request-parameters)  Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `user_intent` | string | Yes | Natural language description of what you want to accomplish |
| `previous_task` | `SuggestedTaskSpec` | No | Previous task specification to iterate upon and improve, or to restrict input columns to a predefined set (see [example](https://docs.parallel.ai/task-api/ingest-api#select-input-columns-from-a-predefined-set) below) |

#### [​](https://docs.parallel.ai/task-api/ingest-api\#response-schema)  Response Schema

Returns a `SuggestedTaskSpec` object with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `input_schema` | object | JSON schema defining expected input structure |
| `output_schema` | object | JSON schema defining expected output structure |
| `inputs` | array | Sample input data, if provided in the user intent |
| `title` | string | Suggested title for the task |
| `warnings` | array | Optional list of warnings about the generated specification |

**Warning Types:**

| Warning Type | Description |
| --- | --- |
| `schema_generalization` | Some fields were generalized to create a more reusable schema |
| `unparsable_input` | User-provided input data couldn’t be fully parsed |
| `unattainable_task` | The requested task cannot be created exactly as specified |

#### [​](https://docs.parallel.ai/task-api/ingest-api\#example-request)  Example Request

- cURL

- Python

- TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/tasks/suggest" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "user_intent": "Find the CEOs of tech companies"
  }'
```

**With previous task iteration:**

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/tasks/suggest" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "user_intent": "I want to also include the company website and founding year in the output schema",
    "previous_task": {
      "input_schema": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "description": "Name of the company"
          }
        },
        "required": ["company_name"]
      },
      "output_schema": {
        "type": "object",
        "properties": {
          "ceo_name": {
            "type": "string",
            "description": "Current CEO of the company"
          }
        }
      }
    }
  }'
```

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1beta/tasks/suggest"
headers = {
    "x-api-key": "PARALLEL_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "user_intent": "Find the CEOs of tech companies"
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)
```

**With previous task iteration:**

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1beta/tasks/suggest"
headers = {
    "x-api-key": "PARALLEL_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "user_intent": "I want to also include the company website and founding year in the output",
    "previous_task": {
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "Name of the company"
                }
            },
            "required": ["company_name"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "ceo_name": {
                    "type": "string",
                    "description": "Current CEO of the company"
                }
            }
        }
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)
```

Copy

Ask AI

```
const response = await fetch('https://api.parallel.ai/v1beta/tasks/suggest', {
  method: 'POST',
  headers: {
    "x-api-key": "PARALLEL_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    user_intent: 'Find the CEOs of tech companies'
  })
});

const result = await response.json();
console.log(result);
```

**With previous task iteration:**

Copy

Ask AI

```
const response = await fetch('https://api.parallel.ai/v1beta/tasks/suggest', {
  method: 'POST',
  headers: {
    "x-api-key": "PARALLEL_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    user_intent: 'I want to also include the company website and founding year',
    previous_task: {
      input_schema: {
        type: 'object',
        properties: {
          company_name: {
            type: 'string',
            description: 'Name of the company'
          }
        },
        required: ['company_name']
      },
      output_schema: {
        type: 'object',
        properties: {
          ceo_name: {
            type: 'string',
            description: 'Current CEO of the company'
          }
        }
      }
    }
  })
});

const result = await response.json();
console.log(result);
```

#### [​](https://docs.parallel.ai/task-api/ingest-api\#example-response)  Example Response

Copy

Ask AI

```
{
  "input_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "Name of the company"
      }
    },
    "required": ["company_name"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "ceo_name": {
        "type": "string",
        "description": "Current CEO of the company"
      },
      "appointed_date": {
        "type": "string",
        "description": "Date when the CEO was appointed"
      }
    }
  },
  "inputs": [],
  "title": "Find Company CEO Information"
}
```

### [​](https://docs.parallel.ai/task-api/ingest-api\#suggest-processor)  Suggest Processor

`POST /v1beta/tasks/suggest-processor`Enhance and optimize a task specification by suggesting the most appropriate processor and refining the schemas.

#### [​](https://docs.parallel.ai/task-api/ingest-api\#suggest-processor-request-parameters)  Suggest Processor Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `task_spec` | object | Yes | Task specification object to be processed |
| `choose_processors_from` | array | No | List of processors to choose from. If not provided, the API will consider all available processors. |

**Valid values:**`base`, `base-fast`, `core`, `core-fast`, `core2x`, `core2x-fast`, `pro`, `pro-fast`, `ultra`, `ultra-fast`, `ultra2x`, `ultra2x-fast`, `ultra4x`, `ultra4x-fast`, `ultra8x`, `ultra8x-fast`

The `lite` and `lite-fast` processors are available for task execution but will never be returned by this endpoint.

See [Processors](https://docs.parallel.ai/task-api/guides/choose-a-processor) for details on each processor.

#### [​](https://docs.parallel.ai/task-api/ingest-api\#suggest-processor-example-request)  Suggest Processor Example Request

- cURL

- Python

- TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/tasks/suggest-processor" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "task_spec": {
      "input_schema": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string"
          }
        }
      },
      "output_schema": {
        "type": "object",
        "properties": {
          "ceo_name": {
            "type": "string"
          }
        }
      }
    },
    "choose_processors_from": ["base", "core", "core2x", "pro", "ultra"]
  }'
```

Copy

Ask AI

```
import requests

url = "https://api.parallel.ai/v1beta/tasks/suggest-processor"
headers = {
    "x-api-key": "PARALLEL_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "task_spec": {
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string"
                }
            }
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "ceo_name": {
                    "type": "string"
                }
            }
        }
    },
    "choose_processors_from": ["base", "core", "core2x", "pro", "ultra"]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)
```

Copy

Ask AI

```
const response = await fetch('https://api.parallel.ai/v1beta/tasks/suggest-processor', {
  method: 'POST',
  headers: {
    "x-api-key": "PARALLEL_API_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    task_spec: {
      input_schema: {
        type: 'object',
        properties: {
          company_name: {
            type: 'string'
          }
        }
      },
      output_schema: {
        type: 'object',
        properties: {
          ceo_name: {
            type: 'string'
          }
        }
      }
    },
    choose_processors_from: ["base", "core", "core2x", "pro", "ultra"]
  })
});

const result = await response.json();
console.log(result);
```

#### [​](https://docs.parallel.ai/task-api/ingest-api\#suggest-processor-response-schema)  Suggest Processor Response Schema

| Field | Type | Description |
| --- | --- | --- |
| `recommended_processors` | array | List of recommended processors in priority order. We recommend using the first element. |

Returns an enhanced task specification with additional fields and optimizations.

#### [​](https://docs.parallel.ai/task-api/ingest-api\#suggest-processor-example-response)  Suggest Processor Example Response

Copy

Ask AI

```
{
  "recommended_processors": ["pro"]
}
```

#### [​](https://docs.parallel.ai/task-api/ingest-api\#how-processor-suggestion-works)  How Processor Suggestion Works

The `/suggest-processor` endpoint analyzes your task specification to recommend the most appropriate processor. The algorithm considers:

1. **Task Complexity** \- Number of output fields, depth of research required
2. **Research Pattern** \- Whether the task requires single-step lookups, multi-step reasoning, or parallel breadth-first research
3. **Data Sources** \- How many disparate sources need to be consulted
4. **Special Tools** \- Whether the task requires specialized capabilities like entity ranking

The recommendation balances task requirements against processor capabilities, selecting the lowest-cost processor that can reliably complete your task.

The first processor in `recommended_processors` is always the best recommendation. The API may return multiple processors if several could handle the task, but we recommend using the first one.

## [​](https://docs.parallel.ai/task-api/ingest-api\#examples)  Examples

### [​](https://docs.parallel.ai/task-api/ingest-api\#select-input-columns-from-a-predefined-set)  Select Input Columns from a Predefined Set

Sometimes you have a specific dataset with fixed columns and need to create a task that works exclusively with those columns. The `previous_task` parameter allows you to constrain the API to generate task specifications that match your exact data structure.**When to use this approach:**

- You have a fixed dataset schema that cannot be modified
- You want to ensure the task only uses your specific input columns
- You need to provide examples that match your exact data format
- You want to prevent the API from suggesting additional input fields

**The workflow:**

1. **Define Your Schema**: Specify exactly which columns you want to use as inputs with their descriptions
2. **Provide Sample Data**: Include examples that match your exact data format
3. **Generate a `SuggestedTaskSpec`**: Use the helper function to create a properly formatted `SuggestedTaskSpec` object
4. **Refine with API**: Pass this as `previous_task` to get a refined task spec that respects your column constraints

The API will use your predefined input schema as a foundation and refine the output schema while preserving your input columns. This guarantees the final task specification integrates seamlessly with your existing dataset.

Copy

Ask AI

```
import requests
import json

if __name__ == "__main__":

    user_intent = "Find the CEO, investments, and customer details for the company"

    columns_with_descriptions = [\
        ("company_id", "The unique identifier of the company to retrieve executive, investment, and customer details for."),\
        ("company_name", "The name of the company to identify and gather detailed information about."),\
        ("company_website", "The domain of the company's website to assist in identifying the correct organization."),\
        ("industry", "The primary industry the company operates in."),\
        ("employee_count", "The exact number of employees at the company.")\
    ]

    examples = [\
        {\
            "company_id": "comp_001",\
            "company_name": "Parallel AI",\
            "company_website": "parallel.ai",\
            "industry": "AI",\
            "employee_count": "25"\
        },\
        {\
            "company_id": "comp_002",\
            "company_name": "Google",\
            "company_website": "google.com",\
            "industry": "Software",\
            "employee_count": "125000"\
        }\
    ]

    def get_suggested_task_spec(columns_with_descriptions, examples, title):
        all_valid_columns = {
            column_name: {
                "type": "string",
                "description": description
            }
            for column_name, description in columns_with_descriptions
        }

        return {
            "input_schema": {
                "type": "object",
                "properties": all_valid_columns
            },
            "output_schema": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string",
                        "description": "answer to the question"
                    }
                },
                "required": ["answer"],
            },
            "inputs": examples,
            "title": title
        }

    suggested_task_spec = get_suggested_task_spec(
        columns_with_descriptions=columns_with_descriptions,
        examples=examples,
        title="Company executive, investments, and customer details"
    )

    url = "https://api.parallel.ai/v1beta/tasks/suggest"
    headers = {
        "x-api-key": "PARALLEL_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "user_intent": f"{user_intent}. Improve output_schema to include more descriptive fields, and only keep input fields that are relevant to answering the question.",
        "previous_task": suggested_task_spec
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    print(json.dumps(result, indent=2))
```

See all 80 lines

### [​](https://docs.parallel.ai/task-api/ingest-api\#end-to-end-ingest-to-task-execution)  End-to-End Ingest to Task Execution

The following Python script demonstrates the complete workflow of the Ingest API, from task suggestion to result retrieval:

Copy

Ask AI

```
#!/usr/bin/env python3
"""
End-to-end test script for Parallel Ingest API

This script demonstrates the complete workflow:
1. Suggest a task based on user intent
2. Suggest a processor for the task
3. Create and run the task
4. Retrieve the results

Usage:
    python test_ingest_api.py

Make sure to set your PARALLEL_API_KEY environment variable or update the script directly.
"""

import os
import requests
import json
import time
from typing import Dict, Any, Optional

# Configuration
API_KEY = "PARALLEL_API_KEY"
BASE_URL = "https://api.parallel.ai"

class IngestAPITester:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def suggest_task(self, user_intent: str) -> Optional[Dict[str, Any]]:
        """Step 1: Suggest a task based on user intent"""
        print(f"🔍 Step 1: Suggesting task for intent: '{user_intent}'")

        url = f"{self.base_url}/v1beta/tasks/suggest"
        data = {"user_intent": user_intent}

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()

            result = response.json()
            print("✅ Task suggestion successful!")
            print(f"   Title: {result.get('title', 'N/A')}")
            print(f"   Input schema: {json.dumps(result.get('input_schema', {}), indent=2)}")
            print(f"   Output schema: {json.dumps(result.get('output_schema', {}), indent=2)}")
            print()

            return result

        except requests.exceptions.RequestException as e:
            print(f"❌ Error suggesting task: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"   Response: {e.response.text}")
            return None

    def suggest_processor(self, task_spec: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Step 2: Suggest a processor for the task"""
        print("🔧 Step 2: Suggesting processor for the task")

        url = f"{self.base_url}/v1beta/tasks/suggest-processor"
        data = {
            "task_spec": task_spec,
            "choose_processors_from": ["base", "core", "core2x", "pro", "ultra"]
        }

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()

            result = response.json()
            print("✅ Processor suggestion successful!")

            # Extract the first recommended processor
            recommended_processors = result.get('recommended_processors', [])
            if recommended_processors:
                selected_processor = recommended_processors[0]
                print(f"   Recommended processors: {recommended_processors}")
                print(f"   Selected processor: {selected_processor}")
                result['selected_processor'] = selected_processor
            else:
                print("   ⚠️ No processors recommended, defaulting to 'core'")
                result['selected_processor'] = 'core'

            print(f"   Enhanced task spec received")
            print()

            return result

        except requests.exceptions.RequestException as e:
            print(f"❌ Error suggesting processor: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"   Response: {e.response.text}")
            return None

    def create_task_run(self, input_data: Any, processor: str = "core", task_spec: Optional[Dict] = None) -> Optional[str]:
        """Step 3: Create a task run"""
        print(f"🚀 Step 3: Creating task run with processor '{processor}'")

        url = f"{self.base_url}/v1/tasks/runs"
        data = {
            "input": input_data,
            "processor": processor
        }

        if task_spec:
            # Format the task_spec according to the documentation
            # Schemas need to be wrapped with type and json_schema fields
            formatted_task_spec = {}

            if "input_schema" in task_spec:
                formatted_task_spec["input_schema"] = {
                    "type": "json",
                    "json_schema": task_spec["input_schema"]
                }

            if "output_schema" in task_spec:
                formatted_task_spec["output_schema"] = {
                    "type": "json",
                    "json_schema": task_spec["output_schema"]
                }

            data["task_spec"] = formatted_task_spec

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()

            result = response.json()
            run_id = result.get("run_id")
            status = result.get("status")

            print(f"✅ Task run created successfully!")
            print(f"   Run ID: {run_id}")
            print(f"   Status: {status}")
            print()

            return run_id

        except requests.exceptions.RequestException as e:
            print(f"❌ Error creating task run: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"   Response: {e.response.text}")
            return None

    def get_task_result(self, run_id: str, max_attempts: int = 30, wait_time: int = 10) -> Optional[Dict[str, Any]]:
        """Step 4: Get task results (with polling)"""
        print(f"📊 Step 4: Retrieving results for run {run_id}")

        url = f"{self.base_url}/v1/tasks/runs/{run_id}/result"
        headers = {"x-api-key": self.api_key}  # No Content-Type needed for GET

        for attempt in range(max_attempts):
            try:
                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    result = response.json()
                    status = result.get("run", {}).get("status")

                    if status == "completed":
                        print("✅ Task completed successfully!")
                        output = result.get("output", {})
                        print(f"   Content: {output.get('content', 'N/A')}")

                        # Show citations if available
                        citations = output.get("citations", [])
                        if citations:
                            print(f"   Citations: {len(citations)} sources")
                            for i, citation in enumerate(citations[:3], 1):  # Show first 3
                                print(f"     {i}. {citation}")

                        return result

                    elif status == "failed":
                        print("❌ Task failed!")
                        return result

                    else:
                        print(f"⏳ Task still {status}... (attempt {attempt + 1}/{max_attempts})")
                        time.sleep(wait_time)

                elif response.status_code == 404:
                    print(f"❌ Task run not found: {run_id}")
                    return None

                else:
                    response.raise_for_status()

            except requests.exceptions.RequestException as e:
                print(f"❌ Error getting task result: {e}")
                if hasattr(e, 'response') and e.response is not None:
                    print(f"   Response: {e.response.text}")
                return None

        print(f"⏰ Task did not complete within {max_attempts * wait_time} seconds")
        return None

    def run_end_to_end_test(self, user_intent: str, sample_input: Any):
        """Run the complete end-to-end test"""
        print("=" * 60)
        print("🧪 PARALLEL INGEST API - END-TO-END TEST")
        print("=" * 60)
        print()

        # Step 1: Suggest task
        task_suggestion = self.suggest_task(user_intent)
        if not task_suggestion:
            print("❌ Test failed at task suggestion step")
            return

        # Step 2: Suggest processor
        processor_suggestion = self.suggest_processor(task_suggestion)
        if not processor_suggestion:
            print("❌ Test failed at processor suggestion step")
            return

        # Step 3: Create task run
        selected_processor = processor_suggestion.get('selected_processor', 'core')
        run_id = self.create_task_run(
            input_data=sample_input,
            processor=selected_processor,
            task_spec=task_suggestion  # Use original task suggestion, not processor suggestion
        )
        if not run_id:
            print("❌ Test failed at task creation step")
            return

        # Step 4: Get results
        result = self.get_task_result(run_id)
        if result:
            print("🎉 End-to-end test completed successfully!")
        else:
            print("❌ Test failed at result retrieval step")

def main():
    """Main function to run the test"""

    # Check API key
    if API_KEY == "PARALLEL_API_KEY":
        print("⚠️  Please set your PARALLEL_API_KEY environment variable or update the script")
        print("   Example: export PARALLEL_API_KEY=your_actual_api_key")
        return

    # Initialize tester
    tester = IngestAPITester(API_KEY, BASE_URL)

    # Test configuration
    user_intent = "Given company_name and company_website, find the CEO information for technology companies"

    # Use object input that matches the expected schema
    sample_input = {
        "company_name": "Google",
        "company_website": "https://www.google.com"
    }

    # Run the test
    tester.run_end_to_end_test(user_intent, sample_input)

if __name__ == "__main__":
    main()
```

See all 268 lines

Running the Example

Copy

Ask AI

```
PARALLEL_API_KEY="PARALLEL_API_KEY" python3 ingest_script.py
```

This example demonstrates the complete workflow:

1. **Suggest Task**: Generate a task specification from natural language intent
2. **Suggest Processor**: Get processor recommendations and enhanced schemas
3. **Create Task Run**: Submit the task for processing with proper schema formatting
4. **Get Results**: Poll for completion and retrieve the final results

The script includes proper error handling, status polling, and demonstrates the correct format for task specifications required by the API.

[Task Group](https://docs.parallel.ai/task-api/group-api) [Streaming Events](https://docs.parallel.ai/task-api/task-sse)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Extract - Parallel

**URL:** https://docs.parallel.ai/api-reference/extract-beta/extract

[Skip to main content](https://docs.parallel.ai/api-reference/extract-beta/extract#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Extract (Beta)

Extract

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

extract = client.beta.extract(
    urls=["https://www.example.com"],
    excerpts=True,
    full_content=True
)
print(extract.results)
```

200

422

Copy

Ask AI

```
{
  "extract_id": "extract_8a911eb27c7a4afaa20d0d9dc98d07c0",
  "results": [\
    {\
      "url": "https://www.example.com",\
      "title": "Example Title",\
      "excerpts": [\
        "Excerpted text ..."\
      ],\
      "full_content": "Full content ..."\
    }\
  ],
  "errors": [\
    {\
      "url": "https://www.example.com",\
      "error_type": "fetch_error",\
      "http_status_code": 500,\
      "content": "Error fetching content from https://www.example.com"\
    }\
  ]
}
```

POST

/

v1beta

/

extract

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

extract = client.beta.extract(
    urls=["https://www.example.com"],
    excerpts=True,
    full_content=True
)
print(extract.results)
```

200

422

Copy

Ask AI

```
{
  "extract_id": "extract_8a911eb27c7a4afaa20d0d9dc98d07c0",
  "results": [\
    {\
      "url": "https://www.example.com",\
      "title": "Example Title",\
      "excerpts": [\
        "Excerpted text ..."\
      ],\
      "full_content": "Full content ..."\
    }\
  ],
  "errors": [\
    {\
      "url": "https://www.example.com",\
      "error_type": "fetch_error",\
      "http_status_code": 500,\
      "content": "Error fetching content from https://www.example.com"\
    }\
  ]
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#parameter-parallel-beta)

parallel-beta

string

default:search-extract-2025-10-10

#### Body

application/json

Extract request.

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#body-urls)

urls

string\[\]

required

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#body-objective-one-of-0)

objective

string \| null

If provided, focuses extracted content on the specified search objective.

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#body-search-queries-one-of-0)

search\_queries

string\[\] \| null

If provided, focuses extracted content on the specified keyword search queries.

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#body-fetch-policy-one-of-0)

fetch\_policy

FetchPolicy · object

Fetch policy: determines when to return cached content from the index (faster) vs fetching live content (fresher). Default is to use a dynamic policy based on the search objective and url.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#body-excerpts-one-of-0)

excerpts

booleanExcerptSettings · objectbooleanExcerptSettings · object

default:true

Include excerpts from each URL relevant to the search objective and queries. Note that if neither objective nor search\_queries is provided, excerpts are redundant with full content.

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#body-full-content-one-of-0)

full\_content

booleanFullContentSettings · objectbooleanFullContentSettings · object

default:false

Include full content from each URL. Note that if neither objective nor search\_queries is provided, excerpts are redundant with full content.

#### Response

200

application/json

Successful Response

Fetch result.

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#response-extract-id)

extract\_id

string

required

Extract request ID, e.g. `extract_cad0a6d2dec046bd95ae900527d880e7`

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#response-results)

results

ExtractResult · object\[\]

required

Successful extract results.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#response-errors)

errors

ExtractError · object\[\]

required

Extract errors: requested URLs not in the results.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#response-warnings-one-of-0)

warnings

Warning · object\[\] \| null

Warnings for the extract request, if any.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/extract-beta/extract#response-usage-one-of-0)

usage

UsageItem · object\[\] \| null

Usage metrics for the extract request.

Showchild attributes

[Chat Completions](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Search](https://docs.parallel.ai/api-reference/search-beta/search)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Polars - Parallel

**URL:** https://docs.parallel.ai/data-integrations/polars

[Skip to main content](https://docs.parallel.ai/data-integrations/polars#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Data Integrations

Polars

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features](https://docs.parallel.ai/data-integrations/polars#features)
- [Installation](https://docs.parallel.ai/data-integrations/polars#installation)
- [Basic Usage](https://docs.parallel.ai/data-integrations/polars#basic-usage)
- [Function Parameters](https://docs.parallel.ai/data-integrations/polars#function-parameters)
- [Return Value](https://docs.parallel.ai/data-integrations/polars#return-value)
- [Column Name Mapping](https://docs.parallel.ai/data-integrations/polars#column-name-mapping)
- [LazyFrame Support](https://docs.parallel.ai/data-integrations/polars#lazyframe-support)
- [Including Citations](https://docs.parallel.ai/data-integrations/polars#including-citations)
- [Processor Selection](https://docs.parallel.ai/data-integrations/polars#processor-selection)
- [Best Practices](https://docs.parallel.ai/data-integrations/polars#best-practices)

This integration is ideal for data scientists and engineers who work with Polars DataFrames and need to enrich data with web intelligence directly in their Python workflows.Parallel provides a native Polars integration that enables DataFrame-native data enrichment with batch processing for efficiency.

View the complete demo notebook:

- [Polars Enrichment Demo](https://github.com/parallel-web/parallel-web-tools/blob/main/notebooks/polars_enrichment_demo.ipynb)

## [​](https://docs.parallel.ai/data-integrations/polars\#features)  Features

- **DataFrame-Native**: Enriched columns added directly to your Polars DataFrame
- **Batch Processing**: All rows processed in a single API call for efficiency
- **LazyFrame Support**: Works with both eager and lazy DataFrames
- **Partial Results**: Failed rows return `None` without stopping the entire batch

## [​](https://docs.parallel.ai/data-integrations/polars\#installation)  Installation

Copy

Ask AI

```
pip install parallel-web-tools[polars]
```

Or with all dependencies:

Copy

Ask AI

```
pip install parallel-web-tools[all]
```

## [​](https://docs.parallel.ai/data-integrations/polars\#basic-usage)  Basic Usage

Copy

Ask AI

```
import polars as pl
from parallel_web_tools.integrations.polars import parallel_enrich

# Create a DataFrame
df = pl.DataFrame({
    "company": ["Google", "Microsoft", "Apple"],
    "website": ["google.com", "microsoft.com", "apple.com"],
})

# Enrich with company information
result = parallel_enrich(
    df,
    input_columns={
        "company_name": "company",
        "website": "website",
    },
    output_columns=[\
        "CEO name",\
        "Founding year",\
        "Headquarters city",\
    ],
)

# Read from CSV lazily
lf = pl.scan_csv("companies.csv")

# Filter and select
lf = lf.filter(pl.col("active") == True).select(["name", "website"])

# Enrich (will collect the LazyFrame)
result = parallel_enrich_lazy(
    lf,
    input_columns={"company_name": "name", "website": "website"},
    output_columns=["CEO name"],
)
```

## [​](https://docs.parallel.ai/data-integrations/polars\#including-citations)  Including Citations

Copy

Ask AI

```
result = parallel_enrich(
    df,
    input_columns={"company_name": "company"},
    output_columns=["CEO name"],
    include_basis=True,
)

# Filter successful rows
successful_df = result.result.filter(pl.col("ceo_name").is_not_null())
```

Batch large datasets

For very large datasets (1000+ rows), consider processing in batches:

Copy

Ask AI

```
def enrich_in_batches(df: pl.DataFrame, batch_size: int = 100):
    results = []
    for i in range(0, len(df), batch_size):
        batch = df.slice(i, batch_size)
        result = parallel_enrich(batch, ...)
        results.append(result.result)
    return pl.concat(results)
```

Cost management

- Use `lite-fast` for high-volume, basic enrichments
- Test with small batches before processing large DataFrames
- Store results to avoid re-enriching the same data

[Google BigQuery](https://docs.parallel.ai/data-integrations/bigquery) [Snowflake](https://docs.parallel.ai/data-integrations/snowflake)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Migration Guide - Parallel

**URL:** https://docs.parallel.ai/search/search-migration-guide

[Skip to main content](https://docs.parallel.ai/search/search-migration-guide#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Version Migration Guides

Migration Guide

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [What’s New](https://docs.parallel.ai/search/search-migration-guide#what%E2%80%99s-new)
- [Overview of Changes](https://docs.parallel.ai/search/search-migration-guide#overview-of-changes)
- [Migration Example](https://docs.parallel.ai/search/search-migration-guide#migration-example)
- [Before (Alpha)](https://docs.parallel.ai/search/search-migration-guide#before-alpha)
- [After (Beta)](https://docs.parallel.ai/search/search-migration-guide#after-beta)
- [Additional Resources](https://docs.parallel.ai/search/search-migration-guide#additional-resources)

This guide helps you migrate from the Alpha Search API to the new Beta version.

Both the Alpha and Beta APIs continue to be supported. Using the Alpha API will result in warnings and no breaking errors in production. We will deprecate the Alpha API in December 2025.

## [​](https://docs.parallel.ai/search/search-migration-guide\#what%E2%80%99s-new)  What’s New

1. **No more processors** \- The Beta API removes the `base` and `pro` processor selection. The API now automatically optimizes search execution.
2. **Optional mode parameter** \- Use `mode` to optimize results for your use case: `one-shot` (default, comprehensive results) or `agentic` (concise, token-efficient for multi-step workflows).
3. **Content freshness control** \- New `fetch_policy` parameter lets you control whether to use cached or fresh content.
4. **MCP integration** \- The Search API is now available through the [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) for seamless integration with AI tools.
5. **Enhanced SDK support** \- Full TypeScript and Python SDK support with better developer experience.

## [​](https://docs.parallel.ai/search/search-migration-guide\#overview-of-changes)  Overview of Changes

| Component | Alpha | Beta |
| --- | --- | --- |
| **Endpoint** | `/alpha/search` | `/v1beta/search` |
| **Beta Header** | Not required | `parallel-beta: search-extract-2025-10-10` (required) |
| **Processor** | `processor: "base"` or `"pro"` (required) | **Removed** |
| **Mode** | Not available | `mode: "one-shot"` or “fast”\` |
| **Excerpt Config** | `max_chars_per_result: 1500` | `excerpts: { max_chars_per_result: 10000 }` |
| **Freshness Control** | Not available | `fetch_policy: { max_age_seconds: 3600 }` (optional) |
| **SDK Method** | N/A | `client.beta.search()` |

## [​](https://docs.parallel.ai/search/search-migration-guide\#migration-example)  Migration Example

### [​](https://docs.parallel.ai/search/search-migration-guide\#before-alpha)  Before (Alpha)

cURL

Python

Copy

Ask AI

```
curl --request POST \
  --url https://api.parallel.ai/alpha/search \
  --header "Content-Type: application/json" \
  --header "x-api-key: $PARALLEL_API_KEY" \
  --data '{
    "objective": "When was the United Nations established?",
    "search_queries": ["Founding year UN"],
    "processor": "base",
    "max_chars_per_result": 1500
  }'
```

### [​](https://docs.parallel.ai/search/search-migration-guide\#after-beta)  After (Beta)

cURL

Python

TypeScript

Copy

Ask AI

```
curl https://api.parallel.ai/v1beta/search \
  -H "Content-Type: application/json" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: search-extract-2025-10-10" \
  -d '{
    "objective": "When was the United Nations established?",
    "search_queries": ["Founding year UN"],
    "mode": "fast",
    "excerpts": {
      "max_chars_per_result": 10000
    }
  }'
```

## [​](https://docs.parallel.ai/search/search-migration-guide\#additional-resources)  Additional Resources

- [Search Quickstart](https://docs.parallel.ai/search/search-quickstart) \- Get started with the Beta API
- [Best Practices](https://docs.parallel.ai/search/best-practices) \- Optimize your search requests
- [Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) \- Use Search via Model Context Protocol
- [API Reference](https://docs.parallel.ai/api-reference/search-beta/search) \- Complete parameter specifications

Questions? Contact [support@parallel.ai](mailto:support@parallel.ai).

[Webhook Setup](https://docs.parallel.ai/resources/webhook-setup) [FindAll Migration Guide](https://docs.parallel.ai/findall-api/findall-migration-guide)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Monitor API Quickstart - Parallel

**URL:** https://docs.parallel.ai/monitor-api/monitor-quickstart

[Skip to main content](https://docs.parallel.ai/monitor-api/monitor-quickstart#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Monitor

Monitor API Quickstart

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Features and Use Cases](https://docs.parallel.ai/monitor-api/monitor-quickstart#features-and-use-cases)
- [Getting Started](https://docs.parallel.ai/monitor-api/monitor-quickstart#getting-started)
- [Prerequisites](https://docs.parallel.ai/monitor-api/monitor-quickstart#prerequisites)
- [Step 1. Create a monitor](https://docs.parallel.ai/monitor-api/monitor-quickstart#step-1-create-a-monitor)
- [Step 2. Detecting and retrieving events via webhooks](https://docs.parallel.ai/monitor-api/monitor-quickstart#step-2-detecting-and-retrieving-events-via-webhooks)
- [Lifecycle](https://docs.parallel.ai/monitor-api/monitor-quickstart#lifecycle)
- [Best Practices](https://docs.parallel.ai/monitor-api/monitor-quickstart#best-practices)
- [Event Tracking](https://docs.parallel.ai/monitor-api/monitor-quickstart#event-tracking)
- [Change Tracking](https://docs.parallel.ai/monitor-api/monitor-quickstart#change-tracking)
- [Writing Effective Queries](https://docs.parallel.ai/monitor-api/monitor-quickstart#writing-effective-queries)
- [Next Steps](https://docs.parallel.ai/monitor-api/monitor-quickstart#next-steps)
- [Rate Limits](https://docs.parallel.ai/monitor-api/monitor-quickstart#rate-limits)

The Monitor API lets you continuously track the web for changes relevant to a query, on a schedule you control. Create a monitor with a natural-language query, choose a frequency, and receive webhook notifications.

**Alpha Notice**: The Monitor API is currently in public alpha. Endpoints and
request/response formats are subject to change.

## [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#features-and-use-cases)  Features and Use Cases

The Monitor API can be used to automate continuous research for any topic, including companies, products, or regulatory areas— without building complicated web monitoring infrastructure. Define a query once along with the desired schedule, and the service will detect relevant changes and deliver concise updates (with source links) to your systems via webhooks.

- **News tracking**: Alert when there’s notable news about a company or product you’re interested in
- **Competitive monitoring**: Detect when competitors launch new features or pricing changes
- **Regulatory updates**: Track new rules or guidance impacting your industry
- **Deal/research watchlists**: Surface events about entities you care about
- **Tracking products**: Track modifications to a product listing

Monitor currently supports the following features:

- **Scheduling**: Set update frequency (e.g., `"1h"`, `"1d"`, `"1w"`) between 1 hour and 30 days
- **Webhooks**: Receive updates when events are detected or when monitors finish a scheduled run
- **Events history**: Retrieve updates from recent runs or via a lookback window (e.g., `10d`)
- **Lifecycle management**: Update frequency, webhook, or metadata; delete to stop future runs

## [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#getting-started)  Getting Started

### [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#prerequisites)  Prerequisites

Generate your API key on [Platform](https://platform.parallel.ai/). Then, set up with the Python SDK, TypeScript SDK, or cURL:

cURL

Python

TypeScript

Copy

Ask AI

```
echo "Install curl and jq via brew, apt, or your favorite package manager"
export PARALLEL_API_KEY="PARALLEL_API_KEY"
```

**Python SDK**: The Monitor API uses low-level `client.post()` and `client.get()` methods in Python because high-level convenience methods are not yet available. The examples below show this pattern.

### [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#step-1-create-a-monitor)  Step 1. Create a monitor

Create a monitor that gathers daily AI news:**Request:**

cURL

Python

TypeScript

Copy

Ask AI

```
curl --request POST \
  --url https://api.parallel.ai/v1alpha/monitors \
  --header 'Content-Type: application/json' \
  --header "x-api-key: $PARALLEL_API_KEY" \
  --data '{
    "query": "Extract recent news about quantum in AI",
        "frequency": "1d",
    "webhook": {
      "url": "https://example.com/webhook",
      "event_types": ["monitor.event.detected"]
    },
    "metadata": { "key": "value" }
  }'
```

**Response:**

Copy

Ask AI

```
{
  "monitor_id": "monitor_b0079f70195e4258a3b982c1b6d8bd3a",
  "query": "Extract recent news about AI",
  "status": "active",
  "frequency": "1d",
  "metadata": { "key": "value" },
  "webhook": {
    "url": "https://example.com/webhook",
    "event_types": ["monitor.event.detected"]
  },
  "created_at": "2025-04-23T20:21:48.037943Z"
}
```

### [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#step-2-detecting-and-retrieving-events-via-webhooks)  Step 2. Detecting and retrieving events via webhooks

When a change is detected, your webhook receives:

Copy

Ask AI

```
{
  "type": "monitor.event.detected",
  "timestamp": "2025-12-10T19:00:36.199543+00:00",
  "data": {
    "event": {
      "event_group_id": "mevtgrp_35ab7d16b00f412b9d6b6c0eff1f49733b5cf0b02056a29c"
    },
    "metadata": { "key": "value" },
    "monitor_id": "monitor_35ab7d16b00f412bbc4d6accbe0fdb41"
  }
}
```

- Use `data.event.event_group_id` with the GET endpoint in Step 2 to fetch the full events.
- `data.monitor_id` tells you which monitor fired.
- `data.metadata` echoes what you set at creation, so you can route the webhook (e.g., to a Slack thread or ticket).

After you receive a webhook with an `event_group_id` (for a detected change),
fetch the full set of related events for that group:**Request:**

cURL

Python

TypeScript

Copy

Ask AI

```
curl --request GET \
  --url "https://api.parallel.ai/v1alpha/monitors/${MONITOR_ID}/event_groups/${EVENT_GROUP_ID}" \
  --header "x-api-key: $PARALLEL_API_KEY"
```

**Response:**

Copy

Ask AI

```
{
  "events": [\
    {\
      "type": "event",\
      "event_group_id": "mevtgrp_b0079f70195e4258eab1e7284340f1a9ec3a8033ed236a24",\
      "output": "New product launch announced",\
      "event_date": "2025-01-15",\
      "source_urls": ["https://example.com/news"]\
    }\
  ]
}
```

To learn about the full event model, alternative ways to access events
(including listing all events), and best practices, see the [Events](https://docs.parallel.ai/monitor-api/monitor-events) page.

## [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#lifecycle)  Lifecycle

The Monitor API follows a straightforward lifecycle:

1. **Create**: Define your `query`, `frequency`, and optional `webhook` and `metadata`.
2. **Update**: Change frequency, webhook, or metadata.
3. **Delete**: Delete a monitor and stop future executions.

At any point, you can retrieve the list of events for a monitor or events within a specific
event group.

See [Pricing](https://docs.parallel.ai/getting-started/pricing) for a detailed schedule of rates.

## [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#best-practices)  Best Practices

1. **Scope your query**: Clear queries with explicit instructions lead to higher-quality event detection.
2. **Choose the right frequency**: Use `"1h"` for fast-moving topics, `"1d"` for most news,
`"1w"` for slower changes.
3. **Use webhooks**: Prefer webhooks to avoid unnecessary polling and reduce latency to updates.
4. **Manage lifecycle**: Cancel monitors you no longer need to reduce your usage bills.

Monitor is a versatile, general-purpose tool for tracking the web. It works best when you write queries in natural language that declare your intent.

### [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#event-tracking)  Event Tracking

Use Monitor to track when something happens on the web:

| Use Case | Example Query |
| --- | --- |
| Brand mentions | ”Let me know when someone mentions Parallel Web Systems on the web” |
| News tracking | ”What is the latest AI funding news?” |
| Product announcements | ”Alert me when Apple announces new MacBook models” |
| Regulatory updates | ”Notify me of any new FDA guidance on AI in medical devices” |

### [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#change-tracking)  Change Tracking

Use Monitor to detect when something changes:

| Use Case | Example Query |
| --- | --- |
| Price monitoring | ”Let me know when the price for AirPods drops below $150” |
| Stock availability | ”Alert me when the PS5 Pro is back in stock at Best Buy” |
| Content updates | ”Notify me when the React documentation is updated” |
| Policy changes | ”Track changes to OpenAI’s terms of service” |

### [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#writing-effective-queries)  Writing Effective Queries

Monitor works best with natural language queries that clearly describe what you’re looking for.

| ❌ Bad Query | ✅ Good Query |
| --- | --- |
| ”Parallel OR Parallel Web Systems OR Parallel AI AND Funding OR Launch OR Announcement" | "Parallel Web Systems (parallel.ai) launch or funding updates” |

Unlike a search engine, the query doesn’t need to be keyword-heavy—it needs to be intent-heavy.**Don’t use for historical research**: Monitor is designed to track _new_ updates as they happen, not to retrieve past news. Use [Deep Research](https://docs.parallel.ai/task-api/task-deep-research) for historical queries.

| ❌ Bad Query | ✅ Good Query |
| --- | --- |
| ”Find all AI funding news from the last 2 years" | "AI startup funding announcements” |

**Don’t include dates**: Monitor automatically tracks updates from when it’s created. Adding specific dates to your query is unnecessary and can cause confusion.

| ❌ Bad Query | ✅ Good Query |
| --- | --- |
| ”Tesla news after December 12, 2025" | "Tesla news and announcements” |

Natural language queries help Monitor understand the context and intent behind your request, leading to more relevant and accurate event detection.

## [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#next-steps)  Next Steps

- **[Events](https://docs.parallel.ai/monitor-api/monitor-events)**: Understand events, when they are emitted and how to access them.
- **[Webhooks](https://docs.parallel.ai/monitor-api/monitor-webhooks)**: Information on setting up webhooks and listening for push notifications.
- **[API Reference](https://docs.parallel.ai/api-reference/monitor/create-monitor)**: Complete endpoint documentation

## [​](https://docs.parallel.ai/monitor-api/monitor-quickstart\#rate-limits)  Rate Limits

See [Rate Limits](https://docs.parallel.ai/getting-started/rate-limits) for default quotas and how to request higher limits.

[Refresh Runs](https://docs.parallel.ai/findall-api/features/findall-refresh) [Structured Outputs](https://docs.parallel.ai/monitor-api/monitor-structured-outputs)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Pricing - Parallel

**URL:** https://docs.parallel.ai/getting-started/pricing

[Skip to main content](https://docs.parallel.ai/getting-started/pricing#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Getting started

Pricing

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Summary](https://docs.parallel.ai/getting-started/pricing#summary)
- [Web Tools](https://docs.parallel.ai/getting-started/pricing#web-tools)
- [Search API](https://docs.parallel.ai/getting-started/pricing#search-api)
- [Extract API](https://docs.parallel.ai/getting-started/pricing#extract-api)
- [Web Agents](https://docs.parallel.ai/getting-started/pricing#web-agents)
- [Chat API](https://docs.parallel.ai/getting-started/pricing#chat-api)
- [Task API](https://docs.parallel.ai/getting-started/pricing#task-api)
- [FindAll API](https://docs.parallel.ai/getting-started/pricing#findall-api)
- [Monitor API](https://docs.parallel.ai/getting-started/pricing#monitor-api)

## [​](https://docs.parallel.ai/getting-started/pricing\#summary)  Summary

| API | Price | Use case | Reasoning | Type | Latency |
| --- | --- | --- | --- | --- | --- |
| Search | $ | Page and excerpt retrieval | - | Synchronous | 1-3s |
| Extract | $ | Page content retrieval | - | Synchronous | 1-20s |
| Chat | $ | Grounded chat completions | Low | Synchronous | 1-3s |
| Task | $-$$$$ | Deep research, enrichment, custom research | Low-High | Asynchronous | 10s - 2hr |
| FindAll | $-$$$$ | List / database building | Low-High | Asynchronous | 10s - 2hr |
| Monitor | $ | Always-on web monitoring | Low | Asynchronous | Ambient |

## [​](https://docs.parallel.ai/getting-started/pricing\#web-tools)  Web Tools

### [​](https://docs.parallel.ai/getting-started/pricing\#search-api)  Search API

By default, the Search API returns 10 page results and their excerpts per request.

| Component | Cost ($/1000) |
| --- | --- |
| Per 1,000 requests (default 10 results) | 5 |
| Per 1,000 additional page results & excerpts | 1 |

**Cost formula:**total cost=0.005+(0.001×additional results & excerpts)\\text{total cost} = 0.005 + (0.001 \\times \\text{additional results \\& excerpts})total cost=0.005+(0.001×additional results & excerpts)

### [​](https://docs.parallel.ai/getting-started/pricing\#extract-api)  Extract API

| Component | Cost ($/1000) |
| --- | --- |
| Per 1,000 URLs | 1 |

## [​](https://docs.parallel.ai/getting-started/pricing\#web-agents)  Web Agents

### [​](https://docs.parallel.ai/getting-started/pricing\#chat-api)  Chat API

Chat API pricing is based on the model you select.

| Model | Type | Cost ($/1000) |
| --- | --- | --- |
| `speed` | Simple completions | 5 |
| `lite` | Research | 5 |
| `base` | Research | 10 |
| `core` | Research | 25 |

### [​](https://docs.parallel.ai/getting-started/pricing\#task-api)  Task API

Task API pricing is based on the [processor](https://docs.parallel.ai/task-api/guides/choose-a-processor) you select. Cost is per 1,000 Task Runs. Fast processors have the same pricing as their standard counterparts.

- Standard

- Fast

| Processor | Cost ($/1000) | Latency | Strengths |
| --- | --- | --- | --- |
| `lite` | 5 | 10s - 60s | Basic metadata, fallback, low latency |
| `base` | 10 | 15s - 100s | Reliable standard enrichments |
| `core` | 25 | 60s - 5min | Cross-referenced, moderately complex outputs |
| `core2x` | 50 | 60s - 10min | High complexity cross referenced outputs |
| `pro` | 100 | 2min - 10min | Exploratory web research |
| `ultra` | 300 | 5min - 25min | Advanced multi-source deep research |
| `ultra2x` | 600 | 5min - 50min | Difficult deep research |
| `ultra4x` | 1200 | 5min - 90min | Very difficult deep research |
| `ultra8x` | 2400 | 5min - 2hr | The most difficult deep research |

| Processor | Cost ($/1000) | Latency | Strengths |
| --- | --- | --- | --- |
| `lite-fast` | 5 | 10s - 20s | Basic metadata, fallback, lowest latency |
| `base-fast` | 10 | 15s - 50s | Reliable standard enrichments |
| `core-fast` | 25 | 15s - 100s | Cross-referenced, moderately complex outputs |
| `core2x-fast` | 50 | 15s - 3min | High complexity cross referenced outputs |
| `pro-fast` | 100 | 30s - 5min | Exploratory web research |
| `ultra-fast` | 300 | 1min - 10min | Advanced multi-source deep research |
| `ultra2x-fast` | 600 | 1min - 20min | Difficult deep research |
| `ultra4x-fast` | 1200 | 1min - 40min | Very difficult deep research |
| `ultra8x-fast` | 2400 | 1min - 1hr | The most difficult deep research |

Pricing is per Task Run (row), not per output field (cell). A single Task Run can populate many output fields—whether you request 1 field or 20 fields, the cost is the same.

### [​](https://docs.parallel.ai/getting-started/pricing\#findall-api)  FindAll API

FindAll API pricing is based on the [generator](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing) you select, with a fixed cost plus a per-match cost.

| Generator | Fixed Cost | Per Match | Best For |
| --- | --- | --- | --- |
| `preview` | $0.10 | $0.00 | Testing queries (~10 candidates) |
| `base` | $0.25 | $0.03 | Broad, common queries where you expect many matches |
| `core` | $2.00 | $0.15 | Specific queries with moderate expected matches |
| `pro` | $10.00 | $1.00 | Highly specific queries with rare or hard-to-find matches |

**Cost formula:**total cost=fixed cost+(cost per match×# matches)\\text{total cost} = \\text{fixed cost} + (\\text{cost per match} \\times \\text{\\# matches})total cost=fixed cost+(cost per match×# matches)If you add [enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich), each enrichment adds its own per-match cost based on the Task API processor you choose (see Task API pricing above).

### [​](https://docs.parallel.ai/getting-started/pricing\#monitor-api)  Monitor API

Monitor requests are priced on a per thousand (CPM) basis for each execution. Execution frequency is defined by the `frequency` parameter of your monitors (e.g., `"1h"`, `"1d"`, `"1w"`).

| Component | Cost ($/1000) |
| --- | --- |
| Per 1,000 requests per frequency | 3 |

**Cost formula:**total cost=0.003×number of executions\\text{total cost} = 0.003 \\times \\text{number of executions}total cost=0.003×number of executions

[Overview](https://docs.parallel.ai/getting-started/overview) [Rate limits](https://docs.parallel.ai/getting-started/rate-limits)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Initialize clients
openai_client = OpenAI()
parallel_client = Parallel(api_key=os.environ["PARALLEL_API_KEY"])

# Tool definition
parallel_search_tool = {
    "type": "function",
    "function": {
        "name": "parallel_search",
        "description": "Search the web for current information using Parallel's AI-powered search. Provide at least one of objective or search_queries.",
        "parameters": {
            "type": "object",
            "properties": {
                "objective": {
                    "type": "string",
                    "description": "A natural language description of what you're searching for."
                },
                "search_queries": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Specific search queries to execute."
                },
                "max_chars_total": {
                    "type": "integer",
                    "description": "Maximum total characters across all excerpts. Default 50000."
                }
            }
        }
    }
}

def parallel_search(objective=None, search_queries=None, max_chars_total=50000):
    response = parallel_client.beta.search(
        objective=objective,
        search_queries=search_queries,
        mode="fast",
        excerpts={"max_chars_per_result": 5000, "max_chars_total": max_chars_total}
    )
    return {
        "results": [\
            {"url": r.url, "title": r.title, "excerpts": r.excerpts[:3] if r.excerpts else []}\
            for r in response.results\
        ]
    }

def chat_with_search(user_message: str) -> str:
    messages = [\
        {\
            "role": "system",\
            "content": "You are a helpful research assistant. Use the parallel_search tool to find current information. Always cite sources with URLs."\
        },\
        {"role": "user", "content": user_message}\
    ]

    # First API call - may trigger tool use
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=[parallel_search_tool],
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    # Check if the model wants to use tools
    if assistant_message.tool_calls:
        messages.append(assistant_message)

        # Process each tool call
        for tool_call in assistant_message.tool_calls:
            if tool_call.function.name == "parallel_search":
                args = json.loads(tool_call.function.arguments)
                result = parallel_search(
                    objective=args.get("objective"),
                    search_queries=args.get("search_queries"),
                    max_chars_total=args.get("max_chars_total", 50000)
                )
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })

        # Second API call with search results
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=[parallel_search_tool],
            tool_choice="auto"
        )

    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    answer = chat_with_search("What are the latest developments in quantum computing?")
    print(answer)
```

## [​](https://docs.parallel.ai/integrations/openai-tool-calling\#tool-parameters)  Tool Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `objective` | string | No\* | Natural language description of your search goal |
| `search_queries` | string\[\] | No\* | Specific search queries to execute |
| `max_chars_total` | integer | No | Maximum total characters across all excerpts (default 50000) |

\*At least one of `objective` or `search_queries` is required.

This example sets `mode` explicitly to `"fast"` in the Search call for predictable low-latency tool responses.

## [​](https://docs.parallel.ai/integrations/openai-tool-calling\#related-resources)  Related Resources

- [Search API Quickstart](https://docs.parallel.ai/search/search-quickstart)
- [Search Best Practices](https://docs.parallel.ai/search/best-practices)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)

[OAuth Provider](https://docs.parallel.ai/integrations/oauth-provider) [Superhuman](https://docs.parallel.ai/integrations/superhuman)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Rate limits - Parallel

**URL:** https://docs.parallel.ai/getting-started/rate-limits

[Skip to main content](https://docs.parallel.ai/getting-started/rate-limits#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Getting started

Rate limits

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Pricing](https://docs.parallel.ai/getting-started/rate-limits#pricing)
- [Need higher limits?](https://docs.parallel.ai/getting-started/rate-limits#need-higher-limits)

The following table shows the default rate limits for each Parallel API product:

| Product | Default Quota | What Counts as a Request |
| --- | --- | --- |
| Search | 600 per min | Each POST to `/v1beta/search` |
| Extract | 600 per min | Each POST to `/v1beta/extract` |
| Tasks/TaskGroups | 2,000 per min | Each POST to `/v1/tasks/runs` or `/v1beta/tasks/groups/{taskgroup_id}/runs` (creating tasks) |
| Chat | 300 per min | Each POST to `/v1/chat/completions` |
| FindAll | 25 per hour | Each POST to `/v1/findall` (creating a generator) |
| Monitor | 300 per min | Each POST to `/v1/monitors` |

**Rate limits apply to POST requests that create new resources.** GET requests
(retrieving results, checking status) do not count against these limits. For
example, polling a task’s status with `GET /v1/tasks/runs/{run_id}` does not
consume your Tasks rate limit—only creating new tasks does.

## [​](https://docs.parallel.ai/getting-started/rate-limits\#pricing)  Pricing

Rate limits are separate from pricing. For cost information, see [Pricing](https://docs.parallel.ai/getting-started/pricing).

## [​](https://docs.parallel.ai/getting-started/rate-limits\#need-higher-limits)  Need higher limits?

If you need to expand your rate limits, please contact **[support@parallel.ai](mailto:support@parallel.ai)** with your use case and requirements.

[Pricing](https://docs.parallel.ai/getting-started/pricing) [Glossary](https://docs.parallel.ai/getting-started/glossary)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# AWS Marketplace - Parallel

**URL:** https://docs.parallel.ai/integrations/aws-marketplace

[Skip to main content](https://docs.parallel.ai/integrations/aws-marketplace#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

AWS Marketplace

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [How to Sign Up Through AWS Marketplace](https://docs.parallel.ai/integrations/aws-marketplace#how-to-sign-up-through-aws-marketplace)
- [Frequently Asked Questions](https://docs.parallel.ai/integrations/aws-marketplace#frequently-asked-questions)

Parallel’s APIs are available through the [Amazon Web Services (AWS) Marketplace](https://aws.amazon.com/marketplace/pp/prodview-zpw7j3ozjqlb4).
You can use your AWS account to access all of Parallel’s features.
Signing up through AWS allows you to provision resources based on your requirements and pay through your existing AWS billing.

## [​](https://docs.parallel.ai/integrations/aws-marketplace\#how-to-sign-up-through-aws-marketplace)  How to Sign Up Through AWS Marketplace

1. Navigate to [AWS Marketplace](https://us-east-1.console.aws.amazon.com/marketplace/search) and search for
Parallel Web Systems, or go directly to our [product listing](https://aws.amazon.com/marketplace/pp/prodview-zpw7j3ozjqlb4).
2. Click on the product listing, then select `View purchase`.
3. Subscribe to our listing. You can review pricing for different processors
[here](https://docs.parallel.ai/task-api/guides/choose-a-processor).
4. Click `Set up your account`. You will need to create a new organization linked to your AWS account,
even if you’re already part of other organizations. See our
[FAQ](https://docs.parallel.ai/integrations/aws-marketplace#frequently-asked-questions) for more details.
5. After creating your new organization, you can use our products as usual through our API or
platform interface.

Your usage charges will appear in the AWS Billing & Cloud Management dashboard with your other AWS services.

## [​](https://docs.parallel.ai/integrations/aws-marketplace\#frequently-asked-questions)  Frequently Asked Questions

Are there advantages to subscribing through AWS Marketplace?

Yes, AWS Marketplace subscriptions provide billing and procurement benefits,
particularly for organizations with centralized cloud spending or AWS credits.These are primarily financial and operational conveniences—Parallel’s features, support, and performance remain identical.

Can I link my existing Parallel account to AWS Marketplace?

No, accounts created directly through our platform cannot be connected to AWS Marketplace retroactively.

Can I migrate to AWS Marketplace billing later?

To use AWS Marketplace billing in the future, you would need to create a new
Parallel account through the Marketplace.

Do I get the same features regardless of how I sign up?

Yes. Parallel delivers identical platform capabilities to all customers—whether you sign up directly or through AWS Marketplace.
The difference is in billing and commercial arrangements, not technical functionality.

I'm getting an error when trying to create an AWS Marketplace account. What should I do?

AWS account creation typically fails for two reasons:i. Your AWS account is already linked to a Parallel account.ii. Your signup token expired due to a delay between subscribing on AWS Marketplace and completing account setup.You’ll see a specific error message indicating which issue you’re experiencing.For expired tokens, try canceling and recreating your subscription. If problems persist,
[contact support](mailto:support@parallel.ai). For existing account conflicts, check with your organization about
joining their existing Parallel account.

When will usage from my Parallel account reflect in my AWS invoice?

For AWS, usages are aggregated hourly and sent to AWS for metering. For a more granular usage report, you
can use the Usage tab in the settings page in our platform.

[Agent Skills](https://docs.parallel.ai/integrations/agent-skills) [Browser Use](https://docs.parallel.ai/integrations/browseruse)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Run Lifecycle - Parallel

**URL:** https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle

[Skip to main content](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Run Lifecycle

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Run Statuses and Termination Reasons](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle#run-statuses-and-termination-reasons)
- [Status Definitions](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle#status-definitions)
- [Termination Reasons](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle#termination-reasons)
- [Related Topics](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle#related-topics)

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle\#run-statuses-and-termination-reasons)  Run Statuses and Termination Reasons

FindAll runs progress from `queued` → `running` → terminal state (`completed`, `failed`, or `cancelled`).
A run is considered **active** when it has status `queued`, `running` and has active candidate generation, evaluation, and enrichments ongoing.

### [​](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle\#status-definitions)  Status Definitions

| Status | Description | Can Extend? | Can Enrich? |
| --- | --- | --- | --- |
| `queued` | Run is waiting to start processing | N/A | N/A |
| `running` | Run is actively evaluating candidates | ❌ No | ✅ Yes |
| `completed` | Run finished (see termination reasons below) | Depends\* | ✅ Yes |
| `failed` | Run encountered an error | ❌ No | ❌ No |
| `cancelled` | Run was cancelled by user | ❌ No | ❌ No |

\\* See termination reasons below for extendability

### [​](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle\#termination-reasons)  Termination Reasons

When a run reaches a terminal state, it will have one of these termination reasons:

| Termination Reason | Description | Can Extend? |
| --- | --- | --- |
| `match_limit_met` | Successfully found the requested number of matches | ✅ Yes |
| `low_match_rate` | Match rate too low to continue efficiently | ❌ No - try a more powerful generator |
| `candidates_exhausted` | All available candidates have been processed | ❌ No - broaden query |
| `error_occurred` | Run encountered an error and cannot be continued | ❌ No |
| `timeout` | Run timed out and cannot be continued | ❌ No |
| `user_cancelled` | Run was cancelled by the user | ❌ No |

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle\#related-topics)  Related Topics

- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run#response-status)**: Complete endpoint documentation

[Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates) [Preview](https://docs.parallel.ai/findall-api/features/findall-preview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Task Runs Lifecycle - Parallel

**URL:** https://docs.parallel.ai/task-api/guides/execute-task-run

[Skip to main content](https://docs.parallel.ai/task-api/guides/execute-task-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Task Runs Lifecycle

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Task Run States](https://docs.parallel.ai/task-api/guides/execute-task-run#task-run-states)
- [Creating a Task Run](https://docs.parallel.ai/task-api/guides/execute-task-run#creating-a-task-run)
- [Rate Limits](https://docs.parallel.ai/task-api/guides/execute-task-run#rate-limits)
- [Examples](https://docs.parallel.ai/task-api/guides/execute-task-run#examples)
- [Completed Status Example](https://docs.parallel.ai/task-api/guides/execute-task-run#completed-status-example)
- [Failed Status Example](https://docs.parallel.ai/task-api/guides/execute-task-run#failed-status-example)

Task runs are stateful objects, which means that creating a Task Run and retrieving its results are separate calls to the API. Each Task Run is an independent instance that progresses through a series of states from `queued` to `completed`. This asynchronous design enables efficient scaling of web research operations.

### [​](https://docs.parallel.ai/task-api/guides/execute-task-run\#task-run-states)  Task Run States

| Status | Description | Can Transition To |
| --- | --- | --- |
| `queued` | Task created and waiting for processing | `running`, `failed` |
| `running` | Task actively being processed | `completed`, `failed` |
| `completed` | Task successfully completed with results available | (Terminal state) |
| `failed` | Task encountered an error | (Terminal state) |

**Note**: Running time varies by processor type and task complexity.

## [​](https://docs.parallel.ai/task-api/guides/execute-task-run\#creating-a-task-run)  Creating a Task Run

The basic requirements of a task run are:

- Input data (string or JSON object)
- A processor selection
- Output schema (optional but recommended)

Optionally, you can include:

- Input schema (optionally used to validate run input)
- Metadata (for tracking or organizing runs)

A Task Run, once created, can be identified by its `run_id`. A Task Run Result can be accessed once the Task Run status becomes `completed`.

## [​](https://docs.parallel.ai/task-api/guides/execute-task-run\#rate-limits)  Rate Limits

The Task API enforces a limit of **2,000 requests per minute** per API key. This limit applies across all POST and GET requests and helps ensure consistent performance for all users.When you exceed this limit, the API returns a `429 Too Many Requests` status code.

## [​](https://docs.parallel.ai/task-api/guides/execute-task-run\#examples)  Examples

### [​](https://docs.parallel.ai/task-api/guides/execute-task-run\#completed-status-example)  Completed Status Example

Copy

Ask AI

```
{
  "run_id": "b0679f70-195e-4f42-8b8a-b8242a0c69c7",
  "status": "completed",
  "is_active": false,
  "result": {
    "population": "29.5 million (2022 estimate)",
    "growth_rate": "1.4% annually",
    "major_cities": [\
      "Houston",\
      "Dallas",\
      "San Antonio"\
    ]
  },
  "result_url": "https://api.parallel.ai/v1/tasks/runs/b0679f70-195e-4f42-8b8a-b8242a0c69c7/result",
  "warnings": null,
  "errors": null,
  "processor": "core",
  "metadata": null,
  "created_at": "2025-04-08T04:28:59.913464",
  "modified_at": "2025-04-08T04:29:32.651298"
}
```

### [​](https://docs.parallel.ai/task-api/guides/execute-task-run\#failed-status-example)  Failed Status Example

If a Task Run encounters an error, the status will be set to `failed` and details will be available in the `errors` field:

Copy

Ask AI

```
{
  "run_id": "b0679f70-195e-4f42-8b8a-b8242a0c69c7",
  "status": "failed",
  "is_active": false,
  "result": null,
  "result_url": null,
  "warnings": null,
  "errors": [\
    {\
      "code": "processing_error",\
      "message": "Unable to process task due to invalid input format",\
      "details": {\
        "field": "input",\
        "reason": "Expected JSON object but received string"\
      }\
    }\
  ],
  "processor": "core",
  "metadata": null,
  "created_at": "2025-04-08T04:28:59.913464",
  "modified_at": "2025-04-08T04:29:01.234567"
}
```

[Processors](https://docs.parallel.ai/task-api/guides/choose-a-processor) [Research Basis](https://docs.parallel.ai/task-api/guides/access-research-basis)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Step 1: Ingest query
ingest_response = requests.post(
    f"{BASE_URL}/v1beta/findall/ingest",
    headers={"x-api-key": API_KEY},
    json={"query": "Find AI companies that raised Series A in 2024 and get CEO names"}
)
findall_spec = ingest_response.json()

# Step 2: Create run (constraints + enrichments together)
run_response = requests.post(
    f"{BASE_URL}/v1beta/findall/runs",
    headers={"x-api-key": API_KEY},
    json={
        "findall_spec": findall_spec,
        "processor": "core",
        "result_limit": 100
    }
)
findall_id = run_response.json()["findall_id"]

# Step 3: Poll until both flags are false
while True:
    poll_response = requests.get(
        f"{BASE_URL}/v1beta/findall/runs/{findall_id}",
        headers={"x-api-key": API_KEY}
    )
    result = poll_response.json()
    if not result["is_active"] and not result["are_enrichments_active"]:
        break
    time.sleep(15)

# Step 4: Access results from poll response
for entity in result["results"]:
    print(f"{entity['name']}: Score {entity['score']}")

    # Loop through arrays to find values
    for filter_result in entity["filter_results"]:
        print(f"  {filter_result['key']}: {filter_result['value']}")
    for enrichment in entity["enrichment_results"]:
        print(f"  {enrichment['key']}: {enrichment['value']}")
```

See all 46 lines

## [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#migration-checklist)  Migration Checklist

Complete these steps to migrate from V0 to V1:

### [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#core-changes)  Core Changes

- Add `parallel-beta: "findall-2025-09-15"` header to all requests
- Change ingest parameter: `query` → `objective`
- Flatten run request: extract `objective`, `entity_type`, `match_conditions` from `findall_spec`
- Rename: `result_limit` → `match_limit`, `processor` → `generator`
- Update status check: `status.status == "completed"` instead of checking two flags
- Fetch results from separate `/result` endpoint
- Update result parsing: `results` → `candidates`, `score` → `relevance_score`
- Change field access: direct object access (`output[field]`) vs array iteration

### [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#enrichment-changes-if-applicable)  Enrichment Changes (if applicable)

- Move enrichments to separate `POST /enrich` call after run creation
- Convert enrichment columns to `output_schema` format (see [Task API](https://docs.parallel.ai/task-api/guides/specify-a-task#output-schema))
- Update result access: enrichments now merged into `output` object

### [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#optional-enhancements)  Optional Enhancements

- Implement streaming via `/events` endpoint for real-time updates
- Add `exclude_list` to filter out specific candidates
- Use `preview: true` for testing queries before full runs
- Implement `/extend` endpoint to increase match limits dynamically
- Implement `/cancel` endpoint to stop runs early

### [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#testing)  Testing

- Validate queries in development environment
- Review pricing impact with generator-based model
- Update error handling for new response schemas
- Monitor performance metrics

## [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#related-topics)  Related Topics

### [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#core-concepts)  Core Concepts

- **[Quickstart](https://docs.parallel.ai/findall-api/findall-quickstart)**: Get started with V1 FindAll API
- **[Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates)**: Understand candidate object structure and states
- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and termination

### [​](https://docs.parallel.ai/findall-api/findall-migration-guide\#features)  Features

- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Cancel Runs](https://docs.parallel.ai/findall-api/features/findall-cancel)**: Stop runs early to save costs
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches

[Migration Guide](https://docs.parallel.ai/search/search-migration-guide) [Crawler](https://docs.parallel.ai/resources/crawler)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Stream Task Run Events - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks v1

Stream Task Run Events

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

events = client.beta.task_run.events(run_id="run_id")
for event in events:
    print(event)
```

200

401

404

422

Copy

Ask AI

```
{
  "type": "task_run.progress_msg.plan",
  "message": "Planning task...",
  "timestamp": "2025-04-23T20:21:48.037943Z"
}
```

GET

/

v1beta

/

tasks

/

runs

/

{run\_id}

/

events

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

events = client.beta.task_run.events(run_id="run_id")
for event in events:
    print(event)
```

200

401

404

422

Copy

Ask AI

```
{
  "type": "task_run.progress_msg.plan",
  "message": "Planning task...",
  "timestamp": "2025-04-23T20:21:48.037943Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events#parameter-run-id)

run\_id

string

required

#### Response

200

text/event-stream

Successful Response

- TaskRunProgressStatsEvent

- TaskRunProgressMessageEvent

- TaskRunEvent

- ErrorEvent

A progress update for a task run.

[​](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events#response-one-of-0-type)

type

string

required

Event type; always 'task\_run.progress\_stats'.

Allowed value: `"task_run.progress_stats"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events#response-one-of-0-source-stats)

source\_stats

TaskRunSourceStats · object

required

Source stats describing progress so far.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/stream-task-run-events#response-one-of-0-progress-meter)

progress\_meter

number

required

Completion percentage of the task run. Ranges from 0 to 100 where 0 indicates no progress and 100 indicates completion.

[Retrieve Task Run Result](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run-result) [Create Task Group](https://docs.parallel.ai/api-reference/tasks-beta/create-task-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Google Sheets - Parallel

**URL:** https://docs.parallel.ai/integrations/gsuite

[Skip to main content](https://docs.parallel.ai/integrations/gsuite#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Google Sheets

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Prerequisites](https://docs.parallel.ai/integrations/gsuite#prerequisites)
- [Function Reference](https://docs.parallel.ai/integrations/gsuite#function-reference)
- [Usage Patterns](https://docs.parallel.ai/integrations/gsuite#usage-patterns)
- [Basic](https://docs.parallel.ai/integrations/gsuite#basic)
- [Targeted data retrieval](https://docs.parallel.ai/integrations/gsuite#targeted-data-retrieval)
- [Best Practices](https://docs.parallel.ai/integrations/gsuite#best-practices)
- [Viewing Basis](https://docs.parallel.ai/integrations/gsuite#viewing-basis)
- [Caching](https://docs.parallel.ai/integrations/gsuite#caching)
- [Admin Setup](https://docs.parallel.ai/integrations/gsuite#admin-setup)
- [Troubleshooting](https://docs.parallel.ai/integrations/gsuite#troubleshooting)
- [FAQ](https://docs.parallel.ai/integrations/gsuite#faq)

Parallel’s Google Sheets integration brings AI-powered web research and retrieval into your spreadsheets.
Ask a natural‑language question, optionally specify the data to target, and add contextual guidance—all from a single formula.The integration is designed for creating and enriching datasets in Sheets (e.g., enrichment, summaries, classifications, and quick insights).![](https://mintcdn.com/parallel-6fabab31-mtje7p526we/X5tandxFdaxBN_wG/images/sheets_example.png?fit=max&auto=format&n=X5tandxFdaxBN_wG&q=85&s=3499489ecf2b96a82152b1f3cc48ef23)

## [​](https://docs.parallel.ai/integrations/gsuite\#prerequisites)  Prerequisites

- Get a Parallel API key from [Platform](https://platform.parallel.ai/).
- Install the integration on Google Sheets directly from [here](https://workspace.google.com/marketplace/app/parallel_web_systems/528853648934)
or follow these steps:  - Go to `Extensions → Add-Ons → Get add-ons`
  - Search for Parallel
  - Click on the listing from Parallel Web Systems
- In Google Sheets, open `Extensions → Parallel → Open Sidebar → Paste your API Key → Click Save API Key`

**For teams**: Admins can set an org-wide API key using Google Apps Script properties, so individual users
don’t need to configure their own keys. See the [Admin Setup](https://docs.parallel.ai/integrations/gsuite#admin-setup) section below.

## [​](https://docs.parallel.ai/integrations/gsuite\#function-reference)  Function Reference

The integration exposes one function with the following signature:

Copy

Ask AI

```
=PARALLEL_QUERY(query, target_data, context)
```

It returns an answer to a query, with optional data targeting and contextual guidance.

- `query` (required): A question or instruction. Accepts either a plain query string or a JSON-encoded structured argument.
- `target_data` (optional, strongly recommended): A cell, range, or column reference to specify the extraction target.
- `context` (optional): Additional information—background, constraints, user intent, or preferences—to tailor the response.

Returns: A concise answer string. When provided, `target_data` and `context` are used to improve relevance and precision.

**For precise results, include `target_data` to extract a specific field corresponding to the input data.**

## [​](https://docs.parallel.ai/integrations/gsuite\#usage-patterns)  Usage Patterns

### [​](https://docs.parallel.ai/integrations/gsuite\#basic)  Basic

Use `PARALLEL_QUERY` for general questions:

Copy

Ask AI

```
=PARALLEL_QUERY("Trends in AI")
```

### [​](https://docs.parallel.ai/integrations/gsuite\#targeted-data-retrieval)  Targeted data retrieval

Use `target_data` to power targeted enrichments in your sheet:

Text

Cell Reference

Copy

Ask AI

```
=PARALLEL_QUERY("Parallel Web Systems", target_data="CEO")
```

Notes

- The function returns a single text value per call. Use `ARRAYFORMULA` to apply it over many rows.
- For long queries, narrow `target_data` to relevant cells/columns to improve speed and fidelity.

## [​](https://docs.parallel.ai/integrations/gsuite\#best-practices)  Best Practices

1. Scope your query: Be explicit about the desired format and constraints.
2. Target the right data: Specify the exact data point you need to retrieve.
3. Provide context: If needed, add audience, tone, or decision criteria via `context`. Being verbose here is helpful.
4. Use cell references: Keep prompts and policies in cells for reuse and review.
5. Validate outputs: For downstream logic, pair insights with checks (e.g., thresholds).

## [​](https://docs.parallel.ai/integrations/gsuite\#viewing-basis)  Viewing Basis

The sidebar displays the sources used to generate each response.

1. Go to `Extensions → Parallel Web Systems → Open Sidebar → Basis`
2. Click on any cell containing a `PARALLEL_QUERY` result to
view the basis—the web pages and documents that informed the answer.
3. To refresh, click on the `Refresh` button in the basis tab

This helps you verify the accuracy of responses and trace information back to its original source.

## [​](https://docs.parallel.ai/integrations/gsuite\#caching)  Caching

Results are cached for up to 6 hours. If you need fresh data, you can force a recalculation by editing the cell or
clearing the cache via the sidebar.

## [​](https://docs.parallel.ai/integrations/gsuite\#admin-setup)  Admin Setup

For organizations that want to deploy Parallel across multiple users, first install the app for your organization
by following the steps mentioned [here](https://support.google.com/a/answer/172482?hl=en)To configure an API key for all users in your organization:

1. Open `Extensions → Apps Script` in your Google Sheet
2. Go to `Project Settings → Script Properties`
3. Add a property with the key `PARALLEL_API_KEY` and your API key as the value
4. Save the script properties

Once configured, all users in your organization will automatically use this API key.

## [​](https://docs.parallel.ai/integrations/gsuite\#troubleshooting)  Troubleshooting

- API key issues
  - Make sure your Parallel API key is saved in the sidebar (or configured via script properties) and has not expired.
- Slow or incomplete responses
  - Avoid volatile formulas that trigger frequent recalculation.
  - Results are cached for up to 6 hours; force refresh if you need updated data.

## [​](https://docs.parallel.ai/integrations/gsuite\#faq)  FAQ

- Can I return multiple fields?
  - No, each response is a single field. You can split one call with multiple output fields into multiple requests, each requesting one field.
    `ARRAYFORMULA` is especially useful for this.
- How do I keep prompts consistent across a team?
  - Store prompts and policies in reference cells or a “Prompts” sheet and reference them in formulas.

[Claude Code](https://docs.parallel.ai/integrations/claude-code-marketplace) [Google Vertex AI](https://docs.parallel.ai/integrations/google-vertex)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![](https://mintcdn.com/parallel-6fabab31-mtje7p526we/X5tandxFdaxBN_wG/images/sheets_example.png?w=1100&fit=max&auto=format&n=X5tandxFdaxBN_wG&q=85&s=9ffd4e825dff7ae51a48b482cdeea362)

---

# FindAll API Quickstart - Parallel

**URL:** https://docs.parallel.ai/findall-api/findall-quickstart

[Skip to main content](https://docs.parallel.ai/findall-api/findall-quickstart#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll

FindAll API Quickstart

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [What is FindAll?](https://docs.parallel.ai/findall-api/findall-quickstart#what-is-findall)
- [Key Features & Use Cases](https://docs.parallel.ai/findall-api/findall-quickstart#key-features-%26-use-cases)
- [Pricing](https://docs.parallel.ai/findall-api/findall-quickstart#pricing)
- [Common Use Cases](https://docs.parallel.ai/findall-api/findall-quickstart#common-use-cases)
- [What Happens During a Run](https://docs.parallel.ai/findall-api/findall-quickstart#what-happens-during-a-run)
- [Quick Example](https://docs.parallel.ai/findall-api/findall-quickstart#quick-example)
- [The Basic Workflow](https://docs.parallel.ai/findall-api/findall-quickstart#the-basic-workflow)
- [Step 1: Ingest](https://docs.parallel.ai/findall-api/findall-quickstart#step-1-ingest)
- [Customizing the ingest schema](https://docs.parallel.ai/findall-api/findall-quickstart#customizing-the-ingest-schema)
- [Step 2: Create FindAll Run](https://docs.parallel.ai/findall-api/findall-quickstart#step-2-create-findall-run)
- [Step 3: Poll for Status](https://docs.parallel.ai/findall-api/findall-quickstart#step-3-poll-for-status)
- [Step 4: Get Results](https://docs.parallel.ai/findall-api/findall-quickstart#step-4-get-results)
- [Troubleshooting](https://docs.parallel.ai/findall-api/findall-quickstart#troubleshooting)
- [Next Steps](https://docs.parallel.ai/findall-api/findall-quickstart#next-steps)
- [Rate Limits](https://docs.parallel.ai/findall-api/findall-quickstart#rate-limits)

**Beta Notice**: Parallel FindAll is currently in public beta. Endpoints and request/response formats are subject to change. We will provide 30 days notice before any breaking changes. For production access, contact [support@parallel.ai](mailto:support@parallel.ai).

## [​](https://docs.parallel.ai/findall-api/findall-quickstart\#what-is-findall)  What is FindAll?

FindAll is a web-scale entity discovery system that turns natural language queries into structured, enriched databases. It answers questions like “FindAll AI companies that raised Series A funding in the last 3 months” by combining intelligent search, evaluation, and enrichment capabilities.Unlike traditional search APIs that return a fixed set of results, FindAll generates candidates from web data, validates them against your criteria, and optionally enriches matches with additional structured information—all from a single natural language query.

## [​](https://docs.parallel.ai/findall-api/findall-quickstart\#key-features-&-use-cases)  Key Features & Use Cases

FindAll excels at entity discovery and research tasks that require both breadth and depth:

- **Natural Language Input**: Express complex search criteria in plain English
- **Intelligent Entity Discovery**: Automatically generates and validates potential matches
- **Structured Enrichment**: Extract specific attributes for each discovered entity
- **Citation-backed Results**: Every data point includes reasoning and source citations
- **Asynchronous Processing**: Handle large-scale searches without blocking your application

## [​](https://docs.parallel.ai/findall-api/findall-quickstart\#pricing)  Pricing

See [Pricing](https://docs.parallel.ai/getting-started/pricing) for a detailed schedule of rates.

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#common-use-cases)  Common Use Cases

- **Market Mapping**: “FindAll fintech companies offering earned-wage access in Brazil.”
- **Competitive Intelligence**: “FindAll AI infrastructure providers that raised Series B funding in the last 6 months.”
- **Lead Generation**: “FindAll residential roofing companies in Charlotte, NC.”
- **Financial Research**: “FindAll S&P 500 stocks that dropped X% in last 30 days and listed tariffs as a key risk.”

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#what-happens-during-a-run)  What Happens During a Run

When you create a FindAll run, the system executes three key stages:

1. **Generate Candidates from Web Data**: FindAll searches across the web to identify potential entities that might match your query. Each candidate enters the `generated` status.
2. **Evaluate Candidates Based on Match Conditions**: Each generated candidate is evaluated against your match conditions. Candidates that satisfy all conditions reach `matched` status and are included in your results. Those that don’t become `unmatched`.
3. **Extract Enrichments for Matched Candidates**: For candidates that matched, FindAll uses the Task API to extract any additional enrichment fields you specified. This enrichment is orchestrated automatically by FindAll.

This three-stage approach ensures efficiency: you only pay to enrich candidates that actually match your criteria.

## [​](https://docs.parallel.ai/findall-api/findall-quickstart\#quick-example)  Quick Example

Here’s a complete example that finds portfolio companies. The workflow consists of four steps: converting natural language to a schema, starting the run, polling for completion, and retrieving results.

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#the-basic-workflow)  The Basic Workflow

The FindAll API follows a simple four-step workflow:

1. **Ingest**: Convert your natural language query into a structured schema
2. **Run**: Start the findall run to discover and match candidates
3. **Poll**: Check status and retrieve results as they become available
4. **Fetch**: Retrieve the final list of matched candidates with reasoning and citations

Copy

Ask AI

```
Natural Language Query → Structured Schema → findall_id → Matched Results
```

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#step-1-ingest)  Step 1: Ingest

**Purpose**: Converts your natural language query into a structured schema with `entity_type` and `match_conditions`.The ingest endpoint automatically extracts:

- What type of entities to search for (companies, people, products, etc.)
- Match conditions that must be satisfied
- Optional enrichment suggestions

**Request:**

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/findall/ingest" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15" \
  -H "Content-Type: application/json" \
  -d '{
    "objective": "FindAll portfolio companies of Khosla Ventures founded after 2020"
  }'
```

**Response:**

Copy

Ask AI

```
{
  "objective": "FindAll portfolio companies of Khosla Ventures founded after 2020",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "khosla_ventures_portfolio_check",\
      "description": "Company must be a portfolio company of Khosla Ventures."\
    },\
    {\
      "name": "founded_after_2020_check",\
      "description": "Company must have been founded after 2020."\
    }\
  ]
}
```

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#customizing-the-ingest-schema)  Customizing the ingest schema

The ingest endpoint generates a suggested schema, but you can (and should) review and modify it before creating a run. Common modifications include:

- **Relaxing temporal conditions**: Ingest may interpret phrases like “founded after 2023” strictly (e.g., “within the last 1 year”). You can broaden the description to be more inclusive.
- **Adjusting match condition descriptions**: Make descriptions more or less specific to control match rates.
- **Adding or removing match conditions**: Tailor the schema to your exact needs.
- **Changing the entity type**: Correct the entity type if ingest misidentified it.

For example, if ingest generated a strict condition like `"Company must have been founded within the last 1 year"`, you might change it to `"Company must have been founded in 2025 or later"` for more reliable matching.

The ingest schema is a starting point, not a final answer. Editing `match_conditions` between the ingest and create steps is the recommended way to refine your query for better results.

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#step-2-create-findall-run)  Step 2: Create FindAll Run

**Purpose**: Starts the asynchronous findall process to generate and evaluate candidates.You can use the schema from ingest directly, or modify it before passing it to the create endpoint. Key parameters:

- `generator`: Choose `preview`, `base`, `core`, or `pro` based on your needs (see [Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing))
- `match_limit`: Maximum number of matched candidates to return

**Request:**

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/findall/runs" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15" \
  -H "Content-Type: application/json" \
  -d '{
    "objective": "FindAll portfolio companies of Khosla Ventures founded after 2020",
    "entity_type": "companies",
    "match_conditions": [\
      {\
        "name": "khosla_ventures_portfolio_check",\
        "description": "Company must be a portfolio company of Khosla Ventures."\
      },\
      {\
        "name": "founded_after_2020_check",\
        "description": "Company must have been founded after 2020."\
      }\
    ],
    "generator": "core",
    "match_limit": 5
  }'
```

**Response:**

Copy

Ask AI

```
{
  "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f"
}
```

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#step-3-poll-for-status)  Step 3: Poll for Status

**Purpose**: Monitor progress and wait for completion.**Request:**

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X GET "https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15"
```

**Response:**

Copy

Ask AI

```
{
  "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
  "status": {
    "status": "running",
    "is_active": true,
    "metrics": {
      "generated_candidates_count": 3,
      "matched_candidates_count": 1
    }
  },
  "generator": "core",
  "metadata": {},
  "created_at": "2025-11-03T20:47:21.580909Z",
  "modified_at": "2025-11-03T20:47:22.024269Z"
}
```

### [​](https://docs.parallel.ai/findall-api/findall-quickstart\#step-4-get-results)  Step 4: Get Results

**Purpose**: Retrieve the final list of candidates with match details, reasoning, and citations.

To understand the complete candidate object structure, see [Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates).

**Request:**

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X GET "https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/result" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15"
```

**Response:**

Copy

Ask AI

```
{
  "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
  "status": {
    "status": "completed",
    "is_active": false,
    "metrics": {
      "generated_candidates_count": 8,
      "matched_candidates_count": 5
    }
  },
  "candidates": [\
    {\
      "candidate_id": "candidate_a062dd17-d77a-4b1b-ad0e-de113e82f838",\
      "name": "Figure AI",\
      "url": "https://www.figure.ai",\
      "description": "AI robotics company building general purpose humanoid robots",\
      "match_status": "matched",\
      "output": {\
        "khosla_ventures_portfolio_check": {\
          "value": "Khosla Ventures led the Series B round",\
          "type": "match_condition",\
          "is_matched": true\
        },\
        "founded_after_2020_check": {\
          "value": "2022",\
          "type": "match_condition",\
          "is_matched": true\
        }\
      },\
      "basis": [\
        {\
          "field": "khosla_ventures_portfolio_check",\
          "citations": [\
            {\
              "title": "Figure AI raises $675M",\
              "url": "https://techcrunch.com/2024/02/29/figure-ai-funding/",\
              "excerpts": ["Khosla Ventures led the Series B round..."]\
            }\
          ],\
          "reasoning": "Figure AI is backed by Khosla Ventures as confirmed by multiple funding announcements.",\
          "confidence": "high"\
        },\
        {\
          "field": "founded_after_2020_check",\
          "citations": [\
            {\
              "title": "Figure AI - Company Profile",\
              "url": "https://www.figure.ai/about",\
              "excerpts": ["Founded in 2022 to build general purpose humanoid robots..."]\
            }\
          ],\
          "reasoning": "Multiple sources confirm that Figure AI was founded in 2022, which is after 2020.",\
          "confidence": "high"\
        }\
      ]\
    }\
    // ... additional candidates omitted for brevity ...\
  ]
}
```

See all 59 lines

## [​](https://docs.parallel.ai/findall-api/findall-quickstart\#troubleshooting)  Troubleshooting

Run completed with 0 matched candidates

This typically happens when match conditions are too strict for the candidate pool. Try these fixes:

1. **Relax match condition descriptions**: The ingest endpoint may generate overly strict conditions, especially for temporal queries. Edit condition descriptions to be more inclusive before creating the run.
2. **Use a stronger generator**: `preview` evaluates ~10 candidates, `base` searches broadly, `core` searches deeper, and `pro` is the most thorough. A stronger generator evaluates more candidates, increasing the chance of finding matches.
3. **Check temporal language**: Phrases like “founded after 2023” may be interpreted as “within the last year.” Use explicit ranges (e.g., “founded in 2025 or later”) for more predictable behavior.
4. **Broaden your query**: If your criteria are very specific, consider starting broad and using [enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich) to filter results after matching.
5. **Start with preview**: Always run with `generator: "preview"` first to validate your schema and see how conditions are being evaluated before committing to a full run.

Ingest generated unexpected conditions

The ingest endpoint interprets natural language heuristically. If the generated `match_conditions` don’t match your intent:

1. **Modify the conditions** before passing them to the create endpoint — see [Customizing the ingest schema](https://docs.parallel.ai/findall-api/findall-quickstart#customizing-the-ingest-schema) above.
2. **Skip ingest entirely** and construct your own schema directly with `objective`, `entity_type`, and `match_conditions`.
3. **Use the schema endpoint** on a completed run (`GET /v1beta/findall/runs/{findall_id}/schema`) to see what schema was used, then iterate on it.

## [​](https://docs.parallel.ai/findall-api/findall-quickstart\#next-steps)  Next Steps

- **[Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates)**: Understand candidate object structure, states, and exclusion
- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run)**: Complete endpoint documentation

## [​](https://docs.parallel.ai/findall-api/findall-quickstart\#rate-limits)  Rate Limits

See [Rate Limits](https://docs.parallel.ai/getting-started/rate-limits) for default quotas and how to request higher limits.

[OpenAI SDK Compatibility](https://docs.parallel.ai/chat-api/sdk-compatibility) [Generators](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Candidates - Parallel

**URL:** https://docs.parallel.ai/findall-api/core-concepts/findall-candidates

[Skip to main content](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Candidates

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Overview](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#overview)
- [Candidate States](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#candidate-states)
- [Candidate Object Structure](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#candidate-object-structure)
- [Understanding the output Field](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#understanding-the-output-field)
- [Understanding the basis Field](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#understanding-the-basis-field)
- [Excluding Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#excluding-candidates)
- [Retrieving Candidates](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#retrieving-candidates)
- [Related Topics](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates#related-topics)

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#overview)  Overview

A **candidate** is an entity that FindAll discovers during the generation phase of a run. Each candidate represents a potential match that is evaluated against your match conditions.

### [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#candidate-states)  Candidate States

Candidates progress through these states during evaluation:

- **Generated**: Discovered from web data, queued for evaluation
- **Matched**: Successfully satisfied all match conditions
- **Unmatched**: Failed to satisfy one or more match conditions

**Post-Match Events**: When using [Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse) or [Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook), you may receive **`enriched`** events for matched candidates. These are event types (not `match_status` values) that indicate when additional data has been extracted via enrichments after a candidate has already matched.

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#candidate-object-structure)  Candidate Object Structure

Every candidate in FindAll results, SSE events, and webhook payloads follows this structure:

| Property | Type | Description |
| --- | --- | --- |
| `candidate_id` | string | Unique identifier for the candidate |
| `name` | string | Name of the entity |
| `url` | string | Primary URL for the entity |
| `description` | string | Brief description of the entity |
| `match_status` | enum | One of `generated`, `matched`, and `unmatched` |
| `output` | object | Key-value pairs showing evaluation results for each match condition and enrichment (see section below for more details) |
| `basis` | array\[FieldBasis\] | Citations, reasoning, and confidence scores for each field. See [FieldBasis](https://docs.parallel.ai/task-api/guides/access-research-basis#the-fieldbasis-object) for more details. |

### [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#understanding-the-output-field)  Understanding the `output` Field

The `output` field contains evaluation results where each key corresponds to a field name. Match conditions include an `is_matched` boolean, while enrichments do not:

Copy

Ask AI

```
{
  "founded_after_2020_check": {
    "value": "2021",
    "type": "match_condition",
    "is_matched": true // only match_condition contains boolean field is_match
  },
  "ceo_name": {
    "value": "Ramin Hasani",
    "type": "enrichment"
  }
}
```

### [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#understanding-the-basis-field)  Understanding the `basis` Field

The `basis` field provides citations, reasoning, and confidence scores for each field in `output`.

**For complete details on basis structure and usage**, see [Access Research Basis](https://docs.parallel.ai/task-api/guides/access-research-basis).

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#excluding-candidates)  Excluding Candidates

**Use case**: Excluding candidates is useful when you already know certain entities match your criteria (such as results from previous runs or entities you’ve already identified), allowing you to focus on discovering new matches. By excluding these known entities, you won’t be charged for generating or evaluating them again, making your searches more cost-effective.

FindAll uses intelligence to deduplicate and disambiguate candidates you provide in the exclude list, which handles aliases and entities with slightly different names or URL variations. However, using the most official and disambiguated name and URL is recommended for best results.

Provide an `exclude_list` to prevent specific entities from being generated or evaluated. Excluded entities won’t incur evaluation costs or appear in results/events.**Exclude list structure:** Array of objects with `name` (string) and `url` (string) fields.

cURL

Python

TypeScript

Copy

Ask AI

```
curl -X POST "https://api.parallel.ai/v1beta/findall/runs" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "objective": "FindAll portfolio companies of Khosla Ventures",
    "match_conditions": [...],
    "exclude_list": [\
      {"name": "Figure AI", "url": "https://www.figure.ai"},\
      {"name": "Anthropic", "url": "https://www.anthropic.com"}\
    ]
  }'
```

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#retrieving-candidates)  Retrieving Candidates

Candidates can be accessed through multiple methods:

- **[`/result` endpoint](https://docs.parallel.ai/findall-api/findall-quickstart#step-4-get-results)**: Retrieve all candidates (matched and unmatched) after run completion
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Stream candidates in real-time as they’re generated and evaluated
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Receive HTTP callbacks for candidate events

## [​](https://docs.parallel.ai/findall-api/core-concepts/findall-candidates\#related-topics)  Related Topics

- **[FindAll Quickstart](https://docs.parallel.ai/findall-api/findall-quickstart)**: Get started with FindAll API
- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: Learn about run statuses and metrics
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional data from matched candidates
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Monitor candidates in real-time
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Set up notifications for candidate events
- **[Access Research Basis](https://docs.parallel.ai/task-api/guides/access-research-basis)**: Deep dive into citation and reasoning structure

[Generators](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing) [Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Task Spec - Parallel

**URL:** https://docs.parallel.ai/task-api/guides/specify-a-task

[Skip to main content](https://docs.parallel.ai/task-api/guides/specify-a-task#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Task Spec

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Task Spec](https://docs.parallel.ai/task-api/guides/specify-a-task#task-spec)
- [Task Spec Structure](https://docs.parallel.ai/task-api/guides/specify-a-task#task-spec-structure)
- [Schema Types](https://docs.parallel.ai/task-api/guides/specify-a-task#schema-types)
- [Task Spec Best Practices](https://docs.parallel.ai/task-api/guides/specify-a-task#task-spec-best-practices)
- [Output Schema Validation Rules](https://docs.parallel.ai/task-api/guides/specify-a-task#output-schema-validation-rules)
- [Schema Structure Rules](https://docs.parallel.ai/task-api/guides/specify-a-task#schema-structure-rules)
- [Size and Complexity Limits](https://docs.parallel.ai/task-api/guides/specify-a-task#size-and-complexity-limits)
- [Unsupported Keywords](https://docs.parallel.ai/task-api/guides/specify-a-task#unsupported-keywords)
- [Common Schema Errors to Avoid](https://docs.parallel.ai/task-api/guides/specify-a-task#common-schema-errors-to-avoid)

## [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#task-spec)  Task Spec

A Task Specification ( [Task Spec](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-task-spec-output-schema)) is a declarative template that defines the structure and requirements for the outputs of a web research operation. While optional in each Task Run, Task Specs provide significant advantages when you need precise control over your research data.Task Specs ensure consistent results by enforcing a specific output structure across multiple runs. They validate schema against expected formats and create reusable templates for common research patterns. By defining the expected outputs clearly, they also serve as self-documentation for your tasks, making them easier to understand and maintain.

| Component | Required | Purpose | Format |
| --- | --- | --- | --- |
| **Output Schema** | Yes | Defines the structure and fields of the task result | JSON Schema or Text |
| **Input Schema** | No | Specifies expected input parameters and their formats | JSON Schema or Text |

## [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#task-spec-structure)  Task Spec Structure

A Task Spec consists of:

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `output` | Schema object or string | Yes | Description and structure of the desired output |
| `input` | Schema object or string | No | Description and structure of input parameters |

When providing a bare string for input or output, it’s equivalent to a text schema with that string as the description.

## [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#schema-types)  Schema Types

Task Spec supports three schema formats:

When using the [Python SDK](https://pypi.org/project/parallel-web/), Parallel Tasks also support Pydantic objects in Task Spec

`auto` mode enables Deep Research style outputs only in processors `pro` and above. Read more about Deep Research [here](https://docs.parallel.ai/task-api/task-deep-research).

- JSON Schema

- Text Schema

- Auto Schema

Copy

Ask AI

```
{
  "json_schema": {
    "type": "object",
    "properties": {
      "population": {
        "type": "string",
        "description": "Current population with year of estimate"
      },
      "area": {
        "type": "string",
        "description": "Total area in square kilometers and square miles"
      }
    },
    "required": ["population", "area"]
  },
  "type": "json"
}
```

Copy

Ask AI

```
{
  "description": "Summary of the country's economic indicators for 2023",
  "type": "text"
}
```

Copy

Ask AI

```
{
  "type": "auto"
}
```

## [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#task-spec-best-practices)  Task Spec Best Practices

Define what entity you’re researching (input) and what specific data points you need back (output). Keep both as flat-structured as possible.

**The `description` field is your primary tool for controlling output quality.** Field-level descriptions are the best way to include specific instructions for each output field. Think of the `description` as your “prompt” for that field—it’s where you specify format requirements, data sources, fallback behavior, and any other instructions.

1

[Navigate to header](https://docs.parallel.ai/task-api/guides/specify-a-task#)

Identify what schema your use case requires

- If executing a Deep Research style Task, use the Task Spec with `auto` schema
- If control and specificity with regards to outputs are required, use Task Spec with a JSONSchema for inputs and outputs
- In other cases, the Task Spec may not be necessary; the system in this case will output a plain text response

2

[Navigate to header](https://docs.parallel.ai/task-api/guides/specify-a-task#)

Define effective inputs

- When using only text based inputs, be as specific as possible about what you are expecting the system to return. Include any instructions and preferences in the input text.
- When using JSON Schema inputs, use the minimum fields required to uniquely identify the entity you want to enrich. For example, include both the company\_name and company\_website, or both the person\_name and social\_url, to help the system disambiguate.
- Avoid deeply nested structures and keep the input schema flat

3

[Navigate to header](https://docs.parallel.ai/task-api/guides/specify-a-task#)

Define effective outputs (relevant when using JSONSchema outputs)

**Use field-level `description` for all instructions.** The `description` field is the most effective way to control how each output field is populated. Include:

- **Entity**: What are you researching?
- **Action**: What do you want to find?
- **Specifics**: Constraints, time periods, formatting requirements
- **Error Handling**: What to return if data is unavailable (e.g., “If unavailable, return null”)

**Example of a well-written description:**

Copy

Ask AI

```
"employee_count": {
  "type": "string",
  "description": "The current number of employees at the company. Use the most recent data available from LinkedIn, company website, or press releases. Format as a range (e.g., '501-1000') if exact count unavailable. If no data found, return 'Unknown'."
}
```

- Use clear, descriptive field names
  - Use `ceo_name` instead of `name`
  - Use `headquarters_address`\\*\\* instead of `address`
  - Use `annual_revenue_2024`\\*\\* instead of `revenue`
- Specify Data Formats
  - Always specify format for dates: `YYYY-MM-DD`
  - Use ranges for numerical values with units: `revenue_in_millions`, `employee_count`
  - Specify quantities for lists: `top_5_products`, `recent_3_acquisitions`
- **Unnecessary Fields**: Don’t include fields like `reasoning` or `confidence_score` as these are already included in the basis

4

[Navigate to header](https://docs.parallel.ai/task-api/guides/specify-a-task#)

Additional instructions

If there are additional requirements or instructions separate from individual fields, the top-level `description` field is available. For example:

Copy

Ask AI

```
{
  "type": "object",
  "description": "Extract all information only from well-known government sites.",
  "properties": {
    "latest_funding_amount": {
      "type": "string",
      "description": "Funding amount in millions USD format (e.g., '50M'). If unavailable, return null."
    },
    "funding_round_type": {
      "type": "string",
      "description": "Type of funding round (Series A, Series B, etc.). If unknown, return 'Type unknown'."
    },
    "funding_date": {
      "type": "string",
      "description": "Date of funding round in YYYY-MM-DD format. If partial date available, use YYYY-MM or YYYY."
    },
    "current_employee_count": {
      "type": "string",
      "description": "Current number of employees as approximate number or range. Allow estimates when precise counts unavailable."
    }
  }
}
```

## [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#output-schema-validation-rules)  Output Schema Validation Rules

The Task API enforces several restrictions on output schemas to ensure compatibility and performance:

### [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#schema-structure-rules)  Schema Structure Rules

| Rule | Type | Description |
| --- | --- | --- |
| Root type must be object | error | The root schema must have `"type": "object"` |
| Root must have properties | error | The root object must have a `properties` field |
| Root cannot use anyOf | error | The root level cannot use `anyOf` |
| Standalone null type | error | `null` type is only allowed in union types or anyOf |
| All fields must be required | warning | All properties should be listed in the `required` array |
| additionalProperties must be false | warning | All object types should set `additionalProperties: false` |

While all fields must be required in the schema, you can create optional parameters by using a union type with `null`. For example, `"type": ["string", "null"]` allows a field to be either a string or null, effectively making it optional while maintaining schema compliance.

### [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#size-and-complexity-limits)  Size and Complexity Limits

**18,000 character limit:** The combined length of your task specification AND input data cannot exceed 18,000 characters. This includes:

- All field names and descriptions in your schemas
- The `objective` or `description` text
- Your input data (the entity you’re researching)

If you hit this limit, simplify your schema descriptions or reduce input size. For large input data, consider splitting into multiple tasks.

| Rule | Type | Limit | Description |
| --- | --- | --- | --- |
| Nesting depth | error | 5 levels | Maximum nesting depth of objects and arrays |
| Total properties | error | 100 | Maximum total number of properties across all levels |
| Total string length | error | 18,000 chars | Maximum total string length for names and values |
| Enum values | error | 500 | Maximum number of enum values across all properties |
| Large enum string length | error | 7,500 chars | Maximum string length for enums with >250 values |
| Task spec size | error | 15,000 chars | Maximum length of the task specification alone |
| **Total size** | error | **18,000 chars** | **Maximum combined length of task specification + input data** |

### [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#unsupported-keywords)  Unsupported Keywords

The following JSON Schema keywords are not supported in output schemas:`contains`, `format`, `maxContains`, `maxItems`, `maxLength`, `maxProperties`, `maximum`, `minContains`, `minItems`, `minLength`, `minimum`, `minProperties`, `multipleOf`, `pattern`, `patternProperties`, `propertyNames`, `uniqueItems`, `unevaluatedItems`, `unevaluatedProperties`irements: it has an object root type with properties, all fields are required, and `additionalProperties` is set to false.

### [​](https://docs.parallel.ai/task-api/guides/specify-a-task\#common-schema-errors-to-avoid)  Common Schema Errors to Avoid

Here are examples of common schema errors and how to fix them:

- Root Type Error

- AnyOf Error

- Missing Required

- Additional Properties

- Unsupported Keywords

Copy

Ask AI

```
{
  "type": "array",  // Error: Root type must be "object"
  "items": {
    "type": "object",
    "properties": {
      "name": { "type": "string" }
    }
  }
}
```

**Fix:** Change the root type to “object” and move array properties to a field:

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" }
        },
        "required": ["name"]
      }
    }
  },
  "required": ["items"],
  "additionalProperties": false
}
```

Copy

Ask AI

```
{
  "type": "object",
  "anyOf": [  // Error: Root level cannot use anyOf\
    {\
      "properties": {\
        "field1": { "type": "string" }\
      }\
    },\
    {\
      "properties": {\
        "field2": { "type": "string" }\
      }\
    }\
  ]
}
```

**Fix:** Combine the properties into a single object:

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "field1": { "type": "string" },
    "field2": { "type": "string" }
  },
  "required": ["field1", "field2"],
  "additionalProperties": false
}
```

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "field1": { "type": "string" },
    "field2": { "type": "string" }
  },
  "required": ["field1"]  // Warning: All fields should be required
}
```

**Fix:** Add all fields to the required array:

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "field1": { "type": "string" },
    "field2": { "type": "string" }
  },
  "required": ["field1", "field2"],
  "additionalProperties": false
}
```

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "field1": { "type": "string" },
    "field2": { "type": "string" }
  },
  "required": ["field1", "field2"],
  "additionalProperties": true  // Warning: should be false
}
```

**Fix:** Set additionalProperties to false:

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "field1": { "type": "string" },
    "field2": { "type": "string" }
  },
  "required": ["field1", "field2"],
  "additionalProperties": false
}
```

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "field1": {
      "type": "string",
      "minLength": 5  // Error: Unsupported keyword
    }
  },
  "required": ["field1"],
  "additionalProperties": false
}
```

**Fix:** Remove unsupported keywords and use descriptions instead:

Copy

Ask AI

```
{
  "type": "object",
  "properties": {
    "field1": {
      "type": "string",
      "description": "A string with at least 5 characters"
    }
  },
  "required": ["field1"],
  "additionalProperties": false
}
```

[Deep Research](https://docs.parallel.ai/task-api/task-deep-research) [Processors](https://docs.parallel.ai/task-api/guides/choose-a-processor)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Zapier - Parallel

**URL:** https://docs.parallel.ai/integrations/zapier

[Skip to main content](https://docs.parallel.ai/integrations/zapier#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Zapier

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Installation](https://docs.parallel.ai/integrations/zapier#installation)
- [Available Actions](https://docs.parallel.ai/integrations/zapier#available-actions)
- [Common Use Cases](https://docs.parallel.ai/integrations/zapier#common-use-cases)
- [Best Practices](https://docs.parallel.ai/integrations/zapier#best-practices)
- [Migration Guide](https://docs.parallel.ai/integrations/zapier#migration-guide)

Integrate Parallel’s AI-powered web research into your Zapier workflows with our official app.

## [​](https://docs.parallel.ai/integrations/zapier\#installation)  Installation

Search for “Parallel Web Systems” when adding a step to your Zap,
or use [this link](https://zapier.com/apps/parallel-web-systems/integrations) to get started.

Version 1.1.0 and later supports OAuth.

## [​](https://docs.parallel.ai/integrations/zapier\#available-actions)  Available Actions

| Name | Key | Description | Use Cases |
| --- | --- | --- | --- |
| **Create Async Web Enrichment** | `async_web_enrichment` | Create an asynchronous Task Run. | Lead enrichment, competitive analysis, content research |
| **Fetch Result for Async Runs** | `process_async_completion` | Retrieve results for an async Task Run. | Complex multi-source research, deep competitive intelligence |

## [​](https://docs.parallel.ai/integrations/zapier\#common-use-cases)  Common Use Cases

- **Sales**: Lead scoring, account research, contact discovery
- **Marketing**: Content research, trend analysis, competitor monitoring
- **Operations**: Vendor research, risk assessment, due diligence
- **Support**: Real-time information lookup, documentation generation

For detailed configuration and advanced features, see the [Task API quickstart](https://docs.parallel.ai/task-api/task-quickstart).

## [​](https://docs.parallel.ai/integrations/zapier\#best-practices)  Best Practices

- **Use webhooks**: Let your workflow continue automatically when results are ready, without continuously polling.
- **Choose processors appropriately**: Use the right processors for your workflow to ensure the best results.
For more information on choosing processors, see our [guide](https://docs.parallel.ai/task-api/guides/choose-a-processor).

## [​](https://docs.parallel.ai/integrations/zapier\#migration-guide)  Migration Guide

If you’re already using Parallel version 1.0.3 or earlier with Zapier, you can easily migrate to the latest version.

1. Open any existing Zap and click `Edit Zap`.
2. In `Setup`, click `Change` under `Account`, then reconnect or create a new account.
3. Update the account connection for all Zaps that use Parallel.

[Vercel](https://docs.parallel.ai/integrations/vercel) [Source Policy](https://docs.parallel.ai/resources/source-policy)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Chat API Quickstart
Source: https://docs.parallel.ai/chat-api/chat-quickstart

Build low-latency web research applications with OpenAI-compatible streaming chat completions

Parallel Chat is a web research API that returns OpenAI ChatCompletions compatible streaming text and JSON.
The Chat API supports multiple models—from the `speed` model for low latency across a
broad range of use cases, to research models (`lite`, `base`, `core`) for deeper research-grade outputs
where you can afford to wait longer for even more comprehensive responses with full [research basis](/task-api/guides/access-research-basis) support.

<Note>
  **Beta Notice**: Parallel Chat is in beta. We provide a rate limit of 300 requests
  per minute for the Chat API out of the box. [Contact us](mailto:support@parallel.ai)
  for production capacity.
</Note>

## Choosing the Right Model

The Chat API supports both the `speed` model for
low latency applications and research models for deeper outputs.
Research models (`lite`, `base`, `core`) are Chat API wrappers over our [Task API processors](/task-api/guides/choose-a-processor),
providing the same research capabilities along with basis in an OpenAI-compatible interface.

| Model   | Best For                                      | Basis Support | Latency (TTFT) |
| ------- | --------------------------------------------- | ------------- | -------------- |
| `speed` | Low latency across a broad range of use cases | No            | \~3s           |
| `lite`  | Simple lookups, basic metadata                | Yes           | 10-60s         |
| `base`  | Standard enrichments, factual queries         | Yes           | 15-100s        |
| `core`  | Complex research, multi-source synthesis      | Yes           | 60s-5min       |

<Tip>Use `speed` for low latency across a broad range of use cases.
Use research models (`lite`, `base`, `core`) for more research-intensive workflows
where you can afford to wait longer for an even deeper response with citations,
reasoning, and confidence levels via the [research basis](/task-api/guides/access-research-basis).</Tip>

## 1. Set up Prerequisites

The Chat API is fully compatible with the OpenAI SDK — just swap the base URL and API key. Generate your API key on [Platform](https://platform.parallel.ai), then install the OpenAI SDK:

<CodeGroup>
  ```bash Python theme={"system"}
  pip install openai
  export PARALLEL_API_KEY="your-api-key"
  ```

  ```bash TypeScript theme={"system"}
  npm install openai
  export PARALLEL_API_KEY="your-api-key"
  ```

  ```bash cURL theme={"system"}
  export PARALLEL_API_KEY="your-api-key"
  ```
</CodeGroup>

## Performance and Rate Limits

Speed is optimized for interactive applications requiring low latency responses:

* **Performance**: With `stream=true`, achieves 3 second p50 TTFT (median time to first token)
* **Default Rate Limit**: 300 requests per minute
* **Use Cases**: Chat interfaces, interactive tools

For research based tasks where latency is not the primary concern, use one of the research models.

For production deployments requiring higher rate limits, [contact our team](https://www.parallel.ai).

## 2. Make Your First Request

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -N https://api.parallel.ai/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $PARALLEL_API_KEY" \
    -d '{
      "model": "speed",
      "messages": [\
        { "role": "user", "content": "What does Parallel Web Systems do?" }\
      ],
      "stream": false,
      "response_format": {
        "type": "json_schema",
        "json_schema": {
          "name": "reasoning_schema",
          "schema": {
            "type": "object",
            "properties": {
              "reasoning": {
                "type": "string",
                "description": "Think step by step to arrive at the answer"
              },
              "answer": {
                "type": "string",
                "description": "The direct answer to the question"
              },
              "citations": {
                "type": "array",
                "items": { "type": "string" },
                "description": "Sources cited to support the answer"
              }
            }
          }
        }
      }
    }'
  ```

  ```bash cURL (Streaming) theme={"system"}
  curl -N https://api.parallel.ai/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $PARALLEL_API_KEY" \
    -d '{
      "model": "speed",
      "messages": [\
        { "role": "user", "content": "What does Parallel Web Systems do?" }\
      ],
      "stream": true,
      "response_format": {
        "type": "json_schema",
        "json_schema": {
          "name": "reasoning_schema",
          "schema": {
            "type": "object",
            "properties": {
              "reasoning": {
                "type": "string",
                "description": "Think step by step to arrive at the answer"
              },
              "answer": {
                "type": "string",
                "description": "The direct answer to the question"
              },
              "citations": {
                "type": "array",
                "items": { "type": "string" },
                "description": "Sources cited to support the answer"
              }
            }
          }
        }
      }
    }'
  ```

  ```python Python theme={"system"}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ["PARALLEL_API_KEY"],
      base_url="https://api.parallel.ai"  # Parallel's API endpoint
  )

  response = client.chat.completions.create(
      model="speed", # Parallel model name
      messages=[\
          {"role": "user", "content": "What does Parallel Web Systems do?"}\
      ],
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "reasoning_schema",
              "schema": {
                  "type": "object",
                  "properties": {
                      "reasoning": {
                          "type": "string",
                          "description": "Think step by step to arrive at the answer",
                      },
                      "answer": {
                          "type": "string",
                          "description": "The direct answer to the question",
                      },
                      "citations": {
                          "type": "array",
                          "items": {"type": "string"},
                          "description": "Sources cited to support the answer",
                      },
                  },
              },
          },
      },
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={"system"}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.PARALLEL_API_KEY,
    baseURL: "https://api.parallel.ai", // Parallel's API endpoint
  });

  async function main() {
    const response = await client.chat.completions.create({
      model: "speed", // Parallel model name
      messages: [{ role: "user", content: "What does Parallel Web Systems do?" }],
      response_format: {
        type: "json_schema",
        json_schema: {
          name: "reasoning_schema",
          schema: {
            type: "object",
            properties: {
              reasoning: {
                type: "string",
                description: "Think step by step to arrive at the answer",
              },
              answer: {
                type: "string",
                description: "The direct answer to the question",
              },
              citations: {
                type: "array",
                items: { type: "string" },
                description: "Sources cited to support the answer",
              },
            },
          },
        },
      },
    });

    console.log(response.choices[0].message.content);
  }

  main();
  ```

  ```python Python (Streaming) theme={"system"}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ["PARALLEL_API_KEY"],
      base_url="https://api.parallel.ai"  # Parallel's API endpoint
  )

  stream = client.chat.completions.create(
      model="speed", # Parallel model name
      messages=[\
          {"role": "user", "content": "What does Parallel Web Systems do?"}\
      ],
      stream=True,
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "reasoning_schema",
              "schema": {
                  "type": "object",
                  "properties": {
                      "reasoning": {
                          "type": "string",
                          "description": "Think step by step to arrive at the answer",
                      },
                      "answer": {
                          "type": "string",
                          "description": "The direct answer to the question",
                      },
                      "citations": {
                          "type": "array",
                          "items": {"type": "string"},
                          "description": "Sources cited to support the answer",
                      },
                  },
              },
          },
      },
  )

  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="", flush=True)

  print()
  ```

  ```typescript TypeScript (Streaming) theme={"system"}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.PARALLEL_API_KEY,
    baseURL: "https://api.parallel.ai", // Parallel's API endpoint
  });

  async function main() {
    const stream = await client.chat.completions.create({
      model: "speed", // Parallel model name
      messages: [{ role: "user", content: "What does Parallel Web Systems do?" }],
      stream: true,
      response_format: {
        type: "json_schema",
        json_schema: {
          name: "reasoning_schema",
          schema: {
            type: "object",
            properties: {
              reasoning: {
                type: "string",
                description: "Think step by step to arrive at the answer",
              },
              answer: {
                type: "string",
                description: "The direct answer to the question",
              },
              citations: {
                type: "array",
                items: { type: "string" },
                description: "Sources cited to support the answer",
              },
            },
          },
        },
      },
    });

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
    process.stdout.write("\\n");
  }

  main();
  ```
</CodeGroup>

## System Prompt

You can provide a custom system prompt to control the AI's behavior and response style by including it in the messages array with `"role": "system"` as the first message in your request.

## Using Research Models

When you use research models (`lite`, `base`, or `core`) instead of `speed`, the
Chat API provides research-grade outputs with
full [research basis](/task-api/guides/access-research-basis) support.
The basis includes citations, reasoning, and confidence levels for each response.

### Example with Research Model

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -N https://api.parallel.ai/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $PARALLEL_API_KEY" \
    -d '{
      "model": "base",
      "messages": [\
        { "role": "user", "content": "What is the founding date and headquarters of Parallel Web Systems?" }\
      ],
      "stream": false
    }'
  ```

  ```python Python theme={"system"}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ["PARALLEL_API_KEY"],
      base_url="https://api.parallel.ai"  # Parallel's API endpoint
  )

  response = client.chat.completions.create(
      model="base",  # Research model for deeper output
      messages=[\
          {"role": "user", "content": "What is the founding date and headquarters of Parallel Web Systems?"}\
      ],
  )

  # Access the response content
  print(response.choices[0].message.content)

  # Access the research basis (citations, reasoning, confidence)
  print(response.basis)
  ```

  ```typescript TypeScript theme={"system"}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.PARALLEL_API_KEY,
    baseURL: "https://api.parallel.ai", // Parallel's API endpoint
  });

  async function main() {
    const response = await client.chat.completions.create({
      model: "base", // Research model for deeper output
      messages: [\
        {\
          role: "user",\
          content: "What is the founding date and headquarters of Parallel Web Systems?",\
        },\
      ],
    });

    // Access the response content
    console.log(response.choices[0].message.content);

    // Access the research basis (citations, reasoning, confidence)
    console.log((response as any).basis);
  }

  main();
  ```
</CodeGroup>

For complete details on the research basis structure, including per-element basis for arrays, see the [Basis documentation](/task-api/guides/access-research-basis).

# Access results
print(result.relation.fetchdf())
print(f"Success: {result.success_count}, Errors: {result.error_count}")
```

Output:

| name      | website       | ceo\_name     | founding\_year | headquarters\_city |
| --------- | ------------- | ------------- | -------------- | ------------------ |
| Google    | google.com    | Sundar Pichai | 1998           | Mountain View      |
| Microsoft | microsoft.com | Satya Nadella | 1975           | Redmond            |
| Apple     | apple.com     | Tim Cook      | 1976           | Cupertino          |

### Function Parameters

| Parameter           | Type                 | Default       | Description                                               |
| ------------------- | -------------------- | ------------- | --------------------------------------------------------- |
| `conn`              | `DuckDBPyConnection` | required      | DuckDB connection                                         |
| `source_table`      | `str`                | required      | Table name or SQL query                                   |
| `input_columns`     | `dict[str, str]`     | required      | Mapping of input descriptions to column names             |
| `output_columns`    | `list[str]`          | required      | List of output column descriptions                        |
| `result_table`      | `str \| None`        | `None`        | Optional permanent table to create                        |
| `api_key`           | `str \| None`        | `None`        | API key (uses `PARALLEL_API_KEY` env var if not provided) |
| `processor`         | `str`                | `"lite-fast"` | Parallel processor to use                                 |
| `timeout`           | `int`                | `600`         | Timeout in seconds                                        |
| `include_basis`     | `bool`               | `False`       | Include citations in results                              |
| `progress_callback` | `Callable`           | `None`        | Callback for progress updates                             |

### Return Value

The function returns an `EnrichmentResult` dataclass:

```python theme={"system"}
@dataclass
class EnrichmentResult:
    relation: duckdb.DuckDBPyRelation  # Enriched data as DuckDB relation
    success_count: int                  # Number of successful rows
    error_count: int                    # Number of failed rows
    errors: list[dict]                  # Error details with row index
    elapsed_time: float                 # Processing time in seconds
```

### Column Name Mapping

Output column descriptions are automatically converted to valid SQL identifiers. Field names are converted to snake\_case:

| Description              | Column Name      |
| ------------------------ | ---------------- |
| `"CEO name"`             | `ceo_name`       |
| `"Founding year (YYYY)"` | `founding_year`  |
| `"Annual revenue [USD]"` | `annual_revenue` |

## SQL Query as Source

You can pass a SQL query instead of a table name:

```python theme={"system"}
result = enrich_table(
    conn,
    source_table="""
        SELECT name, website
        FROM companies
        WHERE active = true
        LIMIT 100
    """,
    input_columns={"company_name": "name", "website": "website"},
    output_columns=["CEO name"],
)
```

## Creating Permanent Tables

Save enriched results to a permanent table:

```python theme={"system"}
result = enrich_table(
    conn,
    source_table="companies",
    input_columns={"company_name": "name"},
    output_columns=["CEO name", "Founding year"],
    result_table="enriched_companies",
)

# Access the enriched DataFrame
print(result.result)
print(f"Success: {result.success_count}, Errors: {result.error_count}")
```

Output:

| company   | website       | ceo\_name     | founding\_year | headquarters\_city |
| --------- | ------------- | ------------- | -------------- | ------------------ |
| Google    | google.com    | Sundar Pichai | 1998           | Mountain View      |
| Microsoft | microsoft.com | Satya Nadella | 1975           | Redmond            |
| Apple     | apple.com     | Tim Cook      | 1976           | Cupertino          |

### Function Parameters

| Parameter        | Type             | Default       | Description                                               |
| ---------------- | ---------------- | ------------- | --------------------------------------------------------- |
| `df`             | `pl.DataFrame`   | required      | DataFrame to enrich                                       |
| `input_columns`  | `dict[str, str]` | required      | Mapping of input descriptions to column names             |
| `output_columns` | `list[str]`      | required      | List of output column descriptions                        |
| `api_key`        | `str \| None`    | `None`        | API key (uses `PARALLEL_API_KEY` env var if not provided) |
| `processor`      | `str`            | `"lite-fast"` | Parallel processor to use                                 |
| `timeout`        | `int`            | `600`         | Timeout in seconds                                        |
| `include_basis`  | `bool`           | `False`       | Include citations in results                              |

### Return Value

The function returns an `EnrichmentResult` dataclass:

```python theme={"system"}
@dataclass
class EnrichmentResult:
    result: pl.DataFrame      # Enriched DataFrame
    success_count: int        # Number of successful rows
    error_count: int          # Number of failed rows
    errors: list[dict]        # Error details with row index
    elapsed_time: float       # Processing time in seconds
```

### Column Name Mapping

Output column descriptions are automatically converted to valid Python identifiers. Field names are converted to snake\_case:

| Description              | Column Name      |
| ------------------------ | ---------------- |
| `"CEO name"`             | `ceo_name`       |
| `"Founding year (YYYY)"` | `founding_year`  |
| `"Annual revenue [USD]"` | `annual_revenue` |

## LazyFrame Support

Use `parallel_enrich_lazy()` to work with LazyFrames:

```python theme={"system"}
from parallel_web_tools.integrations.polars import parallel_enrich_lazy

# Access citations in the _basis column
for row in result.result.iter_rows(named=True):
    print(f"CEO: {row['ceo_name']}")
    print(f"Sources: {row['_basis']}")
```

## Processor Selection

Choose a processor based on your speed vs thoroughness requirements. See [Choose a Processor](/task-api/guides/choose-a-processor) for detailed guidance and [Pricing](/resources/pricing) for cost information.

| Processor   | Speed   | Best For                    |
| ----------- | ------- | --------------------------- |
| `lite-fast` | Fastest | Basic metadata, high volume |
| `base-fast` | Fast    | Standard enrichments        |
| `core-fast` | Medium  | Cross-referenced data       |
| `pro-fast`  | Slower  | Deep research               |

## Best Practices

<AccordionGroup>
  <Accordion title="Use specific descriptions">
    Be specific in your output column descriptions for better results:

    ```python theme={"system"}
    output_columns = [\
        "CEO name (current CEO or equivalent leader)",\
        "Founding year (YYYY format)",\
        "Annual revenue (USD, most recent fiscal year)",\
    ]
    ```
  </Accordion>

  <Accordion title="Handle errors gracefully">
    Errors don't stop processing - partial results are returned:

    ```python theme={"system"}
    result = parallel_enrich(df, ...)

    if result.error_count > 0:
        print(f"Failed rows: {result.error_count}")
        for error in result.errors:
            print(f"  Row {error['row']}: {error['error']}")

    # Filter successful rows
    successful_df = result.result.filter(pl.col("ceo_name").is_not_null())
    ```
  </Accordion>

  <Accordion title="Batch large datasets">
    For very large datasets (1000+ rows), consider processing in batches:

    ```python theme={"system"}
    def enrich_in_batches(df: pl.DataFrame, batch_size: int = 100):
        results = []
        for i in range(0, len(df), batch_size):
            batch = df.slice(i, batch_size)
            result = parallel_enrich(batch, ...)
            results.append(result.result)
        return pl.concat(results)
    ```
  </Accordion>

  <Accordion title="Cost management">
    * Use `lite-fast` for high-volume, basic enrichments
    * Test with small batches before processing large DataFrames
    * Store results to avoid re-enriching the same data
  </Accordion>
</AccordionGroup>

# Extract API Best Practices
Source: https://docs.parallel.ai/extract/best-practices

Learn how to optimize web content extraction with objectives, search queries, and fetch policies for LLM-ready markdown output

The Extract API converts any public URL into clean, LLM-optimized markdown—handling
JavaScript-heavy pages and PDFs automatically. Extract focused excerpts aligned to your
objective or retrieve full page content as needed.

<Note>
  &#x20;**Beta Notice**: This API is currently in beta and subject to change, and
  requires the <code>parallel-beta: search-extract-2025-10-10</code> header. Usage is
  limited to 600 requests per minute; for production access or higher capacity, contact
  [support@parallel.ai](mailto:support@parallel.ai).
</Note>

## Key Benefits

* Search with Natural Language: Describe what you're looking for in plain language and
  handle complex, multi-faceted queries in a single request—no need for multiple
  overlapping keyword searches.

* Intelligent Token Efficiency: Automatically include only the tokens necessary for the
  task at hand. Simple factual queries return concise excerpts; complex research
  objectives return comprehensive content. No wasted tokens on irrelevant information.

* Advanced Content Extraction: Extract clean, structured markdown from any web page—even
  those requiring JavaScript execution or PDF rendering. Focus extraction on your
  specific objective to get only relevant content, or retrieve full page content when
  needed.

* Speed: Reduce latency and improve quality by replacing multi-step pipelines with
  fewer, smarter API calls.

* Quality: Powered by Parallel's web-scale index with advanced ranking that prioritizes
  relevance, clarity, and source reliability.

## Request Fields

The Extract API accepts the following parameters. The `urls` field is required; all
other fields are optional. See the [API\
Reference](/api-reference/extract-beta/extract) for complete parameter
specifications and constraints.

| Field           | Type           | Default  | Notes                                                                                                                                                                                           | Example                                                                                                      |
| --------------- | -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| urls            | string\[]      | -        | List of URLs to extract content from. Maximum 10 URLs per request.                                                                                                                              | \["[https://example.com/article](https://example.com/article)"]                                              |
| objective       | string         | optional | Natural-language description of what information you're looking for, including broader task context. When provided, focuses extracted content on relevant information. Maximum 3000 characters. | "I'm researching React performance optimization. Find best practices for preventing unnecessary re-renders." |
| search\_queries | string\[]      | optional | Optional keyword queries to focus extraction. Use with or without objective to emphasize specific terms.                                                                                        | \["React.memo", "useMemo", "useCallback"]                                                                    |
| fetch\_policy   | object         | dynamic  | Controls when to return indexed vs fresh content. If not provided, a dynamic policy will be used based on the search objective and url. See [Fetch Policy](#fetch-policy) below.                | `{"max_age_seconds": 3600}`                                                                                  |
| excerpts        | bool or object | true     | Return focused excerpts relevant to objective/queries. Set to `false` to disable or pass settings object.                                                                                       | `true` or `{"max_chars_per_result": 5000, "max_chars_total": 25000}`                                         |
| full\_content   | bool or object | false    | Return complete page content. Set to `true` to enable or pass settings object.                                                                                                                  | `false` or `{"max_chars_per_result": 50000}`                                                                 |

## Fetch Policy

The `fetch_policy` parameter controls when to return indexed content (faster) or fetch
fresh content from the source (fresher). Fetching fresh content may take up to a minute
and is subject to rate limits to manage the load on source websites.

| Field                    | Type   | Default | Notes                                                                                                                                                        |
| ------------------------ | ------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| max\_age\_seconds        | int    | dynamic | Maximum age of indexed content in seconds. If older, fetches live. Minimum 600 (10 minutes). If unspecified, uses dynamic policy based on URL and objective. |
| timeout\_seconds         | number | dynamic | Timeout for fetching live content. If unspecified, uses uses a dynamic timeout based on URL and content type (typically 15s-60s).                            |
| disable\_cache\_fallback | bool   | false   | If `true`, returns an error when live fetch fails. If `false`, falls back to older indexed content.                                                          |

## Excerpt and Full Content Settings

Both `excerpts` and `full_content` accept either a boolean or a settings object.

**Boolean usage:**

```json wrap theme={"system"}
{
  "excerpts": true,
  "full_content": false
}
```

**Settings object:**

```json wrap theme={"system"}
{
  "excerpts": {
    "max_chars_per_result": 5000
  },
  "full_content": {
    "max_chars_per_result": 50000
  }
}
```

**Notes:**

* When both `excerpts` and `full_content` are enabled, you'll receive both in the response
* Excerpts are always focused on relevance; full content always starts from the beginning
* Without `objective` or `search_queries`, excerpts will be redundant with full content

## Best Practices

See [Search Best Practices](/search/best-practices#best-practices) on using
objective and search queries effectively.

# Refresh Runs
Source: https://docs.parallel.ai/findall-api/features/findall-refresh

Rerun the same FindAll query with exclude_list to discover net new entities over time

## Overview

Scheduled jobs allow you to run the same FindAll query on a regular basis to discover newly emerging entities and track changes to existing ones. This is ideal for ongoing monitoring use cases like market intelligence, lead generation, or competitive tracking.

Rather than manually re-running queries, you can programmatically create new FindAll runs using a previous run's schema, while excluding candidates you've already discovered.

## Use Cases

Scheduled FindAll jobs are particularly useful for:

* **Market monitoring**: Track new companies entering a market space over time
* **Lead generation**: Continuously discover new potential customers matching your criteria
* **Competitive intelligence**: Monitor emerging competitors and new funding announcements
* **Investment research**: Track new companies meeting specific investment criteria
* **Regulatory compliance**: Discover new entities that may require compliance review

## How It Works

Creating a scheduled FindAll job involves two steps:

1. **Retrieve the schema** from a previous successful run
2. **Create a new run** using that schema, with an exclude list of previously discovered candidates

This approach ensures:

* **Consistent criteria**: Use the exact same evaluation logic across runs
* **No duplicates**: Automatically exclude candidates from previous runs
* **Cost efficiency**: Only pay to evaluate net new candidates

## Step 1: Retrieve the Schema

Get the schema from a completed FindAll run to reuse its `entity_type`, `match_conditions`, and `enrichments`:

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -X GET "https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/schema" \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H "parallel-beta: findall-2025-09-15"
  ```

  ```python Python theme={"system"}
  from parallel import Parallel

  client = Parallel(api_key="YOUR_API_KEY")

  schema = client.beta.findall.schema(
      findall_id="findall_40e0ab8c10754be0b7a16477abb38a2f"
  )
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from 'parallel-web';

  const client = new Parallel({
    apiKey: process.env.PARALLEL_API_KEY
  });

  const schema = await client.beta.findall.schema({
    findallId: "findall_40e0ab8c10754be0b7a16477abb38a2f"
  });
  ```
</CodeGroup>

**Response:**

```json theme={"system"}
{
  "objective": "Find all portfolio companies of Khosla Ventures founded after 2020",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "khosla_ventures_portfolio_check",\
      "description": "Company must be a portfolio company of Khosla Ventures."\
    },\
    {\
      "name": "founded_after_2020_check",\
      "description": "Company must have been founded after 2020."\
    }\
  ],
  "enrichments": [\
    {\
      "name": "funding_amount",\
      "description": "Total funding raised by the company in USD"\
    }\
  ],
  "generator": "core",
  "match_limit": 50
}
```

## Step 2: Create a New Run with `exclude_list`

Use the retrieved schema to create a new FindAll run, adding an `exclude_list` parameter to skip candidates you've already discovered:

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -X POST "https://api.parallel.ai/v1beta/findall/runs" \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H "parallel-beta: findall-2025-09-15" \
    -H "Content-Type: application/json" \
    -d '{
      "objective": "Find all portfolio companies of Khosla Ventures founded after 2020",
      "entity_type": "companies",
      "match_conditions": [\
        {\
          "name": "khosla_ventures_portfolio_check",\
          "description": "Company must be a portfolio company of Khosla Ventures."\
        },\
        {\
          "name": "founded_after_2020_check",\
          "description": "Company must have been founded after 2020."\
        }\
      ],
      "enrichments": [\
        {\
          "name": "funding_amount",\
          "description": "Total funding raised by the company in USD"\
        }\
      ],
      "generator": "core",
      "match_limit": 50,
      "exclude_list": [\
        {\
          "name": "Anthropic",\
          "url": "https://www.anthropic.com/"\
        },\
        {\
          "name": "Adept AI",\
          "url": "https://adept.ai/"\
        },\
        {\
          "name": "Liquid AI",\
          "url": "https://www.liquid.ai/"\
        }\
      ]
    }'
  ```

  ```python Python theme={"system"}
  from parallel import Parallel

  client = Parallel(api_key="YOUR_API_KEY")

  findall_run = client.beta.findall.create(
      objective="Find all portfolio companies of Khosla Ventures founded after 2020",
      entity_type="companies",
      match_conditions=[\
          {\
              "name": "khosla_ventures_portfolio_check",\
              "description": "Company must be a portfolio company of Khosla Ventures."\
          },\
          {\
              "name": "founded_after_2020_check",\
              "description": "Company must have been founded after 2020."\
          }\
      ],
      enrichments=[\
          {\
              "name": "funding_amount",\
              "description": "Total funding raised by the company in USD"\
          }\
      ],
      generator="core",
      match_limit=50,
      exclude_list=[\
          {\
              "name": "Anthropic",\
              "url": "https://www.anthropic.com/"\
          },\
          {\
              "name": "Adept AI",\
              "url": "https://adept.ai/"\
          },\
          {\
              "name": "Liquid AI",\
              "url": "https://www.liquid.ai/"\
          }\
      ]
  )
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from 'parallel-web';

  const client = new Parallel({
    apiKey: process.env.PARALLEL_API_KEY
  });

  const run = await client.beta.findall.create({
    objective: "Find all portfolio companies of Khosla Ventures founded after 2020",
    entity_type: "companies",
    match_conditions: [\
      {\
        name: "khosla_ventures_portfolio_check",\
        description: "Company must be a portfolio company of Khosla Ventures."\
      },\
      {\
        name: "founded_after_2020_check",\
        description: "Company must have been founded after 2020."\
      }\
    ],
    enrichments: [\
      {\
        name: "funding_amount",\
        description: "Total funding raised by the company in USD"\
      }\
    ],
    generator: "core",
    match_limit: 50,
    exclude_list: [\
      {\
        name: "Anthropic",\
        url: "https://www.anthropic.com/"\
      },\
      {\
        name: "Adept AI",\
        url: "https://adept.ai/"\
      },\
      {\
        name: "Liquid AI",\
        url: "https://www.liquid.ai/"\
      }\
    ]
  });
  ```
</CodeGroup>

### Exclude List Parameters

The `exclude_list` is an array of candidate objects to exclude. Each object contains:

| Parameter | Type   | Required | Description                      |
| --------- | ------ | -------- | -------------------------------- |
| `name`    | string | Yes      | Name of the candidate to exclude |
| `url`     | string | Yes      | URL of the candidate to exclude  |

**How exclusions work:**

* Candidates matching any entry in the `exclude_list` will be skipped during generation
* This prevents re-evaluating entities you've already processed
* Exclusions are matched by URL—ensure URLs are normalized consistently across runs

## Building Your Exclude List

To construct the `exclude_list` from previous runs, retrieve the matched candidates and extract their `name` and `url` fields:

```bash cURL theme={"system"}
curl -X GET "https://api.parallel.ai/v1beta/findall/runs/findall_40e0ab8c10754be0b7a16477abb38a2f/result" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: findall-2025-09-15"
```

Extract the `name` and `url` fields from each matched candidate:

```json theme={"system"}
{
  "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
  "candidates": [\
    {\
      "candidate_id": "candidate_abc123",\
      "name": "Anthropic",\
      "url": "https://www.anthropic.com/",\
      "match_status": "matched",\
      ...\
    },\
    {\
      "candidate_id": "candidate_def456",\
      "name": "Adept AI",\
      "url": "https://adept.ai/",\
      "match_status": "matched",\
      ...\
    }\
  ]
}
```

Store these candidates and pass them as the `exclude_list` array in subsequent runs.

## Example: Weekly Scheduled Job

Here's a complete example showing how to set up a weekly FindAll job:

<CodeGroup>
  ```python Python theme={"system"}
  import requests
  import time
  from datetime import datetime

  PARALLEL_API_KEY = "your_api_key"
  BASE_URL = "https://api.parallel.ai/v1beta"
  HEADERS = {
      "x-api-key": PARALLEL_API_KEY,
      "parallel-beta": "findall-2025-09-15",
      "Content-Type": "application/json"
  }

  # Store the original findall_id from your first run
  ORIGINAL_FINDALL_ID = "findall_40e0ab8c10754be0b7a16477abb38a2f"

  # Keep track of all discovered candidates across runs
  all_discovered_candidates = []

  def get_schema(findall_id):
      """Retrieve schema from a previous run"""
      response = requests.get(
          f"{BASE_URL}/findall/runs/{findall_id}/schema",
          headers=HEADERS
      )
      response.raise_for_status()
      return response.json()

  def get_matched_candidates(findall_id):
      """Get all matched candidates from a run"""
      response = requests.get(
          f"{BASE_URL}/findall/runs/{findall_id}/result",
          headers=HEADERS
      )
      response.raise_for_status()
      candidates = response.json().get("candidates", [])
      return [c for c in candidates if c.get("match_status") == "matched"]

  def create_scheduled_run(schema, exclude_candidates):
      """Create a new FindAll run with exclusions"""
      payload = {
          **schema,
          "generator": "core",
          "match_limit": 50,
          "exclude_list": exclude_candidates
      }

      response = requests.post(
          f"{BASE_URL}/findall/runs",
          headers=HEADERS,
          json=payload
      )
      response.raise_for_status()
      return response.json()["findall_id"]

  def run_weekly_job():
      """Execute a scheduled FindAll job"""
      print(f"Starting scheduled job at {datetime.now()}")

      # Step 1: Get schema from original run
      schema = get_schema(ORIGINAL_FINDALL_ID)
      print(f"Retrieved schema: {schema['objective']}")

      # Step 2: Create new run with exclusions
      new_findall_id = create_scheduled_run(schema, all_discovered_candidates)
      print(f"Created new run: {new_findall_id}")

      # Step 3: Poll for completion (simplified)
      while True:
          response = requests.get(
              f"{BASE_URL}/findall/runs/{new_findall_id}",
              headers=HEADERS
          )
          status = response.json()["status"]["status"]

          if status in ["completed", "failed", "cancelled"]:
              break

          time.sleep(30)  # Poll every 30 seconds

      # Step 4: Get new matched candidates
      new_candidates = get_matched_candidates(new_findall_id)
      print(f"Found {len(new_candidates)} new candidates")

      # Step 5: Update exclude list for next run
      for candidate in new_candidates:
          all_discovered_candidates.append({
              "name": candidate["name"],
              "url": candidate["url"]
          })

      return new_candidates

  # Run the job
  if __name__ == "__main__":
      new_results = run_weekly_job()
  ```

  ```typescript TypeScript theme={"system"}
  import axios from 'axios';

  const PARALLEL_API_KEY = 'your_api_key';
  const BASE_URL = 'https://api.parallel.ai/v1beta';
  const HEADERS = {
    'x-api-key': PARALLEL_API_KEY,
    'parallel-beta': 'findall-2025-09-15',
    'Content-Type': 'application/json',
  };

  // Store the original findall_id from your first run
  const ORIGINAL_FINDALL_ID = 'findall_40e0ab8c10754be0b7a16477abb38a2f';

  // Keep track of all discovered candidates across runs
  let allDiscoveredCandidates: Array<{ name: string; url: string }> = [];

  async function getSchema(findallId: string) {
    const response = await axios.get(
      `${BASE_URL}/findall/runs/${findallId}/schema`,
      { headers: HEADERS }
    );
    return response.data;
  }

  async function getMatchedCandidates(findallId: string) {
    const response = await axios.get(
      `${BASE_URL}/findall/runs/${findallId}/result`,
      { headers: HEADERS }
    );
    const candidates = response.data.candidates || [];
    return candidates.filter((c: any) => c.match_status === "matched");
  }

  async function createScheduledRun(
    schema: any,
    excludeCandidates: Array<{ name: string; url: string }>
  ) {
    const payload = {
      ...schema,
      generator: 'core',
      match_limit: 50,
      exclude_list: excludeCandidates,
    };

    const response = await axios.post(
      `${BASE_URL}/findall/runs`,
      payload,
      { headers: HEADERS }
    );
    return response.data.findall_id;
  }

  async function runWeeklyJob() {
    console.log(`Starting scheduled job at ${new Date()}`);

    // Step 1: Get schema from original run
    const schema = await getSchema(ORIGINAL_FINDALL_ID);
    console.log(`Retrieved schema: ${schema.objective}`);

    // Step 2: Create new run with exclusions
    const newFindallId = await createScheduledRun(schema, allDiscoveredCandidates);
    console.log(`Created new run: ${newFindallId}`);

    // Step 3: Poll for completion
    let status = 'running';
    while (!['completed', 'failed', 'cancelled'].includes(status)) {
      await new Promise(resolve => setTimeout(resolve, 30000)); // Wait 30 seconds

      const response = await axios.get(
        `${BASE_URL}/findall/runs/${newFindallId}`,
        { headers: HEADERS }
      );
      status = response.data.status.status;
    }

    // Step 4: Get new matched candidates
    const newCandidates = await getMatchedCandidates(newFindallId);
    console.log(`Found ${newCandidates.length} new candidates`);

    // Step 5: Update exclude list for next run
    newCandidates.forEach((candidate: any) => {
      allDiscoveredCandidates.push({
        name: candidate.name,
        url: candidate.url,
      });
    });

    return newCandidates;
  }

  // Run the job
  runWeeklyJob();
  ```
</CodeGroup>

## Best Practices

### Schema Modifications

While you should keep `match_conditions` consistent across runs, you can adjust:

* **`objective`**: Update to reflect the current time period (e.g., "founded in 2024" → "founded in 2025")
* **`enrichments`**: Add new enrichment fields without affecting matching logic
* **`match_limit`**: Adjust based on expected growth rate
* **`generator`**: Change generators if needed (though this may affect result quality)

### Exclude List Management

* **Persist candidates**: Store discovered candidate objects (name and URL) in a database or file for long-term tracking
* **Normalize URLs**: Ensure consistent URL formatting (trailing slashes, protocols, etc.) across runs
* **Periodic resets**: Consider occasionally running without exclusions to catch entities that may have changed
* **Monitor list size**: Very large exclude lists (>10,000 candidates) may impact performance

### Scheduling

* **Frequency**: Choose intervals based on your domain's update rate (daily, weekly, monthly)
* **Off-peak hours**: Schedule jobs during low-traffic periods if possible
* **Webhooks**: Use [webhooks](/findall-api/features/findall-webhook) to get notified when jobs complete
* **Error handling**: Implement retry logic for failed runs

### Cost Optimization

* **Start small**: Use lower `match_limit` values initially, then [extend](/findall-api/features/findall-extend) if needed
* **Preview first**: Test schema changes with [preview](/findall-api/features/findall-preview) before running full jobs
* **Monitor metrics**: Track `generated_candidates_count` vs `matched_candidates_count` to optimize criteria

## Related Topics

* **[Preview](/findall-api/features/findall-preview)**: Test queries with \~10 candidates before running full searches
* **[Generators and Pricing](/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
* **[Enrichments](/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
* **[Extend Runs](/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
* **[Webhooks](/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
* **[Streaming Events](/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
* **[Run Lifecycle](/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and how to cancel runs
* **[API Reference](/api-reference/findall-api-beta/get-findall-run-schema)**: Complete endpoint documentation

# Webhooks
Source: https://docs.parallel.ai/findall-api/features/findall-webhook

Receive real-time notifications on FindAll runs and candidates using webhooks

<Note>
  **Prerequisites:** Before implementing FindAll webhooks, read **[Webhook Setup & Verification](/resources/webhook-setup)** for critical information on:

  * Recording your webhook secret
  * Verifying HMAC signatures
  * Security best practices
  * Retry policies

  This guide focuses on FindAll-specific webhook events and payloads.
</Note>

## Overview

Webhooks allow you to receive real-time notifications when candidates are discovered, evaluated, or when your FindAll runs complete, eliminating the need for constant polling—especially useful for long-running FindAll operations that may process many candidates over time.

## Setup

To register a webhook for a FindAll run, include a `webhook` parameter in your FindAll run creation request:

<CodeGroup>
  ```bash cURL theme={"system"}
  curl --request POST \
    --url https://api.parallel.ai/v1beta/findall/runs \
    --header "Content-Type: application/json" \
    --header "x-api-key: $PARALLEL_API_KEY" \
    --header "parallel-beta: findall-2025-09-15" \
    --data '{
      "objective": "Find all portfolio companies of Khosla Ventures",
      "entity_type": "companies",
      "match_conditions": [\
        {\
          "name": "khosla_ventures_portfolio_check",\
          "description": "Company must be a portfolio company of Khosla Ventures."\
        }\
      ],
      "generator": "core",
      "match_limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhooks/findall",
        "event_types": [\
          "findall.candidate.generated",\
          "findall.candidate.matched",\
          "findall.candidate.unmatched",\
          "findall.candidate.enriched",\
          "findall.run.completed",\
          "findall.run.cancelled",\
          "findall.run.failed"\
        ]
      }
    }
  ```

  ```python Python theme={"system"}
  from parallel import Parallel

  client = Parallel(api_key="YOUR_API_KEY")

  findall_run = client.beta.findall.create(
      objective="Find all portfolio companies of Khosla Ventures",
      entity_type="companies",
      match_conditions=[\
          {\
              "name": "khosla_ventures_portfolio_check",\
              "description": "Company must be a portfolio company of Khosla Ventures."\
          }\
      ],
      generator="core",
      match_limit=100,
      webhook={
          "url": "https://your-domain.com/webhooks/findall",
          "event_types": [\
              "findall.candidate.generated",\
              "findall.candidate.matched",\
              "findall.candidate.unmatched",\
              "findall.candidate.enriched",\
              "findall.run.completed",\
              "findall.run.cancelled",\
              "findall.run.failed"\
          ]
      }
  )
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from 'parallel-web';

  const client = new Parallel({
    apiKey: process.env.PARALLEL_API_KEY
  });

  const run = await client.beta.findall.create({
    objective: "Find all portfolio companies of Khosla Ventures",
    entity_type: "companies",
    match_conditions: [\
      {\
        name: "khosla_ventures_portfolio_check",\
        description: "Company must be a portfolio company of Khosla Ventures."\
      }\
    ],
    generator: "core",
    match_limit: 100,
    webhook: {
      url: "https://your-domain.com/webhooks/findall",
      event_types: [\
        "findall.candidate.generated",\
        "findall.candidate.matched",\
        "findall.candidate.unmatched",\
        "findall.candidate.enriched",\
        "findall.run.completed",\
        "findall.run.cancelled",\
        "findall.run.failed"\
      ]
    }
  });
  ```
</CodeGroup>

### Webhook Parameters

| Parameter     | Type           | Required | Description                                                  |
| ------------- | -------------- | -------- | ------------------------------------------------------------ |
| `url`         | string         | Yes      | Your webhook endpoint URL. Can be any domain.                |
| `event_types` | array\[string] | Yes      | Array of event types to subscribe to. See Event Types below. |

## Event Types

FindAll supports the following webhook event types:

| Event Type                    | Description                                                         |
| ----------------------------- | ------------------------------------------------------------------- |
| `findall.candidate.generated` | Emitted when a new candidate is generated and queued for evaluation |
| `findall.candidate.matched`   | Emitted when a candidate successfully matches all match conditions  |
| `findall.candidate.unmatched` | Emitted when a candidate fails to match all conditions              |
| `findall.candidate.enriched`  | Emitted when enrichment data has been extracted for a candidate     |
| `findall.run.completed`       | Emitted when a FindAll run completes successfully                   |
| `findall.run.cancelled`       | Emitted when a FindAll run is cancelled                             |
| `findall.run.failed`          | Emitted when a FindAll run fails due to an error                    |

You can subscribe to any combination of these event types in your webhook configuration.

<Note>
  For a complete guide to candidate object structure, states, and fields, see [Candidates](/findall-api/core-concepts/findall-candidates).
</Note>

## Webhook Payload Structure

Each webhook payload contains:

* `timestamp`: ISO 8601 timestamp of when the event occurred
* `type`: Event type
* `data`: Event-specific payload (FindAll Candidate or Run object)

### Candidate Events

<CodeGroup>
  ```json findall.candidate.generated theme={"system"}
  {
    "type": "findall.candidate.generated",
    "timestamp": "2025-10-27T14:56:05.619331Z",
    "data": {
      "candidate_id": "candidate_2edf2301-f80d-46b9-b17a-7b4a9d577296",
      "name": "Anthropic",
      "url": "https://www.anthropic.com/",
      "description": "Anthropic is an AI safety and research company founded in 2021...",
      "match_status": "generated",
      "output": null,
      "basis": null
    }
  }
  ```

  ```json findall.candidate.matched theme={"system"}
  {
    "type": "findall.candidate.matched",
    "timestamp": "2025-10-27T14:57:15.421087Z",
    "data": {
      "candidate_id": "candidate_478fb5ca-4581-4411-9acb-6b78b4cb5bcf",
      "name": "Vivodyne",
      "url": "https://vivodyne.com/",
      "description": "Vivodyne is a biotechnology company...",
      "match_status": "matched",
      "output": {
        "founded_after_2020_check": {
          "value": "2021",
          "type": "match_condition",
          "is_matched": true
        }
      },
      "basis": [\
        {\
          "field": "founded_after_2020_check",\
          "citations": [\
            {\
              "title": "Vivodyne - Crunchbase Company Profile & Funding",\
              "url": "https://www.crunchbase.com/organization/vivodyne",\
              "excerpts": ["Founded in 2021"]\
            }\
          ],\
          "reasoning": "Multiple sources indicate that Vivodyne was founded in 2021...",\
          "confidence": "high"\
        }\
      ]
    }
  }
  ```

  ```json findall.candidate.unmatched theme={"system"}
  {
    "type": "findall.candidate.unmatched",
    "timestamp": "2025-10-27T14:57:20.521203Z",
    "data": {
      "candidate_id": "candidate_abc123-def456-789",
      "name": "Example Company",
      "url": "https://example.com/",
      "description": "Example Company description...",
      "match_status": "unmatched",
      "output": {
        "founded_after_2020_check": {
          "value": "2018",
          "type": "match_condition",
          "is_matched": false
        }
      },
      "basis": [\
        {\
          "field": "founded_after_2020_check",\
          "citations": [...],\
          "reasoning": "The company was founded in 2018, which is before 2020...",\
          "confidence": "high"\
        }\
      ]
    }
  }
  ```
</CodeGroup>

### Run Events

<CodeGroup>
  ```json findall.run.completed theme={"system"}
  {
    "type": "findall.run.completed",
    "timestamp": "2025-10-27T14:58:39.421087Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "status": {
        "status": "completed",
        "is_active": false,
        "metrics": {
          "generated_candidates_count": 5,
          "matched_candidates_count": 1
        },
        "termination_reason": "match_limit_met"
      },
      "generator": "core",
      "metadata": {},
      "created_at": "2025-10-27T14:56:05.619331Z",
      "modified_at": "2025-10-27T14:58:39.421087Z"
    }
  }
  ```

  ```json findall.run.cancelled theme={"system"}
  {
    "type": "findall.run.cancelled",
    "timestamp": "2025-10-27T14:57:00.123456Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "status": {
        "status": "cancelled",
        "is_active": false,
        "metrics": {
          "generated_candidates_count": 3,
          "matched_candidates_count": 0
        },
        "termination_reason": "user_cancelled"
      },
      "generator": "core",
      "metadata": {},
      "created_at": "2025-10-27T14:56:05.619331Z",
      "modified_at": "2025-10-27T14:57:00.123456Z"
    }
  }
  ```

  ```json findall.run.failed theme={"system"}
  {
    "type": "findall.run.failed",
    "timestamp": "2025-10-27T14:57:30.789012Z",
    "data": {
      "findall_id": "findall_40e0ab8c10754be0b7a16477abb38a2f",
      "status": {
        "status": "failed",
        "is_active": false,
        "metrics": {
          "generated_candidates_count": 2,
          "matched_candidates_count": 0
        },
        "termination_reason": "error_occurred"
      },
      "generator": "core",
      "metadata": {},
      "created_at": "2025-10-27T14:56:05.619331Z",
      "modified_at": "2025-10-27T14:57:30.789012Z"
    }
  }
  ```
</CodeGroup>

## Security & Verification

For information on HMAC signature verification, including code examples in multiple languages, see the [Webhook Setup Guide - Security & Verification](/resources/webhook-setup#security--verification) section.

## Retry Policy

See the [Webhook Setup Guide - Retry Policy](/resources/webhook-setup#retry-policy) for details on webhook delivery retry configuration.

## Best Practices

For webhook implementation best practices, including signature verification, handling duplicates, and async processing, see the [Webhook Setup Guide - Best Practices](/resources/webhook-setup#best-practices) section.

## Related Topics

* **[Preview](/findall-api/features/findall-preview)**: Test queries with \~10 candidates before running full searches
* **[Generators and Pricing](/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
* **[Enrichments](/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
* **[Extend Runs](/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
* **[Streaming Events](/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
* **[Run Lifecycle](/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and how to cancel runs
* **[API Reference](/api-reference/findall-api-beta/create-findall-run#body-webhook)**: Complete endpoint documentation

# FindAll Migration Guide
Source: https://docs.parallel.ai/findall-api/findall-migration-guide

Guide for migrating from V0 to V1 FindAll API

<Note>
  **Timeline**: Both APIs are currently available. Include the `parallel-beta: "findall-2025-09-15"` header to use V1 API. Without this header, requests default to V0 API.
</Note>

## Why Migrate to V1?

V1 delivers significant improvements across pricing, performance, and capabilities:

1. **[Pay-per-Match Pricing](/findall-api/core-concepts/findall-generator-pricing)**: Charges based on matches found, not candidates evaluated

2. **[Task-Powered Enrichments](/findall-api/features/findall-enrich)**: Flexible enrichments via Task API with expanded processor options

3. **Enhanced Capabilities:**
   * [Extend](/findall-api/features/findall-extend), [Cancel](/findall-api/features/findall-cancel), and [Preview](/findall-api/features/findall-preview) endpoints
   * [Real-time streaming](/findall-api/features/findall-sse) with incremental updates
   * [Exclude candidates](/findall-api/core-concepts/findall-candidates) from evaluation
   * Match conditions return both `value` and `is_matched` boolean
   * Increased `match_limit` from 200 to 1,000

4. **Better Performance**: Improved latency and match quality across all stages

<Warning>
  **Breaking Changes**: V1 is not backward compatible. V0 runs cannot be accessed via V1 endpoints. Parameter names, response schemas, and pricing have changed.
</Warning>

## Key Differences

### Request Structure

V0 used a nested `findall_spec` object. V1 flattens this structure:

| **Concept**         | **V0 API**                               | **V1 API**                            |
| ------------------- | ---------------------------------------- | ------------------------------------- |
| **Required Header** | None                                     | `parallel-beta: "findall-2025-09-15"` |
| **Search Goal**     | `query`                                  | `objective`                           |
| **Entity Type**     | `findall_spec.name`                      | `entity_type`                         |
| **Filter Criteria** | `findall_spec.columns` (type=constraint) | `match_conditions`                    |
| **Model Selection** | `processor`                              | `generator`                           |
| **Max Results**     | `result_limit` (max: 200)                | `match_limit` (max: 1,000)            |

### Response Structure

V0 included results in poll responses. V1 separates status and results:

| **Concept**         | **V0 API**                                             | **V1 API**                             |
| ------------------- | ------------------------------------------------------ | -------------------------------------- |
| **Status Check**    | `is_active` + `are_enrichments_active`                 | `status.is_active`                     |
| **Get Results**     | `GET /v1beta/findall/runs/{id}` (included in response) | `GET /v1beta/findall/runs/{id}/result` |
| **Results Array**   | `results`                                              | `candidates`                           |
| **Relevance Score** | `score`                                                | `relevance_score`                      |
| **Match Data**      | `filter_results` (array)                               | `output` (object)                      |
| **Field Access**    | Loop through array to find key                         | Direct: `output[field_name]["value"]`  |

### Enrichment Handling

V0 included enrichments in initial spec. V1 adds them via separate endpoint:

| **Aspect**            | **V0 API**                                | **V1 API**                                                  |
| --------------------- | ----------------------------------------- | ----------------------------------------------------------- |
| **Definition**        | Part of `columns` array (type=enrichment) | Separate `POST /v1beta/findall/runs/{id}/enrich` call       |
| **Timing**            | At run creation only                      | Anytime after run creation (multiple enrichments supported) |
| **Output Format**     | Separate `enrichment_results` array       | Merged into `output` object with type=enrichment            |
| **Processor Options** | Limited to FindAll processors             | All Task API processors available                           |

## End-to-End Migration Example

This example shows the complete workflow migration, including enrichments:

<CodeGroup>
  ```python V0 API [expandable] theme={"system"}
  import requests
  import time

  API_KEY = "your_api_key"
  BASE_URL = "https://api.parallel.ai"

  # Step 1: Ingest query
  ingest_response = requests.post(
      f"{BASE_URL}/v1beta/findall/ingest",
      headers={"x-api-key": API_KEY},
      json={"query": "Find AI companies that raised Series A in 2024 and get CEO names"}
  )
  findall_spec = ingest_response.json()

  # Step 2: Create run (constraints + enrichments together)
  run_response = requests.post(
      f"{BASE_URL}/v1beta/findall/runs",
      headers={"x-api-key": API_KEY},
      json={
          "findall_spec": findall_spec,
          "processor": "core",
          "result_limit": 100
      }
  )
  findall_id = run_response.json()["findall_id"]

  # Step 3: Poll until both flags are false
  while True:
      poll_response = requests.get(
          f"{BASE_URL}/v1beta/findall/runs/{findall_id}",
          headers={"x-api-key": API_KEY}
      )
      result = poll_response.json()
      if not result["is_active"] and not result["are_enrichments_active"]:
          break
      time.sleep(15)

  # Step 4: Access results from poll response
  for entity in result["results"]:
      print(f"{entity['name']}: Score {entity['score']}")

      # Loop through arrays to find values
      for filter_result in entity["filter_results"]:
          print(f"  {filter_result['key']}: {filter_result['value']}")
      for enrichment in entity["enrichment_results"]:
          print(f"  {enrichment['key']}: {enrichment['value']}")
  ```

  ```python V1 API [expandable] theme={"system"}
  import requests
  import time

  API_KEY = "your_api_key"
  BASE_URL = "https://api.parallel.ai"
  headers = {
      "x-api-key": API_KEY,
      "parallel-beta": "findall-2025-09-15"
  }

  # Step 1: Ingest objective
  ingest_response = requests.post(
      f"{BASE_URL}/v1beta/findall/ingest",
      headers=headers,
      json={"objective": "Find AI companies that raised Series A in 2024 and get CEO names"}
  )
  ingest_data = ingest_response.json()

  # Step 2: Create run (constraints only, flattened)
  run_response = requests.post(
      f"{BASE_URL}/v1beta/findall/runs",
      headers=headers,
      json={
          "objective": ingest_data["objective"],
          "entity_type": ingest_data["entity_type"],
          "match_conditions": ingest_data["match_conditions"],
          "generator": "core",
          "match_limit": 50
      }
  )
  findall_id = run_response.json()["findall_id"]

  # Step 3: Add enrichments (separate call)
  time.sleep(5)
  requests.post(
      f"{BASE_URL}/v1beta/findall/runs/{findall_id}/enrich",
      headers=headers,
      json={
          "processor": "core",
          "output_schema": ingest_data.get("enrichments")[0]
      }
  )

  # Step 4: Poll until completed
  while True:
      status_response = requests.get(
          f"{BASE_URL}/v1beta/findall/runs/{findall_id}",
          headers=headers
      )
      if status_response.json()["status"]["status"] == "completed":
          break
      time.sleep(10)

  # Step 5: Fetch results from separate endpoint
  result_response = requests.get(
      f"{BASE_URL}/v1beta/findall/runs/{findall_id}/result",
      headers=headers
  )
  result = result_response.json()

  # Step 6: Access results with direct object access
  for candidate in result["candidates"]:
      if candidate["match_status"] == "matched":
          print(f"{candidate['name']}: Score {candidate['relevance_score']}")

          # Direct access to all fields (constraints + enrichments merged)
          for field_name, field_data in candidate["output"].items():
              print(f"  {field_name}: {field_data['value']}")
  ```
</CodeGroup>

## Migration Checklist

Complete these steps to migrate from V0 to V1:

### Core Changes

* Add `parallel-beta: "findall-2025-09-15"` header to all requests
* Change ingest parameter: `query` → `objective`
* Flatten run request: extract `objective`, `entity_type`, `match_conditions` from `findall_spec`
* Rename: `result_limit` → `match_limit`, `processor` → `generator`
* Update status check: `status.status == "completed"` instead of checking two flags
* Fetch results from separate `/result` endpoint
* Update result parsing: `results` → `candidates`, `score` → `relevance_score`
* Change field access: direct object access (`output[field]`) vs array iteration

### Enrichment Changes (if applicable)

* Move enrichments to separate `POST /enrich` call after run creation
* Convert enrichment columns to `output_schema` format (see [Task API](/task-api/guides/specify-a-task#output-schema))
* Update result access: enrichments now merged into `output` object

### Optional Enhancements

* Implement streaming via `/events` endpoint for real-time updates
* Add `exclude_list` to filter out specific candidates
* Use `preview: true` for testing queries before full runs
* Implement `/extend` endpoint to increase match limits dynamically
* Implement `/cancel` endpoint to stop runs early

### Testing

* Validate queries in development environment
* Review pricing impact with generator-based model
* Update error handling for new response schemas
* Monitor performance metrics

## Related Topics

### Core Concepts

* **[Quickstart](/findall-api/findall-quickstart)**: Get started with V1 FindAll API
* **[Candidates](/findall-api/core-concepts/findall-candidates)**: Understand candidate object structure and states
* **[Generators and Pricing](/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
* **[Run Lifecycle](/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and termination

### Features

* **[Preview](/findall-api/features/findall-preview)**: Test queries with \~10 candidates before running full searches
* **[Enrichments](/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
* **[Extend Runs](/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
* **[Cancel Runs](/findall-api/features/findall-cancel)**: Stop runs early to save costs
* **[Streaming Events](/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
* **[Webhooks](/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches

# Glossary
Source: https://docs.parallel.ai/getting-started/glossary

Key terms and concepts used throughout Parallel's documentation

| Term                         | Definition                                                                                                                                                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API key                      | A unique identifier used to authenticate requests to Parallel APIs. Generate your API key at [platform.parallel.ai](https://platform.parallel.ai).                                                                                                                        |
| Asynchronous API             | An API that returns a run ID immediately and processes the request in the background. Task, FindAll, and Monitor APIs are asynchronous. Poll for status or use webhooks to receive results.                                                                               |
| Cadence                      | The frequency at which a monitor executes: `hourly`, `daily`, or `weekly`.                                                                                                                                                                                                |
| Candidate                    | A potential entity discovered during a FindAll run. Candidates are generated from web data and evaluated against match conditions.                                                                                                                                        |
| Chat API                     | A synchronous API that provides OpenAI-compatible streaming chat completions with web-grounded responses. Supports both speed-optimized and research-grade models.                                                                                                        |
| Citation                     | A reference to a web source that contributed to an output field. Includes the URL and relevant excerpts from the source.                                                                                                                                                  |
| Confidence level             | A reliability rating for each output field: **high** (strong evidence from multiple authoritative sources), **medium** (adequate evidence with some inconsistencies), or **low** (limited or conflicting evidence).                                                       |
| Enrichment                   | Additional structured data extracted for matched candidates using the Task API. Enrichments run automatically on candidates that pass all match conditions.                                                                                                               |
| Event                        | A detected change or update that matches a monitor's query. Events include the detected information, event date, and source URLs.                                                                                                                                         |
| Event group                  | A collection of related events detected during a single monitor execution.                                                                                                                                                                                                |
| Excerpt                      | A focused portion of page content that's relevant to your objective. Optimized for LLM consumption.                                                                                                                                                                       |
| Extract API                  | A synchronous API that converts any public URL into clean, LLM-optimized markdown. Handles JavaScript-heavy pages and PDFs.                                                                                                                                               |
| Fast processor               | A processor variant optimized for speed over data freshness. Append `-fast` to any processor name (e.g., `core-fast`) for 2-5x faster response times.                                                                                                                     |
| FieldBasis                   | The specific object containing citations, reasoning, and confidence for an individual output field within the research basis.                                                                                                                                             |
| FindAll API                  | An asynchronous API for web-scale entity discovery. Turns natural language queries into structured, enriched databases by generating candidates, validating them against criteria, and optionally enriching matches.                                                      |
| FindAll run                  | A single execution of a FindAll query. Includes candidate generation, evaluation, and optional enrichment.                                                                                                                                                                |
| Generator                    | The engine that determines the quality and thoroughness of FindAll run results. Options include `preview`, `base`, `core`, and `pro`.                                                                                                                                     |
| Match condition              | A criterion that candidates must satisfy to be included in FindAll results. Defined in natural language as part of the query.                                                                                                                                             |
| Match status                 | The state of a candidate after evaluation: `matched` (satisfies all conditions), `unmatched` (fails one or more conditions), or `generated` (not yet evaluated).                                                                                                          |
| MCP (Model Context Protocol) | A protocol for connecting AI models to external tools and data sources. Parallel provides MCP servers for Search and Task APIs.                                                                                                                                           |
| Monitor                      | A scheduled query that continuously tracks the web for changes relevant to a specific topic.                                                                                                                                                                              |
| Monitor API                  | An asynchronous API for continuous web tracking. Creates scheduled queries that detect relevant changes and deliver updates via webhooks.                                                                                                                                 |
| Objective                    | A natural language description of what you're looking for. Used by Search and Extract APIs to focus results on relevant content.                                                                                                                                          |
| Processor                    | The engine that executes Task Runs. Processors vary in performance characteristics, latency, and reasoning depth. Options include `lite`, `base`, `core`, `core2x`, `pro`, `ultra`, `ultra2x`, `ultra4x`, and `ultra8x`. Each is available in standard and fast variants. |
| Rate limit                   | The maximum number of API requests allowed within a time period. See [Rate limits](/getting-started/rate-limits) for default quotas.                                                                                                                                      |
| Research Basis               | The structured explanation detailing the reasoning and evidence behind each Task Run result. Includes citations, reasoning, and confidence levels.                                                                                                                        |
| SDK                          | Software Development Kit. Parallel provides official SDKs for [Python](https://pypi.org/project/parallel-web/) and [TypeScript](https://www.npmjs.com/package/parallel-web).                                                                                              |
| Search API                   | A synchronous API that executes natural language web searches and returns LLM-optimized excerpts. Replaces multiple keyword searches with a single call for broad or complex queries.                                                                                     |
| Search query                 | A specific search term or phrase used to find relevant pages. Multiple search queries can be combined in a single Search API request.                                                                                                                                     |
| Source policy                | Configuration that controls which web sources can be accessed during research. Can include or exclude specific domains.                                                                                                                                                   |
| Synchronous API              | An API that returns results immediately in the response. Search, Extract, and Chat APIs are synchronous.                                                                                                                                                                  |
| Task API                     | An asynchronous API that combines AI inference with web search and live crawling to turn complex research tasks into repeatable workflows. Returns structured outputs with citations and confidence levels.                                                               |
| Task Group                   | A collection of Task Runs that can be executed and tracked together. Useful for batch processing multiple inputs.                                                                                                                                                         |
| Task Run                     | A single execution of a task specification. Each Task Run processes one input and produces one output with its associated research basis.                                                                                                                                 |
| Task spec                    | The definition of what a Task Run should accomplish. Includes input schema, output schema, and optional instructions.                                                                                                                                                     |
| Webhook                      | An HTTP callback that delivers notifications when specific events occur (e.g., task completion, monitor event detection).                                                                                                                                                 |

# Browser Use
Source: https://docs.parallel.ai/integrations/browseruse

Access private web data in Tasks using Browser Use MCP

Integrate Browser Use with the Parallel Task API to access authenticated web content and private data during task execution. The Browser Use MCP server enables Parallel to interact with websites through a browser that you configure, allowing access to content behind logins, paywalls, or other authentication barriers.

## Overview

By connecting the [Browser Use](https://browser-use.com) MCP server to your Parallel tasks, you can:

* **Access authenticated content**: Research data behind logins, such as internal dashboards, CRM systems, or subscription services
* **Interact with dynamic web applications**: Navigate SPAs and JavaScript-heavy sites that require browser rendering
* **Automate browser workflows**: Fill forms, click buttons, and navigate multi-step processes as part of research tasks
* **Extract private data**: Pull information from accounts and services that require authentication

## Prerequisites

* A Parallel API key from [Platform](https://platform.parallel.ai)
* A Browser Use API key from [Browser Use](https://browser-use.com)
* For authenticated content: A Browser Use profile with saved login sessions. Profiles are persistent storage containers that maintain your credentials and cookies across browser sessions. See the [Browser Use Profile Documentation](https://docs.cloud.browser-use.com/concepts/profile) for setup instructions.

<Note>
  The `browser_task` and `monitor_task` tools are required for basic browser functionality. To access authenticated content via profiles, `list_browser_profiles` must also be included in your `allowed_tools` configuration. Without it, the browser will function but cannot access your saved authenticated sessions.
</Note>

## Configuration

Add the Browser Use MCP server to your Task API requests using the `mcp_servers` field. See [MCP Tool Calling](/task-api/mcp-tool-call) for complete documentation on using MCP servers with the Task API.

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -X POST "https://api.parallel.ai/v1/tasks/runs" \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H "Content-Type: application/json" \
    -H "parallel-beta: mcp-server-2025-07-17" \
    --data '{
    "input": "Go to https://www.nxp.com/products/K66_180 and extract only the migration-related information for the K66-180 chip, specifically documentation on Migration from Kinetis K Series to MCXNx4x Series.",
    "processor": "ultra",
    "mcp_servers": [\
      {\
        "type": "url",\
        "url": "https://api.browser-use.com/mcp",\
        "name": "browseruse",\
        "headers": {\
          "Authorization": "Bearer YOUR_BROWSERUSE_API_KEY"\
        }\
      }\
    ]
  }'
  ```

  ```python Python theme={"system"}
  import requests

  response = requests.post(
      "https://api.parallel.ai/v1/tasks/runs",
      headers={
          "x-api-key": "YOUR_PARALLEL_API_KEY",
          "Content-Type": "application/json",
          "parallel-beta": "mcp-server-2025-07-17"
      },
      json={
          "input": "Go to https://www.nxp.com/products/K66_180 and extract only the "
                   "migration-related information for the K66-180 chip, specifically "
                   "documentation on Migration from Kinetis K Series to MCXNx4x Series.",
          "processor": "ultra",
          "mcp_servers": [\
              {\
                  "type": "url",\
                  "url": "https://api.browser-use.com/mcp",\
                  "name": "browseruse",\
                  "headers": {\
                      "Authorization": "Bearer YOUR_BROWSERUSE_API_KEY"\
                  }\
              }\
          ]
      }
  )

  print(response.json())
  ```

  ```typescript TypeScript theme={"system"}
  const response = await fetch("https://api.parallel.ai/v1/tasks/runs", {
    method: "POST",
    headers: {
      "x-api-key": process.env.PARALLEL_API_KEY,
      "Content-Type": "application/json",
      "parallel-beta": "mcp-server-2025-07-17",
    },
    body: JSON.stringify({
      input:
        "Go to https://www.nxp.com/products/K66_180 and extract only the migration-related information for the K66-180 chip, specifically documentation on Migration from Kinetis K Series to MCXNx4x Series.",
      processor: "ultra",
      mcp_servers: [\
        {\
          type: "url",\
          url: "https://api.browser-use.com/mcp",\
          name: "browseruse",\
          headers: {\
            Authorization: `Bearer ${process.env.BROWSERUSE_API_KEY}`,\
          },\
        },\
      ],
    }),
  });

  console.log(await response.json());
  ```
</CodeGroup>

## Best Practices

* **Use appropriate processors**: Browser interactions require `ultra` or higher processors that support multiple tool calls
* **Be specific with instructions**: Provide clear steps for authentication and navigation when the path is complex
* **Combine with web research**: Browser Use handles private data while Parallel's built-in capabilities handle public web research
* **Manage credentials securely**: Store your Browser Use API key securely and rotate it regularly

## Limitations

* The Browser Use MCP server requires the `parallel-beta: mcp-server-2025-07-17` header
* Browser interactions add latency compared to direct API calls
* Complex multi-step workflows may require higher-tier processors for optimal results

For more details on MCP server configuration and response handling, see the [MCP Tool Calling](/task-api/mcp-tool-call) documentation.

# Second turn with context
messages.append(HumanMessage(content="How does it work?"))
response = chat.invoke(messages)
print(response.content)
```

#### Configuration Options

| Parameter     | Type                 | Default                     | Description                                               |
| ------------- | -------------------- | --------------------------- | --------------------------------------------------------- |
| `model`       | str                  | `"speed"`                   | Parallel model name                                       |
| `api_key`     | Optional\[SecretStr] | None                        | API key (uses `PARALLEL_API_KEY` env var if not provided) |
| `base_url`    | str                  | `"https://api.parallel.ai"` | API base URL                                              |
| `temperature` | Optional\[float]     | None                        | Sampling temperature (ignored by Parallel)                |
| `max_tokens`  | Optional\[int]       | None                        | Max tokens (ignored by Parallel)                          |
| `timeout`     | Optional\[float]     | None                        | Request timeout                                           |
| `max_retries` | int                  | 2                           | Max retry attempts                                        |

### Real-Time Web Research

Parallel's Chat API provides real-time access to web information, making it perfect for:

* **Current Events**: Get up-to-date information about recent events
* **Market Data**: Access current stock prices, market trends
* **Research**: Find the latest research papers, developments
* **Weather**: Get current weather conditions
* **News**: Access breaking news and recent articles

```python theme={"system"}
# Search with an objective
result = search_tool.invoke({
    "objective": "What are the latest developments in renewable energy?",
    "max_results": 5
})

print(result)
# }
```

#### Search API Configuration

| Parameter        | Type                  | Default                     | Description                                                                                   |
| ---------------- | --------------------- | --------------------------- | --------------------------------------------------------------------------------------------- |
| `objective`      | Optional\[str]        | None                        | Natural-language description of research goal                                                 |
| `search_queries` | Optional\[List\[str]] | None                        | Specific search queries (max 5, 200 chars each)                                               |
| `max_results`    | int                   | 10                          | Maximum results to return (1-40)                                                              |
| `excerpts`       | Optional\[dict]       | None                        | Excerpt settings (e.g., `{'max_chars_per_result': 1500}`)                                     |
| `mode`           | Optional\[str]        | None                        | Search mode: 'one-shot' for comprehensive results, 'agentic' for token-efficient results      |
| `fetch_policy`   | Optional\[dict]       | None                        | Policy for cached vs live content (e.g., `{'max_age_seconds': 86400, 'timeout_seconds': 60}`) |
| `api_key`        | Optional\[SecretStr]  | None                        | API key (uses env var if not provided)                                                        |
| `base_url`       | str                   | `"https://api.parallel.ai"` | API base URL                                                                                  |

#### Search with Specific Queries

You can provide specific search queries instead of an objective:

```python theme={"system"}
# Control full content length per extraction
result = extract_tool.invoke({
    "urls": ["https://en.wikipedia.org/wiki/Quantum_computing"],
    "full_content": {"max_chars_per_result": 3000}
})

print(f"Content length: {len(result[0]['content'])} characters")
```

#### Extract API Configuration

| Parameter               | Type                              | Default                     | Description                                                          |
| ----------------------- | --------------------------------- | --------------------------- | -------------------------------------------------------------------- |
| `urls`                  | List\[str]                        | Required                    | List of URLs to extract content from                                 |
| `search_objective`      | Optional\[str]                    | None                        | Natural language objective to focus extraction                       |
| `search_queries`        | Optional\[List\[str]]             | None                        | Specific keyword queries to focus extraction                         |
| `excerpts`              | Union\[bool, ExcerptSettings]     | True                        | Include relevant excerpts (focused on objective/queries if provided) |
| `full_content`          | Union\[bool, FullContentSettings] | False                       | Include full page content                                            |
| `fetch_policy`          | Optional\[FetchPolicy]            | None                        | Cache vs live content policy                                         |
| `max_chars_per_extract` | Optional\[int]                    | None                        | Maximum characters per extraction (tool-level setting)               |
| `api_key`               | Optional\[SecretStr]              | None                        | API key (uses env var if not provided)                               |
| `base_url`              | str                               | `"https://api.parallel.ai"` | API base URL                                                         |

#### Extract Error Handling

The extract tool gracefully handles failed extractions:

```python theme={"system"}
# Programmatic Use
Source: https://docs.parallel.ai/integrations/mcp/programmatic-use

How to use the MCP servers Programmatically

When building an agent or chat experiences that requires search, deep research, or batch task processing capabilities, it can be a good choice to integrate with our MCPs. When you desire more control over the reasoning and tool descriptions for niche use-cases (if the system prompt isn't sufficient) or want to limit or simplify the tools, it may be better to use the APIs directly to build your own tools, for example using the [AI SDK](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling). Using the [MCP-to-AI-SDK](https://github.com/vercel-labs/mcp-to-ai-sdk) is an excellent starting point in that case.

To use the Parallel MCP servers programmatically, you need to either perform the [OAuth flow](/integrations/oauth-provider) to provide an API key, or use your Parallel API key directly as a Bearer token in the Authorization header.

## OpenAI Integration

### Search MCP with OpenAI

<CodeGroup>
  ```bash cURL theme={"system"}
  curl https://api.openai.com/v1/responses \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
      "model": "gpt-5",
      "tools": [\
        {\
          "type": "mcp",\
          "server_label": "parallel_web_search",\
          "server_url": "https://search-mcp.parallel.ai/mcp",\
          "headers": {\
            "Authorization": "Bearer YOUR_PARALLEL_API_KEY"\
          },\
          "require_approval": "never"\
        }\
      ],
      "input": "Who is the CEO of Apple?"
    }'
  ```

  ```python Python theme={"system"}
  from openai import OpenAI
  from openai.types import responses as openai_responses

  parallel_api_key = "PARALLEL_API_KEY"  # Your Parallel API key
  openai_api_key = "YOUR_OPENAI_API_KEY"  # Your OpenAI API key

  tools = [\
      openai_responses.tool_param.Mcp(\
          server_label="parallel_web_search",\
          server_url="https://search-mcp.parallel.ai/mcp",\
          headers={"Authorization": "Bearer " + parallel_api_key},\
          type="mcp",\
          require_approval="never",\
      )\
  ]

  response = OpenAI(
      api_key=openai_api_key
  ).responses.create(
      model="gpt-5",
      input="Who is the CEO of Apple?",
      tools=tools
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={"system"}
  import OpenAI from "openai";
  import { ResponseTool } from "openai/resources/responses";

  const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });

  const parallelApiKey = process.env.PARALLEL_API_KEY;

  const response = await client.responses.create({
    model: "gpt-5",
    tools: [\
      {\
        type: "mcp",\
        server_label: "parallel_web_search",\
        server_url: "https://search-mcp.parallel.ai/mcp",\
        headers: { Authorization: `Bearer ${parallelApiKey}` },\
        require_approval: "never",\
      } as ResponseTool.Mcp,\
    ],
    input: "Who is the CEO of Apple?",
  });

  console.log(response.output_text);
  ```
</CodeGroup>

### Task MCP with OpenAI

<CodeGroup>
  ```bash cURL theme={"system"}
  curl https://api.openai.com/v1/responses \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
      "model": "gpt-5",
      "tools": [\
        {\
          "type": "mcp",\
          "server_label": "parallel_task",\
          "server_url": "https://task-mcp.parallel.ai/mcp",\
          "headers": {\
            "Authorization": "Bearer YOUR_PARALLEL_API_KEY"\
          },\
          "require_approval": "never"\
        }\
      ],
      "input": "Create a deep research task about the latest developments in AI safety research"
    }'
  ```

  ```python Python theme={"system"}
  from openai import OpenAI
  from openai.types import responses as openai_responses

  parallel_api_key = "PARALLEL_API_KEY"  # Your Parallel API key
  openai_api_key = "YOUR_OPENAI_API_KEY"  # Your OpenAI API key

  tools = [\
      openai_responses.tool_param.Mcp(\
          server_label="parallel_task",\
          server_url="https://task-mcp.parallel.ai/mcp",\
          headers={"Authorization": "Bearer " + parallel_api_key},\
          type="mcp",\
          require_approval="never",\
      )\
  ]

  response = OpenAI(
      api_key=openai_api_key
  ).responses.create(
      model="gpt-5",
      input="Create a deep research task about the latest developments in AI safety research",
      tools=tools
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={"system"}
  import OpenAI from "openai";
  import { ResponseTool } from "openai/resources/responses";

  const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });

  const parallelApiKey = process.env.PARALLEL_API_KEY;

  const response = await client.responses.create({
    model: "gpt-5",
    tools: [\
      {\
        type: "mcp",\
        server_label: "parallel_task",\
        server_url: "https://task-mcp.parallel.ai/mcp",\
        headers: { Authorization: `Bearer ${parallelApiKey}` },\
        require_approval: "never",\
      } as ResponseTool.Mcp,\
    ],
    input:
      "Create a deep research task about the latest developments in AI safety research",
  });

  console.log(response.output_text);
  ```
</CodeGroup>

## Anthropic Integration

### Search MCP with Anthropic

<CodeGroup>
  ```bash cURL theme={"system"}
  curl https://api.anthropic.com/v1/messages \
    -H "Content-Type: application/json" \
    -H "X-API-Key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: mcp-client-2025-04-04" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 8000,
      "messages": [\
        {\
          "role": "user",\
          "content": "What is the latest in AI research?"\
        }\
      ],
      "mcp_servers": [\
        {\
          "type": "url",\
          "url": "https://search-mcp.parallel.ai/mcp",\
          "name": "parallel-web-search",\
          "authorization_token": "YOUR_PARALLEL_API_KEY"\
        }\
      ]
    }'
  ```

  ```python Python theme={"system"}
  import anthropic

  client = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")
  parallel_api_key = "PARALLEL_API_KEY"  # Your Parallel API key

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      messages=[{\
          "role": "user",\
          "content": "What is the latest in AI research?"\
      }],
      max_tokens=8000,
      mcp_servers=[{\
          "type": "url",\
          "url": "https://search-mcp.parallel.ai/mcp",\
          "name": "parallel-web-search",\
          "authorization_token": parallel_api_key\
      }],
      betas=["mcp-client-2025-04-04"]
  )

  print(response)
  ```

  ```typescript TypeScript theme={"system"}
  import { Anthropic } from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const parallelApiKey = process.env.PARALLEL_API_KEY;

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    messages: [\
      {\
        role: "user",\
        content: "What is the latest in AI research?",\
      },\
    ],
    max_tokens: 8000,
    mcp_servers: [\
      {\
        type: "url",\
        url: "https://search-mcp.parallel.ai/mcp",\
        name: "parallel-web-search",\
        authorization_token: parallelApiKey,\
      },\
    ],
    betas: ["mcp-client-2025-04-04"],
  });

  console.log(response);
  ```
</CodeGroup>

### Task MCP with Anthropic

<CodeGroup>
  ```bash cURL theme={"system"}
  curl https://api.anthropic.com/v1/messages \
    -H "Content-Type: application/json" \
    -H "X-API-Key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: mcp-client-2025-04-04" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 8000,
      "messages": [\
        {\
          "role": "user",\
          "content": "Create a deep research task about the latest developments in AI safety research"\
        }\
      ],
      "mcp_servers": [\
        {\
          "type": "url",\
          "url": "https://task-mcp.parallel.ai/mcp",\
          "name": "parallel-task",\
          "authorization_token": "YOUR_PARALLEL_API_KEY"\
        }\
      ]
    }'
  ```

  ```python Python theme={"system"}
  import anthropic

  client = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")
  parallel_api_key = "PARALLEL_API_KEY"  # Your Parallel API key

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      messages=[{\
          "role": "user",\
          "content": "Create a deep research task about the latest developments in AI safety research"\
      }],
      max_tokens=8000,
      mcp_servers=[{\
          "type": "url",\
          "url": "https://task-mcp.parallel.ai/mcp",\
          "name": "parallel-task",\
          "authorization_token": parallel_api_key\
      }],
      betas=["mcp-client-2025-04-04"]
  )

  print(response)
  ```

  ```typescript TypeScript theme={"system"}
  import { Anthropic } from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const parallelApiKey = process.env.PARALLEL_API_KEY;

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    messages: [\
      {\
        role: "user",\
        content:\
          "Create a deep research task about the latest developments in AI safety research",\
      },\
    ],
    max_tokens: 8000,
    mcp_servers: [\
      {\
        type: "url",\
        url: "https://task-mcp.parallel.ai/mcp",\
        name: "parallel-task",\
        authorization_token: parallelApiKey,\
      },\
    ],
    betas: ["mcp-client-2025-04-04"],
  });

  console.log(response);
  ```
</CodeGroup>

## Limitations

### Context Window Constraints

The Task MCP is designed for smaller parallel tasks and experimentation, constrained by:

* **Context window size** - Large datasets may overflow the available context
* **Max output tokens** - Results must fit within model output limitations
* **Data source size** - Initial data should be appropriately sized for the model

For large-scale operations, consider using the Parallel APIs directly or other integration methods.

### Asynchronous Nature

Due to current MCP/LLM client limitations:

* Tasks run asynchronously but don't automatically wait for completion
* Users must explicitly request results in follow-up turns
* Multiple workflow steps require manual progression through conversation turns

### Model Requirements

* **Search MCP** - Works well with smaller models (GPT OSS 20B+)
* **Task MCP** - Requires larger models with strong reasoning capabilities (e.g. GPT-5, Claude Sonnet 4.5)
* Smaller models may result in degraded output quality for complex tasks

Reach out to be among the first to overcome current limitations as we continue improving the platform.

# OpenAI Tool Calling
Source: https://docs.parallel.ai/integrations/openai-tool-calling

Use Parallel Search as a tool with OpenAI's function calling to give GPT models real-time web access

Give your OpenAI-powered applications real-time web search capabilities by integrating Parallel Search as a tool. This guide shows how to define Parallel Search as an OpenAI function and handle tool calls in your application.

## Overview

OpenAI's [tool calling](https://platform.openai.com/docs/guides/function-calling) (formerly function calling) allows GPT models to output structured JSON indicating they want to call a function you've defined. Your application then executes the function and returns results to the model. By defining Parallel Search as a tool, your model can:

* Search the web for current information
* Access real-time news, research, and facts
* Cite sources with URLs in responses

## Prerequisites

1. Get your Parallel API key from [Platform](https://platform.parallel.ai)
2. Get your OpenAI API key from [OpenAI](https://platform.openai.com/api-keys)
3. Install the required SDKs:

<CodeGroup>
  ```bash Python theme={"system"}
  pip install openai parallel-web
  export PARALLEL_API_KEY="your-parallel-api-key"
  export OPENAI_API_KEY="your-openai-api-key"
  ```

  ```bash TypeScript theme={"system"}
  npm install openai parallel-web
  export PARALLEL_API_KEY="your-parallel-api-key"
  export OPENAI_API_KEY="your-openai-api-key"
  ```
</CodeGroup>

## Define the Search Tool

First, define the Parallel search tool using OpenAI's tool schema format:

<CodeGroup>
  ```python Python theme={"system"}
  parallel_search_tool = {
      "type": "function",
      "function": {
          "name": "parallel_search",
          "description": "Search the web for current information using Parallel's AI-powered search. Returns relevant excerpts from web pages optimized for LLM consumption. Use this for finding up-to-date information, news, research, and facts. Provide at least one of objective or search_queries.",
          "parameters": {
              "type": "object",
              "properties": {
                  "objective": {
                      "type": "string",
                      "description": "A natural language description of what you're searching for. Be specific about your research goal."
                  },
                  "search_queries": {
                      "type": "array",
                      "items": {"type": "string"},
                      "description": "Specific search queries to execute. Use multiple queries to cover different angles of the search."
                  },
                  "max_chars_total": {
                      "type": "integer",
                      "description": "Maximum total characters across all excerpts. Default 50000."
                  }
              }
          }
      }
  }
  ```

  ```typescript TypeScript theme={"system"}
  import OpenAI from "openai";

  const parallelSearchTool: OpenAI.ChatCompletionTool = {
    type: "function",
    function: {
      name: "parallel_search",
      description:
        "Search the web for current information using Parallel's AI-powered search. Returns relevant excerpts from web pages optimized for LLM consumption. Use this for finding up-to-date information, news, research, and facts. Provide at least one of objective or search_queries.",
      parameters: {
        type: "object",
        properties: {
          objective: {
            type: "string",
            description:
              "A natural language description of what you're searching for. Be specific about your research goal.",
          },
          search_queries: {
            type: "array",
            items: { type: "string" },
            description:
              "Specific search queries to execute. Use multiple queries to cover different angles of the search.",
          },
          max_chars_total: {
            type: "integer",
            description: "Maximum total characters across all excerpts. Default 50000.",
          },
        },
      },
    },
  };
  ```
</CodeGroup>

## Implement the Search Function

Create a function that calls the Parallel Search API when the model requests it:

<CodeGroup>
  ```python Python theme={"system"}
  import os
  import json
  from parallel import Parallel

  parallel_client = Parallel(api_key=os.environ["PARALLEL_API_KEY"])

  def parallel_search(objective: str = None, search_queries: list = None, max_chars_total: int = 50000) -> dict:
      """Execute a search using the Parallel Search API."""
      response = parallel_client.beta.search(
          objective=objective,
          search_queries=search_queries,
          excerpts={"max_chars_per_result": 5000, "max_chars_total": max_chars_total}
      )

      # Format results for the LLM
      return {
          "results": [\
              {"url": r.url, "title": r.title, "excerpts": r.excerpts[:3] if r.excerpts else []}\
              for r in response.results\
          ]
      }
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from "parallel-web";

  const parallel = new Parallel({ apiKey: process.env.PARALLEL_API_KEY });

  interface SearchParams {
    objective?: string;
    search_queries?: string[];
    max_chars_total?: number;
  }

  async function parallelSearch(params: SearchParams) {
    const response = await parallel.beta.search({
      objective: params.objective,
      search_queries: params.search_queries,
      excerpts: { max_chars_per_result: 5000, max_chars_total: params.max_chars_total || 50000 },
    });

    return {
      results: response.results.map((r) => ({
        url: r.url,
        title: r.title,
        excerpts: r.excerpts?.slice(0, 3) || [],
      })),
    };
  }
  ```
</CodeGroup>

## Process Tool Calls

Handle the tool calls returned by OpenAI:

<CodeGroup>
  ```python Python theme={"system"}
  def process_tool_calls(tool_calls):
      """Process tool calls from OpenAI and return results."""
      results = []
      for tool_call in tool_calls:
          if tool_call.function.name == "parallel_search":
              args = json.loads(tool_call.function.arguments)
              search_result = parallel_search(
                  objective=args.get("objective"),
                  search_queries=args.get("search_queries"),
                  max_chars_total=args.get("max_chars_total", 50000)
              )
              results.append({
                  "tool_call_id": tool_call.id,
                  "role": "tool",
                  "content": json.dumps(search_result)
              })
      return results
  ```

  ```typescript TypeScript theme={"system"}
  async function processToolCalls(
    toolCalls: OpenAI.ChatCompletionMessageToolCall[]
  ) {
    const results: OpenAI.ChatCompletionToolMessageParam[] = [];

    for (const toolCall of toolCalls) {
      if (toolCall.function.name === "parallel_search") {
        const args = JSON.parse(toolCall.function.arguments) as SearchParams;
        const searchResult = await parallelSearch(args);

        results.push({
          role: "tool",
          tool_call_id: toolCall.id,
          content: JSON.stringify(searchResult),
        });
      }
    }

    return results;
  }
  ```
</CodeGroup>

## Complete Example

Here's a complete example that ties everything together:

<CodeGroup>
  ```python Python theme={"system"}
  import os
  import json
  from openai import OpenAI
  from parallel import Parallel

  # Initialize clients
  openai_client = OpenAI()
  parallel_client = Parallel(api_key=os.environ["PARALLEL_API_KEY"])

  # Tool definition
  parallel_search_tool = {
      "type": "function",
      "function": {
          "name": "parallel_search",
          "description": "Search the web for current information using Parallel's AI-powered search. Provide at least one of objective or search_queries.",
          "parameters": {
              "type": "object",
              "properties": {
                  "objective": {
                      "type": "string",
                      "description": "A natural language description of what you're searching for."
                  },
                  "search_queries": {
                      "type": "array",
                      "items": {"type": "string"},
                      "description": "Specific search queries to execute."
                  },
                  "max_results": {
                      "type": "integer",
                      "description": "Maximum results (1-20). Default 10."
                  },
                  "max_chars_total": {
                      "type": "integer",
                      "description": "Maximum total characters across all excerpts. Default 50000."
                  }
              }
          }
      }
  }

  def parallel_search(objective=None, search_queries=None, max_results=10, max_chars_total=50000):
      response = parallel_client.beta.search(
          objective=objective,
          search_queries=search_queries,
          max_results=max_results,
          excerpts={"max_chars_per_result": 5000, "max_chars_total": max_chars_total}
      )
      return {
          "results": [\
              {"url": r.url, "title": r.title, "excerpts": r.excerpts[:3] if r.excerpts else []}\
              for r in response.results\
          ]
      }

  def chat_with_search(user_message: str) -> str:
      messages = [\
          {\
              "role": "system",\
              "content": "You are a helpful research assistant. Use the parallel_search tool to find current information. Always cite sources with URLs."\
          },\
          {"role": "user", "content": user_message}\
      ]

      # First API call - may trigger tool use
      response = openai_client.chat.completions.create(
          model="gpt-4o",
          messages=messages,
          tools=[parallel_search_tool],
          tool_choice="auto"
      )

      assistant_message = response.choices[0].message

      # Check if the model wants to use tools
      if assistant_message.tool_calls:
          messages.append(assistant_message)

          # Process each tool call
          for tool_call in assistant_message.tool_calls:
              if tool_call.function.name == "parallel_search":
                  args = json.loads(tool_call.function.arguments)
                  result = parallel_search(
                      objective=args.get("objective"),
                      search_queries=args.get("search_queries"),
                      max_results=args.get("max_results", 10),
                      max_chars_total=args.get("max_chars_total", 50000)
                  )
                  messages.append({
                      "role": "tool",
                      "tool_call_id": tool_call.id,
                      "content": json.dumps(result)
                  })

          # Second API call with search results
          response = openai_client.chat.completions.create(
              model="gpt-4o",
              messages=messages,
              tools=[parallel_search_tool],
              tool_choice="auto"
          )

      return response.choices[0].message.content

  # Example usage
  if __name__ == "__main__":
      answer = chat_with_search("What are the latest developments in quantum computing?")
      print(answer)
  ```

  ```typescript TypeScript theme={"system"}
  import OpenAI from "openai";
  import Parallel from "parallel-web";

  const openai = new OpenAI();
  const parallel = new Parallel({ apiKey: process.env.PARALLEL_API_KEY });

  // Tool definition
  const parallelSearchTool: OpenAI.ChatCompletionTool = {
    type: "function",
    function: {
      name: "parallel_search",
      description: "Search the web for current information using Parallel's AI-powered search. Provide at least one of objective or search_queries.",
      parameters: {
        type: "object",
        properties: {
          objective: {
            type: "string",
            description: "A natural language description of what you're searching for.",
          },
          search_queries: {
            type: "array",
            items: { type: "string" },
            description: "Specific search queries to execute.",
          },
          max_results: {
            type: "integer",
            description: "Maximum results (1-20). Default 10.",
          },
          max_chars_total: {
            type: "integer",
            description: "Maximum total characters across all excerpts. Default 50000.",
          },
        },
      },
    },
  };

  interface SearchArgs {
    objective?: string;
    search_queries?: string[];
    max_results?: number;
    max_chars_total?: number;
  }

  async function parallelSearch(args: SearchArgs) {
    const response = await parallel.beta.search({
      objective: args.objective,
      search_queries: args.search_queries,
      max_results: args.max_results || 10,
      excerpts: { max_chars_per_result: 5000, max_chars_total: args.max_chars_total || 50000 },
    });

    return {
      results: response.results.map((r) => ({
        url: r.url,
        title: r.title,
        excerpts: r.excerpts?.slice(0, 3) || [],
      })),
    };
  }

  async function chatWithSearch(userMessage: string): Promise<string | null> {
    const messages: OpenAI.ChatCompletionMessageParam[] = [\
      {\
        role: "system",\
        content: "You are a helpful research assistant. Use the parallel_search tool to find current information. Always cite sources with URLs.",\
      },\
      { role: "user", content: userMessage },\
    ];

    // First API call
    let response = await openai.chat.completions.create({
      model: "gpt-4o",
      messages,
      tools: [parallelSearchTool],
      tool_choice: "auto",
    });

    let assistantMessage = response.choices[0].message;

    // Handle tool calls
    if (assistantMessage.tool_calls) {
      messages.push(assistantMessage);

      for (const toolCall of assistantMessage.tool_calls) {
        if (toolCall.function.name === "parallel_search") {
          const args = JSON.parse(toolCall.function.arguments) as SearchArgs;
          const result = await parallelSearch(args);

          messages.push({
            role: "tool",
            tool_call_id: toolCall.id,
            content: JSON.stringify(result),
          });
        }
      }

      // Second API call with results
      response = await openai.chat.completions.create({
        model: "gpt-4o",
        messages,
        tools: [parallelSearchTool],
        tool_choice: "auto",
      });
    }

    return response.choices[0].message.content;
  }

  // Example usage
  async function main() {
    const answer = await chatWithSearch("What are the latest developments in quantum computing?");
    console.log(answer);
  }

  main().catch(console.error);
  ```
</CodeGroup>

## Tool Parameters

| Parameter         | Type      | Required | Description                                                  |
| ----------------- | --------- | -------- | ------------------------------------------------------------ |
| `objective`       | string    | No\*     | Natural language description of your search goal             |
| `search_queries`  | string\[] | No\*     | Specific search queries to execute                           |
| `max_chars_total` | integer   | No       | Maximum total characters across all excerpts (default 50000) |

\*At least one of `objective` or `search_queries` is required.

<Note>
  The complete example above shows additional optional parameters (`max_results`) that you can add to the tool definition for more control. See the [Search API documentation](/search/search-quickstart) for all available options.
</Note>

## Related Resources

* [Search API Quickstart](/search/search-quickstart)
* [Search Best Practices](/search/best-practices)
* [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)

# Status Page
Source: https://docs.parallel.ai/resources/status

# Webhook Setup
Source: https://docs.parallel.ai/resources/webhook-setup

Guide to configuring and verifying webhooks for Parallel APIs

## Overview

Webhooks allow you to receive real-time notifications when events occur in your Parallel API operations, eliminating the need for constant polling. Our webhooks follow [standard webhook conventions](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md) to ensure security and interoperability.

## Setup

### 1. Record your webhook secret

Go to **Settings → Webhooks** to view your account webhook secret. You'll need this to verify webhook signatures.

<Note>
  Keep your webhook secret secure. Anyone with access to your secret can forge webhook requests.
</Note>

### 2. Configure webhook in API request

When creating a task run or FindAll run, include a `webhook` parameter in your request:

```json theme={"system"}
{
  "webhook": {
    "url": "https://your-domain.com/webhooks/parallel",
    "event_types": ["event.type"]
  }
}
```

| Parameter     | Type           | Required | Description                                                                                     |
| ------------- | -------------- | -------- | ----------------------------------------------------------------------------------------------- |
| `url`         | string         | Yes      | Your webhook endpoint URL. Can be any domain.                                                   |
| `event_types` | array\[string] | Yes      | Array of event types to subscribe to. See API-specific documentation for available event types. |

### 3. Webhook request headers

Your webhook endpoint will receive requests with these headers:

* `webhook-id`: Unique identifier for each webhook event
* `webhook-timestamp`: Unix timestamp in seconds
* `webhook-signature`: One or more versioned signatures (e.g., `v1,<base64 signature>`)

```json theme={"system"}
{
  "Content-Type": "application/json",
  "webhook-id": "whevent_abc123def456",
  "webhook-timestamp": "1751498975",
  "webhook-signature": "v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4="
}
```

Signatures are space-delimited per the Standard Webhooks format. Under normal circumstances there will only be one signature, but there may be multiple if you rotate your webhook secret without immediately expiring the old secrets.

```text theme={"system"}
webhook-signature: v1,BASE64SIG_A v1,BASE64SIG_B
```

## Security & Verification

### HMAC Signature Verification

Webhook requests are signed using HMAC-SHA256 with **standard Base64 (RFC 4648) encoding with padding**. The signature header is formatted as `v1,<base64 signature>` where `<base64 signature>` is computed over the payload below:

```text theme={"system"}
<webhook-id>.<webhook-timestamp>.<payload>
```

Where:

* `<webhook-id>`: The value of the `webhook-id` header
* `<webhook-timestamp>`: The value of the `webhook-timestamp` header
* `<payload>`: The exact JSON body of the webhook request

You must parse the version and the signature before verifying. The `webhook-signature` header uses space-delimited signatures; check each signature until one matches.

### Verification Examples

<CodeGroup>
  ```typescript TypeScript (Node.js) theme={"system"}
  import crypto from "crypto";

  function computeSignature(
    secret: string,
    webhookId: string,
    webhookTimestamp: string,
    body: string | Buffer
  ): string {
    const payload = `${webhookId}.${webhookTimestamp}.${body.toString()}`;
    const digest = crypto.createHmac("sha256", secret).update(payload).digest();
    return digest.toString("base64"); // standard Base64 with padding
  }

  function isValidSignature(
    webhookSignatureHeader: string,
    expectedSignature: string
  ): boolean {
    // Header may contain multiple space-delimited entries; each is "v1,<sig>"
    const signatures = webhookSignatureHeader.split(" ");

    for (const part of signatures) {
      const [, sig] = part.split(",", 2);
      if (
        crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(expectedSignature))
      ) {
        return true;
      }
    }

    return false;
  }

  // Example usage in an Express endpoint
  import express from "express";

  const app = express();

  app.post(
    "/webhooks/parallel",
    express.raw({ type: "application/json" }),
    (req, res) => {
      const webhookId = req.headers["webhook-id"] as string;
      const webhookTimestamp = req.headers["webhook-timestamp"] as string;
      const webhookSignature = req.headers["webhook-signature"] as string;
      const secret = process.env.PARALLEL_WEBHOOK_SECRET!;

      const expectedSignature = computeSignature(
        secret,
        webhookId,
        webhookTimestamp,
        req.body
      );

      if (!isValidSignature(webhookSignature, expectedSignature)) {
        return res.status(401).send("Invalid signature");
      }

      // Parse and process the webhook payload
      const payload = JSON.parse(req.body.toString());
      console.log("Webhook received:", payload);

      // Your business logic here

      res.status(200).send("OK");
    }
  );
  ```

  ```typescript TypeScript (Web API / Cloudflare Workers) theme={"system"}
  // Example for environments without Node.js crypto module
  async function computeSignature(
    secret: string,
    webhookId: string,
    webhookTimestamp: string,
    body: string
  ): Promise<string> {
    const payload = `${webhookId}.${webhookTimestamp}.${body}`;
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
      "raw",
      encoder.encode(secret),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"]
    );

    const signature = await crypto.subtle.sign(
      "HMAC",
      key,
      encoder.encode(payload)
    );

    // Convert to base64
    const base64 = btoa(String.fromCharCode(...new Uint8Array(signature)));
    return base64;
  }

  function isValidSignature(
    webhookSignatureHeader: string,
    expectedSignature: string
  ): boolean {
    const signatures = webhookSignatureHeader.split(" ");

    for (const part of signatures) {
      const [, sig] = part.split(",", 2);
      if (sig === expectedSignature) {
        return true;
      }
    }

    return false;
  }

  // Example Cloudflare Worker
  export default {
    async fetch(request: Request): Promise<Response> {
      if (request.method !== "POST") {
        return new Response("Method not allowed", { status: 405 });
      }

      const webhookId = request.headers.get("webhook-id")!;
      const webhookTimestamp = request.headers.get("webhook-timestamp")!;
      const webhookSignature = request.headers.get("webhook-signature")!;
      const secret = "your-webhook-secret";

      const body = await request.text();

      const expectedSignature = await computeSignature(
        secret,
        webhookId,
        webhookTimestamp,
        body
      );

      if (!isValidSignature(webhookSignature, expectedSignature)) {
        return new Response("Invalid signature", { status: 401 });
      }

      const payload = JSON.parse(body);
      console.log("Webhook received:", payload);

      return new Response("OK", { status: 200 });
    },
  };
  ```

  ```python Python theme={"system"}
  import base64
  import hashlib
  import hmac

  def compute_signature(secret: str, webhook_id: str, webhook_timestamp: str, body: bytes) -> str:
      payload = f"{webhook_id}.{webhook_timestamp}.{body.decode()}".encode()
      digest = hmac.new(secret.encode(), payload, hashlib.sha256).digest()
      return base64.b64encode(digest).decode()  # standard Base64 with padding

  def is_valid_signature(webhook_signature_header: str, expected_signature: str) -> bool:
      # Header may contain multiple space-delimited entries; each is "v1,<sig>"
      for part in webhook_signature_header.split():
          _, sig = part.split(",", 1)
          if hmac.compare_digest(sig, expected_signature):
              return True
      return False

  # Example usage
  webhook_secret = "your_webhook_secret_from_settings"
  webhook_id = request.headers.get("webhook-id")
  webhook_timestamp = request.headers.get("webhook-timestamp")
  signature_header = request.headers.get("webhook-signature")
  body = request.get_data()

  expected_sig = compute_signature(webhook_secret, webhook_id, webhook_timestamp, body)
  if is_valid_signature(signature_header, expected_sig):
      print("✓ Signature verified")
  else:
      print("✗ Signature verification failed")
  ```

  ```bash Bash theme={"system"}
  #!/bin/bash

  # Inputs: HEADER_SIGNATURE (e.g. "v1,BASE64..."), WEBHOOK_ID, WEBHOOK_TIMESTAMP, PAYLOAD (minified JSON), SECRET
  RECEIVED_SIGNATURE=$(printf "%s" "$HEADER_SIGNATURE" | cut -d',' -f2)
  TO_SIGN="$WEBHOOK_ID.$WEBHOOK_TIMESTAMP.$PAYLOAD"
  EXPECTED_SIGNATURE=$(printf "%s" "$TO_SIGN" | openssl dgst -sha256 -hmac "$SECRET" -binary | base64 | tr -d '\n')

  if [ "$EXPECTED_SIGNATURE" = "$RECEIVED_SIGNATURE" ]; then
    echo "✅ Signature verification successful"
  else
    echo "❌ Signature verification failed"
    exit 1
  fi
  ```
</CodeGroup>

## Retry Policy

Webhook delivery uses the following retry configuration:

* **Initial delay**: 5 seconds
* **Backoff strategy**: Exponential backoff (doubles per failed request)
* **Maximum retries**: Multiple attempts over 48 hours

After exhausting all retry attempts, webhook delivery for that event is terminated.

## Best Practices

### 1. Always Return 2xx Status

Your webhook endpoint should return a 2xx HTTP status code to acknowledge receipt. Any other status code will trigger retries.

### 2. Verify Signatures

Always verify HMAC signatures using your account webhook secret from **Settings → Webhooks** to ensure webhook authenticity. Ensure that you are calculating signatures using the proper process as shown above.

### 3. Handle Duplicates

Although not common, duplicate events may be sent to the configured webhook URL. Ensure your webhook handler can detect and safely ignore duplicate events using the `webhook-id` header.

### 4. Process Asynchronously

Process webhook events asynchronously to avoid timeouts and ensure quick response times. For example, immediately return a 200 response, then queue the event for background processing.

### 5. Rotate Secrets Carefully

When rotating webhook secrets in **Settings → Webhooks**, consider keeping the old secret active temporarily to avoid verification failures during the transition period.

### 6. Monitor Webhook Health

Track webhook delivery failures and response times. Set up alerts for repeated failures that might indicate issues with your endpoint.

## API-Specific Documentation

For details on specific webhook events and payloads for each API:

* **[Task API Webhooks](/task-api/webhooks)**: Task run completion events
* **[FindAll Webhooks](/findall-api/features/findall-webhook)**: Candidate and run events
* **[Monitor API Webhooks](/monitor-api/monitor-webhooks)**: Events and completions

# Task Group
Source: https://docs.parallel.ai/task-api/group-api

Batch process Tasks at scale with the Parallel Task Group API

<Note>
  This API is in beta and is accessible via the
  <code>/v1beta/tasks/groups</code>
  endpoint.
</Note>

The Parallel Task Group API enables you to batch process hundreds or thousands of Tasks efficiently. Instead of running Tasks one by one, you can organize them into groups, monitor their progress collectively, and retrieve results in bulk. The API is comprised of the following endpoints:

**Creation**: To run a batch of tasks in a group, you first need to create a task group, after which you can add runs to it, which will be queued and processed.

* `POST /v1beta/tasks/groups` (Create task-group)
* `POST /v1beta/tasks/groups/{taskgroup_id}/runs` (Add runs. Up to 1,000 runs per POST request.)

**Progress Snapshot**: At any moment during the task, you can get an instant snapshot of the state of it using `GET /{taskgroup_id}` and `GET /{taskgroup_id}/runs`. Please note that the runs endpoint streams back the requested runs instantly (using SSE) to allow for large payloads without pagination, and it doesn't wait for runs to complete. Runs in a task group are stored indefinitely, so unless you have high performance requirements, you may not need to keep your own state of the intermediate results. However, it's recommended to still do so after the task group is completed.

* `GET /v1beta/tasks/groups/{taskgroup_id}` (Get task-group summary)
* `GET /v1beta/tasks/groups/{taskgroup_id}/runs` (Fetch task group runs)

**Realtime updates**: You may want to provide efficient real-time updates to your app. For a high-level summary and run completion events, you can use `GET /{taskgroup_id}/events`. To also retrieve the task run result upon completion you can use the [task run endpoint](/api-reference/tasks-v1/retrieve-task-run-result)

* `GET /v1beta/tasks/groups/{taskgroup_id}/events` (Stream task-group events)
* `GET /v1/tasks/runs/{run_id}/result` (Get task-run result)

To determine whether a task group is fully completed, you can either use realtime update events, or you can poll the task-group summary endpoint. You can also keep adding runs to your task group indefinitely.

## Key Concepts

### Task Groups

A Task Group is a container that organizes multiple task runs. Each group has:

* A unique `taskgroup_id` for identification
* A status object with `is_active` (boolean) and `task_run_status_counts` (counts by status)
* The ability to add new Tasks dynamically

### Group Status

Track progress with real-time status updates:

* Total number of task runs
* Count of runs by status (queued, running, completed, failed)
* Whether the group is still active (`is_active` becomes `false` when all runs finish)
* Human-readable status messages

## Quick Start

### 1. Define Types and Task Structure

<CodeGroup>
  ```bash cURL theme={"system"}
  # Define task specification as a variable
  TASK_SPEC='{
    "input_schema": {
      "json_schema": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "description": "Name of the company"
          },
          "company_website": {
            "type": "string",
            "description": "Company website URL"
          }
        },
        "required": ["company_name", "company_website"]
      }
    },
    "output_schema": {
      "json_schema": {
        "type": "object",
        "properties": {
          "key_insights": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Key business insights"
          },
          "market_position": {
            "type": "string",
            "description": "Market positioning analysis"
          }
        },
        "required": ["key_insights", "market_position"]
      }
    }
  }'
  ```

  ```python Python theme={"system"}
  import pydantic
  from parallel import AsyncParallel
  from parallel.types import TaskSpecParam, JsonSchemaParam
  from parallel.types.beta.beta_run_input_param import BetaRunInputParam

  # Define your input and output models
  class CompanyInput(pydantic.BaseModel):
      company_name: str = pydantic.Field(description="Name of the company")
      company_website: str = pydantic.Field(description="Company website URL")

  class CompanyOutput(pydantic.BaseModel):
      key_insights: list[str] = pydantic.Field(description="Key business insights")
      market_position: str = pydantic.Field(description="Market positioning analysis")

  # Create reusable task specification
  task_spec = TaskSpecParam(
      input_schema=JsonSchemaParam(json_schema=CompanyInput.model_json_schema()),
      output_schema=JsonSchemaParam(json_schema=CompanyOutput.model_json_schema()),
  )
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from "parallel-web";

  // Define your input and output types
  interface CompanyInput {
    company_name: string;
    company_website: string;
  }

  interface CompanyOutput {
    key_insights: string[];
    market_position: string;
  }

  // Use SDK types for Task Group API
  type TaskGroupObject = Parallel.Beta.TaskGroup;
  type TaskGroupStatus = Parallel.Beta.TaskGroupStatus;
  type TaskGroupRunResponse = Parallel.Beta.TaskGroupRunResponse;
  type TaskGroupEventsResponse = Parallel.Beta.TaskGroupEventsResponse;
  type TaskGroupGetRunsResponse = Parallel.Beta.TaskGroupGetRunsResponse;

  // Create reusable task specification using SDK types
  const taskSpec: Parallel.TaskSpec = {
    input_schema: {
      type: "json",
      json_schema: {
        type: "object",
        properties: {
          company_name: {
            type: "string",
            description: "Name of the company",
          },
          company_website: {
            type: "string",
            description: "Company website URL",
          },
        },
        required: ["company_name", "company_website"],
      },
    },
    output_schema: {
      type: "json",
      json_schema: {
        type: "object",
        properties: {
          key_insights: {
            type: "array",
            items: { type: "string" },
            description: "Key business insights",
          },
          market_position: {
            type: "string",
            description: "Market positioning analysis",
          },
        },
        required: ["key_insights", "market_position"],
      },
    },
  };
  ```
</CodeGroup>

### 2. Create a Task Group

<CodeGroup>
  ```bash cURL theme={"system"}
  # Create task group and capture the ID
  response=$(curl --request POST \
    --url https://api.parallel.ai/v1beta/tasks/groups \
    --header 'Content-Type: application/json' \
    --header 'x-api-key: ${PARALLEL_API_KEY}' \
    --data '{}')

  # Extract taskgroup_id from response
  TASKGROUP_ID=$(echo $response | jq -r '.taskgroup_id')
  echo "Created task group: $TASKGROUP_ID"
  ```

  ```python Python theme={"system"}
  # Initialize the client
  client = AsyncParallel(api_key="PARALLEL_API_KEY")

  # Create a new task group
  task_group = await client.beta.task_group.create()

  taskgroup_id = task_group.task_group_id
  print(f"Created task group: {taskgroup_id}")
  ```

  ```typescript TypeScript theme={"system"}
  // Initialize the client
  const client = new Parallel({
    apiKey: process.env.PARALLEL_API_KEY,
  });

  // Create a new task group using the beta API
  const groupResponse = await client.beta.taskGroup.create({});

  const taskgroupId = groupResponse.taskgroup_id;
  console.log(`Created task group: ${taskgroupId}`);
  ```
</CodeGroup>

### 3. Add Tasks to the Group

<CodeGroup>
  ```bash cURL theme={"system"}
  curl --request POST \
    --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID}/runs \
    --header 'Content-Type: application/json' \
    --header 'x-api-key: ${PARALLEL_API_KEY}' \
    --data '{
    "default_task_spec": '$TASK_SPEC',
    "inputs": [\
      {\
        "input": {\
          "company_name": "Acme Corp",\
          "company_website": "https://acme.com"\
        },\
        "processor": "pro"\
      },\
      {\
        "input": {\
          "company_name": "TechStart",\
          "company_website": "https://techstart.io"\
        },\
        "processor": "pro"\
      }\
    ]
  }'
  ```

  ```python Python theme={"system"}
  # Prepare your inputs
  companies = [\
      {"company_name": "Acme Corp", "company_website": "https://acme.com"},\
      {"company_name": "TechStart", "company_website": "https://techstart.io"},\
      # ... more companies\
  ]

  # Create task run inputs
  run_inputs = [\
      BetaRunInputParam(\
          input=CompanyInput(**company).model_dump(),\
          processor="pro",\
      )\
      for company in companies\
  ]

  # Add runs to the group
  response = await client.beta.task_group.add_runs(
      taskgroup_id,
      inputs=run_inputs,
      default_task_spec=task_spec,
  )

  print(f"Added {len(response.run_ids)} Tasks to group")
  ```

  ```typescript TypeScript theme={"system"}
  // Prepare your inputs
  const companies = [\
    { company_name: "Acme Corp", company_website: "https://acme.com" },\
    { company_name: "TechStart", company_website: "https://techstart.io" },\
    // ... more companies\
  ];

  // Create task run inputs using SDK types
  const runInputs: Array<Parallel.Beta.BetaRunInput> = companies.map(
    (company) => ({
      input: {
        company_name: company.company_name,
        company_website: company.company_website,
      },
      processor: "pro",
    })
  );

  // Add runs to the group
  const response = await client.beta.taskGroup.addRuns(taskgroupId, {
    default_task_spec: taskSpec,
    inputs: runInputs,
  });

  console.log(`Added ${response.run_ids.length} Tasks to group`);
  ```
</CodeGroup>

### 4. Monitor Progress

<CodeGroup>
  ```bash cURL theme={"system"}
  # Get status of the group
  curl --request GET \
    --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID} \
    --header 'x-api-key: ${PARALLEL_API_KEY}'

  # Get status of all runs in the group
  curl --request GET \
    --no-buffer \
    --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID}/runs \
    --header 'x-api-key: ${PARALLEL_API_KEY}'
  ```

  ```python Python theme={"system"}
  import asyncio

  async def wait_for_completion(client: AsyncParallel, taskgroup_id: str) -> None:
      while True:
          task_group = await client.beta.task_group.retrieve(taskgroup_id)

          status = task_group.status
          print(f"Status: {status.task_run_status_counts}")

          if not status.is_active:
              print("All tasks completed!")
              break

          await asyncio.sleep(10)

  asyncio.run(wait_for_completion(client, taskgroup_id))
  ```

  ```typescript TypeScript theme={"system"}
  async function waitForCompletion(
    client: Parallel,
    taskgroupId: string
  ): Promise<void> {
    while (true) {
      const response = await client.beta.taskGroup.retrieve(taskgroupId);

      const status = response.status;
      console.log("Status:", status.task_run_status_counts);

      if (!status.is_active) {
        console.log("All tasks completed!");
        break;
      }

      // Wait 10 seconds before checking again
      await new Promise((resolve) => setTimeout(resolve, 10000));
    }
  }

  async function main() {
    const client = new Parallel({ apiKey: process.env["PARALLEL_API_KEY"] });
    // ... create task group and get taskgroupId ...
    await waitForCompletion(client, taskgroupId);
  }

  main();
  ```
</CodeGroup>

### 5. Retrieve Results

The `getRuns` endpoint returns a **Server-Sent Events stream**, not a simple JSON response. Each event in the stream has:

* `type`: Either `"task_run.state"` (a run reached a non-active status: completed, failed, or cancelled) or `"error"`
* `event_id`: Cursor for resuming the stream via the `last_event_id` parameter
* `run`: The `TaskRun` object with `run_id`, `status`, and `is_active`
* `input`: The original input (only included when `include_input=true`)
* `output`: The result output (only included when `include_output=true` **and** the run completed successfully)

<CodeGroup>
  ```bash cURL theme={"system"}
  curl --request GET \
    --no-buffer \
    --url https://api.parallel.ai/v1beta/tasks/groups/${TASKGROUP_ID}/events \
    --header 'x-api-key: ${PARALLEL_API_KEY}'
  ```

  ```python Python theme={"system"}
  from parallel.types.beta.task_run_event import TaskRunEvent
  from parallel.types.beta.error_event import ErrorEvent

  # Stream all results from the group
  async def get_all_results(client: AsyncParallel, taskgroup_id: str):
      results = []

      run_stream = await client.beta.task_group.get_runs(
          taskgroup_id,
          include_input=True,
          include_output=True,
      )

      async for event in run_stream:
          if isinstance(event, TaskRunEvent) and event.output:
              company_output = CompanyOutput.model_validate(event.output.content)

              results.append(
                  {
                      "company": event.input.input["company_name"],
                      "insights": company_output.key_insights,
                      "market_position": company_output.market_position,
                  }
              )
          elif isinstance(event, ErrorEvent):
              print(f"Error: {event.error}")

      return results

  results = await get_all_results(client, taskgroup_id)
  print(f"Processed {len(results)} companies successfully")
  ```

  ```typescript TypeScript theme={"system"}
  // Stream all results from the group
  async function getAllResults(
    client: Parallel,
    taskgroupId: string
  ): Promise<
    Array<{ company: string; insights: string[]; market_position: string }>
  > {
    const results: Array<{
      company: string;
      insights: string[];
      market_position: string;
    }> = [];

    // Use the SDK's streaming API
    const runStream = await client.beta.taskGroup.getRuns(taskgroupId, {
      include_input: true,
      include_output: true,
    });

    for await (const event of runStream) {
      // Handle task run events
      if (event.type === "task_run.state" && event.output) {
        const input = event.input?.input as CompanyInput;
        const output = (event.output as Parallel.TaskRunJsonOutput)
          .content as unknown as CompanyOutput;

        results.push({
          company: input.company_name,
          insights: output.key_insights,
          market_position: output.market_position,
        });
      }
    }

    return results;
  }

  const results = await getAllResults(client, taskgroupId);
  console.log(`Processed ${results.length} companies successfully`);
  ```
</CodeGroup>

## Batch Processing Pattern

For large datasets, process Tasks in batches to optimize performance:

<CodeGroup>
  ```python Python theme={"system"}
  async def process_companies_in_batches(
      client: AsyncParallel,
      taskgroup_id: str,
      companies: list[dict[str, str]],
      batch_size: int = 500,
  ) -> None:
      total_created = 0

      for i in range(0, len(companies), batch_size):
          batch = companies[i : i + batch_size]

          # Create run inputs for this batch
          run_inputs = [\
              BetaRunInputParam(\
                  input=CompanyInput(**company).model_dump(),\
                  processor="pro",\
              )\
              for company in batch\
          ]

          # Add batch to group
          response = await client.beta.task_group.add_runs(
              taskgroup_id,
              inputs=run_inputs,
              default_task_spec=task_spec,
          )
          total_created += len(response.run_ids)

          print(f"Processed {i + len(batch)} companies. Created {total_created} Tasks.")
  ```

  ```typescript TypeScript theme={"system"}
  async function processCompaniesInBatches(
    client: Parallel,
    taskgroupId: string,
    companies: Array<{ company_name: string; company_website: string }>,
    batchSize: number = 500
  ): Promise<void> {
    let totalCreated = 0;

    for (let i = 0; i < companies.length; i += batchSize) {
      const batch = companies.slice(i, i + batchSize);

      // Create run inputs for this batch using SDK types
      const runInputs: Array<Parallel.Beta.BetaRunInput> = batch.map(
        (company) => ({
          input: {
            company_name: company.company_name,
            company_website: company.company_website,
          },
          processor: "pro",
        })
      );

      // Add batch to group
      const response = await client.beta.taskGroup.addRuns(taskgroupId, {
        default_task_spec: taskSpec,
        inputs: runInputs,
      });

      totalCreated += response.run_ids.length;

      console.log(
        `Processed ${i + batch.length} companies. Created ${totalCreated} Tasks.`
      );
    }
  }
  ```
</CodeGroup>

## Error Handling

The Group API provides robust error handling:

<CodeGroup>
  ```python Python theme={"system"}
  async def process_with_error_handling(client: AsyncParallel, taskgroup_id: str):
      successful_results = []
      failed_results = []

      run_stream = await client.beta.task_group.get_runs(
          taskgroup_id,
          include_input=True,
          include_output=True,
      )

      async for event in run_stream:
          if isinstance(event, ErrorEvent):
              failed_results.append(event)
              continue

          if isinstance(event, TaskRunEvent) and event.output:
              try:
                  # Validate the result
                  company_output = CompanyOutput.model_validate(event.output.content)
                  successful_results.append(event)
              except Exception as e:
                  print(f"Validation error: {e}")
                  failed_results.append(event)
          elif isinstance(event, TaskRunEvent):
              # Run failed or was cancelled (no output)
              failed_results.append(event)

      print(f"Success: {len(successful_results)}, Failed: {len(failed_results)}")
      return successful_results, failed_results
  ```

  ```typescript TypeScript theme={"system"}
  async function processWithErrorHandling(
    client: Parallel,
    taskgroupId: string
  ): Promise<{
    successful: Array<Parallel.Beta.TaskGroupGetRunsResponse>;
    failed: Array<Parallel.Beta.TaskGroupGetRunsResponse>;
  }> {
    const successful: Array<Parallel.Beta.TaskGroupGetRunsResponse> = [];
    const failed: Array<Parallel.Beta.TaskGroupGetRunsResponse> = [];

    const runStream = await client.beta.taskGroup.getRuns(taskgroupId, {
      include_input: true,
      include_output: true,
    });

    for await (const event of runStream) {
      if (event.type === "error") {
        failed.push(event);
        continue;
      }

      if (event.type === "task_run.state") {
        try {
          // Validate the result
          const input = event.input?.input as CompanyInput;
          const output = event.output
            ? ((event.output as Parallel.TaskRunJsonOutput)
                .content as CompanyOutput)
            : null;

          if (input && output) {
            successful.push(event);
          }
        } catch (e) {
          console.error("Validation error:", e);
          failed.push(event);
        }
      }
    }

    console.log(`Success: ${successful.length}, Failed: ${failed.length}`);
    return { successful, failed };
  }
  ```
</CodeGroup>

## Complete Example

Here's a complete script that demonstrates the full workflow, including all of
the setup code above.

<CodeGroup>
  ```python Python [expandable] theme={"system"}
  import asyncio
  import pydantic
  from parallel import AsyncParallel
  from parallel.types import TaskSpecParam, JsonSchemaParam
  from parallel.types.beta.beta_run_input_param import BetaRunInputParam
  from parallel.types.beta.task_run_event import TaskRunEvent
  from parallel.types.beta.error_event import ErrorEvent

  # Define your input and output models
  class CompanyInput(pydantic.BaseModel):
      company_name: str = pydantic.Field(description="Name of the company")
      company_website: str = pydantic.Field(description="Company website URL")

  class CompanyOutput(pydantic.BaseModel):
      key_insights: list[str] = pydantic.Field(description="Key business insights")
      market_position: str = pydantic.Field(description="Market positioning analysis")

  # Create reusable task specification
  task_spec = TaskSpecParam(
      input_schema=JsonSchemaParam(json_schema=CompanyInput.model_json_schema()),
      output_schema=JsonSchemaParam(json_schema=CompanyOutput.model_json_schema()),
  )

  async def wait_for_completion(client: AsyncParallel, taskgroup_id: str) -> None:
      while True:
          task_group = await client.beta.task_group.retrieve(taskgroup_id)

          status = task_group.status
          print(f"Status: {status.task_run_status_counts}")

          if not status.is_active:
              print("All tasks completed!")
              break

          await asyncio.sleep(10)

  async def get_all_results(client: AsyncParallel, taskgroup_id: str):
      results = []

      run_stream = await client.beta.task_group.get_runs(
          taskgroup_id,
          include_input=True,
          include_output=True,
      )

      async for event in run_stream:
          if isinstance(event, TaskRunEvent) and event.output:
              company_output = CompanyOutput.model_validate(event.output.content)

              results.append(
                  {
                      "company": event.input.input["company_name"],
                      "insights": company_output.key_insights,
                      "market_position": company_output.market_position,
                  }
              )
          elif isinstance(event, ErrorEvent):
              print(f"Error: {event.error}")

      return results

  async def batch_company_research():
      client = AsyncParallel(api_key="PARALLEL_API_KEY")

      # Create task group
      task_group = await client.beta.task_group.create()
      taskgroup_id = task_group.task_group_id
      print(f"Created taskgroup id {taskgroup_id}")

      # Define companies to research
      companies = [\
          {"company_name": "Stripe", "company_website": "https://stripe.com"},\
          {"company_name": "Shopify", "company_website": "https://shopify.com"},\
          {"company_name": "Salesforce", "company_website": "https://salesforce.com"},\
      ]

      # Add Tasks to group
      run_inputs = [\
          BetaRunInputParam(\
              input=CompanyInput(**company).model_dump(),\
              processor="pro",\
          )\
          for company in companies\
      ]

      response = await client.beta.task_group.add_runs(
          taskgroup_id,
          inputs=run_inputs,
          default_task_spec=task_spec,
      )
      print(f"Added {len(response.run_ids)} runs to taskgroup {taskgroup_id}")

      # Wait for completion and get results
      await wait_for_completion(client, taskgroup_id)
      results = await get_all_results(client, taskgroup_id)
      print(f"Successfully processed {len(results)} companies")
      return results

  # Run the batch job
  results = asyncio.run(batch_company_research())
  ```

  ```typescript TypeScript [expandable] theme={"system"}
  import Parallel from "parallel-web";

  // Define your input and output types
  interface CompanyInput {
    company_name: string;
    company_website: string;
  }

  interface CompanyOutput {
    key_insights: string[];
    market_position: string;
  }

  // Use SDK types for Task Group API
  type TaskGroupObject = Parallel.Beta.TaskGroup;
  type TaskGroupGetRunsResponse = Parallel.Beta.TaskGroupGetRunsResponse;

  // Create reusable task specification using SDK types
  const taskSpec: Parallel.TaskSpec = {
    input_schema: {
      type: "json",
      json_schema: {
        type: "object",
        properties: {
          company_name: {
            type: "string",
            description: "Name of the company",
          },
          company_website: {
            type: "string",
            description: "Company website URL",
          },
        },
        required: ["company_name", "company_website"],
      },
    },
    output_schema: {
      type: "json",
      json_schema: {
        type: "object",
        properties: {
          key_insights: {
            type: "array",
            items: { type: "string" },
            description: "Key business insights",
          },
          market_position: {
            type: "string",
            description: "Market positioning analysis",
          },
        },
        required: ["key_insights", "market_position"],
      },
    },
  };

  async function waitForCompletion(
    client: Parallel,
    taskgroupId: string
  ): Promise<void> {
    while (true) {
      const response = await client.beta.taskGroup.retrieve(taskgroupId);

      const status = response.status;
      console.log("Status:", status.task_run_status_counts);

      if (!status.is_active) {
        console.log("All tasks completed!");
        break;
      }

      await new Promise((resolve) => setTimeout(resolve, 10000));
    }
  }

  async function getAllResults(
    client: Parallel,
    taskgroupId: string
  ): Promise<
    Array<{ company: string; insights: string[]; market_position: string }>
  > {
    const results: Array<{
      company: string;
      insights: string[];
      market_position: string;
    }> = [];

    const runStream = await client.beta.taskGroup.getRuns(taskgroupId, {
      include_input: true,
      include_output: true,
    });

    for await (const event of runStream) {
      if (event.type === "task_run.state" && event.output) {
        const input = event.input?.input as CompanyInput;
        const output = (event.output as Parallel.TaskRunJsonOutput)
          .content as CompanyOutput;

        results.push({
          company: input.company_name,
          insights: output.key_insights,
          market_position: output.market_position,
        });
      }
    }

    return results;
  }

  async function batchCompanyResearch(): Promise<
    Array<{ company: string; insights: string[]; market_position: string }>
  > {
    const client = new Parallel({
      apiKey: process.env.PARALLEL_API_KEY,
    });

    // Create task group
    const groupResponse = await client.beta.taskGroup.create({});
    const taskgroupId = groupResponse.taskgroup_id;
    console.log(`Created taskgroup id ${taskgroupId}`);

    // Define companies to research
    const companies = [\
      { company_name: "Stripe", company_website: "https://stripe.com" },\
      { company_name: "Shopify", company_website: "https://shopify.com" },\
      { company_name: "Salesforce", company_website: "https://salesforce.com" },\
    ];

    // Add Tasks to group
    const runInputs: Array<Parallel.Beta.BetaRunInput> = companies.map(
      (company) => ({
        input: {
          company_name: company.company_name,
          company_website: company.company_website,
        },
        processor: "pro",
      })
    );

    const response = await client.beta.taskGroup.addRuns(taskgroupId, {
      default_task_spec: taskSpec,
      inputs: runInputs,
    });

    console.log(
      `Added ${response.run_ids.length} runs to taskgroup ${taskgroupId}`
    );

    // Wait for completion and get results
    await waitForCompletion(client, taskgroupId);
    const results = await getAllResults(client, taskgroupId);
    console.log(`Successfully processed ${results.length} companies`);
    return results;
  }

  // Run the batch job
  const results = await batchCompanyResearch();
  ```
</CodeGroup>

# Processors
Source: https://docs.parallel.ai/task-api/guides/choose-a-processor

Select the right Task API processor (lite, base, core, pro, ultra) based on task complexity and latency requirements

Processors are the engines that execute Task Runs. The choice of Processor determines the performance profile and reasoning behavior used. Any Task Run can be executed on any Processor.

<Tip> Choose a processor based on **task complexity** and **latency requirements**. Use `lite` or `base` for simple enrichments, `core` for reliable accuracy on up to 10 output fields, and `pro` or `ultra` when reasoning depth is critical. For latency-sensitive workflows, append `-fast` to any processor name. </Tip>

Each processor varies in performance characteristics and supported features. Use the tables below to compare standard and fast processors.

<Note>
  **About "Max Fields" (the `~` symbol):** The max fields column shows approximate limits because actual capacity depends on field complexity. Simple fields like dates or booleans use less capacity than complex fields requiring extensive research. A task with 5 complex analytical fields may require more processing than one with 15 simple lookup fields. Use these numbers as guidelines. If you're near the limit and seeing quality issues, try a higher-tier processor.
</Note>

<Tabs>
  <Tab title="Standard">
    | Processor | Latency      | Strengths                                    | Max Fields  |
    | --------- | ------------ | -------------------------------------------- | ----------- |
    | `lite`    | 10s - 60s    | Basic metadata, fallback, low latency        | \~2 fields  |
    | `base`    | 15s - 100s   | Reliable standard enrichments                | \~5 fields  |
    | `core`    | 60s - 5min   | Cross-referenced, moderately complex outputs | \~10 fields |
    | `core2x`  | 60s - 10min  | High complexity cross referenced outputs     | \~10 fields |
    | `pro`     | 2min - 10min | Exploratory web research                     | \~20 fields |
    | `ultra`   | 5min - 25min | Advanced multi-source deep research          | \~20 fields |
    | `ultra2x` | 5min - 50min | Difficult deep research                      | \~25 fields |
    | `ultra4x` | 5min - 90min | Very difficult deep research                 | \~25 fields |
    | `ultra8x` | 5min - 2hr   | The most difficult deep research             | \~25 fields |
  </Tab>

  <Tab title="Fast">
    | Processor      | Latency      | Strengths                                    | Max Fields  |
    | -------------- | ------------ | -------------------------------------------- | ----------- |
    | `lite-fast`    | 10s - 20s    | Basic metadata, fallback, lowest latency     | \~2 fields  |
    | `base-fast`    | 15s - 50s    | Reliable standard enrichments                | \~5 fields  |
    | `core-fast`    | 15s - 100s   | Cross-referenced, moderately complex outputs | \~10 fields |
    | `core2x-fast`  | 15s - 3min   | High complexity cross referenced outputs     | \~10 fields |
    | `pro-fast`     | 30s - 5min   | Exploratory web research                     | \~20 fields |
    | `ultra-fast`   | 1min - 10min | Advanced multi-source deep research          | \~20 fields |
    | `ultra2x-fast` | 1min - 20min | Difficult deep research                      | \~25 fields |
    | `ultra4x-fast` | 1min - 40min | Very difficult deep research                 | \~25 fields |
    | `ultra8x-fast` | 1min - 1hr   | The most difficult deep research             | \~25 fields |
  </Tab>
</Tabs>

<Note>
  See [Pricing](/getting-started/pricing) for processor costs and all API rates.
</Note>

## Standard vs Fast Processors

Each processor is available in two variants: **Standard** and **Fast**. They differ in how they balance speed versus data freshness.

To use a fast processor, append `-fast` to the processor name:

```python theme={"system"}
task_run = client.task_run.create(
    input="Parallel Web Systems (parallel.ai)",
    task_spec={"output_schema": "The founding date of the company"},
    processor="core-fast"  # Fast processor
)
```

### What's the Trade-off?

| Aspect             | Standard Processors                       | Fast Processors                   |
| ------------------ | ----------------------------------------- | --------------------------------- |
| **Latency**        | Higher                                    | 2-5x faster                       |
| **Data Freshness** | Highest freshness (prioritizes live data) | Very fresh (optimized for speed)  |
| **Best For**       | Background jobs, accuracy-critical tasks  | Interactive apps, agent workflows |

The trade-off is simple: **fast processors optimize for speed, standard processors optimize for freshness**. Both maintain high accuracy—the difference is in how they prioritize when retrieving data.

### Why are Fast Processors Faster?

Fast processors are optimized for speed—they return results as quickly as possible while maintaining high accuracy. Standard processors prioritize data freshness and will wait longer to ensure the most up-to-date information when needed.

In practice, you can expect **2-5x faster response times** with fast processors compared to standard processors for the same tier. This makes fast processors ideal for interactive applications where users are waiting for results.

### How Fresh is the Data?

Both processor types access **very fresh data** sufficient for most use cases. Our data is continuously updated, so for the vast majority of queries—company information, product details, professional backgrounds, market research—both will return accurate, current results.

**When to prefer standard processors for freshness:**

* Real-time financial data (stock prices, exchange rates)
* Breaking news or events from the last few hours
* Rapidly changing information (live scores, election results)
* Any use case where absolute data freshness is more important than speed

### When to Use Each

<Tabs>
  <Tab title="Standard Processors">
    * **Accuracy is paramount** - When correctness matters much more than speed
    * **Real-time data required** - Stock prices, live scores, breaking news
    * **Background/async jobs** - Tasks running without user waiting
    * **Research-heavy tasks** - Deep research benefiting from live sources
    * **High-volume async enrichments** - Processing large datasets in the background
  </Tab>

  <Tab title="Fast Processors">
    * **Testing agents** - Rapid iteration during development
    * **Subagent calls** - A calling agent needs low-latency responses
    * **Interactive applications** - Table UIs where users actively run tasks
    * **Latency-sensitive workflows** - Any use case where speed is critical
  </Tab>
</Tabs>

## Examples

Processors can be used flexibly depending on the scope and structure of your task. The examples below show how to:

* Use a single processor (like `lite`, `base`, `core`, `pro`, or `ultra`) to handle specific types of input and reasoning depth.
* Chain processors together to combine fast lookups with deeper synthesis.

This structure enables flexibility across a variety of tasks—whether you're extracting metadata, enriching structured records, or generating analytical reports.

### Sample Task for each Processor

<CodeGroup>
  ```python lite theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date of the company in the format MM-YYYY"},
      processor="lite"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python base theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date and most recent product launch of the company"},
      processor="base"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python core theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date, founders, and most recent product launch of the company"},
      processor="core"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python pro theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date, founders, mission, benchmarked competitors and most recent product launch of the company"},
      processor="pro"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python ultra theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"A comprehensive analysis of the industry of the company, including growth factors and major competitors."},
      processor="ultra"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```
</CodeGroup>

### Sample Task for each Fast Processor

<CodeGroup>
  ```python lite-fast theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date of the company in the format MM-YYYY"},
      processor="lite-fast"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python base-fast theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date and most recent product launch of the company"},
      processor="base-fast"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python core-fast theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date, founders, and most recent product launch of the company"},
      processor="core-fast"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python pro-fast theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"The founding date, founders, mission, benchmarked competitors and most recent product launch of the company"},
      processor="pro-fast"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```python ultra-fast theme={"system"}
  task_run = client.task_run.create(
      input="Parallel Web Systems (parallel.ai)",
      task_spec={"output_schema":"A comprehensive analysis of the industry of the company, including growth factors and major competitors."},
      processor="ultra-fast"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```
</CodeGroup>

### Multi-Processor Workflows

You can combine processors in sequence to support more advanced workflows.

Start by retrieving basic information with `base`:

```python theme={"system"}
task_run_base = client.task_run.create(
    input="Pfizer",
    task_spec={"output_schema":"Who are the current executive leaders at Pfizer? Include their full name and title. Ensure that you retrieve this information from a reliable source, such as major news outlets or the company website."},
    processor="base"
)
print(f"Run ID: {task_run_base.run_id}")

base_result = client.task_run.result(task_run_base.run_id, api_timeout=3600)
print(base_result.output)
```

Then use the result as input to `core` to generate detailed background information:

```python theme={"system"}
import json

task_run = client.task_run.create(
    input=json.dumps(base_result.output.content),
    task_spec={"output_schema":"For the executive provided, find their professional background tenure at their current company, and notable strategic responsibilities."},
    processor="pro"
)
print(f"Run ID: {task_run.run_id}")

run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
print(run_result.output)
```

This lets you use a lower compute processor for initial retrieval, then switch to a more capable one for analysis and context-building.

# MCP Tool Calling
Source: https://docs.parallel.ai/task-api/mcp-tool-call

Using MCP servers for tool calls in Tasks

<Note>
  This feature is currently in beta and requires the
  <code>parallel-beta: mcp-server-2025-07-17</code> header when using the Task API.
</Note>

## Overview

The Parallel API allows you to specify remote MCP servers for Task API execution. This enables the model to access tools hosted on remote MCP servers without needing a separate MCP client.

### Specifying MCP Servers

MCP servers are specified using the `mcp_servers` field in the Task API call. Each request can include up to 10 MCP servers.

| Parameter       | Type                      | Description                                     |
| --------------- | ------------------------- | ----------------------------------------------- |
| `type`          | `string`                  | Always `url`.                                   |
| `url`           | `string`                  | The URL of the MCP server.                      |
| `name`          | `string`                  | A name for the MCP server.                      |
| `headers`       | `dict[string, string]`    | Headers for authenticating with the MCP server. |
| `allowed_tools` | `array[string]` or `null` | List of tools to allow, or null for all.        |

#### Sample Request

<CodeGroup>
  ```bash Task API theme={"system"}
  curl -X POST "https://api.parallel.ai/v1/tasks/runs" \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H "Content-Type: application/json" \
    -H "parallel-beta: mcp-server-2025-07-17" \
    --data '{
    "input": "What is the latest in AI research?",
    "processor": "lite",
    "mcp_servers": [\
      {\
          "type": "url",\
          "url": "https://dummy_mcp_server",\
          "name": "dummy_mcp_server",\
          "headers": {"x-api-key": "API_KEY"}\
      }\
    ]
  }'
  ```
</CodeGroup>

#### Restrictions

* Only MCP servers with Streamable HTTP transport are currently supported.
* From the [MCP specification](https://modelcontextprotocol.io/specification/2025-03-26), only tools are supported.
* For [MCP servers using OAuth](https://modelcontextprotocol.io/specification/draft/basic/authorization), you must generate the authorization token separately and include it as a bearer token in the headers.
* You can specify up to 10 MCP servers per request, but using fewer is recommended for optimal result quality.

## Using MCP Servers in the Task API

When you make a Task API request, the API first fetches the available tools from the specified MCP servers.
The processor will invoke tools from these servers if it determines they are useful for the task. The number of tool calls depends
on the [processor](/task-api/guides/choose-a-processor):

* For `lite` and `core`, at most one tool is invoked.
* For all other processors, multiple tool calls may be made.

## Response Content

The Task API response includes a list of tool calls made during execution. Each tool call entry contains:

| Parameter      | Type     | Description                                                                                  |
| -------------- | -------- | -------------------------------------------------------------------------------------------- |
| `tool_call_id` | `string` | Unique identifier for the tool call.                                                         |
| `server_name`  | `string` | Name of the MCP server, as provided in the input.                                            |
| `tool_name`    | `string` | Name of the tool invoked.                                                                    |
| `arguments`    | `string` | JSON-encoded string of the arguments used for the tool call.                                 |
| `content`      | `string` | Response from the MCP server.                                                                |
| `error`        | `string` | Error message if the tool call failed. Either `content` or `error` will always be populated. |

If there is an authentication issue with any MCP server, the top-level `warning` field in the Task Run output
will be populated.

<CodeGroup>
  ```bash Success theme={"system"}
  {
    "run": {
      "run_id": "trun_6eb64c73e4324b159fb4c63cc673cb73",
      "status": "completed",
      "is_active": false,
      "warnings": null,
      "error": null,
      "processor": "lite",
      "metadata": {},
      "taskgroup_id": null,
      "created_at": "2025-07-24T21:47:23.245857Z",
      "modified_at": "2025-07-24T21:47:41.874114Z"
    },
    "output": {
      "basis": [\
        {\
          "field": "output",\
          "citations": [\
            {\
              "title": null,\
              "url": "https://www.crescendo.ai/news/latest-ai-news-and-updates",\
              "excerpts": []\
            }\
          ],\
          "reasoning": "I used the provided search results to identify the latest AI research developments as of July 2025. I focused on extracting information about new AI models, applications, and ethical considerations from the search results to provide a comprehensive overview.",\
          "confidence": ""\
        }\
      ],
      "mcp_tool_calls": [\
        {\
          "tool_call_id": "call_p1tBixLzgDAMoTrPIK9R6Gew",\
          "server_name": "parallel_web_search",\
          "tool_name": "web_search_parallel",\
          "arguments": "{\"query\": \"latest AI research July 2025\", \"objective\": \"To find the most recent developments in AI research.\"}",\
          "content": "{\n  \"search_id\": \"search_14c4ca29-5ae3-b74a-de65-dcb8506d9b20\",\n  \"results\": ...}",\
          "error": ""\
        }\
      ],
      "type": "text",
      "content": "As of July 2025, ...."
    }
  }
  ```

  ```bash Failure authenticating to MCP server theme={"system"}
  {
    "run": {
      "run_id": "trun_6eb64c73e4324b15aa537bc630b8a9d9",
      "status": "completed",
      "is_active": false,
      "warnings": [\
        {\
          "type": "warning",\
          "message": "Error listing tools from MCP server dummy_mcp_server. Reference ID: b0ac36f3-ceb6-4290-b7c9-c0bb4257ccf7",\
          "detail": {}\
        }\
      ],
      "error": null,
      "processor": "lite",
      "metadata": {},
      "taskgroup_id": null,
      "created_at": "2025-07-24T21:41:19.103657Z",
      "modified_at": "2025-07-24T21:41:33.650738Z"
    },
    "output": {
      "basis": [\
        {\
          "field": "output",\
          "citations": [\
            {\
              "title": null,\
              "url": "https://www.crescendo.ai/news/latest-ai-news-and-updates",\
              "excerpts": []\
            }\
          ],\
          "reasoning": "The search results provide an overview of the latest AI research developments, including AI models mimicking human decision-making, AI applications in healthcare, and AI-driven automation across various industries. The response summarizes these key developments and cites the relevant articles.",\
          "confidence": ""\
        }\
      ],
      "mcp_tool_calls": null,
      "type": "text",
      "content": "As of July 2025, ...."
    }
  }
  ```
</CodeGroup>

# Task API Deep Research Quickstart
Source: https://docs.parallel.ai/task-api/task-deep-research

Transform natural language queries into comprehensive intelligence reports

## Overview

Deep Research is designed for open-ended research questions where you don't have structured input data to enrich. Instead of bringing data to enhance, you bring a research question or topic, and the Task API conducts comprehensive multi-step web exploration to deliver analyst-grade intelligence.

This powerful capability compresses hours of manual research into minutes, delivering high-quality intelligence at scale. Optimized within the `pro` and `ultra` [processor families](/task-api/guides/choose-a-processor), Deep Research transforms natural language research queries into comprehensive reports complete with inline citations and verification.

<Tip>
  For faster turnaround, use fast processors like `pro-fast` or `ultra-fast`. These deliver 2-5x faster response times while maintaining high accuracy—ideal for interactive applications or when you need quicker results. See [Standard vs Fast Processors](/task-api/guides/choose-a-processor#standard-vs-fast-processors) for details.
</Tip>

<Note>
  This guide focuses on **Deep Research**. If you have structured data you want to enrich with web intelligence (like adding columns to a spreadsheet), see our [Enrichment Quickstart](/task-api/task-quickstart).
</Note>

## How Deep Research Works

With Deep Research, the system automatically:

1. Interprets your research intent from natural language
2. Conducts multi-step web exploration across authoritative sources
3. Synthesizes findings into structured data or markdown reports
4. Provides citations and confidence levels for verification

## Key Features

* **Natural Language Input**: Simply describe what you want to research in plain language—no need for structured data or predefined schemas.
* **Declarative Approach**: Specify what intelligence you need, and the system handles the complex orchestration of research, exploration, and synthesis.
* **Flexible Output Structure**: Choose between `auto` schema mode (automatically structured JSON), `text` mode (markdown reports) or pre-specified structured JSON schema based on your needs.
* **Comprehensive Intelligence**: Multi-step research across authoritative sources with granular citations, reasoning, and confidence levels for every finding.

<Note>
  Long-Running Tasks: Deep Research can take up to 45 minutes to complete. See [Polling vs Webhooks vs SSE](#polling-vs-webhooks-vs-sse) below for how to handle async results.
</Note>

## Creating a Deep Research Task

Deep Research accepts any input schema as input, including plain-text strings.
The more specific and detailed your input, the better the research results would be.

<Note>
  **Input size restriction**: Deep Research is optimized for concise research
  prompts and is not meant for long context inputs. Keep your input under
  **15,000 characters** for optimal performance and results.
</Note>

Deep Research supports two output formats to meet different integration needs:

### Auto Schema

Specifying auto schema mode in the Task API output schema triggers Deep Research
and ensures well-structured outputs, without the need to specify a desired output structure.
The final schema type will follow a [JSONSchema](/api-reference/tasks-v1/create-task-run#body-task-spec-output-schema)
format and will be determined by the processor automatically.

Auto schema mode is the default mode when using `pro` and `ultra` line of processors.
This format is ideal for programmatic processing, data analysis, and integration with other systems.

<CodeGroup>
  ```python Python theme={"system"}
  from parallel import Parallel

  client = Parallel(api_key="PARALLEL_API_KEY")

  task_run = client.task_run.create(
      input="Create a comprehensive market research report on the HVAC industry in the USA including an analysis of recent M&A activity and other relevant details.",
      processor="ultra"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from "parallel-web";

  const client = new Parallel({
    apiKey: process.env["PARALLEL_API_KEY"],
  });

  async function main() {
    const taskRun = await client.taskRun.create({
      input:
        "Create a comprehensive market research report on the HVAC industry in the USA including an analysis of recent M&A activity and other relevant details.",
      processor: "ultra",
    });

    console.log(`Run ID: ${taskRun.run_id}`);

    // Poll for results with 25-second timeout, retry up to 144 times (1 hour total)
    let runResult;
    for (let i = 0; i < 144; i++) {
      try {
        runResult = await client.taskRun.result(taskRun.run_id, { timeout: 25 });
        break;
      } catch (error) {
        if (i === 143) throw error; // Last attempt failed
        await new Promise((resolve) => setTimeout(resolve, 1000));
      }
    }

    console.log(runResult.output);
  }

  main();
  ```

  ```bash cURL theme={"system"}
  curl -X POST "https://api.parallel.ai/v1/tasks/runs" \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H 'Content-Type: application/json' \
    --data-raw '{
    "input": "Create a comprehensive market research report on the HVAC industry in the USA including an analysis of recent M&A activity and other relevant details.",
    "processor": "ultra"
  }'
  ```
</CodeGroup>

### Text Schema

Specifying text schema mode in the Task API output schema triggers Deep Research with a markdown report output format.
The generated result will contain extensive research formatted into a markdown report with in-line citations.
This format is perfect for human-readable content as well as LLM ingestion.

To provide guidance on the output, use the description field when specifying text schema. This
allows users to steer the report generated towards a certain direction like control over the length or the content
of the report.

<CodeGroup>
  ```python Python theme={"system"}
  from parallel import Parallel
  from parallel.types import TaskSpecParam, TextSchemaParam

  client = Parallel(api_key="PARALLEL_API_KEY")

  task_run = client.task_run.create(
      input="Create a comprehensive market research report on the HVAC industry in the USA including an analysis of recent M&A activity and other relevant details.",
      processor="ultra",
      task_spec=TaskSpecParam(output_schema=TextSchemaParam())
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from "parallel-web";

  const client = new Parallel({
    apiKey: process.env["PARALLEL_API_KEY"],
  });

  async function main() {
    const taskRun = await client.taskRun.create({
      input:
        "Create a comprehensive market research report on the HVAC industry in the USA including an analysis of recent M&A activity and other relevant details.",
      processor: "ultra",
      task_spec: {
        output_schema: {
          type: "text",
        },
      },
    });

    console.log(`Run ID: ${taskRun.run_id}`);

    // Poll for results with 25-second timeout, retry up to 144 times (1 hour total)
    let runResult;
    for (let i = 0; i < 144; i++) {
      try {
        runResult = await client.taskRun.result(taskRun.run_id, { timeout: 25 });
        break;
      } catch (error) {
        if (i === 143) throw error; // Last attempt failed
        await new Promise((resolve) => setTimeout(resolve, 1000));
      }
    }

    console.log(runResult.output);
  }

  main();
  ```

  ```bash cURL theme={"system"}
  curl -X POST "https://api.parallel.ai/v1/tasks/runs" \
    -H "x-api-key: $PARALLEL_API_KEY" \
    -H 'Content-Type: application/json' \
    --data-raw '{
    "input": "Create a comprehensive market research report on the HVAC industry in the USA including an analysis of recent M&A activity and other relevant details.",
    "processor": "ultra",
    "task_spec": {
      "output_schema": {
        "type": "text"
      }
    }
  }'
  ```
</CodeGroup>

### Sample Response

<Note>
  **Important**: The response below shows the **final completed result** after
  Deep Research has finished. When you first create a task, you'll receive an
  immediate response with `"status": "running"`. You'll need to poll the task or
  use [webhooks](/task-api/webhooks) to get the final structured research output
  shown below.
</Note>

Below is a shortened sample response using the `auto` schema. The complete response contained 124 content fields, with 610 total citations for this Task.

```json [expandable] theme={"system"}
{
  "output": {
    "content": {
      "market_size_and_forecast": {
        "cagr": "6.9%",
        "market_segment": "U.S. HVAC Systems",
        "current_valuation": "USD 29.89 billion (2024)",
        "forecasted_valuation": "USD 54.02 billion",
        "forecast_period": "2025-2033"
      },
      "company_profiles": [\
        {\
          "company_name": "Carrier Global Corporation",\
          "stock_ticker": "CARR",\
          "revenue": "$22.5 billion (FY2024)",\
          "market_capitalization": "$63.698 billion (July 1, 2025)",\
          "market_position": "Global leader in intelligent climate and energy solutions",\
          "recent_developments": "Acquisition of Viessmann Climate Solutions for $13 billion"\
        },\
        {\
          "company_name": "Daikin Industries, Ltd.",\
          "stock_ticker": "DKILY",\
          "revenue": "¥4,752.3 billion (FY2024)",\
          "market_position": "Japan's leading HVAC manufacturer and top global player",\
          "recent_developments": "Multiple acquisitions to strengthen supply capabilities"\
        }\
      ],
      "recent_mergers_and_acquisitions": {
        "acquiring_company": "Carrier Ventures",
        "target_company": "ZutaCore",
        "deal_summary": "Strategic investment in liquid cooling systems for data centers",
        "date": "February 2025"
      },
      "growth_opportunities": "Data center cooling, building retrofits, electrification, healthcare applications, and enhanced aftermarket services",
      "market_segmentation_analysis": {
        "dominant_segment": "Residential",
        "dominant_segment_share": "39.8% (in 2024)",
        "fastest_growing_segment": "Commercial",
        "fastest_growing_segment_cagr": "7.4% (from 2025 to 2033)"
      },
      "publicly_traded_hvac_companies": [\
        {\
          "company_name": "Carrier Global Corporation",\
          "stock_ticker": "CARR"\
        },\
        {\
          "company_name": "Daikin Industries, Ltd.",\
          "stock_ticker": "DKILY"\
        },\
        {\
          "company_name": "Johnson Controls International plc",\
          "stock_ticker": "JCI"\
        }\
      ]
    },
    "basis": [\
      {\
        "field": "market_size_and_forecast.current_valuation",\
        "reasoning": "Market size data sourced from Grand View Research industry analysis report, which provides comprehensive market valuation for the U.S. HVAC systems market in 2024.",\
        "citations": [\
          {\
            "url": "https://www.grandviewresearch.com/industry-analysis/us-hvac-systems-market",\
            "excerpts": [\
              "The U.S. HVAC systems market size was estimated at USD 29.89 billion in 2024"\
            ],\
            "title": "U.S. HVAC Systems Market Size, Share & Trends Analysis Report"\
          }\
        ],\
        "confidence": "high"\
      },\
      {\
        "field": "company_profiles.0.revenue",\
        "reasoning": "Carrier Global Corporation's 2024 revenue figures are directly reported in their financial communications and investor relations materials.",\
        "citations": [\
          {\
            "url": "https://monexa.ai/blog/carrier-global-corporation-strategic-climate-pivot-CARR-2025-07-02",\
            "excerpts": [\
              "Carrier reported **2024 revenues of $22.49 billion**, a modest increase of +1.76% year-over-year"\
            ],\
            "title": "Carrier Global Corporation: Strategic Climate Pivot"\
          }\
        ],\
        "confidence": "high"\
      },\
      {\
        "field": "recent_mergers_and_acquisitions",\
        "reasoning": "Carrier Ventures' strategic investment in ZutaCore represents recent M&A activity focused on next-generation cooling technologies for data centers.",\
        "citations": [\
          {\
            "url": "https://finance.yahoo.com/news/10-biggest-hvac-companies-usa-142547989.html",\
            "excerpts": [\
              "Strategic investment activity by Carrier Ventures in companies specializing in liquid cooling systems"\
            ],\
            "title": "10 Biggest HVAC Companies in the USA"\
          }\
        ],\
        "confidence": "medium"\
      }\
    ],
    "run_id": "trun_646e167d826747e1b4690e58d2b9941e",
    "status": "completed",
    "created_at": "2025-01-30T20:12:18.123456Z",
    "completed_at": "2025-01-30T20:25:41.654321Z",
    "processor": "ultra",
    "warnings": null,
    "error": null,
    "taskgroup_id": null
  }
}
```

Deep Research returns a response which includes the `content` and the `basis`, as with other [Task API](/task-api/guides/execute-task-run) executions. The key difference is that the `basis` object in an `auto` mode output contains Nested FieldBasis.

### Nested FieldBasis

<Note>
  In `text` mode, FieldBasis is not nested. It contains a list of citations (with
  URLs and excerpts) for all sites visited during research. The most relevant citations
  are included at the base of the report itself, with inline references.
</Note>

In `auto` mode, the [Basis](/task-api/guides/access-research-basis) object maps each output field (including nested fields) with supporting evidence. This ensures that every output, including nested output fields, has citations, excerpts, confidence levels and reasoning.

For nested fields, the basis uses dot notation for indexing:

* `key_players.0` for the first item in a key players array
* `industry_overview.growth_cagr` for nested object fields
* `market_trends.2.description` for nested arrays with objects

## Example: Market Research Assistant

Here's how to build a market research tool with Deep Research, showing different approaches for handling the async nature of the Task API:

<CodeGroup>
  ```python Basic Implementation theme={"system"}
  from parallel import Parallel

  client = Parallel(api_key="PARALLEL_API_KEY")

  # Execute research task (handles polling internally)
  task_run = client.task_run.create(
      input="Create a comprehensive market research report on the renewable energy storage market in Europe, focusing on battery technologies and policy impacts",
      processor="ultra"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)

  print(f"Research completed! Output has {len(run_result.output.basis)} structured fields")
  for field in run_result.output.basis[:3]:
      print(f"- {field.field}: {len(field.citations)} citations")
  ```

  ```typescript Basic Implementation theme={"system"}
  import Parallel from "parallel-web";

  const client = new Parallel({
    apiKey: process.env["PARALLEL_API_KEY"],
  });

  // Execute research task
  const taskRun = await client.taskRun.create({
    input:
      "Create a comprehensive market research report on the renewable energy storage market in Europe, focusing on battery technologies and policy impacts",
    processor: "ultra",
  });

  console.log(`Run ID: ${taskRun.run_id}`);

  // Poll for results with 25-second timeout, retry up to 144 times (1 hour total)
  let runResult;
  for (let i = 0; i < 144; i++) {
    try {
      runResult = await client.taskRun.result(taskRun.run_id, { timeout: 25 });
      break;
    } catch (error) {
      if (i === 143) throw error; // Last attempt failed
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }

  console.log(
    `Research completed! Output has ${runResult.output.basis.length} structured fields`
  );
  runResult.output.basis.slice(0, 3).forEach((field) => {
    console.log(`- ${field.field}: ${field.citations?.length || 0} citations`);
  });
  ```

  ```python With Polling theme={"system"}
  from parallel import Parallel
  import time

  client = Parallel(api_key="PARALLEL_API_KEY")

  # Create the research task (low-level API)
  task_run = client.task_run.create(
      input="Create a comprehensive market research report on the renewable energy storage market in Europe, focusing on battery technologies and policy impacts",
      processor="ultra"
  )

  print(f"Task created: {task_run.run_id}")
  print("Polling for completion...")

  # Manual polling for completion (Deep Research can take up to 15 minutes)
  while True:
      status = client.task_run.retrieve(task_run.run_id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          # Get the final results using the result() method
          run_result = client.task_run.result(task_run.run_id)
          print(f"Research completed! Output has {len(run_result.output.basis)} structured fields")

          # Display sample findings
          for field in run_result.output.basis[:3]:
              print(f"- {field.field}: {len(field.citations)} citations")
          break
      elif status.status == "failed":
          print("Task failed")
          break

      time.sleep(60)  # Check every 60 seconds
  ```

  ```typescript With Polling theme={"system"}
  import Parallel from "parallel-web";

  const client = new Parallel({
    apiKey: process.env["PARALLEL_API_KEY"],
  });

  async function main() {
    // Create the research task (low-level API)
    const taskRun = await client.taskRun.create({
      input:
        "Create a comprehensive market research report on the renewable energy storage market in Europe, focusing on battery technologies and policy impacts",
      processor: "ultra",
    });

    console.log(`Task created: ${taskRun.run_id}`);
    console.log("Polling for completion...");

    // Manual polling for completion (Deep Research can take up to 1 hour)
    let attempts = 0;
    const maxAttempts = 144; // 144 * 25 seconds = 1 hour

    while (attempts < maxAttempts) {
      const status = await client.taskRun.retrieve(taskRun.run_id);
      console.log(
        `Status: ${status.status} (attempt ${attempts + 1}/${maxAttempts})`
      );

      if (status.status === "completed") {
        // Get the final results using the result() method
        const runResult = await client.taskRun.result(taskRun.run_id, {
          timeout: 25,
        });
        console.log(
          `Research completed! Output has ${runResult.output.basis.length} structured fields`
        );

        // Display sample findings
        runResult.output.basis.slice(0, 3).forEach((field) => {
          console.log(
            `- ${field.field}: ${field.citations?.length || 0} citations`
          );
        });
        break;
      } else if (status.status === "failed") {
        console.log("Task failed");
        break;
      }

      attempts++;
      await new Promise((resolve) => setTimeout(resolve, 25000)); // Check every 25 seconds
    }

    if (attempts >= maxAttempts) {
      console.log("Task timed out after 1 hour");
    }
  }

  main();
  ```
</CodeGroup>

## Polling vs Webhooks vs SSE

The Task API is asynchronous—when you create a task, it returns immediately with a `run_id` while processing continues in the background. There are three ways to get results:

| Method       | What It Does                                                          | Best For                              |
| ------------ | --------------------------------------------------------------------- | ------------------------------------- |
| **Polling**  | Your code repeatedly calls the API to check if the task is done       | Simple integrations, scripts, testing |
| **Webhooks** | Parallel sends an HTTP request to your server when the task completes | Production apps with backend servers  |
| **SSE**      | Stream real-time progress updates as the task runs                    | Interactive UIs, monitoring progress  |

### Polling

**How it works:** After creating a task, repeatedly check its status until it completes.

```python theme={"system"}
import time

# Create task
task_run = client.task_run.create(input="...", processor="ultra")

# Poll until complete
while True:
    status = client.task_run.retrieve(task_run.run_id)
    if status.status == "completed":
        break
    if status.status == "failed":
        raise Exception(f"Task failed: {status.error}")
    time.sleep(5)  # Wait 5 seconds between checks

# First, create task with events enabled
curl -X POST "https://api.parallel.ai/v1/tasks/runs" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: events-sse-2025-07-24" \
  -d '{"input": "...", "processor": "ultra", "enable_events": true}'

# Task API Enrichment Quickstart
Source: https://docs.parallel.ai/task-api/task-enrichment

Enrich your structured data with web intelligence using the Task API

## What is Enrichment?

Enrichment is when you have existing structured data—like a list of companies, products, or contacts—and want to enhance it with additional information from the web. The Task API makes it easy to define what data you have and what additional fields you need, then automatically researches and populates those fields at scale.

## How Enrichment Works

With enrichment, you define two schemas:

1. **Input Schema**: The data fields you already have (e.g., company name, website)
2. **Output Schema**: The new fields you want to add (e.g., employee count, funding sources, founding date)

The Task API researches the web and populates your output fields with accurate, cited information.

## 1. Set up Prerequisites

Generate your API key on [Platform](https://platform.parallel.ai). Then, set up with the TypeScript SDK, Python SDK or with cURL:

<CodeGroup>
  ```bash cURL theme={"system"}
  echo "Install curl and jq via brew, apt, or your favorite package manager"
  export PARALLEL_API_KEY="PARALLEL_API_KEY"
  ```

  ```bash Python theme={"system"}
  pip install parallel-web
  export PARALLEL_API_KEY="PARALLEL_API_KEY"
  ```

  ```bash TypeScript theme={"system"}
  npm install parallel-web
  export PARALLEL_API_KEY="PARALLEL_API_KEY"
  ```

  ```bash Python (Async) theme={"system"}
  pip install parallel-web
  export PARALLEL_API_KEY="PARALLEL_API_KEY"
  ```
</CodeGroup>

## 2. Execute your First Enrichment Task

Let's enrich a simple company record. We'll start with just a company name and enrich it with a founding date:

<Tip>
  You can learn about our available Processors [here →](/task-api/guides/choose-a-processor)
</Tip>

<CodeGroup>
  ```bash cURL theme={"system"}
  echo "Creating the run:"
  RUN_JSON=$(curl -s "https://api.parallel.ai/v1/tasks/runs" \
  -H "x-api-key: ${PARALLEL_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
      "task_spec": {
          "output_schema": "The founding date of the company in the format MM-YYYY"
      },
      "input": "United Nations",
      "processor": "base"
  }')
  echo "$RUN_JSON" | jq .
  RUN_ID=$(echo "$RUN_JSON" | jq -r '.run_id')

  echo "Retrieving the run result, blocking until the result is available:"
  curl -s "https://api.parallel.ai/v1/tasks/runs/${RUN_ID}/result" \
    -H "x-api-key: ${PARALLEL_API_KEY}" | jq .

  ```

  ```python Python theme={"system"}
  import os
  from parallel import Parallel
  from parallel.types import TaskSpecParam

  client = Parallel(api_key=os.environ["PARALLEL_API_KEY"])

  task_run = client.task_run.create(
      input="United Nations",
      task_spec=TaskSpecParam(
        output_schema="The founding date of the company in the format MM-YYYY"
      ),
      processor="base"
  )
  print(f"Run ID: {task_run.run_id}")

  run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
  print(run_result.output)
  ```

  ```typescript TypeScript theme={"system"}
  import Parallel from "parallel-web";

  const client = new Parallel({
    apiKey: process.env.PARALLEL_API_KEY,
  });

  const taskRun = await client.taskRun.create({
    input: "United Nations",
    task_spec: {
      output_schema: "The founding date of the company in the format MM-YYYY",
    },
    processor: "base",
  });

  console.log(`Run ID: ${taskRun.run_id}`);

  // Poll for results with 25-second timeout, retry up to 144 times (1 hour total)
  let runResult;
  for (let i = 0; i < 144; i++) {
    try {
      runResult = await client.taskRun.result(taskRun.run_id, { timeout: 25 });
      break;
    } catch (error) {
      if (i === 143) throw error; // Last attempt failed
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }

  console.log(runResult.output);
  ```

  ```python Python (Async) theme={"system"}
  import asyncio
  import os
  from parallel import AsyncParallel
  from parallel.types import TaskSpecParam

  client = AsyncParallel(api_key=os.environ["PARALLEL_API_KEY"])

  async def run_task():
      task_run = await client.task_run.create(
          input="United Nations",
          task_spec=TaskSpecParam(
            output_schema="The founding date of the company in the format MM-YYYY"
          ),
          processor="base"
      )
      print(f"Run ID: {task_run.run_id}")

      run_result = await client.task_run.result(task_run.run_id, api_timeout=3600)
      return run_result

  run_result = asyncio.run(run_task())
  print(run_result.output)
  ```
</CodeGroup>

### Sample Response

Immediately after a Task Run is created, the Task Run object, including the status of the Task Run, is returned. On completion, the Task Run Result object is returned.

[Basis](/task-api/guides/access-research-basis), including citations, reasoning, confidence, and excerpts - is returned with every Task Run Result.

<CodeGroup>
  ```json Task Run Creation theme={"system"}
  {
    "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
    "status": "queued",
    "is_active": true,
    "warnings": null,
    "processor": "base",
    "metadata": null,
    "created_at": "2025-04-23T20:21:48.037943Z",
    "modified_at": "2025-04-23T20:21:48.037943Z"
  }
  ```

  ```json Task Run Result [expandable] theme={"system"}
  {
    "run": {
      "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
      "status": "completed",
      "is_active": false,
      "warnings": null,
      "processor": "base",
      "metadata": null,
      "created_at": "2025-04-23T20:21:48.037943Z",
      "modified_at": "2025-04-23T20:22:47.819416Z"
    },
    "output": {
      "content": "10-1945",
      "basis": [\
        {\
          "field": "output",\
          "citations": [\
            {\
              "title": null,\
              "url": "https://www.un.org/en/about-us/history-of-the-un",\
              "excerpts": []\
            },\
            {\
              "title": null,\
              "url": "https://history.state.gov/milestones/1937-1945/un",\
              "excerpts": []\
            },\
            {\
              "title": null,\
              "url": "https://en.wikipedia.org/wiki/United_Nations",\
              "excerpts": []\
            },\
            {\
              "title": null,\
              "url": "https://research.un.org/en/unmembers/founders",\
              "excerpts": []\
            }\
          ],\
          "reasoning": "The founding date of the United Nations is derived from multiple sources indicating that it officially began on October 24, 1945. This date is consistently mentioned across the explored URLs including the official UN history page and other reputable references, confirming the founding date as 10-1945.",\
          "confidence": ""\
        }\
      ],
      "type": "text"
    }
  }
  ```
</CodeGroup>

## 3. From Simple to Rich Enrichment

The Task API supports increasingly sophisticated enrichment patterns:

<Steps>
  <Step title="Single Input → Single Output Field">
    The simplest enrichment: take one piece of data (like a company name) and add one new field (like founding date). This straightforward approach is illustrated above.
  </Step>

  <Step title="Single Input → Multiple Output Fields">
    Enrich a single input field with multiple new data points. For example, pass in a company name and receive founding date, employee count, and funding sources.

    <CodeGroup>
      ```bash cURL [expandable] theme={"system"}
      echo "Creating the run:"
      RUN_JSON=$(curl -s 'https://api.parallel.ai/v1/tasks/runs' \
      -H "x-api-key: ${PARALLEL_API_KEY}" \
      -H 'Content-Type: application/json' \
      -d '{
      "input": "United Nations",
      "processor": "core",
      "task_spec": {
      "output_schema": {
        "type": "json",
        "json_schema": {
          "type": "object",
          "properties": {
            "founding_date": {
              "type": "string",
              "description": "The official founding date of the company in the format MM-YYYY"
            },
            "employee_count": {
              "type": "string",
              "enum": [\
                "1-10 employees",\
                "11-50 employees",\
                "51-200 employees",\
                "201-500 employees",\
                "501-1000 employees",\
                "1001-5000 employees",\
                "5001-10000 employees",\
                "10001+ employees"\
              ],
              "description": "The range of employees working at the company. Choose the most accurate range possible and make sure to validate across multiple sources."
            },
            "funding_sources": {
              "type": "string",
              "description": "A detailed description, containing 1-4 sentences, of the company's funding sources, including their estimated value."
            }
          },
          "required": ["founding_date", "employee_count", "funding_sources"],
          "additionalProperties": false
        }
      }
      }
      }')
      echo "$RUN_JSON" | jq .
      RUN_ID=$(echo "$RUN_JSON" | jq -r '.run_id')

      echo "Retrieving the run result, blocking until the result is available:"
      curl -s "https://api.parallel.ai/v1/tasks/runs/${RUN_ID}/result" \
        -H "x-api-key: ${PARALLEL_API_KEY}" | jq .
      ```

      ```typescript TypeScript [expandable] theme={"system"}
      import Parallel from 'parallel-web';

      const client = new Parallel({
        apiKey: process.env.PARALLEL_API_KEY,
      });

      const taskRun = await client.taskRun.create({
        input: 'United Nations',
        processor: 'core',
        task_spec: {
          output_schema: {
            type: 'json',
            json_schema: {
              type: 'object',
              properties: {
                founding_date: {
                  type: 'string',
                  description: 'The official founding date of the company in the format MM-YYYY',
                },
                employee_count: {
                  type: 'string',
                  enum: [\
                    '1-10 employees',\
                    '11-50 employees',\
                    '51-200 employees',\
                    '201-500 employees',\
                    '501-1000 employees',\
                    '1001-5000 employees',\
                    '5001-10000 employees',\
                    '10001+ employees',\
                  ],
                  description: 'The range of employees working at the company. Choose the most accurate range possible and make sure to validate across multiple sources.',
                },
                funding_sources: {
                  type: 'string',
                  description: "A detailed description, containing 1-4 sentences, of the company's funding sources, including their estimated value.",
                },
              },
              required: ['founding_date', 'employee_count', 'funding_sources'],
              additionalProperties: false,
            },
          },
        },
      });

      console.log(`Run ID: ${taskRun.run_id}`);

      // Poll for results with 25-second timeout, retry up to 144 times (1 hour total)
      let runResult;
      for (let i = 0; i < 144; i++) {
        try {
          runResult = await client.taskRun.result(taskRun.run_id, { timeout: 25 });
          break;
        } catch (error) {
          if (i === 143) throw error; // Last attempt failed
          await new Promise((resolve) => setTimeout(resolve, 1000));
        }
      }

      console.log(runResult.output);

      ```

      ```python Python [expandable] theme={"system"}
      import os

      from parallel import Parallel
      from pydantic import BaseModel, Field
      from typing import Literal

      class CompanyOutput(BaseModel):
          founding_date: str = Field(
              description="The official founding date of the company in the format MM-YYYY"
          )
          employee_count: Literal[\
              "1-10 employees",\
              "11-50 employees",\
              "51-200 employees",\
              "201-500 employees",\
              "501-1000 employees",\
              "1001-5000 employees",\
              "5001-10000 employees",\
              "10001+ employees"\
          ] = Field(
              description="The range of employees working at the company. Choose the most accurate range possible and make sure to validate across multiple sources."
          )
          funding_sources: str = Field(
              description="A detailed description, containing 1-4 sentences, of the company's funding sources, including their estimated value."
          )

      def main():
          client = Parallel(api_key="PARALLEL_API_KEY")

          task_run = client.task_run.create(
              input="United Nations",
              task_spec={
                "output_schema":{
                  "type":"json",
                  "json_schema":CompanyOutput.model_json_schema()
                }
              },
              processor="core"
          )
          print(f"Run ID: {task_run.run_id}")

          run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
          print(run_result.output)

      if __name__ == "__main__":
          main()
      ```

      ```python Python (Async) [expandable] theme={"system"}
      import asyncio
      import os

      from parallel import AsyncParallel
      from pydantic import BaseModel, Field
      from typing import Literal

      class CompanyOutput(BaseModel):
          founding_date: str = Field(
              description="The official founding date of the company in the format MM-YYYY"
          )
          employee_count: Literal[\
              "1-10 employees",\
              "11-50 employees",\
              "51-200 employees",\
              "201-500 employees",\
              "501-1000 employees",\
              "1001-5000 employees",\
              "5001-10000 employees",\
              "10001+ employees"\
          ] = Field(
              description="The range of employees working at the company. Choose the most accurate range possible and make sure to validate across multiple sources."
          )
          funding_sources: str = Field(
              description="A detailed description, containing 1-4 sentences, of the company's funding sources, including their estimated value."
          )

      async def main():
          client = AsyncParallel(api_key="PARALLEL_API_KEY")

          task_run = await client.task_run.create(
              input="United Nations",
              task_spec={
                "output_schema":{
                  "type":"json",
                  "json_schema":CompanyOutput.model_json_schema()
                }
              },
              processor="core"
          )
          print(f"Run ID: {task_run.run_id}")

          run_result = await client.task_run.result(task_run.run_id, api_timeout=3600)
          print(run_result.output)

      if __name__ == "__main__":
          asyncio.run(main())
      ```
    </CodeGroup>
  </Step>

  <Step title="Multiple Inputs → Multiple Outputs (Full Enrichment)">
    The full enrichment pattern: define both input and output schemas. Provide multiple data fields you already have (company name and website) and specify all the fields you want to enrich. This is the most common pattern for enriching CRM data, compliance checks, and other structured workflows.

    <CodeGroup>
      ```bash cURL [expandable] theme={"system"}
      echo "Creating the run:"
      RUN_JSON=$(curl -s 'https://api.parallel.ai/v1/tasks/runs' \
      -H "x-api-key: ${PARALLEL_API_KEY}" \
      -H 'Content-Type: application/json' \
      -d '{
      "input": {
      "company_name": "United Nations",
      "company_website": "www.un.org"
      },
      "processor": "core",
      "task_spec": {
      "output_schema": {
        "type": "json",
        "json_schema": {
          "type": "object",
          "properties": {
            "founding_date": {
              "type": "string",
              "description": "The official founding date of the company in the format MM-YYYY"
            },
            "employee_count": {
              "type": "string",
              "enum":[\
                "1-10 employees",\
                "11-50 employees",\
                "51-200 employees",\
                "201-500 employees",\
                "501-1000 employees",\
                "1001-5000 employees",\
                "5001-10000 employees",\
                "10001+ employees"\
              ],
              "description": "The range of employees working at the company. Choose the most accurate range possible and make sure to validate across multiple sources."
            },
            "funding_sources": {
              "type": "string",
              "description": "A detailed description, containing 1-4 sentences, of the company's funding sources, including their estimated value."
            }
          },
          "required": ["founding_date", "employee_count", "funding_sources"],
          "additionalProperties": false
        }
      },
      "input_schema": {
        "type": "json",
        "json_schema": {
          "type": "object",
          "properties": {
            "company_name": {
              "type": "string",
              "description": "The name of the company to research"
            },
            "company_website": {
              "type": "string",
              "description": "The website of the company to research"
            }
          },
          "required": ["company_name", "company_website"]
        }
      }
      }
      }')
      echo "$RUN_JSON" | jq .
      RUN_ID=$(echo "$RUN_JSON" | jq -r '.run_id')

      echo "Retrieving the run result, blocking until the result is available:"
      curl -s "https://api.parallel.ai/v1/tasks/runs/${RUN_ID}/result" \
        -H "x-api-key: ${PARALLEL_API_KEY}" | jq .
      ```

      ```typescript TypeScript [expandable] theme={"system"}
      import Parallel from 'parallel-web';

      const client = new Parallel({
        apiKey: process.env.PARALLEL_API_KEY,
      });

      // Define input and output schemas
      const inputSchema = {
        type: 'object' as const,
        properties: {
          company_name: {
            type: 'string' as const,
            description: 'The name of the company to research',
          },
          company_website: {
            type: 'string' as const,
            description: 'The website of the company to research',
          },
        },
        required: ['company_name', 'company_website'],
      };

      const outputSchema = {
        type: 'object' as const,
        properties: {
          founding_date: {
            type: 'string' as const,
            description: 'The official founding date of the company in the format MM-YYYY',
          },
          employee_count: {
            type: 'string' as const,
            enum: [\
              '1-10 employees',\
              '11-50 employees',\
              '51-200 employees',\
              '201-500 employees',\
              '501-1000 employees',\
              '1001-5000 employees',\
              '5001-10000 employees',\
              '10001+ employees',\
            ],
            description: 'The range of employees working at the company. Choose the most accurate range possible and validate across multiple sources.',
          },
          funding_sources: {
            type: 'string' as const,
            description: "A detailed description, containing 1–4 sentences, of the company's funding sources, including their estimated value.",
          },
        },
        required: ['founding_date', 'employee_count', 'funding_sources'],
        additionalProperties: false,
      };

      const taskRun = await client.taskRun.create({
        input: {
          company_name: 'United Nations',
          company_website: 'www.un.org',
        },
        processor: 'core',
        task_spec: {
          input_schema: {
            type: 'json',
            json_schema: inputSchema,
          },
          output_schema: {
            type: 'json',
            json_schema: outputSchema,
          },
        },
      });

      console.log(`Run ID: ${taskRun.run_id}`);

      // Poll for results with 25-second timeout, retry up to 144 times (1 hour total)
      let runResult;
      for (let i = 0; i < 144; i++) {
        try {
          runResult = await client.taskRun.result(taskRun.run_id, { timeout: 25 });
          break;
        } catch (error) {
          if (i === 143) throw error; // Last attempt failed
          await new Promise((resolve) => setTimeout(resolve, 1000));
        }
      }

      console.log(runResult.output);
      ```

      ```python Python [expandable] theme={"system"}
      import os
      from typing import Literal

      from parallel import Parallel
      from parallel.lib._parsing._task_run_result import task_run_result_parser
      from parallel.types import TaskSpecParam
      from pydantic import BaseModel, Field

      class CompanyInput(BaseModel):
          """Input schema for the company research task."""
          company_name: str = Field(description="The name of the company to research")
          company_website: str = Field(description="The website of the company to research")

      class CompanyOutput(BaseModel):
          """Output schema for the company research task."""
          founding_date: str = Field(
              description="The official founding date of the company in the format MM-YYYY"
          )
          employee_count: Literal[\
              "1-10 employees",\
              "11-50 employees",\
              "51-200 employees",\
              "201-500 employees",\
              "501-1000 employees",\
              "1001-5000 employees",\
              "5001-10000 employees",\
              "10001+ employees",\
          ] = Field(
              description="The range of employees working at the company. Choose the most accurate range possible and validate across multiple sources."
          )
          funding_sources: str = Field(
              description="A detailed description, containing 1–4 sentences, of the company's funding sources, including their estimated value."
          )

      def build_task_spec_param(
          input_schema: type[BaseModel], output_schema: type[BaseModel]
      ) -> TaskSpecParam:
          """Build a TaskSpecParam from an input and output schema."""
          return {
              "input_schema": {
                  "type": "json",
                  "json_schema": input_schema.model_json_schema(),
              },
              "output_schema": {
                  "type": "json",
                  "json_schema": output_schema.model_json_schema(),
              },
          }

      client = Parallel(api_key=os.environ.get("PARALLEL_API_KEY"))

      # Prepare structured input
      input_data = CompanyInput(
          company_name="United Nations", company_website="htt"
      )
      task_spec = build_task_spec_param(CompanyInput, CompanyOutput)

      task_run = client.task_run.create(
          input=input_data.model_dump(),
          task_spec=task_spec,
          processor="core",
      )
      print(f"Run ID: {task_run.run_id}")

      run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
      parsed_result = task_run_result_parser(run_result, CompanyOutput)
      print(parsed_result.output.parsed)
      ```

      ```python Python (Async) [expandable] theme={"system"}
      import asyncio
      import os
      from typing import Literal

      from parallel import AsyncParallel
      from parallel.lib._parsing._task_run_result import task_run_result_parser
      from parallel.types import TaskSpecParam
      from pydantic import BaseModel, Field

      class CompanyInput(BaseModel):
          """Input schema for the company research task."""
          company_name: str = Field(description="The name of the company to research")
          company_website: str = Field(description="The website of the company to research")

      class CompanyOutput(BaseModel):
          """Output schema for the company research task."""
          founding_date: str = Field(
              description="The official founding date of the company in the format MM-YYYY"
          )
          employee_count: Literal[\
              "1-10 employees",\
              "11-50 employees",\
              "51-200 employees",\
              "201-500 employees",\
              "501-1000 employees",\
              "1001-5000 employees",\
              "5001-10000 employees",\
              "10001+ employees",\
          ] = Field(
              description="The range of employees working at the company. Choose the most accurate range possible and validate across multiple sources."
          )
          funding_sources: str = Field(
              description="A detailed description, containing 1–4 sentences, of the company's funding sources, including their estimated value."
          )

      def build_task_spec_param(
          input_schema: type[BaseModel], output_schema: type[BaseModel]
      ) -> TaskSpecParam:
          """Build a TaskSpecParam from an input and output schema."""
          return {
              "input_schema": {
                  "type": "json",
                  "json_schema": input_schema.model_json_schema(),
              },
              "output_schema": {
                  "type": "json",
                  "json_schema": output_schema.model_json_schema(),
              },
          }

      async def main():
          # Initialize the Parallel client
          client = AsyncParallel(api_key="PARALLEL_API_KEY")

          # Prepare structured input
          input_data = CompanyInput(
              company_name="United Nations", company_website="www.un.org"
          )
          task_spec = build_task_spec_param(CompanyInput, CompanyOutput)

          task_run = await client.task_run.create(
              input=input_data.model_dump(),
              task_spec=task_spec,
              processor="core",
          )
          print(f"Run ID: {task_run.run_id}")

          run_result = await client.task_run.result(task_run.run_id, api_timeout=3600)
          parsed_result = task_run_result_parser(run_result, CompanyOutput)
          print(parsed_result.output.parsed)

      if __name__ == "__main__":
          asyncio.run(main())

      ```
    </CodeGroup>
  </Step>
</Steps>

<Tip>
  **Writing Effective Task Specs**: For best practices on defining input and output schemas that produce high-quality results, see our [Task Spec Best Practices guide](/task-api/guides/specify-a-task#task-spec-best-practices).
</Tip>

### Sample Enrichment Result

```json [expandable] theme={"system"}
{
  "run": {
    "run_id": "trun_0824bb53c79c407b89614ba22e9db51c",
    "status": "completed",
    "is_active": false,
    "warnings": [],
    "processor": "core",
    "metadata": null,
    "created_at": "2025-04-24T16:05:03.403102Z",
    "modified_at": "2025-04-24T16:05:33.099450Z"
  },
  "output": {
    "content": {
      "funding_sources": "The United Nations' funding comes from governments, multilateral partners, and other non-state entities. This funding is acquired through assessed and voluntary contributions from its member states.",
      "employee_count": "10001+ employees",
      "founding_date": "10-1945"
    },
    "basis": [\
      {\
        "field": "funding_sources",\
        "citations": [\
          {\
            "title": "Funding sources",\
            "url": "https://www.financingun.report/un-financing/un-funding/funding-entity",\
            "excerpts": [\
              "The UN system is funded by a diverse set of partners: governments, multilateral partners, and other non-state funding."\
            ]\
          },\
          {\
            "title": "US Funding for the UN",\
            "url": "https://betterworldcampaign.org/us-funding-for-the-un",\
            "excerpts": [\
              "Funding from Member States for the UN system comes from two main sources: assessed and voluntary contributions."\
            ]\
          }\
        ],\
        "reasoning": "The United Nations' funding is derived from a diverse set of partners, including governments, multilateral organizations, and other non-state entities, as stated by financingun.report. According to betterworldcampaign.org, the funding from member states is acquired through both assessed and voluntary contributions.",\
        "confidence": "high"\
      },\
      {\
        "field": "employee_count",\
        "citations": [\
          {\
            "title": "Funding sources",\
            "url": "https://www.financingun.report/un-financing/un-funding/funding-entity",\
            "excerpts": []\
          }\
        ],\
        "reasoning": "The UN employs approximately 37,000 people, with a total personnel count of 133,126 in 2023.",\
        "confidence": "low"\
      },\
      {\
        "field": "founding_date",\
        "citations": [\
          {\
            "title": "Funding sources",\
            "url": "https://www.financingun.report/un-financing/un-funding/funding-entity",\
            "excerpts": []\
          },\
          {\
            "title": "History of the United Nations",\
            "url": "https://www.un.org/en/about-us/history-of-the-un",\
            "excerpts": [\
              "The United Nations officially began, on 24 October 1945, when it came into existence after its Charter had been ratified by China, France, the Soviet Union, ..."\
            ]\
          },\
          {\
            "title": "The Formation of the United Nations, 1945",\
            "url": "https://history.state.gov/milestones/1937-1945/un",\
            "excerpts": [\
              "The United Nations came into existence on October 24, 1945, after 29 nations had ratified the Charter. Table of Contents. 1937–1945: Diplomacy and the Road to ..."\
            ]\
          }\
        ],\
        "reasoning": "The United Nations officially began on October 24, 1945, as stated in multiple sources including the UN's official history and the US Department of State's historical milestones. This date is when the UN came into existence after its Charter was ratified by key member states.",\
        "confidence": "high"\
      }\
    ],
    "type": "json"
  }
}
```

## Next Steps

* [**Task Groups:**](/task-api/group-api) Enrich multiple records concurrently with parallel execution and batch tracking

* [**Task Spec Best Practices:**](/task-api/guides/specify-a-task) Optimize your input and output schemas for accuracy and speed

* [**Choose a Processor:**](/task-api/guides/choose-a-processor) Select the right processor tier for your enrichment use case

* [**Access Research Basis:**](/task-api/guides/access-research-basis) Understand citations, confidence levels, and reasoning for every enriched field

* [**Deep Research:**](/task-api/task-deep-research) Explore open-ended research without structured input data

* [**Streaming Events:**](/task-api/task-sse) Receive real-time updates via Server-Sent Events for long-running enrichments

* [**Webhooks:**](/task-api/webhooks) Configure HTTP callbacks for task completion notifications

* [**API Reference:**](/api-reference/tasks-v1/create-task-run) Complete endpoint documentation for the Task API

## Rate Limits

See [Rate Limits](/getting-started/rate-limits) for default quotas and how to request higher limits.

# 2-3. Retrieve the result (blocks until complete)
run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
print(run_result.output)
```

For complete end-to-end examples with all languages, polling, and response handling, see:

<CardGroup>
  <Card title="Enrichment Quickstart" icon="table" href="/task-api/task-enrichment">
    Enrich structured data with web intelligence — includes cURL, Python, TypeScript, and async examples
  </Card>

  <Card title="Deep Research Quickstart" icon="magnifying-glass-chart" href="/task-api/task-deep-research">
    Generate comprehensive reports — includes polling, webhooks, and SSE approaches
  </Card>
</CardGroup>

## Core concepts

Before diving in, understand these key concepts:

<CardGroup>
  <Card title="Task specs" icon="file-code" href="/task-api/guides/specify-a-task">
    Define your research task using input/output schemas in plain language or JSON
  </Card>

  <Card title="Processors" icon="microchip" href="/task-api/guides/choose-a-processor">
    Choose the right processor tier based on research depth and latency requirements
  </Card>

  <Card title="Research Basis" icon="quote-left" href="/task-api/guides/access-research-basis">
    Every output includes citations, reasoning, and confidence levels for verification
  </Card>
</CardGroup>

### Output schema types

The Task API supports four output schema types:

| Type            | Description                                                            | When to Use                                           |
| --------------- | ---------------------------------------------------------------------- | ----------------------------------------------------- |
| **Text string** | Plain text description (e.g., `"The founding date in MM-YYYY format"`) | Simple lookups, single-field answers                  |
| **JSON schema** | `{"type": "json", "json_schema": {...}}`                               | Structured enrichment with multiple typed fields      |
| **Text schema** | `{"type": "text"}` with optional `description`                         | Markdown reports with inline citations                |
| **Auto**        | `{"type": "auto"}`, or omit `task_spec` entirely                       | Let the processor determine the best output structure |

See [Specify a Task](/task-api/guides/specify-a-task) for schema best practices and [Processors](/task-api/guides/choose-a-processor) for choosing the right processor tier. For Python SDK users, these correspond to `TaskSpecParam`, `JsonSchemaParam`, and `TextSchemaParam` types from `parallel.types`.

## Input and output patterns

The Task API supports flexible input/output combinations to match your use case:

### Question in → Answer out

The simplest pattern: ask a question, get a researched answer.

```python theme={"system"}
task_run = client.task_run.create(
    input="What is the founding date of the United Nations?",
    task_spec={"output_schema": "The founding date in MM-YYYY format"},
    processor="base"
)
# Create Task Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-v1/create-task-run

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks v1

Create Task Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Beta params

Copy

Ask AI

```
from parallel import Parallel
from parallel.types.beta import McpServerParam
from parallel.types.beta.beta_run_input_param import BetaRunInputParam

client = Parallel(api_key="API Key")

task_run = client.beta.task_run.create(
    input="What was the GDP of France in 2023?",
    processor='base',
    enable_events=True,
    mcp_servers=[\
        McpServerParam(\
            type='url',\
            name='parallel_web_search',\
            url='https://mcp.parallel.ai/v1beta/search_mcp',\
            headers={'x-api-key': 'API Key'}\
        )\
    ],
    betas=['events-sse-2025-07-24','mcp-server-2025-07-17']
)
print(task_run.run_id)
```

202

401

402

403

422

429

Copy

Ask AI

```
{
  "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "status": "queued",
  "is_active": true,
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "created_at": "2025-04-23T20:21:48.037943Z",
  "modified_at": "2025-04-23T20:21:48.037943Z"
}
```

POST

/

v1

/

tasks

/

runs

Try it

Python

Beta params

Copy

Ask AI

```
from parallel import Parallel
from parallel.types.beta import McpServerParam
from parallel.types.beta.beta_run_input_param import BetaRunInputParam

client = Parallel(api_key="API Key")

task_run = client.beta.task_run.create(
    input="What was the GDP of France in 2023?",
    processor='base',
    enable_events=True,
    mcp_servers=[\
        McpServerParam(\
            type='url',\
            name='parallel_web_search',\
            url='https://mcp.parallel.ai/v1beta/search_mcp',\
            headers={'x-api-key': 'API Key'}\
        )\
    ],
    betas=['events-sse-2025-07-24','mcp-server-2025-07-17']
)
print(task_run.run_id)
```

202

401

402

403

422

429

Copy

Ask AI

```
{
  "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "status": "queued",
  "is_active": true,
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "created_at": "2025-04-23T20:21:48.037943Z",
  "modified_at": "2025-04-23T20:21:48.037943Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#parameter-one-of-0)

parallel-beta

string \| null

#### Body

application/json

Task run input with additional beta fields.

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-processor)

processor

string

required

Processor to use for the task.

Example:

`"base"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-input-one-of-0)

input

stringInput · objectstringInput · object

required

Input to the task, either text or a JSON object.

Example:

`"What was the GDP of France in 2023?"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the run. Keys and values must be strings with a maximum length of 16 and 512 characters respectively.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-source-policy-one-of-0)

source\_policy

SourcePolicy · object

Optional source policy governing preferred and disallowed domains in web search results.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-task-spec-one-of-0)

task\_spec

TaskSpec · object

Task specification. If unspecified, defaults to auto output schema.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-previous-interaction-id-one-of-0)

previous\_interaction\_id

string \| null

Interaction ID to use as context for this request.

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-mcp-servers-one-of-0)

mcp\_servers

McpServer · object\[\] \| null

Optional list of MCP servers to use for the run.
To enable this feature in your requests, specify `mcp-server-2025-07-17` as one of the values in `parallel-beta` header (for API calls) or `betas` param (for the SDKs).

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-enable-events-one-of-0)

enable\_events

boolean \| null

Controls tracking of task run execution progress. When set to true, progress events are recorded and can be accessed via the [Task Run events](https://platform.parallel.ai/api-reference) endpoint. When false, no progress events are tracked. Note that progress tracking cannot be enabled after a run has been created. The flag is set to true by default for premium processors (pro and above).
To enable this feature in your requests, specify `events-sse-2025-07-24` as one of the values in `parallel-beta` header (for API calls) or `betas` param (for the SDKs).

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#body-webhook-one-of-0)

webhook

Webhook · object

Callback URL (webhook endpoint) that will receive an HTTP POST when the run completes.
This feature is not available via the Python SDK. To enable this feature in your API requests, specify the `parallel-beta` header with `webhook-2025-08-12` value.

Showchild attributes

#### Response

202

application/json

Successful Response

Status of a task run.

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-run-id)

run\_id

string

required

ID of the task run.

Example:

`"trun_e0083b6aac0544eb8686e8d2a76533d2"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-interaction-id)

interaction\_id

string

required

Identifier for this interaction. Pass this value as `previous_interaction_id` to reuse context for a future request.

Example:

`"trun_e0083b6aac0544eb8686e8d2a76533d2"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-status)

status

enum<string>

required

Status of the run.

Available options:

`queued`,

`action_required`,

`running`,

`completed`,

`failed`,

`cancelling`,

`cancelled`

Examples:

`"queued"`

`"action_required"`

`"running"`

`"completed"`

`"failed"`

`"cancelling"`

`"cancelled"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-is-active)

is\_active

boolean

required

Whether the run is currently active, i.e. status is one of {'cancelling', 'queued', 'running'}.

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-processor)

processor

string

required

Processor used for the run.

Example:

`"base"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-created-at-one-of-0)

created\_at

string \| null

required

Timestamp of the creation of the task, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-modified-at-one-of-0)

modified\_at

string \| null

required

Timestamp of the last modification to the task, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-warnings-one-of-0)

warnings

Warning · object\[\] \| null

Warnings for the run, if any.

Showchild attributes

Example:

```
[]
```

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-error-one-of-0)

error

Error · object

Error for the run, present only if status is 'failed'.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the run.

Showchild attributes

Example:

```
{}
```

[​](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run#response-taskgroup-id-one-of-0)

taskgroup\_id

string \| null

ID of the taskgroup to which the run belongs.

[Simulate Event](https://docs.parallel.ai/api-reference/monitor/simulate-event) [Retrieve Task Run](https://docs.parallel.ai/api-reference/tasks-v1/retrieve-task-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Search Modes - Parallel

**URL:** https://docs.parallel.ai/search/modes

[Skip to main content](https://docs.parallel.ai/search/modes#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Search

Search Modes

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Example](https://docs.parallel.ai/search/modes#example)

The `mode` parameter presets defaults for different use cases:

- **`one-shot`** (default): Returns comprehensive results with longer excerpts. Best for direct user queries, where only a single request will be made, or where lower latency is desired. This is the default mode for the Search API.
- **`agentic`**: Returns more concise, token-efficient results designed for multi-step agentic workflows. This is the mode used by the [Search MCP server](https://docs.parallel.ai/integrations/mcp/search-mcp), and should be used when the search is part of a larger reasoning loop. Latency may be slightly higher than for `one-shot` due to additional processing to increase excerpt relevance.
- **`fast`**: Optimized for latency-sensitive use cases with expected response times of ~1s. Best for real-time applications where speed is critical.

## [​](https://docs.parallel.ai/search/modes\#example)  Example

Using fast mode:

Copy

Ask AI

```
{
  "mode": "fast",
  "objective": "Find recent research on quantum error correction",
  "search_queries": ["quantum error correction 2024", "QEC algorithms"]
}
```

[Best Practices](https://docs.parallel.ai/search/best-practices) [Source Policy](https://docs.parallel.ai/search/source-policy)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Store the original findall_id from your first run
ORIGINAL_FINDALL_ID = "findall_40e0ab8c10754be0b7a16477abb38a2f"

# Keep track of all discovered candidates across runs
all_discovered_candidates = []

def get_schema(findall_id):
    """Retrieve schema from a previous run"""
    response = requests.get(
        f"{BASE_URL}/findall/runs/{findall_id}/schema",
        headers=HEADERS
    )
    response.raise_for_status()
    return response.json()

def get_matched_candidates(findall_id):
    """Get all matched candidates from a run"""
    response = requests.get(
        f"{BASE_URL}/findall/runs/{findall_id}/result",
        headers=HEADERS
    )
    response.raise_for_status()
    candidates = response.json().get("candidates", [])
    return [c for c in candidates if c.get("match_status") == "matched"]

def create_scheduled_run(schema, exclude_candidates):
    """Create a new FindAll run with exclusions"""
    payload = {
        **schema,
        "generator": "core",
        "match_limit": 50,
        "exclude_list": exclude_candidates
    }

    response = requests.post(
        f"{BASE_URL}/findall/runs",
        headers=HEADERS,
        json=payload
    )
    response.raise_for_status()
    return response.json()["findall_id"]

def run_weekly_job():
    """Execute a scheduled FindAll job"""
    print(f"Starting scheduled job at {datetime.now()}")

    # Step 1: Get schema from original run
    schema = get_schema(ORIGINAL_FINDALL_ID)
    print(f"Retrieved schema: {schema['objective']}")

    # Step 2: Create new run with exclusions
    new_findall_id = create_scheduled_run(schema, all_discovered_candidates)
    print(f"Created new run: {new_findall_id}")

    # Step 3: Poll for completion (simplified)
    while True:
        response = requests.get(
            f"{BASE_URL}/findall/runs/{new_findall_id}",
            headers=HEADERS
        )
        status = response.json()["status"]["status"]

        if status in ["completed", "failed", "cancelled"]:
            break

        time.sleep(30)  # Poll every 30 seconds

    # Step 4: Get new matched candidates
    new_candidates = get_matched_candidates(new_findall_id)
    print(f"Found {len(new_candidates)} new candidates")

    # Step 5: Update exclude list for next run
    for candidate in new_candidates:
        all_discovered_candidates.append({
            "name": candidate["name"],
            "url": candidate["url"]
        })

    return new_candidates

# Run the job
if __name__ == "__main__":
    new_results = run_weekly_job()
```

## [​](https://docs.parallel.ai/findall-api/features/findall-refresh\#best-practices)  Best Practices

### [​](https://docs.parallel.ai/findall-api/features/findall-refresh\#schema-modifications)  Schema Modifications

While you should keep `match_conditions` consistent across runs, you can adjust:

- **`objective`**: Update to reflect the current time period (e.g., “founded in 2024” → “founded in 2025”)
- **`enrichments`**: Add new enrichment fields without affecting matching logic
- **`match_limit`**: Adjust based on expected growth rate
- **`generator`**: Change generators if needed (though this may affect result quality)

### [​](https://docs.parallel.ai/findall-api/features/findall-refresh\#exclude-list-management)  Exclude List Management

- **Persist candidates**: Store discovered candidate objects (name and URL) in a database or file for long-term tracking
- **Normalize URLs**: Ensure consistent URL formatting (trailing slashes, protocols, etc.) across runs
- **Periodic resets**: Consider occasionally running without exclusions to catch entities that may have changed
- **Monitor list size**: Very large exclude lists (>10,000 candidates) may impact performance

### [​](https://docs.parallel.ai/findall-api/features/findall-refresh\#scheduling)  Scheduling

- **Frequency**: Choose intervals based on your domain’s update rate (daily, weekly, monthly)
- **Off-peak hours**: Schedule jobs during low-traffic periods if possible
- **Webhooks**: Use [webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook) to get notified when jobs complete
- **Error handling**: Implement retry logic for failed runs

### [​](https://docs.parallel.ai/findall-api/features/findall-refresh\#cost-optimization)  Cost Optimization

- **Start small**: Use lower `match_limit` values initially, then [extend](https://docs.parallel.ai/findall-api/features/findall-extend) if needed
- **Preview first**: Test schema changes with [preview](https://docs.parallel.ai/findall-api/features/findall-preview) before running full jobs
- **Monitor metrics**: Track `generated_candidates_count` vs `matched_candidates_count` to optimize criteria

## [​](https://docs.parallel.ai/findall-api/features/findall-refresh\#related-topics)  Related Topics

- **[Preview](https://docs.parallel.ai/findall-api/features/findall-preview)**: Test queries with ~10 candidates before running full searches
- **[Generators and Pricing](https://docs.parallel.ai/findall-api/core-concepts/findall-generator-pricing)**: Understand generator options and pricing
- **[Enrichments](https://docs.parallel.ai/findall-api/features/findall-enrich)**: Extract additional structured data for matched candidates
- **[Extend Runs](https://docs.parallel.ai/findall-api/features/findall-extend)**: Increase match limits without paying new fixed costs
- **[Webhooks](https://docs.parallel.ai/findall-api/features/findall-webhook)**: Configure HTTP callbacks for run completion and matches
- **[Streaming Events](https://docs.parallel.ai/findall-api/features/findall-sse)**: Receive real-time updates via Server-Sent Events
- **[Run Lifecycle](https://docs.parallel.ai/findall-api/core-concepts/findall-lifecycle)**: Understand run statuses and how to cancel runs
- **[API Reference](https://docs.parallel.ai/api-reference/findall-api-beta/get-findall-run-schema)**: Complete endpoint documentation

[Cancel](https://docs.parallel.ai/findall-api/features/findall-cancel) [Quickstart](https://docs.parallel.ai/monitor-api/monitor-quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Task MCP - Parallel

**URL:** https://docs.parallel.ai/integrations/mcp/task-mcp

[Skip to main content](https://docs.parallel.ai/integrations/mcp/task-mcp#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

MCP

Task MCP

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Enrichment data sources and destinations](https://docs.parallel.ai/integrations/mcp/task-mcp#enrichment-data-sources-and-destinations)
- [Use cases](https://docs.parallel.ai/integrations/mcp/task-mcp#use-cases)
- [Installation](https://docs.parallel.ai/integrations/mcp/task-mcp#installation)
- [Cursor](https://docs.parallel.ai/integrations/mcp/task-mcp#cursor)
- [VS Code](https://docs.parallel.ai/integrations/mcp/task-mcp#vs-code)
- [Claude Desktop / Claude.ai](https://docs.parallel.ai/integrations/mcp/task-mcp#claude-desktop-%2F-claude-ai)
- [Claude Code](https://docs.parallel.ai/integrations/mcp/task-mcp#claude-code)
- [Windsurf](https://docs.parallel.ai/integrations/mcp/task-mcp#windsurf)
- [Cline](https://docs.parallel.ai/integrations/mcp/task-mcp#cline)
- [Gemini CLI](https://docs.parallel.ai/integrations/mcp/task-mcp#gemini-cli)
- [ChatGPT](https://docs.parallel.ai/integrations/mcp/task-mcp#chatgpt)
- [OpenAI Codex CLI](https://docs.parallel.ai/integrations/mcp/task-mcp#openai-codex-cli)
- [Amp](https://docs.parallel.ai/integrations/mcp/task-mcp#amp)
- [Kiro](https://docs.parallel.ai/integrations/mcp/task-mcp#kiro)
- [Google Antigravity](https://docs.parallel.ai/integrations/mcp/task-mcp#google-antigravity)
- [Best Practices](https://docs.parallel.ai/integrations/mcp/task-mcp#best-practices)
- [Choose enabled MCPs carefully](https://docs.parallel.ai/integrations/mcp/task-mcp#choose-enabled-mcps-carefully)
- [Limit data source context size](https://docs.parallel.ai/integrations/mcp/task-mcp#limit-data-source-context-size)
- [Follow up on tasks](https://docs.parallel.ai/integrations/mcp/task-mcp#follow-up-on-tasks)
- [Use with larger models only](https://docs.parallel.ai/integrations/mcp/task-mcp#use-with-larger-models-only)
- [Troubleshooting](https://docs.parallel.ai/integrations/mcp/task-mcp#troubleshooting)
- [Common Installation Issues](https://docs.parallel.ai/integrations/mcp/task-mcp#common-installation-issues)

The Task MCP Server provides two core capabilities: deep research tasks that generate comprehensive reports, and enrichment tasks that transform existing datasets with web intelligence. Built on the same infrastructure that powers our [Task API](https://docs.parallel.ai/task-api/task-quickstart), it delivers the highest quality at every price point while eliminating complex integration work.The Task MCP comprises three tools:

- **Create Deep Research Task** \- Initiates a [deep research](https://docs.parallel.ai/task-api/task-deep-research) task, returns details to view progress
- **Create Task Group** \- Initiates a [task group](https://docs.parallel.ai/task-api/group-api) to enrich multiple items in parallel.
- **Get Result** \- Retrieves the results of both deep research as well as task groups in an LLM friendly format.

The Task MCP Server uses an async architecture that lets agents start research tasks and continue executing other work without blocking. This allows spawning any number of tasks in parallel while continuing the conversation. Due to current MCP and LLM client limitations, you need to request the result tool call in an additional turn after results are ready.The Task MCP works best when following this process:

1. **Choose a data source** \- See [Enrichment data sources and destinations](https://docs.parallel.ai/integrations/mcp/task-mcp#enrichment-data-sources-and-destinations).
2. **Initiate your tasks** \- After you have your initial data, the MCP can initiate deep research or task groups. See [Use cases](https://docs.parallel.ai/integrations/mcp/task-mcp#use-cases) for inspiration.
3. **Analyze the results** \- The LLM provides a link to view progress as results come in. After completion, prompt the LLM to analyze the results and answer your questions.

## [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#enrichment-data-sources-and-destinations)  Enrichment data sources and destinations

The task group tool can be used directly from LLM memory, but is often combined with a data source. The following data sources work well with the Task Group tool:

- **Upload tabular files** \- Use the Task MCP with Excel sheets or CSVs. Some LLM clients (such as ChatGPT) allow uploading Excel or CSV files. Availability varies by client.
- **Connect with databases** \- Several MCPs allow your LLM to retrieve data from your database, such as [Supabase MCP](https://supabase.com/docs/guides/getting-started/mcp) and [Neon MCP](https://neon.com/docs/ai/neon-mcp-server).
- **Connect with documents** \- Documents may contain vital initial information to start a task group. See [Notion MCP](https://developers.notion.com/docs/mcp) and [Linear MCP](https://linear.app/docs/mcp).
- **Connect with web search data** \- [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) or other web tools can provide an initial list of items, which is often a great starting point for a task group.

## [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#use-cases)  Use cases

The Task MCP serves two main purposes. First, it makes Parallel APIs accessible to anyone requiring reliable research or enrichment without coding skills. Second, it’s a great tool for developers to experiment with different use cases and see output quality before writing code.Below are examples of using the Task MCP (sometimes in combination with other MCPs):**Day-to-day data enrichment and research:**

- [Sentiment analysis for ecommerce products](https://claude.ai/share/4ac5f253-e636-4009-8ade-7c6b08f7a135)
- [Improving product listings for a web store](https://claude.ai/share/f4d6e523-3c7c-4354-8577-1c953952a360)
- [Fact checking](https://claude.ai/share/9ec971ec-89dd-4d68-8515-2f037b88db38)
- [Deep research every major MCP client creating a Matrix of the results](https://claude.ai/share/0841e031-a8c4-408d-9201-e1b8a77ff6c9)
- [Reddit Sentiment analysis](https://claude.ai/share/39d98320-fc3e-4bbb-b4d5-da67abac44f2)

**Assisting development with Parallel APIs:**

- [Comparing the output quality between 2 processors](https://claude.ai/share/f4d6e523-3c7c-4354-8577-1c953952a360)
- [Testing and iterating on entity resolution for social media profiles](https://claude.ai/share/198db715-b0dd-4325-9e2a-1dfab531ba41)
- [Performing 100 deep researches and analyzing results quality](https://claude.ai/share/39d98320-fc3e-4bbb-b4d5-da67abac44f2)

This is just the tip of the iceberg. Share your most compelling use cases with us to grow this list and inspire others!

## [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#installation)  Installation

The Task MCP can be installed in any MCP client. The server URL is:**`https://task-mcp.parallel.ai/mcp`**The Task MCP can also be [used programmatically](https://docs.parallel.ai/integrations/mcp/programmatic-use) by providing your Parallel API key in the Authorization header as a Bearer token.

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#cursor)  Cursor

Add to `~/.cursor/mcp.json` or `.cursor/mcp.json` (project-specific):

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "url": "https://task-mcp.parallel.ai/mcp"
    }
  }
}
```

**Deep Link:** [🔗 Install Task MCP](https://cursor.com/en/install-mcp?name=Parallel%20Task%20MCP&config=eyJ1cmwiOiJodHRwczovL3Rhc2stbWNwLnBhcmFsbGVsLmFpL21jcCJ9)For more details, see the [Cursor MCP documentation](https://cursor.com/docs/context/mcp).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#vs-code)  VS Code

Add to `settings.json` in VS Code:

Copy

Ask AI

```
{
  "mcp": {
    "servers": {
      "Parallel Task MCP": {
        "type": "http",
        "url": "https://task-mcp.parallel.ai/mcp"
      }
    }
  }
}
```

**Deep Link:** [🔗 Install Task MCP](https://insiders.vscode.dev/redirect/mcp/install?name=Parallel%20Task%20MCP&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Ftask-mcp.parallel.ai%2Fmcp%22%7D)For more details, see the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#claude-desktop-/-claude-ai)  Claude Desktop / Claude.ai

Go to Settings → Connectors → Add Custom Connector, and fill in:

Copy

Ask AI

```
Name: Parallel Task MCP
URL: https://task-mcp.parallel.ai/mcp
```

If you are part of an organization, you may not have access to custom connectors. Contact your organization administrator for assistance.If you are not an admin, go to Settings → Developer → Edit Config and add the following JSON after retrieving your API key from [Platform](https://platform.parallel.ai/):

Copy

Ask AI

```
"Parallel Task MCP": {
  "command": "npx",
  "args": [\
    "-y",\
    "mcp-remote",\
    "https://task-mcp.parallel.ai/mcp",\
    "--header", "authorization: Bearer YOUR-PARALLEL-API-KEY"\
  ]
}
```

For more details, see the [Claude remote MCP documentation](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#claude-code)  Claude Code

Run this command in your terminal:

Copy

Ask AI

```
claude mcp add --transport http "Parallel-Task-MCP" https://task-mcp.parallel.ai/mcp
```

In Claude code, use the command:

Copy

Ask AI

```
/mcp
```

Then follow the steps in your browser to login.For more details, see the [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#windsurf)  Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "serverUrl": "https://task-mcp.parallel.ai/mcp"
    }
  }
}
```

For more details, see the [Windsurf MCP documentation](https://docs.windsurf.com/windsurf/cascade/mcp).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#cline)  Cline

Go to MCP Servers → Remote Servers → Edit Configuration:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "url": "https://task-mcp.parallel.ai/mcp",
      "type": "streamableHttp"
    }
  }
}
```

For more details, see the [Cline MCP documentation](https://docs.cline.bot/mcp/configuring-mcp-servers).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#gemini-cli)  Gemini CLI

Add to `~/.gemini/settings.json`:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "httpUrl": "https://task-mcp.parallel.ai/mcp"
    }
  }
}
```

For more details, see the [Gemini CLI MCP documentation](https://geminicli.com/docs/tools/mcp-server/).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#chatgpt)  ChatGPT

**WARNING:** Please note that [Developer Mode](https://platform.openai.com/docs/guides/developer-mode) must be enabled, and this feature may not be available to everyone. Additionally, MCPs in ChatGPT are experimental and may not work reliably.First, go to Settings → Connectors → Advanced Settings, and turn on Developer Mode.Then, in connector settings, click Create and fill in:

Copy

Ask AI

```
Name: Parallel Task MCP
URL: https://task-mcp.parallel.ai/mcp
Authentication: OAuth
```

In a new chat, ensure Developer Mode is turned on with the connector(s) selected.For more details, see the [ChatGPT Developer Mode documentation](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#openai-codex-cli)  OpenAI Codex CLI

Add to `~/.codex/config.toml`:

Copy

Ask AI

```
[mcp_servers.parallel-task]
url = "https://task-mcp.parallel.ai/mcp"
```

Alternatively, run this in your terminal. This should start the OAuth flow:

Copy

Ask AI

```
codex mcp add parallel-task --url https://task-mcp.parallel.ai/mcp
```

For more details, see the [Codex MCP documentation](https://developers.openai.com/codex/mcp/).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#amp)  Amp

Run this command in your terminal:

Copy

Ask AI

```
amp mcp add "Parallel-Task-MCP" https://task-mcp.parallel.ai/mcp
```

The OAuth flow will start when you start Amp.For more details, see the [Amp MCP documentation](https://ampcode.com/manual#mcp-oauth).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#kiro)  Kiro

Add to `.kiro/settings/mcp.json` (workspace) or `~/.kiro/settings/mcp.json` (global):

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "url": "https://task-mcp.parallel.ai/mcp"
    }
  }
}
```

For more details, see the [Kiro MCP documentation](https://kiro.dev/docs/mcp/configuration/).

* * *

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#google-antigravity)  Google Antigravity

In the Antigravity Agent pane, click the menu (⋮) → MCP Servers → Manage MCP Servers → View raw config, then add:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel-Task-MCP": {
      "serverUrl": "https://task-mcp.parallel.ai/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

For more details, see the [Antigravity MCP documentation](https://antigravity.google/docs/mcp).

* * *

## [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#best-practices)  Best Practices

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#choose-enabled-mcps-carefully)  Choose enabled MCPs carefully

Be careful which tools and features you have enabled in your MCP client. When using Parallel in combination with many other tools, the increased context window may cause degraded output quality. Additionally, the LLM may prefer standard web search or deep research over Parallel if both are enabled. Turn off other web or deep-research tools, or explicitly mention that you want to use Parallel MCPs.

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#limit-data-source-context-size)  Limit data source context size

The Task MCP is a powerful tool for batch deep research, but it is constrained by the context window size and max output tokens of the LLM. Design your prompts and tool calls to avoid overflowing these limitations, or you may experience failures, degraded performance, or lower output quality. For large datasets, use the API or other no-code integrations. The Task MCP is designed for smaller parallel tasks and experimentation.

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#follow-up-on-tasks)  Follow up on tasks

The Task MCP only initiates Deep Research and Task Groups—it does not wait for tasks to complete. Fetch the status or results using a follow-up tool call after research is complete. The asynchronous nature allows initiating several deep researches and task groups without overflowing the context window. To perform multiple tasks or batches in a workflow, reply each time to verify the task is complete and initiate the next step.

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#use-with-larger-models-only)  Use with larger models only

While our Web [Search](https://docs.parallel.ai/integrations/mcp/search-mcp) MCP works well with smaller models (such as GPT OSS 20B), the Task MCP requires strong reasoning capability. Use it with larger models only (such as GPT-5 or Claude Sonnet 4.5). Smaller models may result in degraded output quality.

* * *

## [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#troubleshooting)  Troubleshooting

### [​](https://docs.parallel.ai/integrations/mcp/task-mcp\#common-installation-issues)  Common Installation Issues

Cline: 'Authorization Error redirect\_uri must be https'

This error occurs when Cline attempts OAuth authentication but the redirect URI isn’t using HTTPS.**Solution:** Use the API key approach instead of OAuth:

1. Get your API key from [platform.parallel.ai](https://platform.parallel.ai/)
2. Configure Cline with the bearer token method:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "command": "npx",
      "args": [\
        "-y",\
        "mcp-remote",\
        "https://task-mcp.parallel.ai/mcp",\
        "--header",\
        "authorization: Bearer YOUR-PARALLEL-API-KEY"\
      ]
    }
  }
}
```

Replace `YOUR-PARALLEL-API-KEY` with your actual API key.

Gemini CLI: Where to provide API key

Gemini CLI uses HTTP MCPs and authenticates via OAuth. If OAuth isn’t working, you can provide your API key directly.**Solution:** Use environment variables or the `mcp-remote` proxy:

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "command": "npx",
      "args": [\
        "-y",\
        "mcp-remote",\
        "https://task-mcp.parallel.ai/mcp",\
        "--header",\
        "authorization: Bearer YOUR-PARALLEL-API-KEY"\
      ]
    }
  }
}
```

Add this to `~/.gemini/settings.json` and replace `YOUR-PARALLEL-API-KEY` with your key from [platform.parallel.ai](https://platform.parallel.ai/).

VS Code: Incorrect configuration format

VS Code requires a specific configuration format. Common mistakes include using the wrong property names.**Incorrect (Cursor format):**

Copy

Ask AI

```
{
  "mcpServers": {
    "parallel-task": {
      "url": "https://task-mcp.parallel.ai/mcp"
    }
  }
}
```

**Correct (VS Code format):**

Copy

Ask AI

```
{
  "mcp": {
    "servers": {
      "Parallel Task MCP": {
        "type": "http",
        "url": "https://task-mcp.parallel.ai/mcp"
      }
    }
  }
}
```

Note: VS Code uses `mcp.servers` (not `mcpServers`) and requires the `type: "http"` field.

Windsurf: Configuration location and format

Windsurf uses a different configuration format than Cursor.**Correct Windsurf configuration:**

Copy

Ask AI

```
{
  "mcpServers": {
    "Parallel Task MCP": {
      "serverUrl": "https://task-mcp.parallel.ai/mcp"
    }
  }
}
```

Note: Windsurf uses `serverUrl` instead of `url`. Add this to your Windsurf MCP configuration file.

Connection timeout or 'server unavailable' errors

If you’re getting connection errors:

1. **Check your network:** Ensure you can reach `https://task-mcp.parallel.ai`
2. **Verify API key:** Make sure your key is valid at [platform.parallel.ai](https://platform.parallel.ai/)
3. **Check balance:** A 402 error means insufficient credits—add funds to your account
4. **Restart your IDE:** Some clients cache MCP connections

Tools not appearing in the IDE

If the MCP installs but tools don’t show up:

1. **Restart your IDE** completely (not just reload)
2. **Check configuration syntax:** Ensure valid JSON with no trailing commas
3. **Verify the server URL:** Must be exactly `https://task-mcp.parallel.ai/mcp`
4. **Check IDE logs:** Look for MCP-related errors in your IDE’s output/debug panel

[Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) [Overview](https://docs.parallel.ai/data-integrations/overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Warnings and Errors - Parallel

**URL:** https://docs.parallel.ai/resources/warnings-and-errors

[Skip to main content](https://docs.parallel.ai/resources/warnings-and-errors#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Additional Resources

Warnings and Errors

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Errors](https://docs.parallel.ai/resources/warnings-and-errors#errors)
- [Warnings](https://docs.parallel.ai/resources/warnings-and-errors#warnings)
- [Warning Handling](https://docs.parallel.ai/resources/warnings-and-errors#warning-handling)
- [Basis Properties](https://docs.parallel.ai/resources/warnings-and-errors#basis-properties)
- [Error Reference](https://docs.parallel.ai/resources/warnings-and-errors#error-reference)
- [Error Response Format](https://docs.parallel.ai/resources/warnings-and-errors#error-response-format)
- [402 Payment Required Troubleshooting](https://docs.parallel.ai/resources/warnings-and-errors#402-payment-required-troubleshooting)
- [Understanding In-Flight Balance](https://docs.parallel.ai/resources/warnings-and-errors#understanding-in-flight-balance)
- [Common Causes](https://docs.parallel.ai/resources/warnings-and-errors#common-causes)
- [How to Resolve](https://docs.parallel.ai/resources/warnings-and-errors#how-to-resolve)

The Task API may return various warnings and errors during operation. This page documents the possible error types you might encounter when using the API.

## [​](https://docs.parallel.ai/resources/warnings-and-errors\#errors)  Errors

Errors result in a failure to process your request and are returned with appropriate HTTP status codes (4xx or 5xx).

| Error | Description | Resolution |
| --- | --- | --- |
| **Invalid JSON Schema** | The JSON schema provided in the task spec for input or output is invalid. | Review your schema against JSON Schema specifications and ensure it follows the required format. |
| **Task Spec + Input Too Long** | The combined task specification and input exceeds 18,000 characters. | Reduce the size of your task spec or input data. Consider splitting into multiple tasks if necessary. |
| **Too-Complex Output Schema** | The output schema exceeds allowed complexity in terms of nesting depth or number of fields. | Simplify your output schema by reducing nested levels to 3 or less. |

## [​](https://docs.parallel.ai/resources/warnings-and-errors\#warnings)  Warnings

Warnings indicate potential issues that don’t prevent the request from being processed but may affect results.

| Warning | Description | Resolution |
| --- | --- | --- |
| **Input Fails Validation** | The provided input does not conform to the input schema. | Verify your input against the schema requirements and make necessary adjustments. |
| **Task Spec + Input Over Size Limit** | The combined task specification and input exceeds the character limit. | Consider optimizing your input or task spec for better performance. |
| **Too Many Output Fields** | The number of requested output fields exceeds the recommended limit. | Consider reducing the number of output fields. |

## [​](https://docs.parallel.ai/resources/warnings-and-errors\#warning-handling)  Warning Handling

The Task API uses a warning system to provide guidance without blocking execution. Warnings are generated during validation and can be handled in two ways:

### [​](https://docs.parallel.ai/resources/warnings-and-errors\#basis-properties)  Basis Properties

It is recommended to use `FieldBasis` in the run output rather than requesting similar information in the output schema.This means you’ve included fields like `citations`, `reasoning`, or `sources` in your output schema, but this information is **already provided automatically** in every Task Run result through the [Basis](https://docs.parallel.ai/task-api/guides/access-research-basis) feature.**What is Basis?** Every Task Run result includes a `basis` array containing citations, reasoning, and confidence levels for each output field. This is provided automatically; you don’t need to request it in your schema.**Why not include these in the output schema?**

- **Redundant**: You’ll get duplicate data, wasting tokens and processing
- **Less structured**: The automatic Basis provides properly structured citations with URLs and excerpts
- **Less reliable**: Asking the model to generate its own citations may produce less accurate results than the built-in citation tracking

The following field names trigger this warning:

- `citations`
- `confidence`
- `evidence`
- `reasoning`
- `source`
- `sources`
- `source_urls`

**Instead of this:**

Copy

Ask AI

```
{
  "properties": {
    "company_name": { "type": "string" },
    "reasoning": { "type": "string" },
    "sources": { "type": "array", "items": { "type": "string" } }
  }
}
```

**Do this:**

Copy

Ask AI

```
{
  "properties": {
    "company_name": { "type": "string" }
  }
}
```

Then access `output.basis` in the response to get citations, reasoning, and confidence for each field. See [Accessing Research Basis](https://docs.parallel.ai/task-api/guides/access-research-basis) for details.

## [​](https://docs.parallel.ai/resources/warnings-and-errors\#error-reference)  Error Reference

| Status Code | Meaning | Retry? | Description | Resolution Approach |
| --- | --- | --- | --- | --- |
| **401** | Unauthorized | No | Invalid or missing credentials | Verify API key and authentication headers |
| **402** | Payment Required | No | Insufficient credit in account | See [402 Troubleshooting](https://docs.parallel.ai/resources/warnings-and-errors#402-payment-required-troubleshooting) below |
| **403** | Forbidden | No | Invalid processor in request | Check processor availability and permissions |
| **404** | Not Found | No | Run ID or resource not found | Verify run ID and resource existence |
| **408** | Request Timeout | Yes | Synchronous request timed out | Use asynchronous polling |
| **422** | Unprocessable Content | No | Request validation failed | Review error details and validate schema |
| **429** | Too Many Requests | Yes | Rate limited or quota exceeded | Implement exponential backoff |
| **500** | Internal Server Error | Yes | Server-side processing error | Retry with backoff, contact support if persistent |
| **502** | Bad Gateway | Yes | Upstream service error | Retry, usually temporary |
| **503** | Service Unavailable | Yes | Service temporarily unavailable | Retry with backoff |

## [​](https://docs.parallel.ai/resources/warnings-and-errors\#error-response-format)  Error Response Format

All errors return a consistent JSON structure:

Copy

Ask AI

```
{
  "error": {
    "message": "Human-readable error description",
    "detail": {
      // Additional error-specific information
    }
  }
}
```

For validation errors (422), the `detail` field contains specific information about which fields failed validation and why.

## [​](https://docs.parallel.ai/resources/warnings-and-errors\#402-payment-required-troubleshooting)  402 Payment Required Troubleshooting

A 402 error indicates your account has insufficient credits to process the request. This can occur even if your account shows a positive balance due to **in-flight balance reservations**.

### [​](https://docs.parallel.ai/resources/warnings-and-errors\#understanding-in-flight-balance)  Understanding In-Flight Balance

When you submit a task, the system reserves credits for the estimated cost before processing begins. This reservation is called the “in-flight balance.” Your **available balance** equals your **total balance** minus the **in-flight balance** from all currently running tasks.**Example scenario:**

- Account balance: $10.00
- 5 running `pro` tasks (each reserves ~0.10):0.10): 0.10):0.50 reserved
- Available balance: $9.50

If your available balance is insufficient for a new task, you’ll receive a 402 error even though your total balance appears positive.

### [​](https://docs.parallel.ai/resources/warnings-and-errors\#common-causes)  Common Causes

| Cause | Solution |
| --- | --- |
| **Multiple concurrent tasks** | Running many tasks simultaneously reserves credits for each. Wait for some to complete or reduce concurrency. |
| **Higher-tier processors** | `ultra` and `pro` processors reserve more credits than `base` or `lite`. Consider using lower-tier processors for less complex tasks. |
| **Insufficient account balance** | Add credits at [platform.parallel.ai](https://platform.parallel.ai/). |
| **Large task groups** | Task groups reserve credits for all runs upfront. Split into smaller batches if needed. |

### [​](https://docs.parallel.ai/resources/warnings-and-errors\#how-to-resolve)  How to Resolve

1. **Check your balance**: View your current balance and usage at [platform.parallel.ai](https://platform.parallel.ai/)
2. **Wait for tasks to complete**: In-flight reservations are released when tasks finish
3. **Add credits**: Top up your account balance if genuinely low
4. **Reduce concurrency**: Lower the number of parallel tasks to reduce reserved credits
5. **Use lower-tier processors**: Reserve fewer credits per task by using `base` or `lite` processors where appropriate

For high-volume workloads, monitor your available balance (not just total balance) and implement backoff logic when approaching limits. See [Pricing](https://parallel.ai/pricing) for processor costs.

[Source Policy](https://docs.parallel.ai/resources/source-policy) [Webhook Setup](https://docs.parallel.ai/resources/webhook-setup)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Retrieve Task Group Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run

[Skip to main content](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tasks (Beta)

Retrieve Task Group Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_run = client.task_run.retrieve("run_id")
print(task_run.status)
```

200

401

404

422

Copy

Ask AI

```
{
  "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "status": "running",
  "is_active": true,
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "created_at": "2025-04-23T20:21:48.037943Z",
  "modified_at": "2025-04-23T20:21:48.037943Z"
}
```

GET

/

v1beta

/

tasks

/

groups

/

{taskgroup\_id}

/

runs

/

{run\_id}

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

task_run = client.task_run.retrieve("run_id")
print(task_run.status)
```

200

401

404

422

Copy

Ask AI

```
{
  "run_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "interaction_id": "trun_9907962f83aa4d9d98fd7f4bf745d654",
  "status": "running",
  "is_active": true,
  "processor": "core",
  "metadata": {
    "my_key": "my_value"
  },
  "created_at": "2025-04-23T20:21:48.037943Z",
  "modified_at": "2025-04-23T20:21:48.037943Z"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#authorization-x-api-key)

x-api-key

string

header

required

#### Path Parameters

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#parameter-taskgroup-id)

taskgroup\_id

string

required

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#parameter-run-id)

run\_id

string

required

#### Response

200

application/json

Successful Response

Status of a task run.

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-run-id)

run\_id

string

required

ID of the task run.

Example:

`"trun_e0083b6aac0544eb8686e8d2a76533d2"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-interaction-id)

interaction\_id

string

required

Identifier for this interaction. Pass this value as `previous_interaction_id` to reuse context for a future request.

Example:

`"trun_e0083b6aac0544eb8686e8d2a76533d2"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-status)

status

enum<string>

required

Status of the run.

Available options:

`queued`,

`action_required`,

`running`,

`completed`,

`failed`,

`cancelling`,

`cancelled`

Examples:

`"queued"`

`"action_required"`

`"running"`

`"completed"`

`"failed"`

`"cancelling"`

`"cancelled"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-is-active)

is\_active

boolean

required

Whether the run is currently active, i.e. status is one of {'cancelling', 'queued', 'running'}.

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-processor)

processor

string

required

Processor used for the run.

Example:

`"base"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-created-at-one-of-0)

created\_at

string \| null

required

Timestamp of the creation of the task, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-modified-at-one-of-0)

modified\_at

string \| null

required

Timestamp of the last modification to the task, as an RFC 3339 string.

Example:

`"2025-04-24T18:56:22.513132Z"`

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-warnings-one-of-0)

warnings

Warning · object\[\] \| null

Warnings for the run, if any.

Showchild attributes

Example:

```
[]
```

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-error-one-of-0)

error

Error · object

Error for the run, present only if status is 'failed'.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-metadata-one-of-0)

metadata

Metadata · object

User-provided metadata stored with the run.

Showchild attributes

Example:

```
{}
```

[​](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run#response-taskgroup-id-one-of-0)

taskgroup\_id

string \| null

ID of the taskgroup to which the run belongs.

[Stream Task Group Events](https://docs.parallel.ai/api-reference/tasks-beta/stream-task-group-events) [Ingest FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Search API Best Practices - Parallel

**URL:** https://docs.parallel.ai/search/best-practices

[Skip to main content](https://docs.parallel.ai/search/best-practices#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Search

Search API Best Practices

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Key Benefits](https://docs.parallel.ai/search/best-practices#key-benefits)
- [Request Fields](https://docs.parallel.ai/search/best-practices#request-fields)
- [Objective and Search Queries](https://docs.parallel.ai/search/best-practices#objective-and-search-queries)

The Search API returns ranked, LLM-optimized excerpts from web sources based on natural
language objectives or keyword queries. Results are designed to serve directly as model
input, enabling faster reasoning and higher-quality completions with minimal
post-processing.

## [​](https://docs.parallel.ai/search/best-practices\#key-benefits)  Key Benefits

- **Context engineering for token efficiency**: The API ranks and compresses web results based on reasoning utility rather than human engagement, delivering the most relevant tokens for each agent’s specific objective.
- **Single-hop resolution of complex queries**: Where traditional search forces agents to make multiple sequential calls, accumulating latency and costs, Parallel resolves complex multi-topic queries in a single request.
- **Multi-hop efficiency**: For deep research workflows requiring multiple reasoning steps, agents using Parallel complete tasks in fewer tool calls while achieving higher accuracy and lower end-to-end latency.

## [​](https://docs.parallel.ai/search/best-practices\#request-fields)  Request Fields

Note that at least one of `objective` or `search_queries` is required. The remaining
fields are optional. See the [API\\
Reference](https://docs.parallel.ai/api-reference/search-beta/search) for complete parameter
specifications and constraints.

| Field | Type | Notes | Example |
| --- | --- | --- | --- |
| mode | string | Presets with varying trade-off profiles for different types of use cases. See [Modes](https://docs.parallel.ai/search/modes) for details. Defauls to `one-shot`. | ”fast” |
| objective | string | Natural-language description of the web research goal, including source or freshness guidance and broader context from the task. Maximum 5000 characters. | ”I want to know when the UN was founded. Prefer UN’s websites.” |
| search\_queries | string\[\] | Optional search queries to supplement the objective. Maximum 200 characters per query. | \[“Founding year UN”, “Year of founding United Nations”\] |
| max\_results | int | Upper bound on the number of results to return (1-20). The actual number of results may be fewer depending on query specificity and available sources. Defaults to 10. | 10 |
| source\_policy | [SourcePolicy](https://docs.parallel.ai/resources/source-policy) | Controls your sources: include/exclude specific domains and optionally set a start date for freshness control via `after_date`. Use when you want stricter source control than objective text alone. | [Source policy example](https://docs.parallel.ai/resources/source-policy#example) |
| excerpts | object | Customize excerpt length. | `{"max_chars_per_result": 10000, "max_chars_total": 50000}` |
| fetch\_policy | object | Controls when to return indexed vs fresh content. Default is to disable live fetch and return cached content from the index. | `{"max_age_seconds": 3600}` |

## [​](https://docs.parallel.ai/search/best-practices\#objective-and-search-queries)  Objective and Search Queries

**For best results, provide both `objective` and `search_queries`.** The objective should include context about your broader task or goal, while search queries ensure specific keywords are prioritized.When writing objectives, be specific about preferred sources, include freshness requirements when relevant, and specify desired content types (e.g., technical documentation, peer-reviewed research, official announcements).**Examples of effective objectives with search queries:**

Copy

Ask AI

```
{
  "mode": "fast",
  "objective": "I'm helping a client decide whether to lease or buy an EV for their small business in California. Find information about federal and state tax credits, rebates, and how they apply to business vehicle purchases vs leases.",
  "search_queries": ["EV tax credit business", "California EV rebate lease", "federal EV incentive purchase vs lease"]
}
```

Copy

Ask AI

```
{
  "mode": "fast",
  "objective": "I'm preparing Q1 2025 investor materials for a fintech startup. Find recent announcements (past 3 months) from the Federal Reserve and SEC about digital asset regulations and banking partnerships with crypto firms.",
  "search_queries": ["Federal Reserve crypto guidance 2025", "SEC digital asset policy", "bank crypto partnership regulations"]
}
```

Copy

Ask AI

```
{
  "mode": "fast",
  "objective": "I'm designing a machine learning course for graduate students. Find technical documentation and API guides that explain how transformer attention mechanisms work, preferably from official framework documentation like PyTorch or Hugging Face.",
  "search_queries": ["transformer attention mechanism", "PyTorch attention documentation", "Hugging Face transformer guide"]
}
```

Copy

Ask AI

```
{
  "mode": "fast",
  "objective": "I'm writing a literature review on Alzheimer's treatments for a medical journal. Find peer-reviewed research papers and clinical trial results from the past 2 years on amyloid-beta targeted therapies.",
  "search_queries": ["amyloid beta clinical trials", "Alzheimer's treatment research 2023-2025", "monoclonal antibody AD trials"]
}
```

[Quickstart](https://docs.parallel.ai/search/search-quickstart) [Modes](https://docs.parallel.ai/search/modes)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Execute research task (handles polling internally)
task_run = client.task_run.create(
    input="Create a comprehensive market research report on the renewable energy storage market in Europe, focusing on battery technologies and policy impacts",
    processor="ultra"
)
print(f"Run ID: {task_run.run_id}")

run_result = client.task_run.result(task_run.run_id, api_timeout=3600)

print(f"Research completed! Output has {len(run_result.output.basis)} structured fields")
for field in run_result.output.basis[:3]:
    print(f"- {field.field}: {len(field.citations)} citations")
```

## [​](https://docs.parallel.ai/task-api/task-deep-research\#polling-vs-webhooks-vs-sse)  Polling vs Webhooks vs SSE

The Task API is asynchronous—when you create a task, it returns immediately with a `run_id` while processing continues in the background. There are three ways to get results:

| Method | What It Does | Best For |
| --- | --- | --- |
| **Polling** | Your code repeatedly calls the API to check if the task is done | Simple integrations, scripts, testing |
| **Webhooks** | Parallel sends an HTTP request to your server when the task completes | Production apps with backend servers |
| **SSE** | Stream real-time progress updates as the task runs | Interactive UIs, monitoring progress |

### [​](https://docs.parallel.ai/task-api/task-deep-research\#polling)  Polling

**How it works:** After creating a task, repeatedly check its status until it completes.

Copy

Ask AI

```
import time

# Get the result
result = client.task_run.result(task_run.run_id)
```

**Key points:**

- Simplest approach—no infrastructure needed
- Use `retrieve()` to check status, then `result()` when complete
- The `result()` method also blocks until complete if you prefer a one-liner: `client.task_run.result(run_id, api_timeout=3600)`

### [​](https://docs.parallel.ai/task-api/task-deep-research\#webhooks)  Webhooks

**How it works:** Provide a webhook URL when creating the task. Parallel sends a POST request to your URL when the task finishes.

Copy

Ask AI

```
task_run = client.beta.task_run.create(
    input="...",
    processor="ultra",
    webhook={
        "url": "https://your-server.com/webhooks/parallel",
        "event_types": ["task_run.status"]
    },
    betas=["webhook-2025-08-12"]
)
```

**Key points:**

- Webhooks notify you when the task **completes**—they don’t send the actual results
- After receiving the webhook, call `result()` to retrieve the output data
- Requires a publicly accessible HTTPS endpoint
- See [Webhooks documentation](https://docs.parallel.ai/task-api/webhooks) for setup and verification

**Important:** Webhooks are a notification mechanism, not a data delivery mechanism. The webhook payload contains the task status and metadata, but you must make a separate API call to retrieve the actual research results.

### [​](https://docs.parallel.ai/task-api/task-deep-research\#server-sent-events-sse)  Server-Sent Events (SSE)

**How it works:** Connect to a streaming endpoint to receive real-time progress updates as the task runs.

Copy

Ask AI

```
# Then connect to the event stream
curl "https://api.parallel.ai/v1beta/tasks/runs/{run_id}/events" \
  -H "x-api-key: $PARALLEL_API_KEY"
```

**Key points:**

- See real-time progress: research plan, sources being explored, intermediate findings
- The final `task_run.state` event includes the complete output
- Ideal for showing users what’s happening during long research tasks
- See [Streaming Events documentation](https://docs.parallel.ai/task-api/task-sse) for event types and examples

### [​](https://docs.parallel.ai/task-api/task-deep-research\#which-should-i-use)  Which Should I Use?

| Scenario | Recommended Method |
| --- | --- |
| Testing or one-off scripts | Polling |
| Backend service processing many tasks | Webhooks |
| User-facing app showing research progress | SSE |
| Simple integration without a server | Polling |
| Production system needing reliability | Webhooks + Polling fallback |

## [​](https://docs.parallel.ai/task-api/task-deep-research\#next-steps)  Next Steps

- [**Choose a Processor:**](https://docs.parallel.ai/task-api/guides/choose-a-processor) Deep Research works best with `pro` or `ultra` processors—use fast variants (`pro-fast`, `ultra-fast`) for quicker turnaround
- [**Task Spec Best Practices:**](https://docs.parallel.ai/task-api/guides/specify-a-task) Craft effective research queries and output specifications
- [**Task Groups:**](https://docs.parallel.ai/task-api/group-api) Run multiple research queries in parallel for batch intelligence gathering
- [**Access Research Basis:**](https://docs.parallel.ai/task-api/guides/access-research-basis) Understand nested FieldBasis structure for auto schema outputs
- [**Streaming Events:**](https://docs.parallel.ai/task-api/task-sse) Monitor long-running research tasks with real-time progress updates
- [**Webhooks:**](https://docs.parallel.ai/task-api/webhooks) Configure HTTP callbacks for research completion notifications
- [**Enrichment:**](https://docs.parallel.ai/task-api/task-quickstart) Learn about enriching structured data instead of open-ended research
- [**API Reference:**](https://docs.parallel.ai/api-reference/tasks-v1/create-task-run) Complete endpoint documentation for the Task API

## [​](https://docs.parallel.ai/task-api/task-deep-research\#rate-limits)  Rate Limits

See [Rate Limits](https://docs.parallel.ai/getting-started/rate-limits) for default quotas and how to request higher limits.

[Enrichment](https://docs.parallel.ai/task-api/task-enrichment) [Task Spec](https://docs.parallel.ai/task-api/guides/specify-a-task)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Search API Quickstart - Parallel

**URL:** https://docs.parallel.ai/search/search-quickstart

[Skip to main content](https://docs.parallel.ai/search/search-quickstart#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Search

Search API Quickstart

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [1\. Set up Prerequisites](https://docs.parallel.ai/search/search-quickstart#1-set-up-prerequisites)
- [2\. Execute your First Search](https://docs.parallel.ai/search/search-quickstart#2-execute-your-first-search)
- [Sample Request](https://docs.parallel.ai/search/search-quickstart#sample-request)
- [Sample Response](https://docs.parallel.ai/search/search-quickstart#sample-response)
- [Next Steps](https://docs.parallel.ai/search/search-quickstart#next-steps)

The **Search API** takes a natural language objective and returns relevant excerpts
optimized for LLMs, replacing multiple keyword searches with a single call for broad or
complex queries.

**Available via MCP**: Search is available as a tool as part of the Parallel Search MCP. Our MCP is optimized for best practices on Search and Extract usage. [Start here](https://docs.parallel.ai/integrations/mcp/search-mcp) with MCP for your use case. If you’re interested in direct use of the API, follow the steps below.

See [Pricing](https://docs.parallel.ai/getting-started/pricing) for a detailed schedule of rates.

## [​](https://docs.parallel.ai/search/search-quickstart\#1-set-up-prerequisites)  1\. Set up Prerequisites

Generate your API key on [Platform](https://platform.parallel.ai/). Then, set up with the TypeScript SDK, Python SDK or with cURL:

cURL

Python

TypeScript

Copy

Ask AI

```
echo "Install curl and jq via brew, apt, or your favorite package manager"
export PARALLEL_API_KEY="PARALLEL_API_KEY"
```

## [​](https://docs.parallel.ai/search/search-quickstart\#2-execute-your-first-search)  2\. Execute your First Search

### [​](https://docs.parallel.ai/search/search-quickstart\#sample-request)  Sample Request

cURL

Python

TypeScript

Copy

Ask AI

```
curl https://api.parallel.ai/v1beta/search \
  -H "Content-Type: application/json" \
  -H "x-api-key: $PARALLEL_API_KEY" \
  -H "parallel-beta: search-extract-2025-10-10" \
  -d '{
    "objective": "When was the United Nations established? Prefer UN'\''s websites.",
    "search_queries": [\
      "Founding year UN",\
      "Year of founding United Nations"\
    ],
    "mode": "fast",
    "excerpts": {
      "max_chars_per_result": 10000
    }
  }'
```

`max_results` is an upper bound, not a guaranteed count. The actual number of results may be fewer depending on query specificity and available sources.

### [​](https://docs.parallel.ai/search/search-quickstart\#sample-response)  Sample Response

The API returns a JSON response with the following structure. The SDK examples above iterate over `results` to print each result’s title, URL, and excerpts.

Copy

Ask AI

```
{
  "search_id": "search_e749586f-00f0-43a0-9f33-730a574d32b9",
  "results": [\
    {\
      "url": "http://un.org/",\
      "title": "Welcome to the United Nations",\
      "publish_date": null,\
      "excerpts": [\
        "Last updated before: 2025-06-10\nUNICEF/UNI510119/Truong Viet Hung\n儿基会/UNI510119/Truong Viet Hung\nUNICEF/UNI510119/Truong Viet Hung\nUNICEF/UNI510119/Truong Viet Hung\nЮНИСЕФ/UNI510119/Труонг Вьет Хонг\nUNICEF/UNI510119/Truong Viet Hung\n[اليوم الدولي للّعب - 11 حزيران/ يونيه](https://www.un.org/ar/observances/international-day-of-play)\n[国际游玩日 - 6月11日](https://www.un.org/zh/observances/international-day-of-play)\n[International Day of Play - 11 June](https://www.un.org/en/observances/international-day-of-play)\n[Journée internationale du jeu - 11 juin](https://www.un.org/fr/observances/international-day-of-play)\n[Международный день игры — 11 июня](https://www.un.org/ru/observances/international-day-of-play)\n[Día Internacional del Juego – 11 de junio](https://www.un.org/es/observances/international-day-of-play)\nUNICEF/UNI510119/Truong Viet Hung\n儿基会/UNI510119/Truong Viet Hung\nUNICEF/UNI510119/Truong Viet Hung\nUNICEF/UNI510119/Truong Viet Hung\nЮНИСЕФ/UNI510119/Труонг Вьет Хонг\nUNICEF/UNI510119/Truong Viet Hung\nاليوم الدولي للّعب - 11 حزيران/ يونيه\n国际游玩日 - 6月11日\nInternational Day of Play - 11 June\nJournée internationale du jeu - 11 juin\nМеждународный день игры — 11 июня\nDía Internacional del Juego – 11 de junio\n[عربي](/ar/)\n[中文](/zh/)\n[English](/en/)\n[Français](/fr/)\n[Русский](/ru/)\n[Español](/es/)\n"\
      ]\
    },\
    {\
      "url": "https://www.un.org/en/about-us/history-of-the-un",\
      "title": "History of the United Nations",\
      "publish_date": "2001-01-01",\
      "excerpts": [\
        "Last updated: 20010101\n[Skip to main content]()\n\nToggle navigation [Welcome to the United Nations](/)\n\n+ [العربية](/ar/about-us/history-of-the-un \"تاريخ الأمم المتحدة\")\n    + [中文](/zh/about-us/history-of-the-un \"联合国历史\")\n    + Nederlands\n    + [English](/en/about-us/history-of-the-un \"History of the United Nations\")\n    + [Français](/fr/about-us/history-of-the-un \"L'histoire des Nations Unies\")\n    + Kreyòl\n    + हिन्दी\n    + Bahasa Indonesia\n    + Polski\n    + Português\n    + [Русский](/ru/about-us/history-of-the-un \"История Организации Объединенных Наций\")\n    + [Español](/es/about-us/history-of-the-un \"Historia de las Naciones Unidas\")\n    + Kiswahili\n    + Türkçe\n    + Українська\n\n... (truncated for brevity)"\
      ]\
    },\
    {\
      "url": "https://research.un.org/en/unmembers/founders",\
      "title": "UN Founding Members - UN Membership",\
      "publish_date": "2018-11-08",\
      "excerpts": [\
        "Last updated: 20181108\n[Skip to Main Content]()\n\nToggle navigation [Welcome to the United Nations](https://www.un.org/en)\n\n... (content omitted for brevity)"\
      ]\
    },\
    {\
      "url": "https://www.un.org/en/about-us/un-charter",\
      "title": "UN Charter | United Nations",\
      "publish_date": "2025-01-01",\
      "excerpts": [\
        "Last updated: 20250101\n[Skip to main content]()\n\n... (content omitted for brevity)"\
      ]\
    },\
    {\
      "url": "https://www.un.org/en/video/founding-united-nations-1945",\
      "title": "Founding of the United Nations 1945",\
      "publish_date": "2023-11-01",\
      "excerpts": [\
        "Last updated: 20231101\n[Skip to main content]()\n\n... (content omitted for brevity)"\
      ]\
    },\
    {\
      "url": "https://www.un.org/en/about-us",\
      "title": "About Us | United Nations",\
      "publish_date": "2017-01-01",\
      "excerpts": [\
        "Last updated: 20170101\n[Skip to main content]()\n\n... (content omitted for brevity)"\
      ]\
    },\
    {\
      "url": "https://www.facebook.com/unitednationsfoundation/posts/eighty-years-of-the-united-nations-on-this-day-in-1945-the-un-charter-came-into-/1404295104587053/",\
      "title": "Eighty years of the United Nations. On this day in 1945, the UN ...",\
      "publish_date": "2025-10-24",\
      "excerpts": [\
        "The United Nations officially came into existence on 24 October 1945, when the Charter had been ratified by China, France, the Soviet Union, the United Kingdom, the United States and by a majority of other signatories."\
      ]\
    },\
    {\
      "url": "https://www.un.org/en/model-united-nations/history-united-nations",\
      "title": "History of the United Nations",\
      "publish_date": null,\
      "excerpts": [\
        "Last updated before: 2025-11-05\nThe purpose of this conference was ..."\
      ]\
    },\
    {\
      "url": "https://en.wikipedia.org/wiki/United_Nations",\
      "title": "United Nations - Wikipedia",\
      "publish_date": "2025-11-03",\
      "excerpts": [\
        "Last updated: 20251103\nIt took the [conference at Yalta] ... (content truncated)"\
      ]\
    },\
    {\
      "url": "https://www.un.org/en/about-us/history-of-the-un/preparatory-years",\
      "title": "Preparatory Years: UN Charter History | United Nations",\
      "publish_date": "2001-01-01",\
      "excerpts": [\
        "Last updated: 20010101\n[Skip to main content]()\n\n... (content truncated)"\
      ]\
    }\
  ],
  "warnings": null,
  "usage": [\
    {\
      "name": "sku_search",\
      "count": 1\
    }\
  ]
}
```

See all 92 lines

## [​](https://docs.parallel.ai/search/search-quickstart\#next-steps)  Next Steps

- **[Best Practices](https://docs.parallel.ai/search/best-practices)** — learn how to craft effective objectives and search queries
- **[Search Modes](https://docs.parallel.ai/search/modes)** — explore mode presets for different use cases
- **[API Reference](https://docs.parallel.ai/api-reference/search-beta/search)** — full parameter specifications, constraints, and response schema
- **[Rate Limits](https://docs.parallel.ai/getting-started/rate-limits)** — default quotas per product

[Glossary](https://docs.parallel.ai/getting-started/glossary) [Best Practices](https://docs.parallel.ai/search/best-practices)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Ingest FindAll Run - Parallel

**URL:** https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run

[Skip to main content](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

FindAll API (Beta)

Ingest FindAll Run

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

objective = "Find all portfolio companies of Khosla Ventures founded after 2020 and CEO names"

ingest = client.beta.findall.ingest(
    objective=objective,
)

print(ingest.model_dump_json(indent=2))
```

200

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    },\
    {\
      "name": "raised_series_a_2024_check",\
      "description": "Company must have raised Series A funding in 2024"\
    }\
  ],
  "generator": "core"
}
```

POST

/

v1beta

/

findall

/

ingest

Try it

Python

Python

Copy

Ask AI

```
from parallel import Parallel

client = Parallel(api_key="API Key")

objective = "Find all portfolio companies of Khosla Ventures founded after 2020 and CEO names"

ingest = client.beta.findall.ingest(
    objective=objective,
)

print(ingest.model_dump_json(indent=2))
```

200

422

Copy

Ask AI

```
{
  "objective": "Find all AI companies that raised Series A funding in 2024",
  "entity_type": "companies",
  "match_conditions": [\
    {\
      "name": "developing_ai_products_check",\
      "description": "Company must be developing artificial intelligence (AI) products"\
    },\
    {\
      "name": "raised_series_a_2024_check",\
      "description": "Company must have raised Series A funding in 2024"\
    }\
  ],
  "generator": "core"
}
```

#### Authorizations

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#authorization-x-api-key)

x-api-key

string

header

required

#### Headers

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#parameter-one-of-0)

parallel-beta

string \| null

#### Body

application/json

Input model for FindAll ingest.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#body-objective)

objective

string

required

Natural language objective to create a FindAll run spec.

Example:

`"Find all AI companies that raised Series A funding in 2024"`

#### Response

200

application/json

Successful Response

Response model for FindAll ingest.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#response-objective)

objective

string

required

Natural language objective of the FindAll run.

Example:

`"Find all AI companies that raised Series A funding in 2024"`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#response-entity-type)

entity\_type

string

required

Type of the entity for the FindAll run.

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#response-match-conditions)

match\_conditions

MatchCondition · object\[\]

required

List of match conditions for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#response-enrichments-one-of-0)

enrichments

FindAllEnrichInput · object\[\] \| null

List of enrichment inputs for the FindAll run.

Showchild attributes

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#response-generator)

generator

enum<string>

default:core

The generator of the FindAll run.

Available options:

`base`,

`core`,

`pro`,

`preview`

[​](https://docs.parallel.ai/api-reference/findall-api-beta/ingest-findall-run#response-match-limit-one-of-0)

match\_limit

integer \| null

Max number of candidates to evaluate

[Retrieve Task Group Run](https://docs.parallel.ai/api-reference/tasks-beta/retrieve-task-group-run) [Create FindAll Run](https://docs.parallel.ai/api-reference/findall-api-beta/create-findall-run)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Slack Integration - Parallel

**URL:** https://docs.parallel.ai/monitor-api/monitor-slack#/monitor

[Skip to main content](https://docs.parallel.ai/monitor-api/monitor-slack#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Slack Integration

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Installation](https://docs.parallel.ai/monitor-api/monitor-slack#installation)
- [Commands](https://docs.parallel.ai/monitor-api/monitor-slack#commands)
- [/monitor](https://docs.parallel.ai/monitor-api/monitor-slack#%2Fmonitor)
- [/hourly](https://docs.parallel.ai/monitor-api/monitor-slack#%2Fhourly)
- [/help](https://docs.parallel.ai/monitor-api/monitor-slack#%2Fhelp)
- [Cancel a Monitor](https://docs.parallel.ai/monitor-api/monitor-slack#cancel-a-monitor)
- [Pricing](https://docs.parallel.ai/monitor-api/monitor-slack#pricing)

The Parallel Slack app brings [Monitor](https://docs.parallel.ai/monitor-api/monitor-quickstart) directly into your Slack workspace. Create monitors with slash commands and receive updates in dedicated threads.

## [​](https://docs.parallel.ai/monitor-api/monitor-slack\#installation)  Installation

1. Go to [platform.parallel.ai](https://platform.parallel.ai/) and navigate to the Integrations section
2. Click **Add to Slack** to begin the OAuth flow
3. Authorize the Parallel app in your workspace
4. Invite the bot to any channel where you want to use monitoring: `/invite @Parallel`

Your Parallel API key is securely linked during the OAuth flow. All monitors created via Slack use your account’s quota and billing.

## [​](https://docs.parallel.ai/monitor-api/monitor-slack\#commands)  Commands

### [​](https://docs.parallel.ai/monitor-api/monitor-slack\#/monitor)  /monitor

Create a **daily** monitor:

Copy

Ask AI

```
/monitor latest AI research papers
```

The bot posts your query and replies in a thread when changes are detected.

### [​](https://docs.parallel.ai/monitor-api/monitor-slack\#/hourly)  /hourly

Create an **hourly** monitor for fast-moving topics:

Copy

Ask AI

```
/hourly breaking news about OpenAI
```

### [​](https://docs.parallel.ai/monitor-api/monitor-slack\#/help)  /help

View available commands:

Copy

Ask AI

```
/help
```

### [​](https://docs.parallel.ai/monitor-api/monitor-slack\#cancel-a-monitor)  Cancel a Monitor

Reply to the monitoring thread with:

Copy

Ask AI

```
cancelmonitor
```

The bot will cancel the monitor and confirm in the thread.

## [​](https://docs.parallel.ai/monitor-api/monitor-slack\#pricing)  Pricing

Monitors created via Slack use the same pricing as the Monitor API. See [Pricing](https://docs.parallel.ai/resources/pricing) for details.

[Webhooks](https://docs.parallel.ai/monitor-api/monitor-webhooks) [Simulate Event](https://docs.parallel.ai/monitor-api/monitor-simulate-event)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---

# Events and Event Groups - Parallel

**URL:** https://docs.parallel.ai/monitor-api/monitor-events

[Skip to main content](https://docs.parallel.ai/monitor-api/monitor-events#content-area)

[Parallel home page![light logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/light.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=363adf4c652fd6c3e2971682bb0faa3f)![dark logo](https://mintcdn.com/parallel-6fabab31-mtje7p526we/l-jei-Nm9EE738qc/logo/dark.svg?fit=max&auto=format&n=l-jei-Nm9EE738qc&q=85&s=9c570fcc4d2ede8939f685361f4eae0c)](https://docs.parallel.ai/)

Search...

Ctrl KAsk AI

Search...

Navigation

Features

Events and Event Groups

[Home](https://docs.parallel.ai/home) [Documentation](https://docs.parallel.ai/getting-started/overview) [API Reference](https://docs.parallel.ai/api-reference/chat-api-beta/chat-completions) [Changelog](https://docs.parallel.ai/resources/changelog) [Pricing](https://docs.parallel.ai/getting-started/pricing)

On this page

- [Event Groups](https://docs.parallel.ai/monitor-api/monitor-events#event-groups)
- [Other Events](https://docs.parallel.ai/monitor-api/monitor-events#other-events)
- [Accessing Events](https://docs.parallel.ai/monitor-api/monitor-events#accessing-events)

Monitors produce a stream of events each time they run. These events capture:

- new results detected by your query (events)
- run completions
- errors (if a run fails)

Related events are grouped by an `event_group_id` so you can
fetch the full set of results that belong to the same discovery.

## [​](https://docs.parallel.ai/monitor-api/monitor-events\#event-groups)  Event Groups

Event groups are primarily relevant for webhook users. When a webhook fires
with a `monitor.event.detected` event, it returns an `event_group_id` that you
use to retrieve the complete set of results.

Event groups collect related results under a single `event_group_id`.
When a monitor detects new results, it creates an event group. Subsequent runs can add
additional events to the same group if they’re related to the same discovery.Use event groups to present the full context of a discovery (multiple sources, follow‑up updates) as one
unit. To fetch the complete set of results for a discovery, use the [`GET` event group](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group) endpoint
with the `event_group_id` received in your webhook payload.

## [​](https://docs.parallel.ai/monitor-api/monitor-events\#other-events)  Other Events

Besides events with new results, monitors emit:

- **Completion** (`type: "completion"`): indicates a run finished successfully.
- **Error** (`type: "error"`): indicates a run failed.

These are useful for sanity checks, alerting, and operational visibility (e.g., dashboards, retries).

Runs with non-empty events are not included in completions. This means that a
run will correspond to only one of succesful event detection, completion or
failure.

## [​](https://docs.parallel.ai/monitor-api/monitor-events\#accessing-events)  Accessing Events

You can receive events via webhooks (recommended) or retrieve them via endpoints.

- **Webhooks (recommended)**: lowest latency, push-based delivery.
Subscribe to `monitor.event.detected`, `monitor.execution.completed`, and `monitor.execution.failed`.
See [Monitor webhooks](https://docs.parallel.ai/monitor-api/monitor-webhooks) for more details on setting up webhooks.
- **Endpoints (for history/backfill)**:  - [`GET` monitor events](https://docs.parallel.ai/api-reference/monitor/list-events)—
      list events for a monitor in reverse chronological order (up to recent ~300 runs).

    - This flattens out events, meaning that multiple events from the same event group
      will be listed as different events.
  - [`GET` event group](https://docs.parallel.ai/api-reference/monitor/retrieve-event-group) -
    list all events given an `event_group_id`.

[Structured Outputs](https://docs.parallel.ai/monitor-api/monitor-structured-outputs) [Webhooks](https://docs.parallel.ai/monitor-api/monitor-webhooks)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---
