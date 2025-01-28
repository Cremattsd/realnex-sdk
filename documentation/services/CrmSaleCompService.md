# CrmSaleCompService

A list of all methods in the `CrmSaleCompService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description |
| :---------------------------------------------------------- | :---------- |
| [get_sale_comp_async](#get_sale_comp_async)                 |             |
| [post_sale_comp_async](#post_sale_comp_async)               |             |
| [get_edit_sale_comp_async](#get_edit_sale_comp_async)       |             |
| [put_edit_sale_comp_async](#put_edit_sale_comp_async)       |             |
| [delete_sale_comp_async](#delete_sale_comp_async)           |             |
| [get_sale_comp_notes_async](#get_sale_comp_notes_async)     |             |
| [put_sale_comp_notes_async](#put_sale_comp_notes_async)     |             |
| [get_sale_comp_details_async](#get_sale_comp_details_async) |             |
| [put_sale_comp_details_async](#put_sale_comp_details_async) |             |
| [get_sale_comp_listing_async](#get_sale_comp_listing_async) |             |
| [put_sale_comp_listing_async](#put_sale_comp_listing_async) |             |
| [get_sale_comp_usage_async](#get_sale_comp_usage_async)     |             |
| [put_sale_comp_usage_async](#put_sale_comp_usage_async)     |             |

## get_sale_comp_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/full`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| sale_comp_key | str  | ✅       |             |

**Return Type**

`SaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_sale_comp.get_sale_comp_async(sale_comp_key="saleCompKey")

print(result)
```

## post_sale_comp_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/SaleComp`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [CreateSaleComp](../models/CreateSaleComp.md) | ❌       | The request body. |

**Return Type**

`SaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import CreateSaleComp

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateSaleComp(
    user_key="userKey",
    team_key="teamKey",
    property_key="propertyKey",
    buyer_principal_key="buyerPrincipalKey",
    seller_principal_key="sellerPrincipalKey",
    procuring_principal_key="procuringPrincipalKey",
    listing_principal_key="listingPrincipalKey",
    property={
        "property_name": "propertyName",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "cross_streets": "crossStreets",
        "address_number1": "addressNumber1",
        "address_number2": "addressNumber2",
        "address_direction": "addressDirection",
        "address_street": "addressStreet",
        "address_suite": "addressSuite",
        "property_type_key": 6,
        "sale_price": 6.49,
        "sale_date": "saleDate"
    },
    buyer_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    },
    seller_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    },
    procuring_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    },
    listing_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    },
    object_groups=[
        "objectGroups"
    ]
)

result = sdk.crm_sale_comp.post_sale_comp_async(request_body=request_body)

print(result)
```

## get_edit_sale_comp_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| sale_comp_key | str  | ✅       |             |

**Return Type**

`EditSaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_sale_comp.get_edit_sale_comp_async(sale_comp_key="saleCompKey")

print(result)
```

## put_edit_sale_comp_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}`

**Parameters**

| Name          | Type                                      | Required | Description       |
| :------------ | :---------------------------------------- | :------- | :---------------- |
| request_body  | [EditSaleComp](../models/EditSaleComp.md) | ❌       | The request body. |
| sale_comp_key | str                                       | ✅       |                   |

**Return Type**

`SaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditSaleComp

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditSaleComp(
    user_key="userKey",
    team_key="teamKey",
    property_key="propertyKey",
    buyer_principal_key="buyerPrincipalKey",
    seller_principal_key="sellerPrincipalKey",
    procuring_principal_key="procuringPrincipalKey",
    listing_principal_key="listingPrincipalKey",
    property={
        "property_name": "propertyName",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "cross_streets": "crossStreets",
        "address_number1": "addressNumber1",
        "address_number2": "addressNumber2",
        "address_direction": "addressDirection",
        "address_street": "addressStreet",
        "address_suite": "addressSuite",
        "property_type_key": 6,
        "sale_price": 6.49,
        "sale_date": "saleDate"
    },
    buyer_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    },
    seller_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    },
    procuring_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    },
    listing_contact={
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "salutation": "salutation",
        "greeting": "greeting",
        "title": "title",
        "company": "company",
        "address": {
            "address1": "address1",
            "address2": "address2",
            "city": "city",
            "state": "state",
            "zip_code": "zipCode",
            "country": "country",
            "latitude": 6.78,
            "longitude": 4.17,
            "time_zone_key": 6
        },
        "work": "work",
        "fax": "fax",
        "mobile": "mobile",
        "home": "home",
        "email": "email",
        "web_site": "webSite",
        "work_extension": "workExtension",
        "fax_extension": "faxExtension",
        "mobile_extension": "mobileExtension",
        "home_extension": "homeExtension"
    }
)

result = sdk.crm_sale_comp.put_edit_sale_comp_async(
    request_body=request_body,
    sale_comp_key="saleCompKey"
)

print(result)
```

## delete_sale_comp_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| sale_comp_key | str  | ✅       |             |

**Return Type**

`SaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_sale_comp.delete_sale_comp_async(sale_comp_key="saleCompKey")

print(result)
```

## get_sale_comp_notes_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/notes`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| sale_comp_key | str  | ✅       |             |

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

result = sdk.crm_sale_comp.get_sale_comp_notes_async(sale_comp_key="saleCompKey")

print(result)
```

## put_sale_comp_notes_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/notes`

**Parameters**

| Name          | Type                                | Required | Description       |
| :------------ | :---------------------------------- | :------- | :---------------- |
| request_body  | [EditNotes](../models/EditNotes.md) | ❌       | The request body. |
| sale_comp_key | str                                 | ✅       |                   |

**Return Type**

`SaleComp`

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

result = sdk.crm_sale_comp.put_sale_comp_notes_async(
    request_body=request_body,
    sale_comp_key="saleCompKey"
)

print(result)
```

## get_sale_comp_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/details`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| sale_comp_key | str  | ✅       |             |

**Return Type**

`EditSaleCompDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_sale_comp.get_sale_comp_details_async(sale_comp_key="saleCompKey")

print(result)
```

## put_sale_comp_details_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/details`

**Parameters**

| Name          | Type                                                    | Required | Description       |
| :------------ | :------------------------------------------------------ | :------- | :---------------- |
| request_body  | [EditSaleCompDetails](../models/EditSaleCompDetails.md) | ❌       | The request body. |
| sale_comp_key | str                                                     | ✅       |                   |

**Return Type**

`SaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditSaleCompDetails

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditSaleCompDetails(
    parcel="parcel",
    building_id="buildingId",
    description="description",
    property_type_key=2,
    building_class="buildingClass",
    construction_type="constructionType",
    location="location",
    zoning="zoning",
    market="market",
    submarket="submarket",
    area="area",
    county="county",
    use_code="useCode",
    acres=1.61,
    sqft=5.14,
    units=9,
    stories=3,
    assessed_value=8.06,
    sale_price=1.07,
    sale_date="saleDate",
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
    }
)

result = sdk.crm_sale_comp.put_sale_comp_details_async(
    request_body=request_body,
    sale_comp_key="saleCompKey"
)

print(result)
```

## get_sale_comp_listing_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/listing`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| sale_comp_key | str  | ✅       |             |

**Return Type**

`EditSaleCompListing`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_sale_comp.get_sale_comp_listing_async(sale_comp_key="saleCompKey")

print(result)
```

## put_sale_comp_listing_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/listing`

**Parameters**

| Name          | Type                                                    | Required | Description       |
| :------------ | :------------------------------------------------------ | :------- | :---------------- |
| request_body  | [EditSaleCompListing](../models/EditSaleCompListing.md) | ❌       | The request body. |
| sale_comp_key | str                                                     | ✅       |                   |

**Return Type**

`SaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditSaleCompListing

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditSaleCompListing(
    down_payment=3.42,
    base_rent=2.42,
    reimburse=3.76,
    expenses=4.09,
    vacancy_factor=5.55,
    gsi=5.54,
    effective_rent=2.71,
    noi=3.51,
    cap_rate=6.07,
    grm=6.32,
    percent_down=2.39,
    per_foot=0.72,
    per_acre=2.16,
    per_unit=9.31,
    cash_flow=7.63,
    cash_on_cash=5.43,
    irr=2.85,
    loan_orig="loanOrig",
    loan_amount=3.2,
    loan_rate=5.38,
    loan_term=1,
    loan_periods=5,
    debt_service=5.55,
    lender="lender",
    loan_type="loanType",
    auto_calc=False,
    loan_maturity="loanMaturity",
    loan_trans_type="loanTransType",
    trans_type="transType",
    per_foot_land=3.42,
    tax_account_number="taxAccountNumber",
    tax_amount=0.75,
    tax_year=6,
    tax_deliquent_year=10,
    taxes=1.25,
    taxes_door=8.89
)

result = sdk.crm_sale_comp.put_sale_comp_listing_async(
    request_body=request_body,
    sale_comp_key="saleCompKey"
)

print(result)
```

## get_sale_comp_usage_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/usage`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| sale_comp_key | str  | ✅       |             |

**Return Type**

`EditSaleCompUsage`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_sale_comp.get_sale_comp_usage_async(sale_comp_key="saleCompKey")

print(result)
```

## put_sale_comp_usage_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/salecomp/{saleCompKey}/usage`

**Parameters**

| Name          | Type                                                | Required | Description       |
| :------------ | :-------------------------------------------------- | :------- | :---------------- |
| request_body  | [EditSaleCompUsage](../models/EditSaleCompUsage.md) | ❌       | The request body. |
| sale_comp_key | str                                                 | ✅       |                   |

**Return Type**

`SaleComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditSaleCompUsage

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditSaleCompUsage(
    building_status="buildingStatus",
    year_built=0,
    year_renovated=10,
    usable_sqft=2.03,
    vacant_sqft=3.13,
    load_factor=1.37,
    office_sqft=3.36,
    condition="condition",
    tenants=2,
    grade_doors="gradeDoors",
    dock_doors="dockDoors",
    truck_doors="truckDoors",
    power="power",
    clear_height="clearHeight",
    rail_service="railService",
    yard="yard",
    lot_size=8.76,
    percent_improved=8.88,
    exclusions="exclusions",
    major_tenants="majorTenants",
    highlights="highlights",
    anchors="anchors",
    demographics="demographics",
    traffic_count="trafficCount",
    signage="signage",
    extras="extras",
    population=1,
    median_income=1,
    floors=4,
    elevators=6,
    hvac="hvac",
    security="security",
    sprinklers="sprinklers",
    views="views",
    net_acres=5.47,
    land_status="landStatus",
    general_use="generalUse",
    legal_description="legalDescription",
    topography="topography",
    dimensions="dimensions",
    electric="electric",
    gas="gas",
    sewers="sewers",
    phones="phones",
    core_factor=5.9,
    parking="parking",
    parking_ratio="parkingRatio",
    parking_fees="parkingFees",
    parking_spaces=7,
    on_market="onMarket",
    off_market="offMarket",
    days_on_market=5,
    fips="fips",
    fa_property_id="faPropertyId",
    fa_doc_number="faDocNumber",
    census_tract="censusTract",
    census_block="censusBlock",
    year_assessed=1,
    block="block",
    reo="reo",
    subdivision="subdivision",
    parking_surface_type="parkingSurfaceType",
    parking_spaces_reserved=10,
    parking_spaces_unreserved=4,
    living_sqft=0.69,
    building_quality="buildingQuality",
    roof_material="roofMaterial",
    water_provider="waterProvider",
    water_service="waterService",
    water_location="waterLocation",
    rentable_sqft=3.9,
    lot_depth=9.58,
    ext_walls="extWalls",
    style="style",
    sewer_provider="sewerProvider",
    sewer_location="sewerLocation",
    gas_provider="gasProvider",
    electric_provider="electricProvider",
    electric_location="electricLocation",
    voltage_low=1,
    voltage_high=5,
    drive_in_size="driveInSize",
    drive_in=1,
    clearance_min=7.76,
    clearance_max=1.86,
    prior_use="priorUse",
    interstate="interstate",
    barge="barge",
    airport="airport",
    market_year=10,
    foreclosed=True,
    industrial_sqft=8.93,
    retail_sqft=1.16,
    min_divis=3.89,
    max_divis=1.89,
    primary_use="primaryUse",
    secondary_use="secondaryUse",
    construction_status="constructionStatus",
    date_built="dateBuilt",
    occupancy=2.33,
    multi_tenant="multiTenant",
    spec_bts="specBts",
    roof_type="roofType",
    roof_age=2,
    heat="heat",
    ac="ac",
    lighting="lighting",
    ceiling_height_min=1.09,
    ceiling_height_max=8.88,
    bay_column_width=0.59,
    bay_column_depth=7.8,
    int_docks=4,
    int_levelers=1,
    ext_docks=1,
    ext_levelers=8,
    gl_did=3,
    gl_did_dimensions="glDidDimensions",
    cross_docked="crossDocked",
    dh_truck_doors=3,
    trailer_spots=1,
    rail_doors=2,
    total_doors=6,
    loading_door_comments="loadingDoorComments",
    rail_status="railStatus",
    ex_spots=1,
    int_spots=3,
    rail_line="railLine",
    rail_comments="railComments",
    cranes=9,
    crane_capacity_min=7,
    crane_capacity_max=5,
    hook_height=0,
    clearance=10,
    crane_comments="craneComments",
    freezer_sqft=1.42,
    freezer_comments="freezerComments",
    cooler_sqft=9.67,
    cooler_comments="coolerComments",
    covered_spaces=0,
    comments_public="commentsPublic",
    comments_restricted="commentsRestricted",
    max_contig_land_sf=9.61,
    max_contig_land_ac=5.09,
    land_zoning="landZoning",
    additional_site_information="additionalSiteInformation",
    business_park="businessPark",
    amps=10,
    phase=4,
    overhead_cranes=4,
    clear_height_max=8.95,
    clear_height_min=3.6,
    complex="complex",
    dock_levelers_capacity=10,
    estimated_hold_period=0,
    estimated_sale_date="estimatedSaleDate",
    fa_trans_id=9,
    floor_thickness=9,
    frontage="frontage",
    location_overview="locationOverview",
    overhead_crane_size=5,
    property_overview="propertyOverview",
    warehouse_sf=0.83,
    floor_type="floorType",
    surface_type="surfaceType",
    cranes_clearance=4,
    property_subtype="propertySubtype",
    tenancy="tenancy",
    property_description="propertyDescription"
)

result = sdk.crm_sale_comp.put_sale_comp_usage_async(
    request_body=request_body,
    sale_comp_key="saleCompKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
