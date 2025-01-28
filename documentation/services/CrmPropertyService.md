# CrmPropertyService

A list of all methods in the `CrmPropertyService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description |
| :---------------------------------------------------------------------------- | :---------- |
| [get_property_async](#get_property_async)                                     |             |
| [post_property_async](#post_property_async)                                   |             |
| [get_edit_property_async](#get_edit_property_async)                           |             |
| [put_edit_property_async](#put_edit_property_async)                           |             |
| [delete_property_async](#delete_property_async)                               |             |
| [get_property_notes_async](#get_property_notes_async)                         |             |
| [put_property_notes_async](#put_property_notes_async)                         |             |
| [get_property_details_async](#get_property_details_async)                     |             |
| [put_property_details_async](#put_property_details_async)                     |             |
| [get_property_usage_async](#get_property_usage_async)                         |             |
| [put_property_usage_async](#put_property_usage_async)                         |             |
| [get_property_listing_for_lease_async](#get_property_listing_for_lease_async) |             |
| [put_property_listing_for_lease_async](#put_property_listing_for_lease_async) |             |
| [get_property_listing_for_sale_async](#get_property_listing_for_sale_async)   |             |
| [put_property_listing_for_sale_async](#put_property_listing_for_sale_async)   |             |

## get_property_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/full`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_property.get_property_async(property_key="propertyKey")

print(result)
```

## post_property_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/property`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [CreateProperty](../models/CreateProperty.md) | ❌       | The request body. |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import CreateProperty

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateProperty(
    user_key="userKey",
    team_key="teamKey",
    property_name="propertyName",
    address={
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
    property_type_key=10,
    address_number1="addressNumber1",
    address_number2="addressNumber2",
    address_direction="addressDirection",
    address_street="addressStreet",
    address_suite="addressSuite",
    cross_streets="crossStreets",
    for_sale=True,
    for_lease=False,
    owner_principal_key="ownerPrincipalKey",
    site_principal_key="sitePrincipalKey",
    agent_principal_key="agentPrincipalKey",
    object_groups=[
        "objectGroups"
    ]
)

result = sdk.crm_property.post_property_async(request_body=request_body)

print(result)
```

## get_edit_property_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`EditProperty`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_property.get_edit_property_async(property_key="propertyKey")

print(result)
```

## put_edit_property_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/property/{propertyKey}`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | [EditProperty](../models/EditProperty.md) | ❌       | The request body. |
| property_key | str                                       | ✅       |                   |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditProperty

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditProperty(
    user_key="userKey",
    team_key="teamKey",
    property_name="propertyName",
    address={
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
    property_type_key=5,
    address_number1="addressNumber1",
    address_number2="addressNumber2",
    address_direction="addressDirection",
    address_street="addressStreet",
    address_suite="addressSuite",
    cross_streets="crossStreets",
    for_sale=True,
    for_lease=False,
    owner_principal_key="ownerPrincipalKey",
    site_principal_key="sitePrincipalKey",
    agent_principal_key="agentPrincipalKey"
)

result = sdk.crm_property.put_edit_property_async(
    request_body=request_body,
    property_key="propertyKey"
)

print(result)
```

## delete_property_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/property/{propertyKey}`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_property.delete_property_async(property_key="propertyKey")

print(result)
```

## get_property_notes_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/notes`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

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

result = sdk.crm_property.get_property_notes_async(property_key="propertyKey")

print(result)
```

## put_property_notes_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/notes`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditNotes](../models/EditNotes.md) | ❌       | The request body. |
| property_key | str                                 | ✅       |                   |

**Return Type**

`Property`

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

result = sdk.crm_property.put_property_notes_async(
    request_body=request_body,
    property_key="propertyKey"
)

print(result)
```

## get_property_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/details`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`EditPropertyDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_property.get_property_details_async(property_key="propertyKey")

print(result)
```

## put_property_details_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/details`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditPropertyDetails](../models/EditPropertyDetails.md) | ❌       | The request body. |
| property_key | str                                                     | ✅       |                   |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditPropertyDetails

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditPropertyDetails(
    assessed=1.96,
    construction_type="constructionType",
    owner_occupied=True,
    cross_streets="crossStreets",
    building_class="buildingClass",
    location="location",
    description="description",
    building_id="buildingId",
    last_trans_price=1.83,
    last_trans_date="lastTransDate",
    map_coord="mapCoord",
    acres=4.67,
    units=0,
    sqft=2.11,
    parcel="parcel",
    stories=3,
    market="market",
    submarket="submarket",
    zoning="zoning",
    web_site="webSite",
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

result = sdk.crm_property.put_property_details_async(
    request_body=request_body,
    property_key="propertyKey"
)

print(result)
```

## get_property_usage_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/usage`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`EditPropertyUsage`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_property.get_property_usage_async(property_key="propertyKey")

print(result)
```

## put_property_usage_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/usage`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [EditPropertyUsage](../models/EditPropertyUsage.md) | ❌       | The request body. |
| property_key | str                                                 | ✅       |                   |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditPropertyUsage

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditPropertyUsage(
    bldg_status="bldgStatus",
    usable_area=9.94,
    load_factor=6.68,
    net_acres=6.07,
    yr_renov=5,
    condition="condition",
    vacant_area=8.56,
    year_built=6,
    parking="parking",
    parking_ratio="parkingRatio",
    parking_spc=8,
    lot_size=4.51,
    parkingfee="parkingfee",
    improved=9.78,
    exclusions="exclusions",
    office_area=4.83,
    electric="electric",
    general_use="generalUse",
    majors="majors",
    grade_doors="gradeDoors",
    gas="gas",
    legal_descr="legalDescr",
    anchors="anchors",
    dock_doors="dockDoors",
    sewers="sewers",
    topography="topography",
    demographics="demographics",
    truck_doors="truckDoors",
    phones="phones",
    population=4,
    dimensions="dimensions",
    traffic_count="trafficCount",
    clear_height="clearHeight",
    power="power",
    signage="signage",
    rail_service="railService",
    med_income=7,
    yard="yard",
    elevators=10,
    hvac="hvac",
    sprinklers="sprinklers",
    extras="extras",
    security="security",
    highlights="highlights",
    land_status="landStatus",
    views="views",
    overhead_cranes=5,
    airport_access="airportAccess",
    barge_access="bargeAccess",
    block="block",
    building_quality="buildingQuality",
    census_block="censusBlock",
    census_tract="censusTract",
    clear_height_max=2.76,
    clear_height_min=0.8,
    complex="complex",
    dock_levelers_capacity=0,
    drive_in=3,
    drive_in_size="driveInSize",
    electric_location="electricLocation",
    electric_provider="electricProvider",
    estimated_hold_period=5,
    estimated_sale_date="estimatedSaleDate",
    ext_walls="extWalls",
    fa_doc_number="faDocNumber",
    fa_trans_id=6,
    fips="fips",
    floor_thickness=9,
    frontage="frontage",
    gas_provider="gasProvider",
    interstate="interstate",
    living_sqft=9.72,
    location_overview="locationOverview",
    lot_depth=8.42,
    overhead_crane_size=4,
    parking_spaces_reserved=10,
    parking_spaces_unreserved=8,
    parking_surface_type="parkingSurfaceType",
    prior_use="priorUse",
    property_overview="propertyOverview",
    rentable_sqft=4.63,
    roof_material="roofMaterial",
    sewer_location="sewerLocation",
    sewer_provider="sewerProvider",
    style="style",
    subdivision="subdivision",
    taxes=5.93,
    taxes_door=9.56,
    voltage_high=6,
    voltage_min=7,
    warehouse_sf=0.4,
    water_location="waterLocation",
    water_provider="waterProvider",
    year_assessed=7,
    curr_cap_rate=1.7,
    curr_cash_flow=6.54,
    curr_cash_on_cash=4.84,
    curr_debt_service=9.82,
    curr_grm=6.78,
    curr_irr=4.71,
    curr_lender="currLender",
    curr_loan_amount=9.26,
    curr_loan_maturity="currLoanMaturity",
    curr_loan_orig="currLoanOrig",
    curr_loan_periods=3,
    curr_loan_rate=6.73,
    curr_loan_term=5,
    curr_loan_type="currLoanType",
    curr_per_acre=0.39,
    curr_per_foot=8.02,
    curr_per_foot_land=0.77,
    curr_per_unit=0.05,
    floor_type="floorType",
    surface_type="surfaceType",
    tax_amount=3.54,
    tax_year=5,
    tax_deliquent_year=9,
    tax_account_number="taxAccountNumber",
    market_year=9,
    loan_trans_type="loanTransType",
    trans_type="transType",
    cranes_clearance=3,
    property_subtype="propertySubtype",
    tenancy="tenancy",
    property_description="propertyDescription"
)

result = sdk.crm_property.put_property_usage_async(
    request_body=request_body,
    property_key="propertyKey"
)

print(result)
```

## get_property_listing_for_lease_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/listingforlease`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`EditPropertyListingForLease`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_property.get_property_listing_for_lease_async(property_key="propertyKey")

print(result)
```

## put_property_listing_for_lease_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/listingforlease`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EditPropertyListingForLease](../models/EditPropertyListingForLease.md) | ❌       | The request body. |
| property_key | str                                                                     | ✅       |                   |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditPropertyListingForLease

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditPropertyListingForLease(
    available="available",
    min_contig_sf=7.53,
    percent_rent="percentRent",
    lease_list_no="leaseListNo",
    max_contig_sf=9.44,
    cam=8.73,
    lease_list_acq="leaseListAcq",
    min_rent_sf=6.14,
    tax=9.85,
    lease_list_exp="leaseListExp",
    max_rent_sf=0.62,
    insurance=7.37,
    signup="signup",
    min_rent_mo=3.16,
    tia="tia",
    signdown="signdown",
    max_rent_mo=5.56,
    lockbox="lockbox",
    per_foot_land=3.92,
    lease_type="leaseType",
    nnn_expenses=4.47
)

result = sdk.crm_property.put_property_listing_for_lease_async(
    request_body=request_body,
    property_key="propertyKey"
)

print(result)
```

## get_property_listing_for_sale_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/listingforsale`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| property_key | str  | ✅       |             |

**Return Type**

`EditPropertyListingForSale`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_property.get_property_listing_for_sale_async(property_key="propertyKey")

print(result)
```

## put_property_listing_for_sale_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/property/{propertyKey}/listingforsale`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EditPropertyListingForSale](../models/EditPropertyListingForSale.md) | ❌       | The request body. |
| property_key | str                                                                   | ✅       |                   |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditPropertyListingForSale

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditPropertyListingForSale(
    sale_price=7.95,
    expenses=3.81,
    cap_rate=9.34,
    down_payment=9.66,
    noi=3.59,
    grm=5.2,
    percent_down=3.15,
    loan_amount=3.91,
    cash_flow=9.42,
    base_rent=6.66,
    interest=2.31,
    cash_on_cash=4.52,
    reimburse=6.12,
    years=7,
    gsi=4.76,
    payments_yr=3,
    vacancy_factor=2.88,
    debt_service=2.34,
    effective=4.13,
    auto_calc=False,
    price_acre=5.13,
    price_foot=6.56,
    price_unit=3.66,
    sale_list_acq="saleListAcq",
    sale_list_exp="saleListExp",
    loan_maturity="loanMaturity",
    loan_origination="loanOrigination",
    sale_list_no="saleListNo",
    irr=3.63,
    lender="lender",
    loan_type="loanType"
)

result = sdk.crm_property.put_property_listing_for_sale_async(
    request_body=request_body,
    property_key="propertyKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
