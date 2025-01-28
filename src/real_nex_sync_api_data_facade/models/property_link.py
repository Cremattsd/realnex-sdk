# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address


@JsonMap({"property_name": "propertyName"})
class PropertyLink(BaseModel):
    """PropertyLink

    :param key: key, defaults to None
    :type key: str, optional
    :param property_name: property_name, defaults to None
    :type property_name: str, optional
    :param address: address, defaults to None
    :type address: Address, optional
    """

    def __init__(
        self,
        key: str = None,
        property_name: str = None,
        address: Address = None,
        **kwargs,
    ):
        """PropertyLink

        :param key: key, defaults to None
        :type key: str, optional
        :param property_name: property_name, defaults to None
        :type property_name: str, optional
        :param address: address, defaults to None
        :type address: Address, optional
        """
        if key is not None:
            self.key = self._define_str("key", key, nullable=True)
        if property_name is not None:
            self.property_name = self._define_str(
                "property_name", property_name, nullable=True
            )
        if address is not None:
            self.address = self._define_object(address, Address)
        self._kwargs = kwargs
