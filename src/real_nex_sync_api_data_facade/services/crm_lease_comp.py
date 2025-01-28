# This file was generated by liblab | https://liblab.com/

from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.request_error import RequestError
from ..models.utils.cast_models import cast_models
from ..models import (
    CreateLeaseComp,
    EditLeaseComp,
    EditLeaseCompDetails,
    EditNotes,
    LeaseComp,
)


class CrmLeaseCompService(BaseService):

    @cast_models
    def get_lease_comp_async(self, lease_comp_key: str) -> Union[
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        str,
        str,
        bytes,
        str,
    ]:
        """get_lease_comp_async

        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, str, str, bytes, str]
        """

        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}/full",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json":
            return LeaseComp._unmap(response)
        if content == "application/xml":
            return LeaseComp._unmap(response)
        if content == "text/plain":
            return LeaseComp._unmap(response)
        if content == "application/octet-stream":
            return LeaseComp._unmap(response)
        if content == "text/json":
            return LeaseComp._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def post_lease_comp_async(self, request_body: CreateLeaseComp = None) -> Union[
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        str,
        str,
        bytes,
        str,
    ]:
        """post_lease_comp_async

        :param request_body: The request body., defaults to None
        :type request_body: CreateLeaseComp, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, str, str, bytes, str]
        """

        Validator(CreateLeaseComp).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(
                request_body,
                "application/json;odata.metadata=minimal;odata.streaming=true",
            )
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json":
            return LeaseComp._unmap(response)
        if content == "application/xml":
            return LeaseComp._unmap(response)
        if content == "text/plain":
            return LeaseComp._unmap(response)
        if content == "application/octet-stream":
            return LeaseComp._unmap(response)
        if content == "text/json":
            return LeaseComp._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def get_edit_lease_comp_async(self, lease_comp_key: str) -> Union[
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        EditLeaseComp,
        str,
        str,
        bytes,
        str,
    ]:
        """get_edit_lease_comp_async

        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, EditLeaseComp, str, str, bytes, str]
        """

        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.streaming=true":
            return EditLeaseComp._unmap(response)
        if content == "application/json;odata.streaming=false":
            return EditLeaseComp._unmap(response)
        if content == "application/json":
            return EditLeaseComp._unmap(response)
        if content == "application/xml":
            return EditLeaseComp._unmap(response)
        if content == "text/plain":
            return EditLeaseComp._unmap(response)
        if content == "application/octet-stream":
            return EditLeaseComp._unmap(response)
        if content == "text/json":
            return EditLeaseComp._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def put_edit_lease_comp_async(
        self, lease_comp_key: str, request_body: EditLeaseComp = None
    ) -> Union[
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        str,
        str,
        bytes,
        str,
    ]:
        """put_edit_lease_comp_async

        :param request_body: The request body., defaults to None
        :type request_body: EditLeaseComp, optional
        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, str, str, bytes, str]
        """

        Validator(EditLeaseComp).is_optional().validate(request_body)
        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("PUT")
            .set_body(request_body, "application/merge-patch+json")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json":
            return LeaseComp._unmap(response)
        if content == "application/xml":
            return LeaseComp._unmap(response)
        if content == "text/plain":
            return LeaseComp._unmap(response)
        if content == "application/octet-stream":
            return LeaseComp._unmap(response)
        if content == "text/json":
            return LeaseComp._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_lease_comp_async(
        self, lease_comp_key: str
    ) -> Union[
        str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str
    ]:
        """delete_lease_comp_async

        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str]
        """

        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return response
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return response
        if content == "application/json;odata.metadata=minimal":
            return response
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return response
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return response
        if content == "application/json;odata.metadata=full":
            return response
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return response
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return response
        if content == "application/json;odata.metadata=none":
            return response
        if content == "application/json;odata.streaming=true":
            return response
        if content == "application/json;odata.streaming=false":
            return response
        if content == "application/json":
            return response
        if content == "application/xml":
            return response
        if content == "text/plain":
            return response
        if content == "application/octet-stream":
            return response
        if content == "text/json":
            return response
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def get_lease_comp_notes_async(self, lease_comp_key: str) -> Union[
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        EditNotes,
        str,
        str,
        bytes,
        str,
    ]:
        """get_lease_comp_notes_async

        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, EditNotes, str, str, bytes, str]
        """

        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}/notes",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=full":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return EditNotes._unmap(response)
        if content == "application/json;odata.metadata=none":
            return EditNotes._unmap(response)
        if content == "application/json;odata.streaming=true":
            return EditNotes._unmap(response)
        if content == "application/json;odata.streaming=false":
            return EditNotes._unmap(response)
        if content == "application/json":
            return EditNotes._unmap(response)
        if content == "application/xml":
            return EditNotes._unmap(response)
        if content == "text/plain":
            return EditNotes._unmap(response)
        if content == "application/octet-stream":
            return EditNotes._unmap(response)
        if content == "text/json":
            return EditNotes._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def put_lease_comp_notes_async(
        self, lease_comp_key: str, request_body: EditNotes = None
    ) -> Union[
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        str,
        str,
        bytes,
        str,
    ]:
        """put_lease_comp_notes_async

        :param request_body: The request body., defaults to None
        :type request_body: EditNotes, optional
        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, str, str, bytes, str]
        """

        Validator(EditNotes).is_optional().validate(request_body)
        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}/notes",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("PUT")
            .set_body(
                request_body,
                "application/json;odata.metadata=minimal;odata.streaming=true",
            )
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json":
            return LeaseComp._unmap(response)
        if content == "application/xml":
            return LeaseComp._unmap(response)
        if content == "text/plain":
            return LeaseComp._unmap(response)
        if content == "application/octet-stream":
            return LeaseComp._unmap(response)
        if content == "text/json":
            return LeaseComp._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def get_lease_comp_details_async(self, lease_comp_key: str) -> Union[
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        EditLeaseCompDetails,
        str,
        str,
        bytes,
        str,
    ]:
        """get_lease_comp_details_async

        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, EditLeaseCompDetails, str, str, bytes, str]
        """

        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}/details",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=full":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.metadata=none":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.streaming=true":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json;odata.streaming=false":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/json":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/xml":
            return EditLeaseCompDetails._unmap(response)
        if content == "text/plain":
            return EditLeaseCompDetails._unmap(response)
        if content == "application/octet-stream":
            return EditLeaseCompDetails._unmap(response)
        if content == "text/json":
            return EditLeaseCompDetails._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def put_lease_comp_details_async(
        self, lease_comp_key: str, request_body: EditLeaseCompDetails = None
    ) -> Union[
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        LeaseComp,
        str,
        str,
        bytes,
        str,
    ]:
        """put_lease_comp_details_async

        :param request_body: The request body., defaults to None
        :type request_body: EditLeaseCompDetails, optional
        :param lease_comp_key: lease_comp_key
        :type lease_comp_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, LeaseComp, str, str, bytes, str]
        """

        Validator(EditLeaseCompDetails).is_optional().validate(request_body)
        Validator(str).validate(lease_comp_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/leasecomp/{{leaseCompKey}}/details",
                self.get_default_headers(),
            )
            .add_path("leaseCompKey", lease_comp_key)
            .serialize()
            .set_method("PUT")
            .set_body(request_body, "application/merge-patch+json")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=full":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.metadata=none":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=true":
            return LeaseComp._unmap(response)
        if content == "application/json;odata.streaming=false":
            return LeaseComp._unmap(response)
        if content == "application/json":
            return LeaseComp._unmap(response)
        if content == "application/xml":
            return LeaseComp._unmap(response)
        if content == "text/plain":
            return LeaseComp._unmap(response)
        if content == "application/octet-stream":
            return LeaseComp._unmap(response)
        if content == "text/json":
            return LeaseComp._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)
