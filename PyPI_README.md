# RealNexSyncApiDataFacade Python SDK 1.0.0<a id="realnexsyncapidatafacade-python-sdk-100"></a>

Welcome to the RealNexSyncApiDataFacade SDK documentation. This guide will help you get started with integrating and using the RealNexSyncApiDataFacade SDK in your project.

[![This SDK was generated by liblab](https://public-liblab-readme-assets.s3.us-east-1.amazonaws.com/built-by-liblab-icon.svg)](https://liblab.com/?utm_source=readme)

## Versions<a id="versions"></a>

- API version: `1.0`
- SDK version: `1.0.0`

## Table of Contents<a id="table-of-contents"></a>

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [API Key Authentication](#api-key-authentication)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)

## Setup & Configuration<a id="setup--configuration"></a>

### Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install real_nex_sync_api_data_facade
```

## Authentication<a id="authentication"></a>

### API Key Authentication<a id="api-key-authentication"></a>

The RealNexSyncApiDataFacade API uses API keys as a form of authentication. An API key is a unique identifier used to authenticate a user, developer, or a program that is calling the API.

#### Setting the API key<a id="setting-the-api-key"></a>

When you initialize the SDK, you can set the API key as follows:

```py
RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)
```

If you need to set or update the API key after initializing the SDK, you can use:

```py
sdk.set_api_key("YOUR_API_KEY", "YOUR_API_KEY_HEADER")
```

## Setting a Custom Timeout<a id="setting-a-custom-timeout"></a>

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(timeout=10000)
```

# Sample Usage<a id="sample-usage"></a>

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

sdk = RealNexSyncApiDataFacade(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.client.get_user(api_version="1.0")

print(result)

```

## Services<a id="services"></a>

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services:</summary>

| Name             |
| :--------------- |
| client           |
| crm              |
| crm_attachment   |
| crm_company      |
| crm_contact      |
| crm_event        |
| crm_history      |
| crm_lease_comp   |
| crm_object_group |
| crm_o_data       |
| crm_project      |
| crm_property     |
| crm_sale_comp    |
| crm_space        |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                                  | Description |
| :------------------------------------ | :---------- |
| ClientInfo                            |             |
| ClientCallbacks                       |             |
| ClientRetrySettings                   |             |
| FieldDefinition                       |             |
| User                                  |             |
| Team                                  |             |
| Attachment                            |             |
| EditAttachment                        |             |
| AttachmentPageResponse                |             |
| AttachmentSorting                     |             |
| Company                               |             |
| EditCompany                           |             |
| CreateCompany                         |             |
| EditNotes                             |             |
| EditCompanyDetails                    |             |
| Contact                               |             |
| EditContact                           |             |
| CreateContact                         |             |
| ContactAddress                        |             |
| EditAddressPrincipal                  |             |
| EditAddressRole                       |             |
| EditContactPersonal                   |             |
| EditContactAgent                      |             |
| EditContactInvestor                   |             |
| EditContactTenant                     |             |
| EditContactVendor                     |             |
| EventDetails                          |             |
| EditEvent                             |             |
| Event                                 |             |
| EventObject                           |             |
| EventParticipant                      |             |
| EventPageResponse                     |             |
| EventSorting                          |             |
| EditHistory                           |             |
| HistoryDetails                        |             |
| History                               |             |
| HistoryObject                         |             |
| HistoryPageResponse                   |             |
| HistorySorting                        |             |
| LeaseComp                             |             |
| CreateLeaseComp                       |             |
| EditLeaseComp                         |             |
| EditLeaseCompDetails                  |             |
| ObjectGroupPageResponse               |             |
| ObjectType                            |             |
| ObjectGroupSorting                    |             |
| EditObjectGroup                       |             |
| ObjectGroup                           |             |
| ObjectGroupDetails                    |             |
| ObjectGroupMemberPageResponse         |             |
| ObjectGroupMember                     |             |
| ContactListItem                       |             |
| CompanyListItem                       |             |
| PropertyListItem                      |             |
| SpaceListItem                         |             |
| ProjectListItem                       |             |
| LeaseCompListItem                     |             |
| SaleCompListItem                      |             |
| Project                               |             |
| CreateProject                         |             |
| EditProject                           |             |
| EditProjectDetails                    |             |
| ProjectLead                           |             |
| LeadObjectType                        |             |
| ProjectLeadSorting                    |             |
| EditProjectLead                       |             |
| EditProjectLeadJsonMergePatchDocument |             |
| Property                              |             |
| CreateProperty                        |             |
| EditProperty                          |             |
| EditPropertyDetails                   |             |
| EditPropertyUsage                     |             |
| EditPropertyListingForLease           |             |
| EditPropertyListingForSale            |             |
| SaleComp                              |             |
| CreateSaleComp                        |             |
| EditSaleComp                          |             |
| EditSaleCompDetails                   |             |
| EditSaleCompListing                   |             |
| EditSaleCompUsage                     |             |
| Space                                 |             |
| PropertySpace                         |             |
| CreateSpace                           |             |
| EditSpace                             |             |
| EditSpaceDetails                      |             |
| Int32KeyNameObject                    |             |
| Base64File                            |             |
| GuidKeyNameObject                     |             |
| Address                               |             |
| CompanyDetails                        |             |
| UserFields                            |             |
| UserDataFields                        |             |
| LogicalFields                         |             |
| ContactInvestor                       |             |
| ContactTenant                         |             |
| ContactAgent                          |             |
| ContactVendor                         |             |
| ContactPersonal                       |             |
| ContactTenantSpace                    |             |
| ContactAddressRole                    |             |
| ObjectLink                            |             |
| PrincipalLink                         |             |
| CompSpace                             |             |
| CompContact                           |             |
| LeaseCompDetails                      |             |
| PrincipalType                         |             |
| EditCompSpace                         |             |
| EditCompContact                       |             |
| EditAddress                           |             |
| ObjectGroupListItem                   |             |
| SaleCompDetails                       |             |
| SaleCompUsage                         |             |
| ContactLink                           |             |
| CompanyLink                           |             |
| PropertyLink                          |             |
| SpaceLink                             |             |
| PropertyContact                       |             |
| PropertyListingForSale                |             |
| PropertyListingForLease               |             |
| PropertyUsage                         |             |
| PropertyContactRole                   |             |
| CompProperty                          |             |
| SaleCompListing                       |             |
| EditCompProperty                      |             |

</details>

<!-- This file was generated by liblab | https://liblab.com/ -->
