# CrmContactService

A list of all methods in the `CrmContactService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                           | Description |
| :------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- |
| [get_contact_async](#get_contact_async)                                                                                                           |             |
| [get_edit_contact_async](#get_edit_contact_async)                                                                                                 |             |
| [put_edit_contact_async](#put_edit_contact_async)                                                                                                 |             |
| [delete_contact_async](#delete_contact_async)                                                                                                     |             |
| [post_contact_async](#post_contact_async)                                                                                                         |             |
| [get_contact_address_async](#get_contact_address_async)                                                                                           |             |
| [post_contact_address_async](#post_contact_address_async)                                                                                         |             |
| [put_contact_address_async](#put_contact_address_async)                                                                                           |             |
| [delete_contact_address_async](#delete_contact_address_async)                                                                                     |             |
| [put_contact_address_role_async](#put_contact_address_role_async)                                                                                 |             |
| [get_contact_notes_async](#get_contact_notes_async)                                                                                               |             |
| [put_contact_notes_async](#put_contact_notes_async)                                                                                               |             |
| [get_contact_personal_async](#get_contact_personal_async)                                                                                         |             |
| [put_contact_personal_async](#put_contact_personal_async)                                                                                         |             |
| [get_contact_agent_async](#get_contact_agent_async)                                                                                               |             |
| [put_contact_agent_async](#put_contact_agent_async)                                                                                               |             |
| [put_contact_investor_async](#put_contact_investor_async)                                                                                         |             |
| [put_contact_investor_async_put_api_v1_crm_contact_contact_key_investor](#put_contact_investor_async_put_api_v1_crm_contact_contact_key_investor) |             |
| [get_contact_tenant_async](#get_contact_tenant_async)                                                                                             |             |
| [put_contact_tenant_async](#put_contact_tenant_async)                                                                                             |             |
| [get_contact_vendor_async](#get_contact_vendor_async)                                                                                             |             |
| [put_contact_vendor_async](#put_contact_vendor_async)                                                                                             |             |

## get_contact_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/full`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.get_contact_async(contact_key="contactKey")

print(result)
```

## get_edit_contact_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`EditContact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.get_edit_contact_async(contact_key="contactKey")

print(result)
```

## put_edit_contact_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [EditContact](../models/EditContact.md) | ❌       | The request body. |
| contact_key  | str                                     | ✅       |                   |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditContact

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditContact(
    user_key="userKey",
    team_key="teamKey",
    full_name="fullName",
    first_name="firstName",
    last_name="lastName",
    salutation="salutation",
    greeting="greeting",
    title="title",
    company_key="companyKey",
    use_company_address=False,
    address={
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "state": "state",
        "zip_code": "zipCode",
        "country": "country",
        "latitude": 8.53,
        "longitude": 4.96,
        "time_zone_key": 5,
        "company": "company"
    },
    investor=True,
    tenant=False,
    agent=True,
    vendor=False,
    prospect=False,
    personal=True,
    work="work",
    fax="fax",
    mobile="mobile",
    home="home",
    email="email",
    web_site="webSite",
    do_not_call=True,
    do_not_email=False,
    do_not_fax=False,
    do_not_mail=True
)

result = sdk.crm_contact.put_edit_contact_async(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

## delete_contact_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/contact/{contactKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.delete_contact_async(contact_key="contactKey")

print(result)
```

## post_contact_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/contact`

**Parameters**

| Name         | Type                                        | Required | Description       |
| :----------- | :------------------------------------------ | :------- | :---------------- |
| request_body | [CreateContact](../models/CreateContact.md) | ❌       | The request body. |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import CreateContact

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateContact(
    user_key="userKey",
    team_key="teamKey",
    full_name="fullName",
    first_name="firstName",
    last_name="lastName",
    salutation="salutation",
    greeting="greeting",
    title="title",
    company_key="companyKey",
    use_company_address=False,
    address={
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "state": "state",
        "zip_code": "zipCode",
        "country": "country",
        "latitude": 8.53,
        "longitude": 4.96,
        "time_zone_key": 5,
        "company": "company"
    },
    investor=True,
    tenant=True,
    agent=True,
    vendor=False,
    prospect=True,
    personal=False,
    work="work",
    fax="fax",
    mobile="mobile",
    home="home",
    email="email",
    web_site="webSite",
    do_not_call=True,
    do_not_email=True,
    do_not_fax=True,
    do_not_mail=True,
    object_groups=[
        "objectGroups"
    ]
)

result = sdk.crm_contact.post_contact_async(request_body=request_body)

print(result)
```

## get_contact_address_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/address`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`List[ContactAddress]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.get_contact_address_async(contact_key="contactKey")

print(result)
```

## post_contact_address_async

- HTTP Method: `POST`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/address`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [EditAddressPrincipal](../models/EditAddressPrincipal.md) | ❌       | The request body. |
| contact_key  | str                                                       | ✅       |                   |

**Return Type**

`List[ContactAddress]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditAddressPrincipal

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditAddressPrincipal(
    address1="address1",
    address2="address2",
    city="city",
    state="state",
    zip_code="zipCode",
    country="country",
    latitude=8.53,
    longitude=4.96,
    time_zone_key=5,
    company="company"
)

result = sdk.crm_contact.post_contact_address_async(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

## put_contact_address_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/address/{addressKey}`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [EditAddressPrincipal](../models/EditAddressPrincipal.md) | ❌       | The request body. |
| contact_key  | str                                                       | ✅       |                   |
| address_key  | str                                                       | ✅       |                   |

**Return Type**

`List[ContactAddress]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditAddressPrincipal

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditAddressPrincipal(
    address1="address1",
    address2="address2",
    city="city",
    state="state",
    zip_code="zipCode",
    country="country",
    latitude=8.53,
    longitude=4.96,
    time_zone_key=5,
    company="company"
)

result = sdk.crm_contact.put_contact_address_async(
    request_body=request_body,
    contact_key="contactKey",
    address_key="addressKey"
)

print(result)
```

## delete_contact_address_async

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/address/{addressKey}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |
| address_key | str  | ✅       |             |

**Return Type**

`List[ContactAddress]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.delete_contact_address_async(
    contact_key="contactKey",
    address_key="addressKey"
)

print(result)
```

## put_contact_address_role_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/address/{addressKey}/role`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [EditAddressRole](../models/EditAddressRole.md) | ❌       | The request body. |
| contact_key  | str                                             | ✅       |                   |
| address_key  | str                                             | ✅       |                   |

**Return Type**

`List[ContactAddress]`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditAddressRole

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditAddressRole(
    address_roles=[
        "Primary"
    ]
)

result = sdk.crm_contact.put_contact_address_role_async(
    request_body=request_body,
    contact_key="contactKey",
    address_key="addressKey"
)

print(result)
```

## get_contact_notes_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/notes`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

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

result = sdk.crm_contact.get_contact_notes_async(contact_key="contactKey")

print(result)
```

## put_contact_notes_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/notes`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [EditNotes](../models/EditNotes.md) | ❌       | The request body. |
| contact_key  | str                                 | ✅       |                   |

**Return Type**

`Contact`

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

result = sdk.crm_contact.put_contact_notes_async(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

## get_contact_personal_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/personal`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`EditContactPersonal`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.get_contact_personal_async(contact_key="contactKey")

print(result)
```

## put_contact_personal_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/personal`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditContactPersonal](../models/EditContactPersonal.md) | ❌       | The request body. |
| contact_key  | str                                                     | ✅       |                   |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditContactPersonal

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditContactPersonal(
    business="business",
    secretary="secretary",
    other_info="otherInfo",
    keywords="keywords",
    spouse="spouse",
    relationship="relationship",
    dev_stage="devStage",
    go_status="goStatus",
    designations="designations",
    associations="associations",
    functional_role="functionalRole",
    referred_by="referredBy",
    lead_source="leadSource",
    fips="fips",
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

result = sdk.crm_contact.put_contact_personal_async(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

## get_contact_agent_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/agent`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`EditContactAgent`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.get_contact_agent_async(contact_key="contactKey")

print(result)
```

## put_contact_agent_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/agent`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [EditContactAgent](../models/EditContactAgent.md) | ❌       | The request body. |
| contact_key  | str                                               | ✅       |                   |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditContactAgent

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditContactAgent(
    area="area",
    listings="listings",
    reference="reference",
    other="other",
    offices=True,
    apartments=False,
    hotels=True,
    industrial=False,
    investments=False,
    land=False,
    leasing=True,
    residential=False,
    retail=False,
    capital_markets=True,
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

result = sdk.crm_contact.put_contact_agent_async(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

## put_contact_investor_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/investor`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`EditContactInvestor`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.put_contact_investor_async(contact_key="contactKey")

print(result)
```

## put_contact_investor_async_put_api_v1_crm_contact_contact_key_investor

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/investor`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditContactInvestor](../models/EditContactInvestor.md) | ❌       | The request body. |
| contact_key  | str                                                     | ✅       |                   |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditContactInvestor

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditContactInvestor(
    office_rating="officeRating",
    office_min=3.87,
    office_max=9.16,
    industrial_rating="industrialRating",
    industrial_min=5.5,
    industrial_max=1.83,
    retail_rating="retailRating",
    retail_min=5.42,
    retail_max=7.28,
    land_rating="landRating",
    land_min=6.97,
    land_max=2.81,
    apartment_rating="apartmentRating",
    apartment_min=5.01,
    apartment_max=4.2,
    hotel_rating="hotelRating",
    hotel_min=2.28,
    hotel_max=3.32,
    residential_rating="residentialRating",
    residential_min=6.36,
    residential_max=1.8,
    other_rating="otherRating",
    other_min=2.81,
    other_max=0.39,
    min_price=2.71,
    max_price=8.16,
    max_age=3,
    last_purchase="lastPurchase",
    last_purchase_date="lastPurchaseDate",
    last_purchase_price=6.11,
    areas="areas",
    geographic_description="geographicDescription",
    hold_period=9,
    investor_type="investorType",
    reference="reference",
    broker=False,
    rehabs=True,
    joint_venture=True,
    triple_net=True,
    single_tenant=True,
    multiple_tenant=True,
    single_family=False,
    credit_tenant=False,
    num_properties=5,
    business_type="businessType",
    submarket="submarket",
    property_type="propertyType",
    market="market",
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

result = sdk.crm_contact.put_contact_investor_async_put_api_v1_crm_contact_contact_key_investor(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

## get_contact_tenant_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/tenant`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`EditContactTenant`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.get_contact_tenant_async(contact_key="contactKey")

print(result)
```

## put_contact_tenant_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/tenant`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [EditContactTenant](../models/EditContactTenant.md) | ❌       | The request body. |
| contact_key  | str                                                 | ✅       |                   |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditContactTenant

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditContactTenant(
    office=False,
    retail=True,
    industrial=False,
    other=True,
    owner=False,
    in_market=False,
    business_type="businessType",
    num_employees=5,
    num_units=8,
    founded=3,
    sales=9,
    sic_codes="sicCodes",
    rating="rating",
    org_type="orgType",
    min_sqft=2.17,
    max_sqft=7.4,
    location="location",
    office_sqft=3.54,
    acres=7.13,
    buy_lease="buyLease",
    clearance="clearance",
    power="power",
    timing="timing",
    dock_doors=9,
    grade_doors=7,
    other_req="otherReq",
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

result = sdk.crm_contact.put_contact_tenant_async(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

## get_contact_vendor_async

- HTTP Method: `GET`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/vendor`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| contact_key | str  | ✅       |             |

**Return Type**

`EditContactVendor`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.crm_contact.get_contact_vendor_async(contact_key="contactKey")

print(result)
```

## put_contact_vendor_async

- HTTP Method: `PUT`
- Endpoint: `/api/v1/Crm/contact/{contactKey}/vendor`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [EditContactVendor](../models/EditContactVendor.md) | ❌       | The request body. |
| contact_key  | str                                                 | ✅       |                   |

**Return Type**

`Contact`

**Example Usage Code Snippet**

```python
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade
from real_nex_sync_api_data_facade.models import EditContactVendor

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = EditContactVendor(
    business="business",
    rate="rate",
    quality="quality",
    keywords="keywords",
    areas="areas",
    contract_date="contractDate",
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

result = sdk.crm_contact.put_contact_vendor_async(
    request_body=request_body,
    contact_key="contactKey"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
