# CrmCompanyService

A list of all methods in the `CrmCompanyService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description |
| :------------------------------------------------------------ | :---------- |
| [get_company_async](#get_company_async)                       |             |
| [get_edit_company_async](#get_edit_company_async)             |             |
| [put_edit_company_async](#put_edit_company_async)             |             |
| [delete_company_async](#delete_company_async)                 |             |
| [post_company_async](#post_company_async)                     |             |
| [get_edit_company_notes_async](#get_edit_company_notes_async) |             |
| [put_company_notes_async](#put_company_notes_async)           |             |
| [get_company_details_async](#get_company_details_async)       |             |
| [put_company_details_async](#put_company_details_async)       |             |

## get_company_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/company/{companyKey}/full`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| company_key | str  | ✅       |             |

**Return Type**

`Company`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_company.get_company_async(company_key="companyKey")

print(result)
```

## get_edit_company_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/company/{companyKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| company_key | str  | ✅       |             |

**Return Type**

`EditCompany`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_company.get_edit_company_async(company_key="companyKey")

print(result)
```

## put_edit_company_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/company/{companyKey}`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [EditCompany](../models/EditCompany.md) | ❌       | The request body. |
| company_key  | str                                     | ✅       |                   |

**Return Type**

`Company`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditCompany

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditCompany(
    user_key="userKey",
    team_key="teamKey",
    organization="organization",
    subsidiary="subsidiary",
    address={
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "state": "state",
        "zip_code": "zipCode",
        "country": "country",
        "latitude": 8.53,
        "longitude": 4.96,
        "time_zone_key": 5,
        "company": "company"
    },
    investor=False,
    tenant=False,
    agent=True,
    vendor=True,
    prospect=False,
    personal=True,
    phone="phone",
    fax="fax",
    email="email",
    web_site="webSite",
    do_not_call=False,
    do_not_email=True,
    do_not_fax=True,
    do_not_mail=False
)

result = sdk.crm_company.put_edit_company_async(
    request_body=request_body,
    company_key="companyKey"
)

print(result)
```

## delete_company_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/company/{companyKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| company_key | str  | ✅       |             |

**Return Type**

`Company`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_company.delete_company_async(company_key="companyKey")

print(result)
```

## post_company_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/company`

**Parameters**

| Name         | Type                                        | Required | Description       |
| :----------- | :------------------------------------------ | :------- | :---------------- |
| request_body | [CreateCompany](../models/CreateCompany.md) | ❌       | The request body. |

**Return Type**

`Company`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import CreateCompany

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateCompany(
    user_key="userKey",
    team_key="teamKey",
    organization="organization",
    subsidiary="subsidiary",
    address={
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "state": "state",
        "zip_code": "zipCode",
        "country": "country",
        "latitude": 8.53,
        "longitude": 4.96,
        "time_zone_key": 5,
        "company": "company"
    },
    investor=True,
    tenant=True,
    agent=True,
    vendor=True,
    prospect=True,
    personal=False,
    phone="phone",
    fax="fax",
    email="email",
    web_site="webSite",
    do_not_call=False,
    do_not_email=True,
    do_not_fax=True,
    do_not_mail=False,
    object_groups=[
        "objectGroups"
    ]
)

result = sdk.crm_company.post_company_async(request_body=request_body)

print(result)
```

## get_edit_company_notes_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/company/{companyKey}/notes`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| company_key | str  | ✅       |             |

**Return Type**

`EditNotes`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_company.get_edit_company_notes_async(company_key="companyKey")

print(result)
```

## put_company_notes_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/company/{companyKey}/notes`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditNotes](../models/EditNotes.md) | ❌       | The request body. |
| company_key  | str                                 | ✅       |                   |

**Return Type**

`Company`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditNotes

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditNotes(
    notes="notes"
)

result = sdk.crm_company.put_company_notes_async(
    request_body=request_body,
    company_key="companyKey"
)

print(result)
```

## get_company_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/company/{companyKey}/details`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| company_key | str  | ✅       |             |

**Return Type**

`EditCompanyDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_company.get_company_details_async(company_key="companyKey")

print(result)
```

## put_company_details_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/company/{companyKey}/details`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [EditCompanyDetails](../models/EditCompanyDetails.md) | ❌       | The request body. |
| company_key  | str                                                   | ✅       |                   |

**Return Type**

`Company`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditCompanyDetails

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditCompanyDetails(
    relationship="relationship",
    investor_type="investorType",
    property_type="propertyType",
    market="market",
    investment_hold_period=8.63,
    max_age=4.99,
    owned_properties_number=9,
    owned_units_number=1,
    last_purchase_date="lastPurchaseDate",
    next_sale_date="nextSaleDate",
    dev_stage="devStage",
    business_type="businessType",
    property_subtype="propertySubtype",
    submarket="submarket",
    target_cap_rate=6.65,
    min_price=3.72,
    sf_min=3.51,
    units_min=5.13,
    purchase_amount=7.99,
    next_loan_maturity="nextLoanMaturity",
    go_status="goStatus",
    branch="branch",
    total_engagements=7,
    areas="areas",
    target_irr=4.71,
    max_price=8.1,
    sf_max=0.46,
    units_max=1.73,
    estimated_sales_volume=3.38,
    next_lease_expiration="nextLeaseExpiration",
    spaces_number=8,
    current_sf=1.96,
    lease_types="leaseTypes",
    alt_company_name="altCompanyName",
    fips="fips",
    user_fields={
        "user1": "user1",
        "user2": "user2",
        "user3": "user3",
        "user4": "user4",
        "user5": "user5",
        "user6": "user6",
        "user7": "user7",
        "user8": "user8",
        "user9": "user9",
        "user10": "user10",
        "user11": "user11",
        "user12": "user12",
        "user13": "user13",
        "user14": "user14",
        "user15": "user15",
        "user16": "user16",
        "user17": "user17",
        "user18": "user18",
        "user19": "user19",
        "user20": "user20",
        "user21": "user21",
        "user22": "user22",
        "user23": "user23",
        "user24": "user24",
        "user25": "user25",
        "user26": "user26",
        "user27": "user27",
        "user28": "user28",
        "user29": "user29",
        "user30": "user30"
    },
    user_data_fields={
        "user_number1": 8.72,
        "user_number2": 8.9,
        "user_number3": 1.72,
        "usernumber4": 1.14,
        "usernumber5": 9.98,
        "usernumber6": 9.46,
        "usernumber7": 4.08,
        "usernumber8": 8.85,
        "usernumber9": 4.4,
        "usernumber10": 0.56,
        "usernumber11": 2.56,
        "usernumber12": 0.59,
        "usernumber13": 9.96,
        "usernumber14": 4.46,
        "usernumber15": 5.2,
        "usernumber16": 1.09,
        "usernumber17": 1.47,
        "usernumber18": 6.97,
        "usernumber19": 4.05,
        "usernumber20": 2.62,
        "usernumber21": 7.14,
        "usernumber22": 9.71,
        "usernumber23": 1.19,
        "usernumber24": 5.75,
        "usernumber25": 8.11,
        "usernumber26": 3.56,
        "usernumber27": 5.1,
        "usernumber28": 2.32,
        "usernumber29": 1.95,
        "usernumber30": 0.65,
        "user_date1": "userDate1",
        "user_date2": "userDate2",
        "user_date3": "userDate3",
        "userdate4": "userdate4",
        "userdate5": "userdate5",
        "userdate6": "userdate6",
        "userdate7": "userdate7",
        "userdate8": "userdate8",
        "userdate9": "userdate9",
        "userdate10": "userdate10",
        "userdate11": "userdate11",
        "userdate12": "userdate12",
        "userdate13": "userdate13",
        "userdate14": "userdate14",
        "userdate15": "userdate15",
        "userdate16": "userdate16",
        "userdate17": "userdate17",
        "userdate18": "userdate18",
        "userdate19": "userdate19",
        "userdate20": "userdate20",
        "userdate21": "userdate21",
        "userdate22": "userdate22",
        "userdate23": "userdate23",
        "userdate24": "userdate24",
        "userdate25": "userdate25",
        "userdate26": "userdate26",
        "userdate27": "userdate27",
        "userdate28": "userdate28",
        "userdate29": "userdate29",
        "userdate30": "userdate30",
        "user_multi": "userMulti"
    },
    logical_fields={
        "logical1": True,
        "logical2": True,
        "logical3": False,
        "logical4": False,
        "logical5": True,
        "logical6": False,
        "logical7": False,
        "logical8": False,
        "logical9": False,
        "logical10": True,
        "logical11": True,
        "logical12": False,
        "logical13": False,
        "logical14": True,
        "logical15": False,
        "logical16": False,
        "logical17": True,
        "logical18": False,
        "logical19": True,
        "logical20": False,
        "logical21": False,
        "logical22": False,
        "logical23": False,
        "logical24": False
    }
)

result = sdk.crm_company.put_company_details_async(
    request_body=request_body,
    company_key="companyKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
