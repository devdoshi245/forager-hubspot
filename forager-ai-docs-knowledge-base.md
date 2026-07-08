# Forager.ai — Complete Documentation Knowledge Base

> Scraped from https://docs.forager.ai on 2026-05-17 via Firecrawl.
> Single-file knowledge base — all endpoints, all fields, all pricing, all delivery options.

---

## Table of Contents

- [Intro](#intro)
- [Quickstart — Create an Account](#quickstart--create-an-account)
- [Quickstart — Authentication](#quickstart--authentication)
- [Quickstart — API Credit Pricing](#quickstart--api-credit-pricing)
- [Quickstart — Recipes](#quickstart--recipes)
- [API Reference — Overview](#api-reference--overview)
- [API Reference — Job Posts](#api-reference--job-posts)
- [API Reference — Organizations](#api-reference--organizations)
- [API Reference — People](#api-reference--people)
- [API Reference — People (Personal Emails detail)](#api-reference--people-personal-emails-detail)
- [API Reference — People (Phone Numbers detail)](#api-reference--people-phone-numbers-detail)
- [API Reference — People (Reverse lookup by phone detail)](#api-reference--people-reverse-lookup-by-phone-detail)
- [API Reference — Websites](#api-reference--websites)
- [API Reference — Users](#api-reference--users)
- [API Reference — Users (Create API Key)](#api-reference--users-create-api-key)
- [API Reference — Users (Delete API Key)](#api-reference--users-delete-api-key)
- [API Reference — Autocomplete](#api-reference--autocomplete)
- [API Reference — Autocomplete (Web technologies detail)](#api-reference--autocomplete-web-technologies-detail)
- [Data Feeds V2 — Overview](#data-feeds-v2--overview)
- [Data Feeds V2 — Schema](#data-feeds-v2--schema)
- [Data Feeds V2 — Delivery via S3](#data-feeds-v2--delivery-via-s3)
- [Data Feeds V2 — Delivery via Snowflake](#data-feeds-v2--delivery-via-snowflake)
- [Data Feeds V2 — Migrate v1 → v2](#data-feeds-v2--migrate-v1--v2)
- [Data Feeds V2 — Output Data File Details](#data-feeds-v2--output-data-file-details)
- [Data Feeds V1 — Overview](#data-feeds-v1--overview)
- [Data Feeds V1 — Schema](#data-feeds-v1--schema)
- [Data Feeds V1 — Delivery via Snowflake](#data-feeds-v1--delivery-via-snowflake)

---

## Intro

_Source: https://docs.forager.ai_

### Welcome to Our Docs!

Use the **side panel** on the left to navigate individual sections, or use the **Search bar** in the top right to find something specific.

* * *

#### Get Started

🚀 **Sign up for a free account here:** [https://app.forager.ai](https://app.forager.ai/)

Once you've signed up:

- Visit our **[API Quickstart](https://docs.forager.ai/api-overview/create-an-account)** to get moving right away.
- Check out our **[API Reference](https://docs.forager.ai/openapi)** tool to start testing without writing a single line of code.

* * *

#### Already Familiar with APIs?

📌 Explore our **[Recipes](https://docs.forager.ai/api-overview/recipes)** for a step-by-step walkthrough of implementing our APIs.

* * *

#### Need a Flat-File Instead?

📄 Visit **[Data License Overview](https://docs.forager.ai/data-license/v2/data-feed-overview)** to learn more and connect with a member of our team.

---

## Quickstart — Create an Account

_Source: https://docs.forager.ai/api-overview/create-an-account_

### Create an Account

To access our data, you will need an **API key**.

You can get one by **creating a free account** at [app.forager.ai/sign-up](https://app.forager.ai/sign-up), clicking **[API](https://app.forager.ai/keys)**, and create a new key by clicking **create**.

You will also need to copy your **Account ID** that can be found in the **[My Account](https://app.forager.ai/profile)** page

* * *

> 🚧 **Warning!**
>
> This is your **secret API key**, so please **keep it private**.
>
> We charge you credits based on usage associated with it. If you need a new API key, you can always generate one from the **[Forager Web App](https://app.forager.ai/keys)**.

---

## Quickstart — Authentication

_Source: https://docs.forager.ai/api-overview/authentication_

### Authentication

To interact with **Forager.ai's API**, you must authenticate every request using your **API key**. This ensures secure access to our data services.

* * *

#### Obtaining an API Key

1. **Sign up for an account** at [app.forager.ai](https://app.forager.ai/).
2. Navigate to the **API** section.
3. Create and copy your **API Key** – you’ll need this for all API requests.

* * *

#### Using Your API Key

Forager.ai uses **API key authentication** via the `X-API-KEY` header. You must include this key in all requests to successfully access the API.

##### Example: Sending an Authenticated API Request

Below is an example of how to make a request to the **Person Phone Number Lookup API** using `curl` with your API key.

```
curl -X POST "https://api-v2.forager.ai/api/{account_id}/datastorage/person_contacts_lookup/phone_numbers/" \
     -H "Content-Type: application/json" \
     -H "X-API-KEY: YOUR_API_KEY" \
     -d '{
           "linkedin_public_identifier": "billgates"
         }'
```

##### Explanation

- Replace {account\_id} with your Forager.ai account ID.
- Replace YOUR\_API\_KEY with your actual API key.
- The X-API-KEY header must be included in every request to authenticate.
- The API will return an error if the key is missing or invalid.

---

## Quickstart — API Credit Pricing

_Source: https://docs.forager.ai/api-overview/credit-pricing_

### API Credit Pricing

#### Overview

This document provides an overview of the credit cost associated with each API request available in our system. Each request consumes a specific number of credits based on the type of the data retrieval.

To purchase credits or review the latest pricing details, please visit:

[Manage Subscription & Buy Credits](https://app.forager.ai/subscription)

#### Credit Cost Per API Request

The table below outlines the number of credits consumed per request for each API endpoint:

| API Request Name | Credits per Request |
| --- | --- |
| [Person details lookup](https://docs.forager.ai/openapi/persons/datastorage_person_detail_lookup_create) | 1 |
| [Person work email lookup](https://docs.forager.ai/openapi/persons/datastorage_person_contacts_lookup_work_emails_create) | 5 |
| [Person personal email lookup](https://docs.forager.ai/openapi/persons/datastorage_person_contacts_lookup_personal_emails_create) | 5 |
| [Person phone number lookup](https://docs.forager.ai/openapi/persons/datastorage_person_contacts_lookup_phone_numbers_create) | 15 |
| [Person reverse email search](https://docs.forager.ai/openapi/persons/datastorage_person_detail_reverse_lookup_by_email_create) | 5 |
| [Person reverse phone number search](https://docs.forager.ai/openapi/persons/datastorage_person_detail_reverse_lookup_by_phone_number_create) | 15 |
| [Person role details lookup](https://docs.forager.ai/openapi/persons/datastorage_person_role_search_totals_create) | 1 |
| [Person role search API call](https://docs.forager.ai/openapi/persons/datastorage_person_role_search_create) | 1 |
| [Job search API call](https://docs.forager.ai/openapi/datastorage/datastorage_job_search_create) | 2 |
| [Organization search API call](https://docs.forager.ai/openapi/organizations/datastorage_organization_search_create) | 1 |
| [Organization technologies lookup](https://docs.forager.ai/openapi/datastorage/datastorage_website_detail_lookup_create) | 1 |

Looking to buy credits in bulk or have other pricing quesitons? [Book a call with our team here](https://calendly.com/d/46p-2vr-83n).

---

## Quickstart — Recipes

_Source: https://docs.forager.ai/api-overview/recipes_

### Recipes

This section provides step-by-step API usage examples. Below, you'll learn how to **search for a person by job title**, extract their `id` from the response, and use that ID to **perform a phone number lookup**.

* * *

#### Search for a Person by Job Title

Use the **Person Role Search API** to find a person by job title. The request below searches for **"Software Engineer"**.

##### Request

```
curl -X POST "https://api-v2.forager.ai/api/{account_id}/datastorage/person_role_search/" \
     -H "Content-Type: application/json" \
     -H "X-API-KEY: YOUR_API_KEY" \
     -d '{
           "role_title": "Software Engineer",
           "role_is_current": true
         }'
```

##### Sample Response

```
{
  "search_results": [\
    {\
      "id": 123456,\
      "person": {\
        "id": 123,\
        "full_name": "John Doe",\
        "location": "San Francisco, CA"\
      },\
      "role_title": "Software Engineer",\
      "organization": {\
        "name": "Tech Corp"\
      }\
    }\
  ],
  "total_search_results": 1
}
```

Extract the `person.id` value (123 in this case) for the next step.

#### Look Up a Person's Phone Number

Once you have the `person.id`, use the Person Phone Number Lookup API to retrieve phone number details.

##### Request

```
curl -X POST "https://api-v2.forager.ai/api/{account_id}/datastorage/person_contacts_lookup/phone_numbers/" \
     -H "Content-Type: application/json" \
     -H "X-API-KEY: YOUR_API_KEY" \
     -d '{
           "person_id": 123
         }'
```

##### Sample Response

```
[\
  {\
    "phone_number": "+14155552671"\
  }\
]
```

---

## API Reference — Overview

_Source: https://docs.forager.ai/openapi_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Websites

#### Users

#### Autocomplete

---

## API Reference — Job Posts

_Source: https://docs.forager.ai/openapi/job-posts_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Job post event search

###### Request

Job post event search.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Body
application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

page _integer_

job\_source _string_ _(JobSourceEnum)_

- `indeed` \- Indeed
- `linkedin` \- LinkedIn
- `angellist` \- AngelList

Enum"indeed""linkedin""angellist"

date\_featured\_start _string_ _(date)_

date\_featured\_end _string_ _(date)_

organization\_ids _Array of integers_

To get a list of IDs use [Organizations lookup endpoint](https://docs.forager.ai/openapi/job-posts#v1_organization_lookup).

title _string_

This field supports a boolean text search query.

description _string_

This field supports a boolean text search query.

is\_remote _boolean or null_

is\_active _boolean_

Defaulttrue

locations _Array of integers_

To get a list of IDs use [Locations lookup endpoint](https://docs.forager.ai/openapi/job-posts#v1_location_lookup).

locations\_exclude _Array of integers_

To get a list of IDs use [Locations lookup endpoint](https://docs.forager.ai/openapi/job-posts#v1_location_lookup).

post

/api/{account\_id}/datastorage/job\_search/

- https://api-v2.forager.ai/api/{account\_id}/datastorage/job\_search/

curl

application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

```
curl -i -X POST \
  'https://api-v2.forager.ai/api/{account_id}/datastorage/job_search/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE' \
  -d '{
    "page": 0,
    "job_source": "indeed",
    "date_featured_start": "2019-08-24",
    "date_featured_end": "2019-08-24",
    "organization_ids": [\
      0\
    ],
    "title": "string",
    "description": "string",
    "is_remote": true,
    "is_active": true,
    "locations": [\
      0\
    ],
    "locations_exclude": [\
      0\
    ]
  }'
```

Try it

###### Responses

1. 200

Expand all

Bodyapplication/json

search\_results _Array of objects_ _(JobPostEventSearchResult)_ read-onlyrequired

-

search\_results\[\].​id _integer_ read-onlyrequired

search\_results\[\].​source _string_ read-onlyrequired

- `indeed` \- Indeed
- `linkedin` \- LinkedIn
- `angellist` \- AngelList

Enum"indeed""linkedin""angellist"

search\_results\[\].​date\_featured _string_ _(date)_ required

search\_results\[\].​organization _object_ read-onlyrequired

Short serializer for the Organization model.

-

search\_results\[\].​organization.​id _integer_ read-onlyrequired

search\_results\[\].​organization.​name _string_ _<= 255 characters_ required

search\_results\[\].​organization.​domain _string or null_ _(uri)_ _<= 200 characters_

search\_results\[\].​organization.​linkedin\_info _object_ read-onlyrequired

Serializer for the OrganizationLinkedinInfo model.

-

search\_results\[\].​organization.​linkedin\_info.​public\_identifier _string or null_ _<= 255 characters_

search\_results\[\].​organization.​linkedin\_info.​industry _object_ read-onlyrequired

Serializer for the LinkedinIndustry document.

-

search\_results\[\].​organization.​linkedin\_info.​industry.​id _integer_ read-onlyrequired

search\_results\[\].​organization.​linkedin\_info.​industry.​name _string_ _<= 255 characters_ required

search\_results\[\].​organization.​linkedin\_info.​public\_profile\_url _string or null_ read-onlyrequired

Get LinkedIn public profile URL.

search\_results\[\].​source\_id _string_ _<= 65 characters_ required

search\_results\[\].​url _string_ _(uri)_ _<= 510 characters_ required

search\_results\[\].​title _string_ _<= 255 characters_ required

search\_results\[\].​description _string or null_

search\_results\[\].​is\_remote _boolean_ _(Is remote?)_ required

search\_results\[\].​location _object_ read-onlyrequired

Serializer for the InnerLocation model for Jobs search API.

-

search\_results\[\].​location.​id _integer_ read-onlyrequired

search\_results\[\].​location.​name _string_ _<= 255 characters_ required

search\_results\[\].​location.​osm\_locations _Array of objects_ _(JobOSMLocation)_ read-onlyrequired

-

search\_results\[\].​location.​osm\_locations\[\].​id _integer_ read-onlyrequired

search\_results\[\].​location.​osm\_locations\[\].​name _string_ _<= 255 characters_ required

search\_results\[\].​location.​osm\_locations\[\].​place\_type _string_ _(Type)_ _<= 255 characters_ required

search\_results\[\].​is\_active _boolean_ _(Is active?)_ required

total\_search\_results _integer_ _>= 0_ required

Response

1. 200

application/json

```
{
  "search_results": [\
    { … }\
  ],
  "total_search_results": 0
}
```

---

## API Reference — Organizations

_Source: https://docs.forager.ai/openapi/organizations_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### Organization search

###### Request

Organization search.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Body
application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

page _integer_

organization\_ids _Array of integers_

To get a list of IDs use [Organizations lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_organization_lookup).

description _string_

locations _Array of integers_

To get a list of IDs use [Locations lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_location_lookup).

industries _Array of integers_

To get a list of IDs use [Industries lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_industry_lookup).

industries\_exclude _Array of integers_

To get a list of IDs use [Industries lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_industry_lookup).

keywords _Array of integers_

To get a list of IDs use [Organization keywords lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_organization_keyword_lookup).

employees\_start _integer_

employees\_end _integer_

founded\_date\_start _string_ _(date)_

founded\_date\_end _string_ _(date)_

revenue\_start _integer_

revenue\_end _integer_

domains _Array of strings_

domain\_rank\_start _integer_

domain\_rank\_end _integer_

domain\_traffic\_start _integer_

domain\_traffic\_end _integer_

web\_technologies _Array of integers_

To get a list of IDs use [Organization keywords lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_organization_keyword_lookup).

linkedin\_public\_identifiers _Array of strings_

LinkedIn organization "Public identifier/Slug/ID" - "linkedin.com/company/!slug!/".

funding\_types _Array of strings_ _(FundingTypesEnum)_

ItemsEnum"angel""convertible\_note""corporate\_round""debt\_financing""equity\_crowdfunding""grant""initial\_coin\_offering""non\_equity\_assistance""post\_ipo\_debt""post\_ipo\_equity"+18 more

funding\_total\_start _integer_

funding\_total\_end _integer_

funding\_event\_date\_featured\_start _string_ _(date)_

funding\_event\_date\_featured\_end _string_ _(date)_

job\_post\_title _string_

This field supports a boolean text search query.

job\_post\_description _string_

This field supports a boolean text search query.

job\_post\_is\_remote _boolean or null_

job\_post\_is\_active _boolean or null_

job\_post\_date\_featured\_start _string_ _(date)_

job\_post\_date\_featured\_end _string_ _(date)_

job\_post\_locations _Array of integers_

To get a list of IDs use [Locations lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_location_lookup).

job\_post\_locations\_exclude _Array of integers_

To get a list of IDs use [Locations lookup endpoint](https://docs.forager.ai/openapi/organizations#v1_location_lookup).

simple\_event\_source _string_ _(SimpleEventSourceEnum)_

- `product_hunt` \- Product Hunt
- `form_c_sec_gov` \- Form C sec.gov
- `form_d_sec_gov` \- Form D sec.gov

Enum"product\_hunt""form\_c\_sec\_gov""form\_d\_sec\_gov"

simple\_event\_reason _string_ _(SimpleEventReasonEnum)_

- `report_released` \- Report released
- `promoted_on_site` \- Promoted on site

Enum"report\_released""promoted\_on\_site"

simple\_event\_date\_featured\_start _string_ _(date)_

simple\_event\_date\_featured\_end _string_ _(date)_

post

/api/{account\_id}/datastorage/organization\_search/

- https://api-v2.forager.ai/api/{account\_id}/datastorage/organization\_search/

curl

application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

```
curl -i -X POST \
  'https://api-v2.forager.ai/api/{account_id}/datastorage/organization_search/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE' \
  -d '{
    "page": 0,
    "organization_ids": [\
      0\
    ],
    "description": "string",
    "locations": [\
      0\
    ],
    "industries": [\
      0\
    ],
    "industries_exclude": [\
      0\
    ],
    "keywords": [\
      0\
    ],
    "employees_start": 0,
    "employees_end": 0,
    "founded_date_start": "2019-08-24",
    "founded_date_end": "2019-08-24",
    "revenue_start": 0,
    "revenue_end": 0,
    "domains": [\
      "string"\
    ],
    "domain_rank_start": 0,
    "domain_rank_end": 0,
    "domain_traffic_start": 0,
    "domain_traffic_end": 0,
    "web_technologies": [\
      0\
    ],
    "linkedin_public_identifiers": [\
      "string"\
    ],
    "funding_types": [\
      "angel"\
    ],
    "funding_total_start": 0,
    "funding_total_end": 0,
    "funding_event_date_featured_start": "2019-08-24",
    "funding_event_date_featured_end": "2019-08-24",
    "job_post_title": "string",
    "job_post_description": "string",
    "job_post_is_remote": true,
    "job_post_is_active": true,
    "job_post_date_featured_start": "2019-08-24",
    "job_post_date_featured_end": "2019-08-24",
    "job_post_locations": [\
      0\
    ],
    "job_post_locations_exclude": [\
      0\
    ],
    "simple_event_source": "product_hunt",
    "simple_event_reason": "report_released",
    "simple_event_date_featured_start": "2019-08-24",
    "simple_event_date_featured_end": "2019-08-24"
  }'
```

Try it

###### Responses

1. 200

Expand all

Bodyapplication/json

search\_results _Array of objects_ _(OrganizationSearchResult)_ read-onlyrequired

-

search\_results\[\].​id _integer_ read-onlyrequired

search\_results\[\].​name _string_ _<= 255 characters_ required

search\_results\[\].​legal\_name _string_ _<= 255 characters_ required

search\_results\[\].​website _string or null_ _(uri)_ _<= 16384 characters_

search\_results\[\].​domain _string or null_ _(uri)_ _<= 200 characters_

search\_results\[\].​domain\_rank _integer or null_ read-onlyrequired

Domain rank.

search\_results\[\].​logo _string or null_ _(uri)_ _<= 510 characters_

search\_results\[\].​description _string or null_

search\_results\[\].​founded\_date _string or null_ _(date)_

search\_results\[\].​operating\_status _string or null_ _<= 255 characters_

search\_results\[\].​employees\_range _string or null_ _<= 255 characters_

search\_results\[\].​employees\_amount _integer or null_ _\[ 0 .. 2147483647 \]_

search\_results\[\].​keywords _Array of objects_ _(OrganizationKeyword)_ read-onlyrequired

-

search\_results\[\].​keywords\[\].​id _integer_ read-onlyrequired

search\_results\[\].​keywords\[\].​name _string_ _<= 255 characters_ required

search\_results\[\].​location _object_ read-onlyrequired

Serializer for the InnerLocation model.

-

search\_results\[\].​location.​id _integer_ read-onlyrequired

search\_results\[\].​location.​name _string_ _<= 255 characters_ required

search\_results\[\].​location.​osm\_locations _Array of objects_ _(OSMLocation)_ read-onlyrequired

-

search\_results\[\].​location.​osm\_locations\[\].​id _integer_ read-onlyrequired

search\_results\[\].​location.​osm\_locations\[\].​name _string_ _<= 255 characters_ required

search\_results\[\].​location.​osm\_locations\[\].​place\_type _string_ _(Type)_ _<= 255 characters_ required

search\_results\[\].​finance\_info _object_ read-onlyrequired

Serializer for the OrganizationFinanceInfo model.

-

search\_results\[\].​finance\_info.​revenue _integer or null_ _(int64)_ _\[ 0 .. 9223372036854776000 \]_

search\_results\[\].​linkedin\_info _object_ read-onlyrequired

Serializer for the OrganizationLinkedinInfo model.

-

search\_results\[\].​linkedin\_info.​public\_identifier _string or null_ _<= 255 characters_

search\_results\[\].​linkedin\_info.​industry _object_ read-onlyrequired

Serializer for the LinkedinIndustry document.

-

search\_results\[\].​linkedin\_info.​industry.​id _integer_ read-onlyrequired

search\_results\[\].​linkedin\_info.​industry.​name _string_ _<= 255 characters_ required

search\_results\[\].​linkedin\_info.​public\_profile\_url _string or null_ read-onlyrequired

Get LinkedIn public profile URL.

search\_results\[\].​addresses _Array of objects_ _(OrganizationAddress)_ read-onlyrequired

-

search\_results\[\].​addresses\[\].​street\_number _string or null_ _<= 255 characters_

search\_results\[\].​addresses\[\].​street\_name _string or null_ _<= 255 characters_

search\_results\[\].​addresses\[\].​city _string or null_ _<= 255 characters_

search\_results\[\].​addresses\[\].​state _string or null_ _(State/County)_ _<= 255 characters_

search\_results\[\].​addresses\[\].​postcode _string or null_ _(Post/Zip-code)_ _<= 64 characters_

search\_results\[\].​addresses\[\].​country _string_ _<= 255 characters_ required

search\_results\[\].​addresses\[\].​summary _string_ required

search\_results\[\].​date\_updated _string_ _(date-time)_ read-onlyrequired

search\_results\[\].​found\_simple\_events _Array of objects_ _(OrganizationSimpleEvent)_ required

Events will be available in case any event field would be used for the search. In results will be available 30 most recent matches.

-

search\_results\[\].​found\_simple\_events\[\].​id _integer_ read-onlyrequired

search\_results\[\].​found\_simple\_events\[\].​source _string_ read-onlyrequired

- `product_hunt` \- Product Hunt
- `form_c_sec_gov` \- Form C sec.gov
- `form_d_sec_gov` \- Form D sec.gov

Enum"product\_hunt""form\_c\_sec\_gov""form\_d\_sec\_gov"

search\_results\[\].​found\_simple\_events\[\].​date\_featured _string_ _(date)_ required

search\_results\[\].​found\_simple\_events\[\].​organization\_id _integer_ read-onlyrequired

search\_results\[\].​found\_simple\_events\[\].​reason _string_ _(ReasonEnum)_ required

- `report_released` \- Report released
- `promoted_on_site` \- Promoted on site

Enum"report\_released""promoted\_on\_site"

search\_results\[\].​found\_simple\_events\[\].​url _string_ _(uri)_ _<= 255 characters_ required

search\_results\[\].​found\_funding\_events _Array of objects_ _(OrganizationFundingEvent)_ required

Events will be available in case any event field would be used for the search. In results will be available 30 most recent matches.

-

search\_results\[\].​found\_funding\_events\[\].​id _integer_ read-onlyrequired

search\_results\[\].​found\_funding\_events\[\].​source _string_ read-onlyrequired

- `crunchbase` \- Crunchbase

Value"crunchbase"

search\_results\[\].​found\_funding\_events\[\].​date\_featured _string_ _(date)_ required

search\_results\[\].​found\_funding\_events\[\].​organization\_id _integer_ read-onlyrequired

search\_results\[\].​found\_funding\_events\[\].​funding\_type _string_ _<= 255 characters_ required

search\_results\[\].​found\_funding\_events\[\].​funding\_total _integer_ _(int64)_ _\[ 0 .. 9223372036854776000 \]_ required

search\_results\[\].​found\_job\_post\_events _Array of objects_ _(OrganizationJobPostEvent)_ required

Events will be available in case any event field would be used for the search. In results will be available 30 most recent matches.

-

search\_results\[\].​found\_job\_post\_events\[\].​id _integer_ read-onlyrequired

search\_results\[\].​found\_job\_post\_events\[\].​source _string_ read-onlyrequired

- `indeed` \- Indeed
- `linkedin` \- LinkedIn
- `angellist` \- AngelList

Enum"indeed""linkedin""angellist"

search\_results\[\].​found\_job\_post\_events\[\].​date\_featured _string_ _(date)_ required

search\_results\[\].​found\_job\_post\_events\[\].​organization\_id _integer_ read-onlyrequired

search\_results\[\].​found\_job\_post\_events\[\].​source\_id _string_ _<= 65 characters_ required

search\_results\[\].​found\_job\_post\_events\[\].​url _string_ _(uri)_ _<= 510 characters_ required

search\_results\[\].​found\_job\_post\_events\[\].​title _string_ _<= 255 characters_ required

search\_results\[\].​found\_job\_post\_events\[\].​is\_remote _boolean_ _(Is remote?)_ required

search\_results\[\].​found\_job\_post\_events\[\].​is\_active _boolean_ _(Is active?)_ required

total\_search\_results _integer_ _>= 0_ required

Response

1. 200

application/json

```
{
  "search_results": [\
    { … }\
  ],
  "total_search_results": 0
}
```

---

## API Reference — People

_Source: https://docs.forager.ai/openapi/people_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Personal emails lookup

###### Request

The Person Personal Emails Lookup endpoint retrieves personal email addresses associated with an individual in the Forager dataset. It allows you to input identifying information (such as Linkedin handle or Forager ID) and returns available personal contact emails. Personal emails may include both free webmail addresses (e.g., Gmail, Yahoo) and custom domains that look like company domains but are used for personal purposes. For example, if a user registers for services like LinkedIn with a custom domain for personal use, that email will appear in personal searches.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Body
application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

person\_id _integer_

linkedin\_public\_identifier _string_

LinkedIn organization "Public identifier/Slug/ID" - "linkedin.com/in/!slug!/".

post

/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

- https://api-v2.forager.ai/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

curl

application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

```
curl -i -X POST \
  'https://api-v2.forager.ai/api/{account_id}/datastorage/person_contacts_lookup/personal_emails/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE' \
  -d '{
    "person_id": 0,
    "linkedin_public_identifier": "string"
  }'
```

Try it

###### Responses

1. 200

Bodyapplication/jsonArray \[\
\
email _string_ _(email)_ read-onlyrequired\
\
email\_type _string_ read-onlyrequired\
\
validation\_status _string_ read-onlyrequired\
\
- `valid` \- Valid\
- `risky` \- Risky\
- `invalid` \- Invalid\
- `unknown` \- Unknown\
\
Enum"valid""risky""invalid""unknown"\
\
\]

Response

1. 200

application/json

```
[\
  {\
    "email": "user@example.com",\
    "email_type": "string",\
    "validation_status": "valid"\
  }\
]
```

---

## API Reference — People (Personal Emails detail)

_Source: https://docs.forager.ai/openapi/people/datastorage_person_contacts_lookup_personal_emails_create_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Personal emails lookup

###### Request

The Person Personal Emails Lookup endpoint retrieves personal email addresses associated with an individual in the Forager dataset. It allows you to input identifying information (such as Linkedin handle or Forager ID) and returns available personal contact emails. Personal emails may include both free webmail addresses (e.g., Gmail, Yahoo) and custom domains that look like company domains but are used for personal purposes. For example, if a user registers for services like LinkedIn with a custom domain for personal use, that email will appear in personal searches.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Body
application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

person\_id _integer_

linkedin\_public\_identifier _string_

LinkedIn organization "Public identifier/Slug/ID" - "linkedin.com/in/!slug!/".

post

/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

- https://api-v2.forager.ai/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

curl

application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

```
curl -i -X POST \
  'https://api-v2.forager.ai/api/{account_id}/datastorage/person_contacts_lookup/personal_emails/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE' \
  -d '{
    "person_id": 0,
    "linkedin_public_identifier": "string"
  }'
```

Try it

###### Responses

1. 200

Bodyapplication/jsonArray \[\
\
email _string_ _(email)_ read-onlyrequired\
\
email\_type _string_ read-onlyrequired\
\
validation\_status _string_ read-onlyrequired\
\
- `valid` \- Valid\
- `risky` \- Risky\
- `invalid` \- Invalid\
- `unknown` \- Unknown\
\
Enum"valid""risky""invalid""unknown"\
\
\]

Response

1. 200

application/json

```
[\
  {\
    "email": "user@example.com",\
    "email_type": "string",\
    "validation_status": "valid"\
  }\
]
```

---

## API Reference — People (Phone Numbers detail)

_Source: https://docs.forager.ai/openapi/people/datastorage_person_contacts_lookup_phone_numbers_create_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Personal emails lookup

###### Request

The Person Personal Emails Lookup endpoint retrieves personal email addresses associated with an individual in the Forager dataset. It allows you to input identifying information (such as Linkedin handle or Forager ID) and returns available personal contact emails. Personal emails may include both free webmail addresses (e.g., Gmail, Yahoo) and custom domains that look like company domains but are used for personal purposes. For example, if a user registers for services like LinkedIn with a custom domain for personal use, that email will appear in personal searches.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Body
application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

person\_id _integer_

linkedin\_public\_identifier _string_

LinkedIn organization "Public identifier/Slug/ID" - "linkedin.com/in/!slug!/".

post

/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

- https://api-v2.forager.ai/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

curl

application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

```
curl -i -X POST \
  'https://api-v2.forager.ai/api/{account_id}/datastorage/person_contacts_lookup/personal_emails/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE' \
  -d '{
    "person_id": 0,
    "linkedin_public_identifier": "string"
  }'
```

Try it

###### Responses

1. 200

Bodyapplication/jsonArray \[\
\
email _string_ _(email)_ read-onlyrequired\
\
email\_type _string_ read-onlyrequired\
\
validation\_status _string_ read-onlyrequired\
\
- `valid` \- Valid\
- `risky` \- Risky\
- `invalid` \- Invalid\
- `unknown` \- Unknown\
\
Enum"valid""risky""invalid""unknown"\
\
\]

Response

1. 200

application/json

```
[\
  {\
    "email": "user@example.com",\
    "email_type": "string",\
    "validation_status": "valid"\
  }\
]
```

---

## API Reference — People (Reverse lookup by phone detail)

_Source: https://docs.forager.ai/openapi/people/datastorage_person_detail_reverse_lookup_by_phone_number_create_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Personal emails lookup

###### Request

The Person Personal Emails Lookup endpoint retrieves personal email addresses associated with an individual in the Forager dataset. It allows you to input identifying information (such as Linkedin handle or Forager ID) and returns available personal contact emails. Personal emails may include both free webmail addresses (e.g., Gmail, Yahoo) and custom domains that look like company domains but are used for personal purposes. For example, if a user registers for services like LinkedIn with a custom domain for personal use, that email will appear in personal searches.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Body
application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

person\_id _integer_

linkedin\_public\_identifier _string_

LinkedIn organization "Public identifier/Slug/ID" - "linkedin.com/in/!slug!/".

post

/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

- https://api-v2.forager.ai/api/{account\_id}/datastorage/person\_contacts\_lookup/personal\_emails/

curl

application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

```
curl -i -X POST \
  'https://api-v2.forager.ai/api/{account_id}/datastorage/person_contacts_lookup/personal_emails/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE' \
  -d '{
    "person_id": 0,
    "linkedin_public_identifier": "string"
  }'
```

Try it

###### Responses

1. 200

Bodyapplication/jsonArray \[\
\
email _string_ _(email)_ read-onlyrequired\
\
email\_type _string_ read-onlyrequired\
\
validation\_status _string_ read-onlyrequired\
\
- `valid` \- Valid\
- `risky` \- Risky\
- `invalid` \- Invalid\
- `unknown` \- Unknown\
\
Enum"valid""risky""invalid""unknown"\
\
\]

Response

1. 200

application/json

```
[\
  {\
    "email": "user@example.com",\
    "email_type": "string",\
    "validation_status": "valid"\
  }\
]
```

---

## API Reference — Websites

_Source: https://docs.forager.ai/openapi/websites_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Websites

#### Website Details Lookup

###### Request

The Website Details Lookup endpoint retrieves detailed information about a specific website, including its domain, web rank, traffic, and associated web technologies. This API is useful for analyzing website performance, understanding technology stack, and integrating website data into your applications.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Body
application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

domain _string_

organization\_id _integer_

organization\_linkedin\_public\_identifier _string_

post

/api/{account\_id}/datastorage/website\_detail\_lookup/

- https://api-v2.forager.ai/api/{account\_id}/datastorage/website\_detail\_lookup/

curl

application/json

- application/json
- application/x-www-form-urlencoded
- multipart/form-data

```
curl -i -X POST \
  'https://api-v2.forager.ai/api/{account_id}/datastorage/website_detail_lookup/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE' \
  -d '{
    "domain": "string",
    "organization_id": 0,
    "organization_linkedin_public_identifier": "string"
  }'
```

Try it

###### Responses

1. 200

Expand all

Bodyapplication/json

id _integer_ read-onlyrequired

domain _string_ _(uri)_ _<= 200 characters_ required

tranco\_rank _integer or null_ _\[ 0 .. 2147483647 \]_

The Tranco three month average traffic rank

similarweb\_rank _integer or null_ _\[ 0 .. 2147483647 \]_

similarweb\_traffic _integer or null_ _(int64)_ _\[ 0 .. 9223372036854776000 \]_

website\_technologies _Array of objects_ _(WebSiteTechnology)_ read-onlyrequired

-

website\_technologies\[\].​web\_technology\_id _integer_ read-onlyrequired

website\_technologies\[\].​is\_active _boolean_ _(Is active?)_

website\_technologies\[\].​name _string_ read-onlyrequired

Get WebTechnology name.

Response

1. 200

application/json

```
{
  "id": 0,
  "domain": "http://example.com",
  "tranco_rank": 2147483647,
  "similarweb_rank": 2147483647,
  "similarweb_traffic": 9223372036854776000,
  "website_technologies": [\
    { … }\
  ]
}
```

---

## API Reference — Users

_Source: https://docs.forager.ai/openapi/users_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Websites

#### Users

#### Credit Balance Change Log

###### Request

The Credit Balance Change Log endpoint provides a list of all credit balance change logs related to the current subscription. It returns a list of credit balance change logs, including the change type, change sum, and change data. This endpoint is useful for tracking and analyzing credit consumption patterns, monitoring usage, and ensuring proper subscription management.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Query

date\_created\_end _string_ _(date-time)_

date\_created\_start _string_ _(date-time)_

page _integer_

A page number within the paginated result set.

get

/api/{account\_id}/subscriptions/balance\_change\_logs/

- https://api-v2.forager.ai/api/{account\_id}/subscriptions/balance\_change\_logs/

curl

```
curl -i -X GET \
  'https://api-v2.forager.ai/api/{account_id}/subscriptions/balance_change_logs/?date_created_end=2019-08-24T14%3A15%3A22Z&date_created_start=2019-08-24T14%3A15%3A22Z&page=0' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE'
```

Try it

###### Responses

1. 200

Expand all

Bodyapplication/json

count _integer_

Example:15

next _integer or null_

Example:2

previous _integer or null_

Example:null

results _Array of objects_ _(CreditsBalanceChangeLog)_

+Show 5 array properties

Response

1. 200

application/json

```
{
  "count": 15,
  "next": 2,
  "previous": null,
  "results": [\
    { … }\
  ]
}
```

---

## API Reference — Users (Create API Key)

_Source: https://docs.forager.ai/openapi/users/api_keys_create_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Websites

#### Users

#### Credit Balance Change Log

###### Request

The Credit Balance Change Log endpoint provides a list of all credit balance change logs related to the current subscription. It returns a list of credit balance change logs, including the change type, change sum, and change data. This endpoint is useful for tracking and analyzing credit consumption patterns, monitoring usage, and ensuring proper subscription management.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Query

date\_created\_end _string_ _(date-time)_

date\_created\_start _string_ _(date-time)_

page _integer_

A page number within the paginated result set.

get

/api/{account\_id}/subscriptions/balance\_change\_logs/

- https://api-v2.forager.ai/api/{account\_id}/subscriptions/balance\_change\_logs/

curl

```
curl -i -X GET \
  'https://api-v2.forager.ai/api/{account_id}/subscriptions/balance_change_logs/?date_created_end=2019-08-24T14%3A15%3A22Z&date_created_start=2019-08-24T14%3A15%3A22Z&page=0' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE'
```

Try it

###### Responses

1. 200

Expand all

Bodyapplication/json

count _integer_

Example:15

next _integer or null_

Example:2

previous _integer or null_

Example:null

results _Array of objects_ _(CreditsBalanceChangeLog)_

+Show 5 array properties

Response

1. 200

application/json

```
{
  "count": 15,
  "next": 2,
  "previous": null,
  "results": [\
    { … }\
  ]
}
```

---

## API Reference — Users (Delete API Key)

_Source: https://docs.forager.ai/openapi/users/api_keys_destroy_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Websites

#### Users

#### Credit Balance Change Log

###### Request

The Credit Balance Change Log endpoint provides a list of all credit balance change logs related to the current subscription. It returns a list of credit balance change logs, including the change type, change sum, and change data. This endpoint is useful for tracking and analyzing credit consumption patterns, monitoring usage, and ensuring proper subscription management.

SecurityView security details

Api-Key

Path

account\_id _integer_ required

Query

date\_created\_end _string_ _(date-time)_

date\_created\_start _string_ _(date-time)_

page _integer_

A page number within the paginated result set.

get

/api/{account\_id}/subscriptions/balance\_change\_logs/

- https://api-v2.forager.ai/api/{account\_id}/subscriptions/balance\_change\_logs/

curl

```
curl -i -X GET \
  'https://api-v2.forager.ai/api/{account_id}/subscriptions/balance_change_logs/?date_created_end=2019-08-24T14%3A15%3A22Z&date_created_start=2019-08-24T14%3A15%3A22Z&page=0' \
  -H 'X-API-KEY: YOUR_API_KEY_HERE'
```

Try it

###### Responses

1. 200

Expand all

Bodyapplication/json

count _integer_

Example:15

next _integer or null_

Example:2

previous _integer or null_

Example:null

results _Array of objects_ _(CreditsBalanceChangeLog)_

+Show 5 array properties

Response

1. 200

application/json

```
{
  "count": 15,
  "next": 2,
  "previous": null,
  "results": [\
    { … }\
  ]
}
```

---

## API Reference — Autocomplete

_Source: https://docs.forager.ai/openapi/autocomplete_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Websites

#### Users

#### Autocomplete

#### Industries lookup

###### Request

Industries objects lookup.

Query

q _string_ required

Industry name.

page _integer_

get

/api/datastorage/autocomplete/industries/

- https://api-v2.forager.ai/api/datastorage/autocomplete/industries/

curl

```
curl -i -X GET \
  'https://api-v2.forager.ai/api/datastorage/autocomplete/industries/?q=string&page=0'
```

Try it

###### Responses

1. 200

Expand all

Valid response.

Bodyapplication/json

results _Array of objects_

+Show 2 array properties

pagination _object_

+Show property

Response

1. 200

application/json

```
{
  "results": [\
    { … }\
  ],
  "pagination": {
    "more": true
  }
}
```

---

## API Reference — Autocomplete (Web technologies detail)

_Source: https://docs.forager.ai/openapi/autocomplete/v1_web_technology_lookup_

# Forager public API (1.0.0)    

Forager public API endpoints documentation

Download OpenAPI description

[openapi.json](https://docs.forager.ai/_bundle/openapi.json?download)

[openapi.yaml](https://docs.forager.ai/_bundle/openapi.yaml?download)

Languages

curlJavaScriptNode.jsPythonJavaC#PHPGo

- Ruby
- R
- Payload

Servers

https://api-v2.forager.ai

#### Job Posts

#### Organizations

#### People

#### Websites

#### Users

#### Autocomplete

#### Industries lookup

###### Request

Industries objects lookup.

Query

q _string_ required

Industry name.

page _integer_

get

/api/datastorage/autocomplete/industries/

- https://api-v2.forager.ai/api/datastorage/autocomplete/industries/

curl

```
curl -i -X GET \
  'https://api-v2.forager.ai/api/datastorage/autocomplete/industries/?q=string&page=0'
```

Try it

###### Responses

1. 200

Expand all

Valid response.

Bodyapplication/json

results _Array of objects_

+Show 2 array properties

pagination _object_

+Show property

Response

1. 200

application/json

```
{
  "results": [\
    { … }\
  ],
  "pagination": {
    "more": true
  }
}
```

---

## Data Feeds V2 — Overview

_Source: https://docs.forager.ai/data-license/v2/data-feed-overview_

### Data Feed V2 Overview

We provide bulk people, company and job datasets through an **annual license**. Whether you need our entire dataset or a custom subset, we can tailor a solution to meet your specific needs. To learn more, speak with one of our **[Data Consultants](https://calendly.com/d/46p-2vr-83n)**.

* * *

#### Data Feed Products

We offer three continuously refreshed datasets designed for production-grade analytics, enrichment, and AI-driven workflows.

##### Person Data Feed

**[Schema](https://docs.forager.ai/data-license/v2/schema#person-data-feed)**

~800M profiles refreshed on a rolling basis

###### What's included

A comprehensive professional profile for each person, including identity attributes, location, current and historical employment, titles and roles, education, skills, certifications, and organization relationships — all normalized into a consistent, query-ready schema.

###### Common use cases

- Bulk enrichment of CRM, lead, or contact records
- Workforce and talent analytics
- Training or powering AI models that require structured person data
- Segmentation, matching, and identity resolution across systems

##### Organization Data Feed

**[Schema](https://docs.forager.ai/data-license/v2/schema#organization-data-feed)**

~61M company profiles

###### What's included

Standardized firmographic and company-level data including organization identifiers, domains, industries, locations, employee size ranges, and other attributes needed to model companies at scale.

###### Common use cases

- Account and company enrichment
- ICP expansion and TAM modeling
- Firmographic segmentation and reporting
- Creating a canonical company layer across internal systems

##### Job Post Data Feed

**[Schema](https://docs.forager.ai/data-license/v2/schema#job-post-data-feed)**

~16M job posts collected per month on average

###### What's included

Structured job listings with titles, associated companies, locations, posting dates, sources, and activity metadata — collected and normalized across major online sources.

###### Common use cases

- Hiring intent and demand signals
- Labor-market and trend analysis
- Competitor hiring and team expansion tracking
- Enhancing person and company profiles with real-time opportunity data

* * *

#### Delivery Options

We support two primary delivery models depending on how your data team prefers to consume data.

##### Snowflake Private Listing

We publish the data directly into your Snowflake account as a shared, continuously refreshed table. Your team can query, join, and transform the data just like any internal dataset.

**[Documentation](https://docs.forager.ai/data-license/v2/data-delivery-snowflake#how-to-access-a-private-listing)**

##### Cloud Storage (S3, S3-compatible, or GCS)

We can deliver daily, weekly, or monthly drops to your own bucket. Data is provided as compressed, partitioned NDJSON files for efficient ingestion into data lakes, warehouses, and pipelines.

**Documentation:** [S3](https://docs.forager.ai/data-license/v2/data-delivery-s3) \| [GCS](https://docs.forager.ai/data-license/v2/data-delivery-gcs)

#### Learn more

- [Output Data File Details](https://docs.forager.ai/data-license/v2/output-data-file-details)
- [Data Feed Schema's](https://docs.forager.ai/data-license/v2/schema)
- [Migrate from Forager Data Feeds V1 -> V2](https://docs.forager.ai/data-license/v2/migrate-from-v1-v2)
- Delivery methods
  - [Snowflake](https://docs.forager.ai/data-license/v2/data-delivery-snowflake)
  - [Amazon S3](https://docs.forager.ai/data-license/v2/data-delivery-s3)
  - [Google Cloud Storage](https://docs.forager.ai/data-license/v2/data-delivery-gcs)
  - Azure Blob (comming soon)

* * *

#### Why Choose Forager.ai?

✅ **Fastest Refresh Rate**: Stay ahead with data updated **every 2-3 weeks**.

🌍 **Global Reach**: Access to **millions of verified profiles worldwide**.

💰 **Cost-Effective**: Unlimited access at a **competitive price**.

🔍 **Tailored Solutions**: Custom datasets to fit your **unique requirements**.

💡 **Exceptional Support**: Dedicated **customer success team** to ensure your success.

* * *

#### Get Started

Ready to explore how **Forager.ai** can power your business? **[Contact us today](https://calendly.com/d/46p-2vr-83n)** to speak with a **Data Consultant** and tailor a solution for your needs.

---

## Data Feeds V2 — Schema

_Source: https://docs.forager.ai/data-license/v2/schema_

### Schema

Below is our data schema for our current data feed products.

> **Important**
>
> The below schema objects repreent the JSON object in the `serialized_data` property of any given data feed.

#### Person Data Feed

Version: **2.0.4** (latest)

forager\_id _integer_ _(Forager Id)_ required

linkedin\_id _integer_ _(Linkedin Numeric Id)_

date\_updated _string_ _(date-time)_ _(Date Updated)_ required

first\_name _string_ _(First Name)_

last\_name _string_ _(Last Name)_

headline _string_ _(Headline)_

description _string_ _(Description)_

skills _Array of strings_ _(Skills)_

Default\[\]

country _string_ _(Country)_

area _string_ _(Area)_

city _string_ _(City)_

location _string_ _(Location)_

locations _Array of objects_ _(Locations)_

Default\[\]

+Show 2 array properties

linkedin\_url _string_ _(Linkedin Url)_

linkedin\_slug _string_ _(Linkedin Slug)_

industry _string_ _(Industry)_

number\_of\_connections _integer_ _(Number of Linkedin Connections)_

number\_of\_followers _integer_ _(Number of Linkedin Followers)_

linkedin\_country _string_ _(Linkedin Country)_

linkedin\_area _string_ _(Linkedin Area)_

educations _Array of objects_ _(Educations)_

Default\[\]

+Show 14 array properties

roles _Array of objects_ _(Roles)_

Default\[\]

+Show 16 array properties

certifications _Array of objects_ _(Certifications)_

Default\[\]

+Show 12 array properties

organizations _Array of objects_ _(Organizations)_

Default\[\]

+Show 7 array properties

projects _Array of objects_ _(Projects)_

Default\[\]

+Show 10 array properties

volunteering _Array of objects_ _(Volunteering)_

Default\[\]

+Show 7 array properties

courses _Array of objects_ _(Courses)_

Default\[\]

+Show 5 array properties

honors _Array of objects_ _(Honors)_

Default\[\]

+Show 7 array properties

languages _Array of objects_ _(Languages)_

Default\[\]

+Show 2 array properties

patents _Array of objects_ _(Patents)_

Default\[\]

+Show 11 array properties

publications _Array of objects_ _(Publications)_

Default\[\]

+Show 8 array properties

test\_scores _Array of objects_ _(Test Scores)_

Default\[\]

+Show 5 array properties

is\_available _boolean_ _(Is Available)_

photo _string_ _(Photo)_

volunteer\_causes _Array of strings_ _(Volunteer Causes)_

Default\[\]

Version: **2.0.3**

forager\_id _integer_ _(Forager Id)_ required

linkedin\_id _integer_ _(Linkedin Numeric Id)_

date\_updated _string_ _(date-time)_ _(Date Updated)_ required

first\_name _string_ _(First Name)_

last\_name _string_ _(Last Name)_

headline _string_ _(Headline)_

description _string_ _(Description)_

skills _Array of strings_ _(Skills)_

Default\[\]

country _string_ _(Country)_

area _string_ _(Area)_

city _string_ _(City)_

location _string_ _(Location)_

locations _Array of objects_ _(Locations)_

Default\[\]

+Show 2 array properties

linkedin\_url _string_ _(Linkedin Url)_

linkedin\_slug _string_ _(Linkedin Slug)_

industry _string_ _(Industry)_

linkedin\_country _string_ _(Linkedin Country)_

linkedin\_area _string_ _(Linkedin Area)_

educations _Array of objects_ _(Educations)_

Default\[\]

+Show 14 array properties

roles _Array of objects_ _(Roles)_

Default\[\]

+Show 16 array properties

certifications _Array of objects_ _(Certifications)_

Default\[\]

+Show 12 array properties

organizations _Array of objects_ _(Organizations)_

Default\[\]

+Show 7 array properties

projects _Array of objects_ _(Projects)_

Default\[\]

+Show 10 array properties

volunteering _Array of objects_ _(Volunteering)_

Default\[\]

+Show 7 array properties

courses _Array of objects_ _(Courses)_

Default\[\]

+Show 5 array properties

honors _Array of objects_ _(Honors)_

Default\[\]

+Show 7 array properties

languages _Array of objects_ _(Languages)_

Default\[\]

+Show 2 array properties

patents _Array of objects_ _(Patents)_

Default\[\]

+Show 11 array properties

publications _Array of objects_ _(Publications)_

Default\[\]

+Show 8 array properties

test\_scores _Array of objects_ _(Test Scores)_

Default\[\]

+Show 5 array properties

is\_available _boolean_ _(Is Available)_

photo _string_ _(Photo)_

volunteer\_causes _Array of strings_ _(Volunteer Causes)_

Default\[\]

Version: **2.0.2**

forager\_id _integer_ _(Forager Id)_ required

linkedin\_id _integer_ _(Linkedin Numeric Id)_

date\_updated _string_ _(date-time)_ _(Date Updated)_ required

first\_name _string_ _(First Name)_

last\_name _string_ _(Last Name)_

headline _string_ _(Headline)_

description _string_ _(Description)_

skills _Array of strings_ _(Skills)_

Default\[\]

country _string_ _(Country)_

area _string_ _(Area)_

city _string_ _(City)_

location _string_ _(Location)_

locations _Array of objects_ _(Locations)_

Default\[\]

+Show 2 array properties

linkedin\_url _string_ _(Linkedin Url)_

linkedin\_slug _string_ _(Linkedin Slug)_

industry _string_ _(Industry)_

linkedin\_country _string_ _(Linkedin Country)_

linkedin\_area _string_ _(Linkedin Area)_

educations _Array of objects_ _(Educations)_

Default\[\]

+Show 14 array properties

roles _Array of objects_ _(Roles)_

Default\[\]

+Show 15 array properties

certifications _Array of objects_ _(Certifications)_

Default\[\]

+Show 12 array properties

organizations _Array of objects_ _(Organizations)_

Default\[\]

+Show 7 array properties

projects _Array of objects_ _(Projects)_

Default\[\]

+Show 10 array properties

volunteering _Array of objects_ _(Volunteering)_

Default\[\]

+Show 7 array properties

courses _Array of objects_ _(Courses)_

Default\[\]

+Show 5 array properties

honors _Array of objects_ _(Honors)_

Default\[\]

+Show 7 array properties

languages _Array of objects_ _(Languages)_

Default\[\]

+Show 2 array properties

patents _Array of objects_ _(Patents)_

Default\[\]

+Show 11 array properties

publications _Array of objects_ _(Publications)_

Default\[\]

+Show 8 array properties

test\_scores _Array of objects_ _(Test Scores)_

Default\[\]

+Show 5 array properties

is\_available _boolean_ _(Is Available)_

photo _string_ _(Photo)_

volunteer\_causes _Array of strings_ _(Volunteer Causes)_

Default\[\]

Version: **2.0.1**

forager\_id _integer_ _(Forager Id)_ required

linkedin\_id _integer_ _(Linkedin Numeric Id)_

date\_updated _string_ _(date-time)_ _(Date Updated)_ required

first\_name _string_ _(First Name)_

last\_name _string_ _(Last Name)_

headline _string_ _(Headline)_

description _string_ _(Description)_

skills _Array of strings_ _(Skills)_

Default\[\]

country _string_ _(Country)_

area _string_ _(Area)_

city _string_ _(City)_

location _string_ _(Location)_

locations _Array of objects_ _(Locations)_

Default\[\]

+Show 2 array properties

linkedin\_url _string_ _(Linkedin Url)_

linkedin\_slug _string_ _(Linkedin Slug)_

industry _string_ _(Industry)_

linkedin\_country _string_ _(Linkedin Country)_

linkedin\_area _string_ _(Linkedin Area)_

educations _Array of objects_ _(Educations)_

Default\[\]

+Show 12 array properties

roles _Array of objects_ _(Roles)_

Default\[\]

+Show 13 array properties

certifications _Array of objects_ _(Certifications)_

Default\[\]

+Show 10 array properties

organizations _Array of objects_ _(Organizations)_

Default\[\]

+Show 7 array properties

projects _Array of objects_ _(Projects)_

Default\[\]

+Show 10 array properties

volunteering _Array of objects_ _(Volunteering)_

Default\[\]

+Show 7 array properties

courses _Array of objects_ _(Courses)_

Default\[\]

+Show 5 array properties

honors _Array of objects_ _(Honors)_

Default\[\]

+Show 7 array properties

languages _Array of objects_ _(Languages)_

Default\[\]

+Show 2 array properties

patents _Array of objects_ _(Patents)_

Default\[\]

+Show 11 array properties

publications _Array of objects_ _(Publications)_

Default\[\]

+Show 8 array properties

test\_scores _Array of objects_ _(Test Scores)_

Default\[\]

+Show 5 array properties

photo _string_ _(Photo)_

volunteer\_causes _Array of strings_ _(Volunteer Causes)_

Version: **2.0.0**

forager\_id _integer_ _(Forager Id)_ required

date\_updated _string_ _(date-time)_ _(Date Updated)_ required

first\_name _string_ _(First Name)_

last\_name _string_ _(Last Name)_

headline _string_ _(Headline)_

description _string_ _(Description)_

skills _Array of strings_ _(Skills)_

Default\[\]

country _string_ _(Country)_

area _string_ _(Area)_

city _string_ _(City)_

location _string_ _(Location)_

locations _Array of objects_ _(Locations)_

Default\[\]

+Show 2 array properties

linkedin\_url _string_ _(Linkedin Url)_

linkedin\_slug _string_ _(Linkedin Slug)_

industry _string_ _(Industry)_

linkedin\_country _string_ _(Linkedin Country)_

linkedin\_area _string_ _(Linkedin Area)_

educations _Array of objects_ _(Educations)_

Default\[\]

+Show 12 array properties

roles _Array of objects_ _(Roles)_

Default\[\]

+Show 12 array properties

certifications _Array of objects_ _(Certifications)_

Default\[\]

+Show 10 array properties

organizations _Array of objects_ _(Organizations)_

Default\[\]

+Show 6 array properties

projects _Array of objects_ _(Projects)_

Default\[\]

+Show 10 array properties

volunteering _Array of objects_ _(Volunteering)_

Default\[\]

+Show 7 array properties

courses _Array of objects_ _(Courses)_

Default\[\]

+Show 5 array properties

honors _Array of objects_ _(Honors)_

Default\[\]

+Show 7 array properties

languages _Array of objects_ _(Languages)_

Default\[\]

+Show 2 array properties

patents _Array of objects_ _(Patents)_

Default\[\]

+Show 11 array properties

publications _Array of objects_ _(Publications)_

Default\[\]

+Show 8 array properties

test\_scores _Array of objects_ _(Test Scores)_

Default\[\]

+Show 5 array properties

photo _string_ _(Photo)_

volunteer\_causes _Array of strings_ _(Volunteer Causes)_

#### Organization Data Feed

Version: **2.0.0** (latest)

forager\_id _integer_ required

date\_updated _string_ _(date-time)_ required

name _string or null_ required

domain _string or null_

website _string or null_

logo\_url _string or null_ required

description _string or null_ required

founded\_date _string or null_ _(date)_

employees\_number _number or null_

employees\_range _string or null_

keywords _Array of strings_

addresses _Array of objects_ _(Address)_

+Show 7 array properties

funding\_rounds _Array of objects_ _(FundingRound)_

+Show 3 array properties

technologies _Array of strings_

domain\_rank _integer or null_

domain\_traffic _integer or null_

domain\_tranco\_rank _integer or null_

country _string or null_

area _string or null_

city _string or null_

location _string or null_

locations _Array of objects_ _(LocationEntry)_

+Show 2 array properties

linkedin\_url _string or null_

linkedin\_slug _string or null_

industry _string or null_

linkedin\_id _integer or null_

#### Job Post Data Feed

Version: **2.0.0** (latest)

forager\_id _integer_ required

source\_id _string or null_ required

date\_updated _string or null_ _(date)_ required

date\_featured _string or null_ _(date)_ required

url _string or null_ required

title _string or null_ required

description _string or null_ required

is\_remote _boolean_ required

is\_active _boolean_ required

location _string or null_

parsed\_location _Array of objects_ _(ParsedLocation)_

+Show 2 array properties

salary\_details _string or null_

organization\_forager\_id _integer or null_ required

organization\_name _string or null_ required

organization\_domain _string or null_

organization\_linkedin\_url _string or null_ required

### Data Samples

[Find data samples here](https://docs.forager.ai/data-license/v2/output-data-file-details#example-file)

---

## Data Feeds V2 — Delivery via S3

_Source: https://docs.forager.ai/data-license/v2/data-delivery-s3_

### Data Delivery Using S3

Our preferred mode of data delivery is through **Amazon AWS S3**.

* * *

#### How to Set Up S3 Delivery

To receive data via **S3**, follow these steps:

##### 1\. Sign Into AWS

Log into the **AWS S3 console**.

##### 2\. Create an S3 Bucket

- **Create a new bucket** for deliveries (e.g., `s3://YOURCOMPANY-data-deliveries`).

##### 3\. Configure Bucket Policy

To allow **Forager.ai** to send data to your S3 bucket, you will need to apply the following **bucket policy**:

###### 📌 **Bucket Policy (Replace `YOURCOMPANY-data-deliveries` with your actual bucket name)**

```
{
    "Version": "2012-10-17",
    "Statement": [\
        {\
            "Effect": "Allow",\
            "Action": [\
                "s3:PutObject",\
                "s3:GetObject",\
                "s3:GetObjectVersion",\
                "s3:DeleteObject",\
                "s3:DeleteObjectVersion"\
            ],\
            "Resource": "arn:aws:s3:::<your bucket>/*"\
        },\
        {\
            "Effect": "Allow",\
            "Action": [\
                "s3:ListBucket",\
                "s3:GetBucketLocation"\
            ],\
            "Resource": "arn:aws:s3:::<your bucket>",\
            "Condition": {\
                "StringLike": {\
                    "s3:prefix": [\
                        "*"\
                    ]\
                }\
            }\
        }\
    ]
}
```

##### 4\. Provide AWS Access Keys

Once the bucket is set up, send the following details to Forager.ai:

- AWS Access Key
- AWS Secret Key

Our team will configure the data delivery to send data directly to your S3 bucket.

#### File output paths and file names

Read more about file paths [here](https://docs.forager.ai/data-license/v2/output-data-file-details).

#### Need Help?

📩 For Support: Contact us at support@forager.ai.

---

## Data Feeds V2 — Delivery via Snowflake

_Source: https://docs.forager.ai/data-license/v2/data-delivery-snowflake_

### Data Delivery Using Snowflake

#### How to Request Snowflake Delivery

You can receive delivery through Snowflake by requesting a Forager.ai subscription for our Person Data License. Here's how:

1. Log into your Snowflake account (or sign up for one at [https://app.snowflake.com](https://app.snowflake.com/)).

2. Go to the Snowflake Marketplace page and search for "Forager.ai." Then click the Forager.ai Person Data License.

3. Click **Request Data**

4. Enter the following required information:

   - **Email**
   - **Name**
   - **Title**
   - **Company Name**
   - **Company Website**
   - Describe how you intend to use the data in the **Message** box.
5. Click **Request Data**.

> **Note:** All the above fields are required.

* * *

#### How to Access a Private Listing

To access a private listing that was shared with you, follow these steps:

1. Sign in to Snowflake.
2. Select **Data Products** » **Private Sharing**.
3. On the **Shared with Me** page under **Private Listings**, select the listing you want to access.
4. Click **Get**.

> **📘 Note:** You must use the `ACCOUNTADMIN` role or another role with the `CREATE DATABASE` and `IMPORT SHARE` privileges to access a listing.

* * *

#### Schemas

View our full Snowflake data dictionary **[here](https://docs.forager.ai/data-license/v2/schema)**.

---

## Data Feeds V2 — Migrate v1 → v2

_Source: https://docs.forager.ai/data-license/v2/migrate-from-v1-v2_

### Migration to Forager Datafeeds V2

> **Data feed V1 EOL (end of life) support**
>
> Data feed V1 will no longer be supported as of January 31st. V1 data feed exports will be completely shut down.

#### Summary

We are migrating our underlying data feed database to Snowflake, this will enable you to have access to following to features:

- Access **near realtime crawled data** directly in a Snowflake database shared with your account (updates daily are made in snowflake daily)
- Additional export destinations, we now support sending data feeds to the following destinations:
  - Amazon S3
  - Google Cloud Storage
  - Azure Blob
- **Customizable export job schedules**, we can now define any schedule to export your Forager data feed to your destination. Have data sent to your export destination at any frequency (charges do apply).
- Additional file formats, we now can support the following:
  - JSON (NDJSON format)
  - CSV/TSV
  - Parquet
- Compression can now be applied to your data feed export files using any of the following:
  - Gzip (default)
  - bzip2
  - Brotli
  - Zstandard
- Ability to opt into net new data only. Only export data that has been updated from last export.

#### Schema

View the full OpenAPI schema documentation [here](https://docs.forager.ai/data-license/v2/schema).

#### File paths and names

View new file path and name formats [here](https://docs.forager.ai/data-license/v2/output-data-file-details)

#### Breaking changes:

1. File export compression, all files are now exported using gzip by default, you do have the option to disable this or select from one of the other supported compression types above.
2. JSON export format, all JSON files will now use NDJSON (one JSON object per line), instead of an array of JSON objects. See an example file [here](https://docs.forager.ai/assets/data_0_0_0.d57db7821548feaf629855f6ded1ec65b190fa448a57a88ec27265222c24889c.cdba73be.ndjson).
3. File paths are now restructured to allow schema changes and to easily retrieve updated data only. For example: `/forager_data_feed/<data_feed_id>/<date_created>/<data_feed_type>_<schema_version>/data_<partition_id>.<file_type>.<compression_type>`. See changes [here](https://docs.forager.ai/data-license/v2/output-data-file-details).
4. Properties no longer supported:
01. `background_picture`
02. `is_creator`
03. `is_influencer`
04. `temporary_status`
05. `temporary_emoji_status`
06. `accessibility_hashtags`
07. `accessibility_text`
08. `address`
09. `primary_locale`
10. `supported_locales`

---

## Data Feeds V2 — Output Data File Details

_Source: https://docs.forager.ai/data-license/v2/output-data-file-details_

# Example:
/forager_data_feed/123/2025-10-15/person_1.0.0/data_0_0_1.json.gzip
```

Where the above variables represent:

- `data_feed_id`: A Forager provided data feed ID, provide by our support team.
- `data_feed_type`: Possible options are; `person`, `organization`, or `job`.
- `schema_version`: Forager schema version that represents the versioning of serialized data for data feed type, this will be provided by your customer support rep.
- `date_created`: Date when the export was created, Ex: `2025-10-16`.
- `partition_id`: Partition column values generated when exporting your files, Ex: `0_0_0`, `0_0_1`, etc.
- `file_type`: This will be one of the following options; `json`, `csv`, `tsv`, `parquet`.'
- `compression_type`: This will be one of the following options; `gzip`, `bz2`, `brotli`, `zstd`.

#### Serialized Data Schema

[Schema located here.](https://docs.forager.ai/data-license/v2/schema)

---

## Data Feeds V1 — Overview

_Source: https://docs.forager.ai/data-license/v1/data-license-overview_

### Data License Overview

At **Forager.ai**, we provide bulk people and company datasets through an **annual license**. Whether you need our entire dataset or a custom subset, we can tailor a solution to meet your specific needs. To learn more, speak with one of our **[Data Consultants](https://calendly.com/d/46p-2vr-83n)**.

* * *

#### The Value of a Forager.ai License

##### 1\. On-Premise Data Access

During the license period, you have the right to use the data on your premises in any way, as long as it complies with our **[Terms and Conditions](https://www.forager.ai/terms-conditions)**.

##### 2\. Fastest Refresh Rate in the Industry

We refresh our people and company data **every 2-3 weeks**, ensuring you always have the most up-to-date information. Updated files are delivered within a **maximum range of 2 to 6 weeks**, so your data stays current and actionable.

##### 3\. Unmatched Data Coverage

Our dataset offers **global coverage** with a focus on **accuracy, depth, and relevance**.

##### 4\. Dedicated Customer Success Team

Our Data-feed and API customers receive dedicated support, including:

- **Email support** on weekdays from **9:00 AM – 5:00 PM Eastern Time**, excluding **Federal Holidays**.
- **Expert guidance** to ensure you achieve ROI as quickly as possible.

##### 5\. Unlimited Access at Scale

Unlike search and matching APIs that become costly at scale, **Forager.ai** provides **unlimited access** to high-quality data at a fraction of the price, making it ideal for **large-scale projects**.

##### 6\. Flexible Licensing Options

We allow you to **customize the data** to ensure you only receive—and pay for—the profiles that matter most to your business.

* * *

#### Tailored Delivery Solutions

We offer a variety of delivery options to suit your needs:

- **Cloud Platforms**: Deliveries via **S3, Snowflake**, and more.

* * *

#### Why Choose Forager.ai?

✅ **Fastest Refresh Rate**: Stay ahead with data updated **every 2-3 weeks**.

🌍 **Global Reach**: Access to **millions of verified profiles worldwide**.

💰 **Cost-Effective**: Unlimited access at a **competitive price**.

🔍 **Tailored Solutions**: Custom datasets to fit your **unique requirements**.

💡 **Exceptional Support**: Dedicated **customer success team** to ensure your success.

* * *

#### Get Started

Ready to explore how **Forager.ai** can power your business? **[Contact us today](https://calendly.com/d/46p-2vr-83n)** to speak with a **Data Consultant** and tailor a solution for your needs.

---

## Data Feeds V1 — Schema

_Source: https://docs.forager.ai/data-license/v1/data-license-schema_

### Data Dictionary

Below is our data schema for people and companies with available fields.

#### People Data

| Field Name | Data Type |
| --- | --- |
| ACCESSIBILITY\_HASHTAGS | VARCHAR |
| ACCESSIBILITY\_TEXT | VARCHAR |
| ADDRESS | VARCHAR |
| AREA | VARCHAR |
| BACKGROUND\_PICTURE | VARCHAR |
| CERTIFICATIONS | ARRAY |
| CITY | VARCHAR |
| COUNTRY | VARCHAR |
| COURSES | ARRAY |
| DATE\_UPDATED | TIMESTAMP\_NTZ |
| DESCRIPTION | VARCHAR |
| EDUCATIONS | ARRAY |
| FIRST\_NAME | VARCHAR |
| FORAGER\_ID | NUMBER |
| HEADLINE | VARCHAR |
| HONORS | ARRAY |
| INDUSTRY | VARCHAR |
| IS\_CREATOR | BOOLEAN |
| IS\_INFLUENCER | BOOLEAN |
| LANGUAGES | ARRAY |
| LAST\_NAME | VARCHAR |
| LINKEDIN\_AREA | VARCHAR |
| LINKEDIN\_COUNTRY | VARCHAR |
| LINKEDIN\_SLUG | VARCHAR |
| LINKEDIN\_URL | VARCHAR |
| LOCATION | VARCHAR |
| LOCATIONS | ARRAY |
| ORGANIZATIONS | ARRAY |
| PATENTS | ARRAY |
| PHOTO | VARCHAR |
| PRIMARY\_LOCALE | OBJECT |
| PROJECTS | ARRAY |
| PUBLICATIONS | ARRAY |
| ROLES | ARRAY |
| SKILLS | ARRAY |
| TEMPORARY\_EMOJI\_STATUS | VARCHAR |
| TEMPORARY\_STATUS | VARCHAR |
| TEST\_SCORES | ARRAY |
| VOLUNTEER\_CAUSES | ARRAY |
| VOLUNTEERINGS | ARRAY |

#### Company Data

| Field Name | Data Type |
| --- | --- |
| ADDRESSES | ARRAY |
| AREA | VARCHAR |
| CITY | VARCHAR |
| COUNTRY | VARCHAR |
| DATE\_UPDATED | TIMESTAMP\_NTZ |
| DESCRIPTION | VARCHAR |
| DOMAIN | VARCHAR |
| DOMAIN\_SIMILARWEB\_RANK | NUMBER |
| DOMAIN\_SIMILARWEB\_TRAFFIC | NUMBER |
| DOMAIN\_TRANCO\_RANK | VARCHAR |
| EMPLOYEES\_NUMBER | NUMBER |
| EMPLOYEES\_RANGE | VARCHAR |
| FORAGER\_ID | NUMBER |
| FOUNDED\_DATE | DATE |
| FUNDING\_ROUNDS | VARCHAR |
| INDUSTRY | VARCHAR |
| KEYWORDS | VARCHAR |
| LINKEDIN\_SLUG | VARCHAR |
| LINKEDIN\_URL | VARCHAR |
| LOCATION | VARCHAR |
| LOCATIONS | ARRAY |
| LOGO\_URL | VARCHAR |
| NAME | VARCHAR |
| TECHNOLOGIES | VARCHAR |
| WEBSITE | VARCHAR |

---

## Data Feeds V1 — Delivery via Snowflake

_Source: https://docs.forager.ai/data-license/v1/data-delivery-snowflake_

### Data Delivery Using Snowflake

#### How to Request Snowflake Delivery

You can receive delivery through Snowflake by requesting a Forager.ai subscription for our Person Data License. Here's how:

1. Log into your Snowflake account (or sign up for one at [https://app.snowflake.com](https://app.snowflake.com/)).

2. Go to the Snowflake Marketplace page and search for "Forager.ai." Then click the Forager.ai Person Data License.

3. Click **Request Data**

4. Enter the following required information:

   - **Email**
   - **Name**
   - **Title**
   - **Company Name**
   - **Company Website**
   - Describe how you intend to use the data in the **Message** box.
5. Click **Request Data**.

> **Note:** All the above fields are required.

* * *

#### How to Access a Private Listing

To access a private listing that was shared with you, follow these steps:

1. Sign in to Snowflake.
2. Select **Data Products** » **Private Sharing**.
3. On the **Shared with Me** page under **Private Listings**, select the listing you want to access.
4. Click **Get**.

> **📘 Note:** You must use the `ACCOUNTADMIN` role or another role with the `CREATE DATABASE` and `IMPORT SHARE` privileges to access a listing.

* * *

#### Tabular Schemas

View our full Snowflake data dictionary **[here](https://docs.forager.ai/data-license/v1/data-license-schema)**.

---
