# CrmService

A list of all methods in the `CrmService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description |
| :---------------------------------------------------------------- | :---------- |
| [get_definition_tables_async](#get_definition_tables_async)       |             |
| [get_definitions_by_table_async](#get_definitions_by_table_async) |             |
| [get_users_async](#get_users_async)                               |             |
| [get_teams_async](#get_teams_async)                               |             |
| [get_countries_async](#get_countries_async)                       |             |
| [get_time_zones_async](#get_time_zones_async)                     |             |
| [get_attachment_types_async](#get_attachment_types_async)         |             |
| [get_property_types_async](#get_property_types_async)             |             |
| [get_event_types_async](#get_event_types_async)                   |             |
| [get_priorities_async](#get_priorities_async)                     |             |
| [get_history_statuses_async](#get_history_statuses_async)         |             |
| [get_project_types_async](#get_project_types_async)               |             |
| [get_project_statuses_async](#get_project_statuses_async)         |             |
| [get_project_results_async](#get_project_results_async)           |             |

## get_definition_tables_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/definitions`

**Return Type**

`List[str]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_definition_tables_async()

print(result)
```

## get_definitions_by_table_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/definitions/{tableName}`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| table_name | str  | ✅       |             |

**Return Type**

`List[FieldDefinition]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_definitions_by_table_async(table_name="tableName")

print(result)
```

## get_users_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/users`

**Return Type**

`List[User]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_users_async()

print(result)
```

## get_teams_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/teams`

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_teams_async()

print(result)
```

## get_countries_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/countries`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_countries_async()

print(result)
```

## get_time_zones_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/timezones`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_time_zones_async()

print(result)
```

## get_attachment_types_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/attachmenttypes`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_attachment_types_async()

print(result)
```

## get_property_types_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/propertytypes`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_property_types_async()

print(result)
```

## get_event_types_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/eventtypes`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_event_types_async()

print(result)
```

## get_priorities_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/priorities`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_priorities_async()

print(result)
```

## get_history_statuses_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/historystatuses`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_history_statuses_async()

print(result)
```

## get_project_types_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/projecttypes`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_project_types_async()

print(result)
```

## get_project_statuses_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/projectstatuses`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_project_statuses_async()

print(result)
```

## get_project_results_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/projectresults`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm.get_project_results_async()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
