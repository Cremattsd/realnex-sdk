from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.request_error import RequestError
from ..models.utils.cast_models import cast_models
from ..models import ClientInfo


class ClientService(BaseService):
    def __init__(self, base_url="https://sync.realnex.com/api"):  # ✅ Ensure base_url is passed
        super().__init__(base_url=base_url)  
        self.base_url = base_url  

    @cast_models
    def get_user(self, api_version: str = None) -> Union[ClientInfo, str]:
        """Fetch user info using API Key."""

        Validator(str).is_optional().validate(api_version)

        request_url = f"{self.base_url}/Client"  

        serialized_request = (
            Serializer(request_url, self.get_default_headers())
            .add_query("api-version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)

        if content.startswith("application/json"):
            return ClientInfo._unmap(response)
        raise RequestError("Error on deserializing the response.", status, response)
