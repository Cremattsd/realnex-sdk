# CrmProjectService

A list of all methods in the `CrmProjectService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description |
| :---------------------------------------------------------------- | :---------- |
| [get_project_async](#get_project_async)                           |             |
| [post_project_async](#post_project_async)                         |             |
| [get_edit_project_async](#get_edit_project_async)                 |             |
| [put_project_async](#put_project_async)                           |             |
| [delete_project_async](#delete_project_async)                     |             |
| [get_edit_project_notes_async](#get_edit_project_notes_async)     |             |
| [put_project_notes_async](#put_project_notes_async)               |             |
| [get_edit_project_details_async](#get_edit_project_details_async) |             |
| [put_project_details_async](#put_project_details_async)           |             |
| [get_project_leads_async](#get_project_leads_async)               |             |
| [post_project_lead_async](#post_project_lead_async)               |             |
| [get_project_lead_async](#get_project_lead_async)                 |             |
| [put_project_lead_async](#put_project_lead_async)                 |             |
| [delete_project_lead_async](#delete_project_lead_async)           |             |

## get_project_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/project/{projectKey}/full`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| project_key | str  | ✅       |             |

**Return Type**

`Project`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_project.get_project_async(project_key="projectKey")

print(result)
```

## post_project_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/project`

**Parameters**

| Name         | Type                                        | Required | Description       |
| :----------- | :------------------------------------------ | :------- | :---------------- |
| request_body | [CreateProject](../models/CreateProject.md) | ❌       | The request body. |

**Return Type**

`Project`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import CreateProject

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateProject(
    user_key="userKey",
    team_key="teamKey",
    project_name="projectName",
    project_type="projectType",
    project_status="projectStatus",
    project_result="projectResult",
    client_key="clientKey",
    counter_party_client_key="counterPartyClientKey",
    listing_key="listingKey",
    size=1.56,
    amount=3.05,
    date_opened="dateOpened",
    date_expected="dateExpected",
    date_closed="dateClosed",
    probability=10,
    commission=6.07,
    reason="reason",
    investment=False,
    inhouselisting=False,
    inhouserepresentation=False,
    commissionpercentage=1.04,
    flatfee=5.93,
    object_groups=[
        "objectGroups"
    ]
)

result = sdk.crm_project.post_project_async(request_body=request_body)

print(result)
```

## get_edit_project_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/project/{projectKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| project_key | str  | ✅       |             |

**Return Type**

`EditProject`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_project.get_edit_project_async(project_key="projectKey")

print(result)
```

## put_project_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/project/{projectKey}`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [EditProject](../models/EditProject.md) | ❌       | The request body. |
| project_key  | str                                     | ✅       |                   |

**Return Type**

`Project`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditProject

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditProject(
    user_key="userKey",
    team_key="teamKey",
    project_name="projectName",
    project_type="projectType",
    project_status="projectStatus",
    project_result="projectResult",
    client_key="clientKey",
    counter_party_client_key="counterPartyClientKey",
    listing_key="listingKey",
    size=6.42,
    amount=3.02,
    date_opened="dateOpened",
    date_expected="dateExpected",
    date_closed="dateClosed",
    probability=1,
    commission=0.13,
    reason="reason",
    investment=True,
    inhouselisting=False,
    inhouserepresentation=True,
    commissionpercentage=2.89,
    flatfee=6.6
)

result = sdk.crm_project.put_project_async(
    request_body=request_body,
    project_key="projectKey"
)

print(result)
```

## delete_project_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/project/{projectKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| project_key | str  | ✅       |             |

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

result = sdk.crm_project.delete_project_async(project_key="projectKey")

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_edit_project_notes_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/project/{projectKey}/notes`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| project_key | str  | ✅       |             |

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

result = sdk.crm_project.get_edit_project_notes_async(project_key="projectKey")

print(result)
```

## put_project_notes_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/project/{projectKey}/notes`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditNotes](../models/EditNotes.md) | ❌       | The request body. |
| project_key  | str                                 | ✅       |                   |

**Return Type**

`Project`

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

result = sdk.crm_project.put_project_notes_async(
    request_body=request_body,
    project_key="projectKey"
)

print(result)
```

## get_edit_project_details_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/project/{projectKey}/details`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| project_key | str  | ✅       |             |

**Return Type**

`EditProjectDetails`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_project.get_edit_project_details_async(project_key="projectKey")

print(result)
```

## put_project_details_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/project/{projectKey}/details`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [EditProjectDetails](../models/EditProjectDetails.md) | ❌       | The request body. |
| project_key  | str                                                   | ✅       |                   |

**Return Type**

`Project`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditProjectDetails

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditProjectDetails(
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

result = sdk.crm_project.put_project_details_async(
    request_body=request_body,
    project_key="projectKey"
)

print(result)
```

## get_project_leads_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/project/{projectKey}/lead`

**Parameters**

| Name         | Type                                                  | Required | Description |
| :----------- | :---------------------------------------------------- | :------- | :---------- |
| project_key  | str                                                   | ✅       |             |
| object_types | [List[LeadObjectType]](../models/LeadObjectType.md)   | ❌       |             |
| order        | [ProjectLeadSorting](../models/ProjectLeadSorting.md) | ❌       |             |
| page_size    | int                                                   | ❌       |             |
| page_number  | int                                                   | ❌       |             |

**Return Type**

`List[ProjectLead]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import ProjectLeadSorting

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)
object_types=[
    "None"
]

result = sdk.crm_project.get_project_leads_async(
    project_key="projectKey",
    object_types=object_types,
    order="Default",
    page_size=3,
    page_number=4
)

print(result)
```

## post_project_lead_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/project/{projectKey}/lead`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [EditProjectLead](../models/EditProjectLead.md) | ❌       | The request body. |
| project_key  | str                                             | ✅       |                   |

**Return Type**

`List[ProjectLead]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditProjectLead

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditProjectLead(
    published=False,
    project_status_key=6,
    object_key="objectKey",
    size=0.75,
    amount=8.71,
    date_opened="dateOpened",
    date_expected="dateExpected",
    date_closed="dateClosed",
    probability=2,
    commission=8.76,
    project_result_key=9,
    reason="reason",
    notes="notes"
)

result = sdk.crm_project.post_project_lead_async(
    request_body=request_body,
    project_key="projectKey"
)

print(result)
```

## get_project_lead_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/project/{projectKey}/lead/{leadKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| project_key | str  | ✅       |             |
| lead_key    | str  | ✅       |             |

**Return Type**

`EditProjectLead`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_project.get_project_lead_async(
    project_key="projectKey",
    lead_key="leadKey"
)

print(result)
```

## put_project_lead_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/project/{projectKey}/lead/{leadKey}`

**Parameters**

| Name         | Type                                                                                        | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditProjectLeadJsonMergePatchDocument](../models/EditProjectLeadJsonMergePatchDocument.md) | ❌       | The request body. |
| project_key  | str                                                                                         | ✅       |                   |
| lead_key     | str                                                                                         | ✅       |                   |

**Return Type**

`List[ProjectLead]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditProjectLeadJsonMergePatchDocument

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditProjectLeadJsonMergePatchDocument(
    example_field="exampleField"
)

result = sdk.crm_project.put_project_lead_async(
    request_body=request_body,
    project_key="projectKey",
    lead_key="leadKey"
)

print(result)
```

## delete_project_lead_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/project/{projectKey}/lead/{leadKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| project_key | str  | ✅       |             |
| lead_key    | str  | ✅       |             |

**Return Type**

`List[ProjectLead]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_project.delete_project_lead_async(
    project_key="projectKey",
    lead_key="leadKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
