# CrmSpaceService

A list of all methods in the `CrmSpaceService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description |
| :------------------------------------------------------ | :---------- |
| [get_space_async](#get_space_async)                     |             |
| [get_property_spaces_async](#get_property_spaces_async) |             |
| [post_property_space_async](#post_property_space_async) |             |
| [get_edit_space_async](#get_edit_space_async)           |             |
| [put_edit_space_async](#put_edit_space_async)           |             |
| [delete_space_async](#delete_space_async)               |             |
| [get_space_notes_async](#get_space_notes_async)         |             |
| [put_space_notes_async](#put_space_notes_async)         |             |
| [get_space_details_async](#get_space_details_async)     |             |
| [put_space_details_async](#put_space_details_async)     |             |

## get_space_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/space/{spaceKey}/full`

**Parameters**

| Name             | Type | Required | Description |
| :--------------- | :--- | :------- | :---------- |
| space_key        | str  | ✅       |             |
| include_property | bool | ❌       |             |

**Return Type**

`Space`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_space.get_space_async(
    space_key="spaceKey",
    include_property=True
)

print(result)
```

## get_property_spaces_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/space`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`List[PropertySpace]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_space.get_property_spaces_async(property_key="propertyKey")

print(result)
```

## post_property_space_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/space`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [CreateSpace](../models/CreateSpace.md) | ❌       | The request body. |
| property_key | str                                     | ✅       |                   |

**Return Type**

`PropertySpace`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import CreateSpace

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateSpace(
    floor="floor",
    suite="suite",
    size=7.36,
    is_available=True,
    is_retail=True,
    is_vacant=True,
    is_industrial=True,
    is_office=False,
    is_sublease=True,
    is_other=True,
    tenant_principal_key="tenantPrincipalKey",
    lease_commencement="leaseCommencement",
    rent_per_sqft=6.15,
    lease_expiry="leaseExpiry",
    rent_per_month=9.22,
    lease_term="leaseTerm",
    lease_type="leaseType",
    web_site="webSite",
    object_groups=[
        "objectGroups"
    ]
)

result = sdk.crm_space.post_property_space_async(
    request_body=request_body,
    property_key="propertyKey"
)

print(result)
```

## get_edit_space_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/space/{spaceKey}`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| space_key | str  | ✅       |             |

**Return Type**

`EditSpace`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_space.get_edit_space_async(space_key="spaceKey")

print(result)
```

## put_edit_space_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/space/{spaceKey}`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditSpace](../models/EditSpace.md) | ❌       | The request body. |
| space_key    | str                                 | ✅       |                   |

**Return Type**

`Space`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditSpace

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditSpace(
    floor="floor",
    suite="suite",
    size=1.67,
    is_available=False,
    is_retail=True,
    is_vacant=True,
    is_industrial=False,
    is_office=True,
    is_sublease=True,
    is_other=True,
    tenant_principal_key="tenantPrincipalKey",
    lease_commencement="leaseCommencement",
    rent_per_sqft=5.68,
    lease_expiry="leaseExpiry",
    rent_per_month=7.43,
    lease_term="leaseTerm",
    lease_type="leaseType",
    web_site="webSite"
)

result = sdk.crm_space.put_edit_space_async(
    request_body=request_body,
    space_key="spaceKey"
)

print(result)
```

## delete_space_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/space/{spaceKey}`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| space_key | str  | ✅       |             |

**Return Type**

`Space`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_space.delete_space_async(space_key="spaceKey")

print(result)
```

## get_space_notes_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/space/{spaceKey}/notes`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| space_key | str  | ✅       |             |

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

result = sdk.crm_space.get_space_notes_async(space_key="spaceKey")

print(result)
```

## put_space_notes_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/space/{spaceKey}/notes`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditNotes](../models/EditNotes.md) | ❌       | The request body. |
| space_key    | str                                 | ✅       |                   |

**Return Type**

`Space`

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

result = sdk.crm_space.put_space_notes_async(
    request_body=request_body,
    space_key="spaceKey"
)

print(result)
```

## get_space_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/space/{spaceKey}/details`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| space_key | str  | ✅       |             |

**Return Type**

`EditSpaceDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_space.get_space_details_async(space_key="spaceKey")

print(result)
```

## put_space_details_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/space/{spaceKey}/details`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [EditSpaceDetails](../models/EditSpaceDetails.md) | ❌       | The request body. |
| space_key    | str                                               | ✅       |                   |

**Return Type**

`Space`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditSpaceDetails

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditSpaceDetails(
    cam=3.59,
    occupancy="occupancy",
    taxes=4.91,
    insurance=6.93,
    usable_area=0.18,
    load_factor=6.05,
    frontage="frontage",
    percent_rent="percentRent",
    office_area=5.72,
    grade_doors="gradeDoors",
    dock_doors="dockDoors",
    truck_doors="truckDoors",
    clear_ht="clearHt",
    power="power",
    rail_service="railService",
    yard="yard",
    exp_stop="expStop",
    effective_rent=6.36,
    increases="increases",
    options="options",
    tia="tia",
    lease_commencement="leaseCommencement",
    rent_per_sqft=5.22,
    lease_expiry="leaseExpiry",
    rent_per_month=5.02,
    lease_term="leaseTerm",
    lease_type="leaseType",
    web_site="webSite",
    business_type="businessType",
    days_on_market=2,
    escalation_date="escalationDate",
    max_divisible=5.24,
    min_divisible=5.59,
    nnn_expenses=3.76,
    occupancy_date="occupancyDate",
    off_market="offMarket",
    on_market="onMarket",
    ror_date="rorDate",
    rot_date="rotDate",
    submarket="submarket",
    tenant_pro_rata_share=7.43,
    warehouse_sf=7.79,
    annual_rate_per_sf=3.85,
    total_annual_rate=1,
    security_deposit=5.99,
    retail_sf=6.75,
    rentable_sf=1.36,
    space_id=4,
    total_lease_value=8.29,
    rent_abatement=6.78,
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
    }
)

result = sdk.crm_space.put_space_details_async(
    request_body=request_body,
    space_key="spaceKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
