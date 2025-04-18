# This file was generated by liblab | https://liblab.com/

from typing import List, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.request_error import RequestError
from ..models.utils.cast_models import cast_models
from ..models import (
    Attachment,
    AttachmentPageResponse,
    AttachmentSorting,
    EditAttachment,
)


class CrmAttachmentService(BaseService):

    @cast_models
    def get_attachments_async(self, object_key: str) -> Union[
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        str,
        str,
        bytes,
        str,
    ]:
        """get_attachments_async

        :param object_key: object_key
        :type object_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], str, str, bytes, str]
        """

        Validator(str).validate(object_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/attachment/{{objectKey}}",
                self.get_default_headers(),
            )
            .add_path("objectKey", object_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=minimal":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json":
            return [Attachment._unmap(item) for item in response]
        if content == "application/xml":
            return [Attachment._unmap(item) for item in response]
        if content == "text/plain":
            return [Attachment._unmap(item) for item in response]
        if content == "application/octet-stream":
            return [Attachment._unmap(item) for item in response]
        if content == "text/json":
            return [Attachment._unmap(item) for item in response]
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def post_attachment_async(
        self, object_key: str, request_body: EditAttachment = None
    ) -> Union[
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        List[Attachment],
        str,
        str,
        bytes,
        str,
    ]:
        """post_attachment_async

        :param request_body: The request body., defaults to None
        :type request_body: EditAttachment, optional
        :param object_key: object_key
        :type object_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], List[Attachment], str, str, bytes, str]
        """

        Validator(EditAttachment).is_optional().validate(request_body)
        Validator(str).validate(object_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/attachment/{{objectKey}}",
                self.get_default_headers(),
            )
            .add_path("objectKey", object_key)
            .serialize()
            .set_method("POST")
            .set_body(
                request_body,
                "application/json;odata.metadata=minimal;odata.streaming=true",
            )
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=minimal":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.streaming=true":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json;odata.streaming=false":
            return [Attachment._unmap(item) for item in response]
        if content == "application/json":
            return [Attachment._unmap(item) for item in response]
        if content == "application/xml":
            return [Attachment._unmap(item) for item in response]
        if content == "text/plain":
            return [Attachment._unmap(item) for item in response]
        if content == "application/octet-stream":
            return [Attachment._unmap(item) for item in response]
        if content == "text/json":
            return [Attachment._unmap(item) for item in response]
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def get_attachment_async(self, object_key: str, attachment_key: str) -> Union[
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        Attachment,
        str,
        str,
        bytes,
        str,
    ]:
        """get_attachment_async

        :param object_key: object_key
        :type object_key: str
        :param attachment_key: attachment_key
        :type attachment_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Attachment, Attachment, Attachment, Attachment, Attachment, Attachment, Attachment, Attachment, Attachment, Attachment, Attachment, Attachment, str, str, bytes, str]
        """

        Validator(str).validate(object_key)
        Validator(str).validate(attachment_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/attachment/{{objectKey}}/{{attachmentKey}}",
                self.get_default_headers(),
            )
            .add_path("objectKey", object_key)
            .add_path("attachmentKey", attachment_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=full":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return Attachment._unmap(response)
        if content == "application/json;odata.metadata=none":
            return Attachment._unmap(response)
        if content == "application/json;odata.streaming=true":
            return Attachment._unmap(response)
        if content == "application/json;odata.streaming=false":
            return Attachment._unmap(response)
        if content == "application/json":
            return Attachment._unmap(response)
        if content == "application/xml":
            return Attachment._unmap(response)
        if content == "text/plain":
            return Attachment._unmap(response)
        if content == "application/octet-stream":
            return Attachment._unmap(response)
        if content == "text/json":
            return Attachment._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def put_attachment_async(
        self, object_key: str, attachment_key: str, request_body: EditAttachment = None
    ) -> Union[
        str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str
    ]:
        """put_attachment_async

        :param request_body: The request body., defaults to None
        :type request_body: EditAttachment, optional
        :param object_key: object_key
        :type object_key: str
        :param attachment_key: attachment_key
        :type attachment_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str]
        """

        Validator(EditAttachment).is_optional().validate(request_body)
        Validator(str).validate(object_key)
        Validator(str).validate(attachment_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/attachment/{{objectKey}}/{{attachmentKey}}",
                self.get_default_headers(),
            )
            .add_path("objectKey", object_key)
            .add_path("attachmentKey", attachment_key)
            .serialize()
            .set_method("PUT")
            .set_body(
                request_body,
                "application/json;odata.metadata=minimal;odata.streaming=true",
            )
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
    def get_attachment_file_async(self, object_key: str, attachment_key: str) -> Union[
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        bytes,
        str,
        str,
        bytes,
        str,
    ]:
        """get_attachment_file_async

        :param object_key: object_key
        :type object_key: str
        :param attachment_key: attachment_key
        :type attachment_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, str, str, bytes, str]
        """

        Validator(str).validate(object_key)
        Validator(str).validate(attachment_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/attachment/{{objectKey}}/{{attachmentKey}}/file",
                self.get_default_headers(),
            )
            .add_path("objectKey", object_key)
            .add_path("attachmentKey", attachment_key)
            .serialize()
            .set_method("GET")
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
    def get_object_attachments_async(
        self,
        object_key: str,
        order: AttachmentSorting = None,
        page_size: int = None,
        page_number: int = None,
    ) -> Union[
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        AttachmentPageResponse,
        str,
        str,
        bytes,
        str,
    ]:
        """get_object_attachments_async

        :param object_key: object_key
        :type object_key: str
        :param order: order, defaults to None
        :type order: AttachmentSorting, optional
        :param page_size: page_size, defaults to None
        :type page_size: int, optional
        :param page_number: page_number, defaults to None
        :type page_number: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, AttachmentPageResponse, str, str, bytes, str]
        """

        Validator(str).validate(object_key)
        Validator(AttachmentSorting).is_optional().validate(order)
        Validator(int).is_optional().validate(page_size)
        Validator(int).is_optional().validate(page_number)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/object/{{objectKey}}/attachments",
                self.get_default_headers(),
            )
            .add_path("objectKey", object_key)
            .add_query("Order", order)
            .add_query("PageSize", page_size)
            .add_query("PageNumber", page_number)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=full":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.metadata=none":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.streaming=true":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json;odata.streaming=false":
            return AttachmentPageResponse._unmap(response)
        if content == "application/json":
            return AttachmentPageResponse._unmap(response)
        if content == "application/xml":
            return AttachmentPageResponse._unmap(response)
        if content == "text/plain":
            return AttachmentPageResponse._unmap(response)
        if content == "application/octet-stream":
            return AttachmentPageResponse._unmap(response)
        if content == "text/json":
            return AttachmentPageResponse._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)
