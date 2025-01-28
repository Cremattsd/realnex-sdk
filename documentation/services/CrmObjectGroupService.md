# CrmObjectGroupService

A list of all methods in the `CrmObjectGroupService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description |
| :------------------------------------------------------------------------------ | :---------- |
| [get_object_group_list_async](#get_object_group_list_async)                     |             |
| [post_object_group_async](#post_object_group_async)                             |             |
| [get_object_group_async](#get_object_group_async)                               |             |
| [put_object_group_async](#put_object_group_async)                               |             |
| [delete_object_group_async](#delete_object_group_async)                         |             |
| [get_object_group_members_async](#get_object_group_members_async)               |             |
| [post_object_group_members_async](#post_object_group_members_async)             |             |
| [delete_object_group_member_async](#delete_object_group_member_async)           |             |
| [get_object_group_list_by_object_async](#get_object_group_list_by_object_async) |             |

## get_object_group_list_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/group`

**Parameters**

| Name         | Type                                                  | Required | Description |
| :----------- | :---------------------------------------------------- | :------- | :---------- |
| object_types | [List[ObjectType]](../models/ObjectType.md)           | ❌       |             |
| order        | [ObjectGroupSorting](../models/ObjectGroupSorting.md) | ❌       |             |
| search_name  | str                                                   | ❌       |             |
| page_size    | int                                                   | ❌       |             |
| page_number  | int                                                   | ❌       |             |

**Return Type**

`ObjectGroupPageResponse`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import ObjectGroupSorting

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)
object_types=[
    "None"
]

result = sdk.crm_object_group.get_object_group_list_async(
    object_types=object_types,
    order="Default",
    search_name="SearchName",
    page_size=4,
    page_number=0
)

print(result)
```

## post_object_group_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/group`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [EditObjectGroup](../models/EditObjectGroup.md) | ❌       | The request body. |

**Return Type**

`ObjectGroup`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditObjectGroup

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditObjectGroup(
    user_key="userKey",
    team_key="teamKey",
    type_="None",
    name="name"
)

result = sdk.crm_object_group.post_object_group_async(request_body=request_body)

print(result)
```

## get_object_group_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/group/{objectGroupKey}`

**Parameters**

| Name             | Type | Required | Description |
| :--------------- | :--- | :------- | :---------- |
| object_group_key | str  | ✅       |             |

**Return Type**

`ObjectGroupDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_object_group.get_object_group_async(object_group_key="objectGroupKey")

print(result)
```

## put_object_group_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/group/{objectGroupKey}`

**Parameters**

| Name             | Type                                            | Required | Description       |
| :--------------- | :---------------------------------------------- | :------- | :---------------- |
| request_body     | [EditObjectGroup](../models/EditObjectGroup.md) | ❌       | The request body. |
| object_group_key | str                                             | ✅       |                   |

**Return Type**

`EditObjectGroup`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditObjectGroup

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditObjectGroup(
    user_key="userKey",
    team_key="teamKey",
    type_="None",
    name="name"
)

result = sdk.crm_object_group.put_object_group_async(
    request_body=request_body,
    object_group_key="objectGroupKey"
)

print(result)
```

## delete_object_group_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/group/{objectGroupKey}`

**Parameters**

| Name             | Type | Required | Description |
| :--------------- | :--- | :------- | :---------- |
| object_group_key | str  | ✅       |             |

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

result = sdk.crm_object_group.delete_object_group_async(object_group_key="objectGroupKey")

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_object_group_members_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/group/{objectGroupKey}/members`

**Parameters**

| Name             | Type                                        | Required | Description |
| :--------------- | :------------------------------------------ | :------- | :---------- |
| object_group_key | str                                         | ✅       |             |
| object_types     | [List[ObjectType]](../models/ObjectType.md) | ❌       |             |
| page_size        | int                                         | ❌       |             |
| page_number      | int                                         | ❌       |             |

**Return Type**

`ObjectGroupMemberPageResponse`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)
object_types=[
    "None"
]

result = sdk.crm_object_group.get_object_group_members_async(
    object_group_key="objectGroupKey",
    object_types=object_types,
    page_size=2,
    page_number=10
)

print(result)
```

## post_object_group_members_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/group/{objectGroupKey}/members`

**Parameters**

| Name             | Type                                                      | Required | Description       |
| :--------------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body     | [List[ObjectGroupMember]](../models/ObjectGroupMember.md) | ❌       | The request body. |
| object_group_key | str                                                       | ✅       |                   |

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

result = sdk.crm_object_group.post_object_group_members_async(
    request_body=request_body,
    object_group_key="objectGroupKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## delete_object_group_member_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/group/{objectGroupKey}/members/{objectKey}`

**Parameters**

| Name             | Type | Required | Description |
| :--------------- | :--- | :------- | :---------- |
| object_group_key | str  | ✅       |             |
| object_key       | str  | ✅       |             |

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

result = sdk.crm_object_group.delete_object_group_member_async(
    object_group_key="objectGroupKey",
    object_key="objectKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_object_group_list_by_object_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/object/{objectKey}/memberof`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| object_key | str  | ✅       |             |

**Return Type**

`List[ObjectGroup]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_object_group.get_object_group_list_by_object_async(object_key="objectKey")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
