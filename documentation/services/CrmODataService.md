# CrmODataService

A list of all methods in the `CrmODataService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description |
| :---------------------------------------------------------------------- | :---------- |
| [get_api_v1_crm_o_data_contacts](#get_api_v1_crm_o_data_contacts)       |             |
| [get_api_v1_crm_o_data_companies](#get_api_v1_crm_o_data_companies)     |             |
| [get_api_v1_crm_o_data_properties](#get_api_v1_crm_o_data_properties)   |             |
| [get_api_v1_crm_o_data_spaces](#get_api_v1_crm_o_data_spaces)           |             |
| [get_api_v1_crm_o_data_projects](#get_api_v1_crm_o_data_projects)       |             |
| [get_api_v1_crm_o_data_lease_comps](#get_api_v1_crm_o_data_lease_comps) |             |
| [get_api_v1_crm_o_data_sale_comps](#get_api_v1_crm_o_data_sale_comps)   |             |

## get_api_v1_crm_o_data_contacts

- HTTP Method: `GET`
- Endpoint: `/api/v1/CrmOData/Contacts`

**Parameters**

| Name        | Type | Required | Description               |
| :---------- | :--- | :------- | :------------------------ |
| api_version | str  | ❌       | The requested API version |

**Return Type**

`List[ContactListItem]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_o_data.get_api_v1_crm_o_data_contacts(api_version="1.0")

print(result)
```

## get_api_v1_crm_o_data_companies

- HTTP Method: `GET`
- Endpoint: `/api/v1/CrmOData/Companies`

**Parameters**

| Name        | Type | Required | Description               |
| :---------- | :--- | :------- | :------------------------ |
| api_version | str  | ❌       | The requested API version |

**Return Type**

`List[CompanyListItem]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_o_data.get_api_v1_crm_o_data_companies(api_version="1.0")

print(result)
```

## get_api_v1_crm_o_data_properties

- HTTP Method: `GET`
- Endpoint: `/api/v1/CrmOData/Properties`

**Parameters**

| Name        | Type | Required | Description               |
| :---------- | :--- | :------- | :------------------------ |
| api_version | str  | ❌       | The requested API version |

**Return Type**

`List[PropertyListItem]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_o_data.get_api_v1_crm_o_data_properties(api_version="1.0")

print(result)
```

## get_api_v1_crm_o_data_spaces

- HTTP Method: `GET`
- Endpoint: `/api/v1/CrmOData/Spaces`

**Parameters**

| Name        | Type | Required | Description               |
| :---------- | :--- | :------- | :------------------------ |
| api_version | str  | ❌       | The requested API version |

**Return Type**

`List[SpaceListItem]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_o_data.get_api_v1_crm_o_data_spaces(api_version="1.0")

print(result)
```

## get_api_v1_crm_o_data_projects

- HTTP Method: `GET`
- Endpoint: `/api/v1/CrmOData/Projects`

**Parameters**

| Name        | Type | Required | Description               |
| :---------- | :--- | :------- | :------------------------ |
| api_version | str  | ❌       | The requested API version |

**Return Type**

`List[ProjectListItem]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_o_data.get_api_v1_crm_o_data_projects(api_version="1.0")

print(result)
```

## get_api_v1_crm_o_data_lease_comps

- HTTP Method: `GET`
- Endpoint: `/api/v1/CrmOData/LeaseComps`

**Parameters**

| Name        | Type | Required | Description               |
| :---------- | :--- | :------- | :------------------------ |
| api_version | str  | ❌       | The requested API version |

**Return Type**

`List[LeaseCompListItem]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_o_data.get_api_v1_crm_o_data_lease_comps(api_version="1.0")

print(result)
```

## get_api_v1_crm_o_data_sale_comps

- HTTP Method: `GET`
- Endpoint: `/api/v1/CrmOData/SaleComps`

**Parameters**

| Name        | Type | Required | Description               |
| :---------- | :--- | :------- | :------------------------ |
| api_version | str  | ❌       | The requested API version |

**Return Type**

`List[SaleCompListItem]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_o_data.get_api_v1_crm_o_data_sale_comps(api_version="1.0")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
