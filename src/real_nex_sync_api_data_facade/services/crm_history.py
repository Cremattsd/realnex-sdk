# This file was generated by liblab | https://liblab.com/

from typing import List, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.request_error import RequestError
from ..models.utils.cast_models import cast_models
from ..models import (
    EditHistory,
    History,
    HistoryDetails,
    HistoryObject,
    HistoryPageResponse,
    HistorySorting,
)


class CrmHistoryService(BaseService):

    @cast_models
    def get_history_async(self, history_key: str) -> Union[
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        EditHistory,
        str,
        str,
        bytes,
        str,
    ]:
        """get_history_async

        :param history_key: history_key
        :type history_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, EditHistory, str, str, bytes, str]
        """

        Validator(str).validate(history_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=full":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return EditHistory._unmap(response)
        if content == "application/json;odata.metadata=none":
            return EditHistory._unmap(response)
        if content == "application/json;odata.streaming=true":
            return EditHistory._unmap(response)
        if content == "application/json;odata.streaming=false":
            return EditHistory._unmap(response)
        if content == "application/json":
            return EditHistory._unmap(response)
        if content == "application/xml":
            return EditHistory._unmap(response)
        if content == "text/plain":
            return EditHistory._unmap(response)
        if content == "application/octet-stream":
            return EditHistory._unmap(response)
        if content == "text/json":
            return EditHistory._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def put_history_async(
        self, history_key: str, request_body: EditHistory = None
    ) -> Union[
        str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str
    ]:
        """put_history_async

        :param request_body: The request body., defaults to None
        :type request_body: EditHistory, optional
        :param history_key: history_key
        :type history_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str]
        """

        Validator(EditHistory).is_optional().validate(request_body)
        Validator(str).validate(history_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
            .serialize()
            .set_method("PUT")
            .set_body(request_body, "application/merge-patch+json")
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
    def delete_history_async(
        self, history_key: str
    ) -> Union[
        str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str
    ]:
        """delete_history_async

        :param history_key: history_key
        :type history_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str]
        """

        Validator(str).validate(history_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
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
    def get_history_details_async(self, history_key: str) -> Union[
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        HistoryDetails,
        str,
        str,
        bytes,
        str,
    ]:
        """get_history_details_async

        :param history_key: history_key
        :type history_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, HistoryDetails, str, str, bytes, str]
        """

        Validator(str).validate(history_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}/details",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=full":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.metadata=none":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.streaming=true":
            return HistoryDetails._unmap(response)
        if content == "application/json;odata.streaming=false":
            return HistoryDetails._unmap(response)
        if content == "application/json":
            return HistoryDetails._unmap(response)
        if content == "application/xml":
            return HistoryDetails._unmap(response)
        if content == "text/plain":
            return HistoryDetails._unmap(response)
        if content == "application/octet-stream":
            return HistoryDetails._unmap(response)
        if content == "text/json":
            return HistoryDetails._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def post_history_async(self, request_body: EditHistory = None) -> Union[
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        str,
        str,
        bytes,
        str,
    ]:
        """post_history_async

        :param request_body: The request body., defaults to None
        :type request_body: EditHistory, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[History, History, History, History, History, History, History, History, History, History, History, History, str, str, bytes, str]
        """

        Validator(EditHistory).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history", self.get_default_headers()
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
            return History._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return History._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return History._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json;odata.metadata=full":
            return History._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return History._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json;odata.metadata=none":
            return History._unmap(response)
        if content == "application/json;odata.streaming=true":
            return History._unmap(response)
        if content == "application/json;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json":
            return History._unmap(response)
        if content == "application/xml":
            return History._unmap(response)
        if content == "text/plain":
            return History._unmap(response)
        if content == "application/octet-stream":
            return History._unmap(response)
        if content == "text/json":
            return History._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def get_history_objects_async(self, history_key: str) -> Union[
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        List[HistoryObject],
        str,
        str,
        bytes,
        str,
    ]:
        """get_history_objects_async

        :param history_key: history_key
        :type history_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], List[HistoryObject], str, str, bytes, str]
        """

        Validator(str).validate(history_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}/object",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json;odata.metadata=minimal;odata.streaming=true":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=minimal":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=full":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.metadata=none":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.streaming=true":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json;odata.streaming=false":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/json":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/xml":
            return [HistoryObject._unmap(item) for item in response]
        if content == "text/plain":
            return [HistoryObject._unmap(item) for item in response]
        if content == "application/octet-stream":
            return [HistoryObject._unmap(item) for item in response]
        if content == "text/json":
            return [HistoryObject._unmap(item) for item in response]
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def post_history_objects_async(
        self, history_key: str, request_body: List[HistoryObject] = None
    ) -> Union[
        str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str
    ]:
        """post_history_objects_async

        :param request_body: The request body., defaults to None
        :type request_body: List[HistoryObject], optional
        :param history_key: history_key
        :type history_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str]
        """

        Validator(HistoryObject).is_array().is_optional().validate(request_body)
        Validator(str).validate(history_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}/object",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
            .serialize()
            .set_method("POST")
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
    def delete_history_objects_async(
        self, history_key: str, object_key: str
    ) -> Union[
        str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str
    ]:
        """delete_history_objects_async

        :param history_key: history_key
        :type history_key: str
        :param object_key: object_key
        :type object_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, str, str, str, str, str, str, str, str, str, str, str, str, str, bytes, str]
        """

        Validator(str).validate(history_key)
        Validator(str).validate(object_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}/object/{{objectKey}}",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
            .add_path("objectKey", object_key)
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
    def get_object_histories_async(
        self,
        object_key: str,
        order: HistorySorting = None,
        page_size: int = None,
        page_number: int = None,
    ) -> Union[
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        HistoryPageResponse,
        str,
        str,
        bytes,
        str,
    ]:
        """get_object_histories_async

        :param object_key: object_key
        :type object_key: str
        :param order: order, defaults to None
        :type order: HistorySorting, optional
        :param page_size: page_size, defaults to None
        :type page_size: int, optional
        :param page_number: page_number, defaults to None
        :type page_number: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, HistoryPageResponse, str, str, bytes, str]
        """

        Validator(str).validate(object_key)
        Validator(HistorySorting).is_optional().validate(order)
        Validator(int).is_optional().validate(page_size)
        Validator(int).is_optional().validate(page_number)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/object/{{objectKey}}/history",
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
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=full":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.metadata=none":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.streaming=true":
            return HistoryPageResponse._unmap(response)
        if content == "application/json;odata.streaming=false":
            return HistoryPageResponse._unmap(response)
        if content == "application/json":
            return HistoryPageResponse._unmap(response)
        if content == "application/xml":
            return HistoryPageResponse._unmap(response)
        if content == "text/plain":
            return HistoryPageResponse._unmap(response)
        if content == "application/octet-stream":
            return HistoryPageResponse._unmap(response)
        if content == "text/json":
            return HistoryPageResponse._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def post_object_history_async(
        self, object_key: str, request_body: EditHistory = None
    ) -> Union[
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        History,
        str,
        str,
        bytes,
        str,
    ]:
        """post_object_history_async

        :param request_body: The request body., defaults to None
        :type request_body: EditHistory, optional
        :param object_key: object_key
        :type object_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[History, History, History, History, History, History, History, History, History, History, History, History, str, str, bytes, str]
        """

        Validator(EditHistory).is_optional().validate(request_body)
        Validator(str).validate(object_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/object/{{objectKey}}/history",
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
            return History._unmap(response)
        if content == "application/json;odata.metadata=minimal;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json;odata.metadata=minimal":
            return History._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=true":
            return History._unmap(response)
        if content == "application/json;odata.metadata=full;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json;odata.metadata=full":
            return History._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=true":
            return History._unmap(response)
        if content == "application/json;odata.metadata=none;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json;odata.metadata=none":
            return History._unmap(response)
        if content == "application/json;odata.streaming=true":
            return History._unmap(response)
        if content == "application/json;odata.streaming=false":
            return History._unmap(response)
        if content == "application/json":
            return History._unmap(response)
        if content == "application/xml":
            return History._unmap(response)
        if content == "text/plain":
            return History._unmap(response)
        if content == "application/octet-stream":
            return History._unmap(response)
        if content == "text/json":
            return History._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)

    @cast_models
    def get_history_file_async(self, history_key: str) -> Union[
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
        None,
    ]:
        """get_history_file_async

        :param history_key: history_key
        :type history_key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes, str, str, bytes, str, None]
        """

        Validator(str).validate(history_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v1/Crm/history/{{historyKey}}/file",
                self.get_default_headers(),
            )
            .add_path("historyKey", history_key)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if (
            status == 200
            and content
            == "application/json;odata.metadata=minimal;odata.streaming=true"
        ):
            return response
        if (
            status == 200
            and content
            == "application/json;odata.metadata=minimal;odata.streaming=false"
        ):
            return response
        if status == 200 and content == "application/json;odata.metadata=minimal":
            return response
        if (
            status == 200
            and content == "application/json;odata.metadata=full;odata.streaming=true"
        ):
            return response
        if (
            status == 200
            and content == "application/json;odata.metadata=full;odata.streaming=false"
        ):
            return response
        if status == 200 and content == "application/json;odata.metadata=full":
            return response
        if (
            status == 200
            and content == "application/json;odata.metadata=none;odata.streaming=true"
        ):
            return response
        if (
            status == 200
            and content == "application/json;odata.metadata=none;odata.streaming=false"
        ):
            return response
        if status == 200 and content == "application/json;odata.metadata=none":
            return response
        if status == 200 and content == "application/json;odata.streaming=true":
            return response
        if status == 200 and content == "application/json;odata.streaming=false":
            return response
        if status == 200 and content == "application/json":
            return response
        if status == 200 and content == "application/xml":
            return response
        if status == 200 and content == "text/plain":
            return response
        if status == 200 and content == "application/octet-stream":
            return response
        if status == 200 and content == "text/json":
            return response
        if status == 204 and not response:
            return response
        raise RequestError("Error on deserializing the response.", status, response)
