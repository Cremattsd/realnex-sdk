# CrmEventService

A list of all methods in the `CrmEventService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description |
| :---------------------------------------------------------------- | :---------- |
| [get_event_details_async](#get_event_details_async)               |             |
| [post_event_async](#post_event_async)                             |             |
| [get_event_async](#get_event_async)                               |             |
| [put_event_async](#put_event_async)                               |             |
| [delete_event_async](#delete_event_async)                         |             |
| [get_event_objects_async](#get_event_objects_async)               |             |
| [post_event_objects_async](#post_event_objects_async)             |             |
| [delete_event_object_async](#delete_event_object_async)           |             |
| [get_event_participants_async](#get_event_participants_async)     |             |
| [post_event_participants_async](#post_event_participants_async)   |             |
| [delete_event_participant_async](#delete_event_participant_async) |             |
| [get_object_events_async](#get_object_events_async)               |             |
| [post_object_event_async](#post_object_event_async)               |             |

## get_event_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/event/{eventKey}/details`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| event_key | str  | ✅       |             |

**Return Type**

`EventDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_event.get_event_details_async(event_key="eventKey")

print(result)
```

## post_event_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/event`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditEvent](../models/EditEvent.md) | ❌       | The request body. |

**Return Type**

`Event`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditEvent

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditEvent(
    user_key="userKey",
    team_key="teamKey",
    start_date="startDate",
    end_date="endDate",
    time_zone_key=3,
    start_offset=1,
    timeless=True,
    all_day=True,
    finished=False,
    alarm_minutes=2,
    event_type_key=0,
    priority_key=2,
    subject="subject",
    project_key="projectKey",
    color="color",
    notes="notes"
)

result = sdk.crm_event.post_event_async(request_body=request_body)

print(result)
```

## get_event_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/event/{eventKey}`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| event_key | str  | ✅       |             |

**Return Type**

`EditEvent`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_event.get_event_async(event_key="eventKey")

print(result)
```

## put_event_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/event/{eventKey}`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditEvent](../models/EditEvent.md) | ❌       | The request body. |
| event_key    | str                                 | ✅       |                   |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditEvent

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditEvent(
    user_key="userKey",
    team_key="teamKey",
    start_date="startDate",
    end_date="endDate",
    time_zone_key=3,
    start_offset=1,
    timeless=True,
    all_day=True,
    finished=False,
    alarm_minutes=2,
    event_type_key=0,
    priority_key=2,
    subject="subject",
    project_key="projectKey",
    color="color",
    notes="notes"
)

result = sdk.crm_event.put_event_async(
    request_body=request_body,
    event_key="eventKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## delete_event_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/event/{eventKey}`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| event_key | str  | ✅       |             |

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

result = sdk.crm_event.delete_event_async(event_key="eventKey")

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_event_objects_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/event/{eventKey}/object`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| event_key | str  | ✅       |             |

**Return Type**

`List[EventObject]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_event.get_event_objects_async(event_key="eventKey")

print(result)
```

## post_event_objects_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/event/{eventKey}/object`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [List[EventObject]](../models/EventObject.md) | ❌       | The request body. |
| event_key    | str                                           | ✅       |                   |

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

result = sdk.crm_event.post_event_objects_async(
    request_body=request_body,
    event_key="eventKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## delete_event_object_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/event/{eventKey}/object/{objectKey}`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| event_key  | str  | ✅       |             |
| object_key | str  | ✅       |             |

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

result = sdk.crm_event.delete_event_object_async(
    event_key="eventKey",
    object_key="objectKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_event_participants_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/event/{eventKey}/participant`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| event_key | str  | ✅       |             |

**Return Type**

`List[EventParticipant]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_event.get_event_participants_async(event_key="eventKey")

print(result)
```

## post_event_participants_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/event/{eventKey}/participant`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [List[EventParticipant]](../models/EventParticipant.md) | ❌       | The request body. |
| event_key    | str                                                     | ✅       |                   |

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
        "user_name": "userName",
        "email": "email"
    }
]

result = sdk.crm_event.post_event_participants_async(
    request_body=request_body,
    event_key="eventKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## delete_event_participant_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/event/{eventKey}/participant/{participantKey}`

**Parameters**

| Name            | Type | Required | Description |
| :-------------- | :--- | :------- | :---------- |
| event_key       | str  | ✅       |             |
| participant_key | str  | ✅       |             |

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

result = sdk.crm_event.delete_event_participant_async(
    event_key="eventKey",
    participant_key="participantKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_object_events_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/object/{objectKey}/event`

**Parameters**

| Name        | Type                                      | Required | Description |
| :---------- | :---------------------------------------- | :------- | :---------- |
| object_key  | str                                       | ✅       |             |
| order       | [EventSorting](../models/EventSorting.md) | ❌       |             |
| page_size   | int                                       | ❌       |             |
| page_number | int                                       | ❌       |             |

**Return Type**

`EventPageResponse`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EventSorting

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_event.get_object_events_async(
    object_key="objectKey",
    order="Default",
    page_size=8,
    page_number=4
)

print(result)
```

## post_object_event_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/object/{objectKey}/event`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditEvent](../models/EditEvent.md) | ❌       | The request body. |
| object_key   | str                                 | ✅       |                   |

**Return Type**

`Event`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditEvent

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditEvent(
    user_key="userKey",
    team_key="teamKey",
    start_date="startDate",
    end_date="endDate",
    time_zone_key=3,
    start_offset=1,
    timeless=True,
    all_day=True,
    finished=False,
    alarm_minutes=2,
    event_type_key=0,
    priority_key=2,
    subject="subject",
    project_key="projectKey",
    color="color",
    notes="notes"
)

result = sdk.crm_event.post_object_event_async(
    request_body=request_body,
    object_key="objectKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
