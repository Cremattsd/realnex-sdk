# CrmHistoryService

A list of all methods in the `CrmHistoryService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description |
| :------------------------------------------------------------ | :---------- |
| [get_history_async](#get_history_async)                       |             |
| [put_history_async](#put_history_async)                       |             |
| [delete_history_async](#delete_history_async)                 |             |
| [get_history_details_async](#get_history_details_async)       |             |
| [post_history_async](#post_history_async)                     |             |
| [get_history_objects_async](#get_history_objects_async)       |             |
| [post_history_objects_async](#post_history_objects_async)     |             |
| [delete_history_objects_async](#delete_history_objects_async) |             |
| [get_object_histories_async](#get_object_histories_async)     |             |
| [post_object_history_async](#post_object_history_async)       |             |
| [get_history_file_async](#get_history_file_async)             |             |

## get_history_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/history/{historyKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| history_key | str  | ✅       |             |

**Return Type**

`EditHistory`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_history.get_history_async(history_key="historyKey")

print(result)
```

## put_history_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/history/{historyKey}`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [EditHistory](../models/EditHistory.md) | ❌       | The request body. |
| history_key  | str                                     | ✅       |                   |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditHistory

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditHistory(
    user_key="userKey",
    team_key="teamKey",
    published=False,
    start_date="startDate",
    end_date="endDate",
    timeless=True,
    event_type_key=5,
    status_key=0,
    subject="subject",
    project_key="projectKey",
    user1="user1",
    user2="user2",
    user3="user3",
    user4="user4",
    logical1=False,
    logical2=True,
    logical3=False,
    logical4=True,
    color="color",
    notes="notes"
)

result = sdk.crm_history.put_history_async(
    request_body=request_body,
    history_key="historyKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## delete_history_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/history/{historyKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| history_key | str  | ✅       |             |

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

result = sdk.crm_history.delete_history_async(history_key="historyKey")

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_history_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/history/{historyKey}/details`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| history_key | str  | ✅       |             |

**Return Type**

`HistoryDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_history.get_history_details_async(history_key="historyKey")

print(result)
```

## post_history_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/history`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [EditHistory](../models/EditHistory.md) | ❌       | The request body. |

**Return Type**

`History`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditHistory

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditHistory(
    user_key="userKey",
    team_key="teamKey",
    published=False,
    start_date="startDate",
    end_date="endDate",
    timeless=True,
    event_type_key=5,
    status_key=0,
    subject="subject",
    project_key="projectKey",
    user1="user1",
    user2="user2",
    user3="user3",
    user4="user4",
    logical1=False,
    logical2=True,
    logical3=False,
    logical4=True,
    color="color",
    notes="notes"
)

result = sdk.crm_history.post_history_async(request_body=request_body)

print(result)
```

## get_history_objects_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/history/{historyKey}/object`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| history_key | str  | ✅       |             |

**Return Type**

`List[HistoryObject]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_history.get_history_objects_async(history_key="historyKey")

print(result)
```

## post_history_objects_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/history/{historyKey}/object`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [List[HistoryObject]](../models/HistoryObject.md) | ❌       | The request body. |
| history_key  | str                                               | ✅       |                   |

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

request_body = [
    {
        "key": "key",
        "type_": "None",
        "description": "description"
    }
]

result = sdk.crm_history.post_history_objects_async(
    request_body=request_body,
    history_key="historyKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## delete_history_objects_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/history/{historyKey}/object/{objectKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| history_key | str  | ✅       |             |
| object_key  | str  | ✅       |             |

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

result = sdk.crm_history.delete_history_objects_async(
    history_key="historyKey",
    object_key="objectKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_object_histories_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/object/{objectKey}/history`

**Parameters**

| Name        | Type                                          | Required | Description |
| :---------- | :-------------------------------------------- | :------- | :---------- |
| object_key  | str                                           | ✅       |             |
| order       | [HistorySorting](../models/HistorySorting.md) | ❌       |             |
| page_size   | int                                           | ❌       |             |
| page_number | int                                           | ❌       |             |

**Return Type**

`HistoryPageResponse`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import HistorySorting

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_history.get_object_histories_async(
    object_key="objectKey",
    order="Default",
    page_size=9,
    page_number=4
)

print(result)
```

## post_object_history_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/object/{objectKey}/history`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [EditHistory](../models/EditHistory.md) | ❌       | The request body. |
| object_key   | str                                     | ✅       |                   |

**Return Type**

`History`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditHistory

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditHistory(
    user_key="userKey",
    team_key="teamKey",
    published=False,
    start_date="startDate",
    end_date="endDate",
    timeless=True,
    event_type_key=5,
    status_key=0,
    subject="subject",
    project_key="projectKey",
    user1="user1",
    user2="user2",
    user3="user3",
    user4="user4",
    logical1=False,
    logical2=True,
    logical3=False,
    logical4=True,
    color="color",
    notes="notes"
)

result = sdk.crm_history.post_object_history_async(
    request_body=request_body,
    object_key="objectKey"
)

print(result)
```

## get_history_file_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/history/{historyKey}/file`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| history_key | str  | ✅       |             |

**Return Type**

`bytes`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_history.get_history_file_async(history_key="historyKey")

with open("output-file.ext", "wb") as f:
    f.write(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
