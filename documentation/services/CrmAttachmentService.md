# CrmAttachmentService

A list of all methods in the `CrmAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description |
| :------------------------------------------------------------ | :---------- |
| [get_attachments_async](#get_attachments_async)               |             |
| [post_attachment_async](#post_attachment_async)               |             |
| [get_attachment_async](#get_attachment_async)                 |             |
| [put_attachment_async](#put_attachment_async)                 |             |
| [get_attachment_file_async](#get_attachment_file_async)       |             |
| [get_object_attachments_async](#get_object_attachments_async) |             |

## get_attachments_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/attachment/{objectKey}`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| object_key | str  | ✅       |             |

**Return Type**

`List[Attachment]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_attachment.get_attachments_async(object_key="objectKey")

print(result)
```

## post_attachment_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/attachment/{objectKey}`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [EditAttachment](../models/EditAttachment.md) | ❌       | The request body. |
| object_key   | str                                           | ✅       |                   |

**Return Type**

`List[Attachment]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditAttachment

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditAttachment(
    user_key="userKey",
    team_key="teamKey",
    file={
        "file_name": "fileName",
        "file_content": "fileContent",
        "media_type": "mediaType"
    },
    description="description",
    attachment_type_key=6,
    attachment_date="attachmentDate",
    picture=False
)

result = sdk.crm_attachment.post_attachment_async(
    request_body=request_body,
    object_key="objectKey"
)

print(result)
```

## get_attachment_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/attachment/{objectKey}/{attachmentKey}`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| object_key     | str  | ✅       |             |
| attachment_key | str  | ✅       |             |

**Return Type**

`Attachment`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_attachment.get_attachment_async(
    object_key="objectKey",
    attachment_key="attachmentKey"
)

print(result)
```

## put_attachment_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/attachment/{objectKey}/{attachmentKey}`

**Parameters**

| Name           | Type                                          | Required | Description       |
| :------------- | :-------------------------------------------- | :------- | :---------------- |
| request_body   | [EditAttachment](../models/EditAttachment.md) | ❌       | The request body. |
| object_key     | str                                           | ✅       |                   |
| attachment_key | str                                           | ✅       |                   |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditAttachment

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditAttachment(
    user_key="userKey",
    team_key="teamKey",
    file={
        "file_name": "fileName",
        "file_content": "fileContent",
        "media_type": "mediaType"
    },
    description="description",
    attachment_type_key=6,
    attachment_date="attachmentDate",
    picture=False
)

result = sdk.crm_attachment.put_attachment_async(
    request_body=request_body,
    object_key="objectKey",
    attachment_key="attachmentKey"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_attachment_file_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/attachment/{objectKey}/{attachmentKey}/file`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| object_key     | str  | ✅       |             |
| attachment_key | str  | ✅       |             |

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

result = sdk.crm_attachment.get_attachment_file_async(
    object_key="objectKey",
    attachment_key="attachmentKey"
)

with open("output-file.ext", "wb") as f:
    f.write(result)
```

## get_object_attachments_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/object/{objectKey}/attachments`

**Parameters**

| Name        | Type                                                | Required | Description |
| :---------- | :-------------------------------------------------- | :------- | :---------- |
| object_key  | str                                                 | ✅       |             |
| order       | [AttachmentSorting](../models/AttachmentSorting.md) | ❌       |             |
| page_size   | int                                                 | ❌       |             |
| page_number | int                                                 | ❌       |             |

**Return Type**

`AttachmentPageResponse`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import AttachmentSorting

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_attachment.get_object_attachments_async(
    object_key="objectKey",
    order="Default",
    page_size=0,
    page_number=1
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
