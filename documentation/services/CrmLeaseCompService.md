# CrmLeaseCompService

A list of all methods in the `CrmLeaseCompService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description |
| :------------------------------------------------------------ | :---------- |
| [get_lease_comp_async](#get_lease_comp_async)                 |             |
| [post_lease_comp_async](#post_lease_comp_async)               |             |
| [get_edit_lease_comp_async](#get_edit_lease_comp_async)       |             |
| [put_edit_lease_comp_async](#put_edit_lease_comp_async)       |             |
| [delete_lease_comp_async](#delete_lease_comp_async)           |             |
| [get_lease_comp_notes_async](#get_lease_comp_notes_async)     |             |
| [put_lease_comp_notes_async](#put_lease_comp_notes_async)     |             |
| [get_lease_comp_details_async](#get_lease_comp_details_async) |             |
| [put_lease_comp_details_async](#put_lease_comp_details_async) |             |

## get_lease_comp_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}/full`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| lease_comp_key | str  | ✅       |             |

**Return Type**

`LeaseComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_lease_comp.get_lease_comp_async(lease_comp_key="leaseCompKey")

print(result)
```

## post_lease_comp_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/leasecomp`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [CreateLeaseComp](../models/CreateLeaseComp.md) | ❌       | The request body. |

**Return Type**

`LeaseComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import CreateLeaseComp

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateLeaseComp(
    user_key="userKey",
    team_key="teamKey",
    space_key="spaceKey",
    lessee_principal_key="lesseePrincipalKey",
    lessor_principal_key="lessorPrincipalKey",
    procuring_principal_key="procuringPrincipalKey",
    listing_principal_key="listingPrincipalKey",
    space={
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
        "suite": "suite",
        "floor": "floor",
        "deal_date": "dealDate",
        "comp_source": "compSource",
        "sub_market": "subMarket",
        "region": "region",
        "on_market": 3,
        "is_office": True,
        "is_other": True,
        "is_retail": False,
        "is_industrial": True
    },
    lessee_contact={
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
    lessor_contact={
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

result = sdk.crm_lease_comp.post_lease_comp_async(request_body=request_body)

print(result)
```

## get_edit_lease_comp_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| lease_comp_key | str  | ✅       |             |

**Return Type**

`EditLeaseComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_lease_comp.get_edit_lease_comp_async(lease_comp_key="leaseCompKey")

print(result)
```

## put_edit_lease_comp_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}`

**Parameters**

| Name           | Type                                        | Required | Description       |
| :------------- | :------------------------------------------ | :------- | :---------------- |
| request_body   | [EditLeaseComp](../models/EditLeaseComp.md) | ❌       | The request body. |
| lease_comp_key | str                                         | ✅       |                   |

**Return Type**

`LeaseComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditLeaseComp

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditLeaseComp(
    user_key="userKey",
    team_key="teamKey",
    space_key="spaceKey",
    lessee_principal_key="lesseePrincipalKey",
    lessor_principal_key="lessorPrincipalKey",
    procuring_principal_key="procuringPrincipalKey",
    listing_principal_key="listingPrincipalKey",
    space={
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
        "suite": "suite",
        "floor": "floor",
        "deal_date": "dealDate",
        "comp_source": "compSource",
        "sub_market": "subMarket",
        "region": "region",
        "on_market": 3,
        "is_office": True,
        "is_other": True,
        "is_retail": False,
        "is_industrial": True
    },
    lessee_contact={
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
    lessor_contact={
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

result = sdk.crm_lease_comp.put_edit_lease_comp_async(
    request_body=request_body,
    lease_comp_key="leaseCompKey"
)

print(result)
```

## delete_lease_comp_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| lease_comp_key | str  | ✅       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_lease_comp.delete_lease_comp_async(lease_comp_key="leaseCompKey")

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_lease_comp_notes_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}/notes`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| lease_comp_key | str  | ✅       |             |

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

result = sdk.crm_lease_comp.get_lease_comp_notes_async(lease_comp_key="leaseCompKey")

print(result)
```

## put_lease_comp_notes_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}/notes`

**Parameters**

| Name           | Type                                | Required | Description       |
| :------------- | :---------------------------------- | :------- | :---------------- |
| request_body   | [EditNotes](../models/EditNotes.md) | ❌       | The request body. |
| lease_comp_key | str                                 | ✅       |                   |

**Return Type**

`LeaseComp`

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

result = sdk.crm_lease_comp.put_lease_comp_notes_async(
    request_body=request_body,
    lease_comp_key="leaseCompKey"
)

print(result)
```

## get_lease_comp_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}/details`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| lease_comp_key | str  | ✅       |             |

**Return Type**

`EditLeaseCompDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_lease_comp.get_lease_comp_details_async(lease_comp_key="leaseCompKey")

print(result)
```

## put_lease_comp_details_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/leasecomp/{leaseCompKey}/details`

**Parameters**

| Name           | Type                                                      | Required | Description       |
| :------------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body   | [EditLeaseCompDetails](../models/EditLeaseCompDetails.md) | ❌       | The request body. |
| lease_comp_key | str                                                       | ✅       |                   |

**Return Type**

`LeaseComp`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditLeaseCompDetails

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditLeaseCompDetails(
    comp_source="compSource",
    previous_location="previousLocation",
    submarket="submarket",
    region="region",
    deal_date="dealDate",
    on_market=10,
    floor="floor",
    suite="suite",
    office=False,
    retail=True,
    industrial=True,
    other=True,
    sqft=1.69,
    usable_sqft=3.38,
    load_factor=8.58,
    office_sqft=1.06,
    lease_commencement="leaseCommencement",
    lease_expiry="leaseExpiry",
    lease_term="leaseTerm",
    lease_type="leaseType",
    rent_per_sqft=6.23,
    rent_per_mo=8.42,
    effective_rent=9.62,
    increases="increases",
    options="options",
    tax_per_sqft=6.67,
    ins_per_sqft=0.41,
    cam_per_sqft=5.51,
    tia="tia",
    percent_rent="percentRent",
    expense_stop="expenseStop",
    frontage="frontage",
    grade_doors="gradeDoors",
    dock_doors="dockDoors",
    truck_doors="truckDoors",
    power="power",
    clear_height="clearHeight",
    rail_service="railService",
    yard="yard",
    occupancy="occupancy",
    business_type="businessType",
    escalation_date="escalationDate",
    max_divisible=9.85,
    min_divisible=3.05,
    occupancy_date="occupancyDate",
    off_market_date="offMarketDate",
    on_market_date="onMarketDate",
    retail_sf=4.9,
    ror_date="rorDate",
    rot_date="rotDate",
    warehouse_sf=3.41,
    annual_rate_per_sf=7.62,
    total_annual_rate=7.52,
    security_deposit=3.45,
    nnn_expenses=1.28,
    rentable_sf=7.01,
    tenant_pro_rata_share=3.42,
    space_id=2,
    total_lease_value=5.04,
    rent_abatement=6.09,
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

result = sdk.crm_lease_comp.put_lease_comp_details_async(
    request_body=request_body,
    lease_comp_key="leaseCompKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
