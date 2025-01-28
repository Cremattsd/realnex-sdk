# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .edit_address import EditAddress


@JsonMap(
    {
        "user_key": "userKey",
        "team_key": "teamKey",
        "property_name": "propertyName",
        "property_type_key": "propertyTypeKey",
        "address_number1": "addressNumber1",
        "address_number2": "addressNumber2",
        "address_direction": "addressDirection",
        "address_street": "addressStreet",
        "address_suite": "addressSuite",
        "cross_streets": "crossStreets",
        "for_sale": "forSale",
        "for_lease": "forLease",
        "owner_principal_key": "ownerPrincipalKey",
        "site_principal_key": "sitePrincipalKey",
        "agent_principal_key": "agentPrincipalKey",
    }
)
class EditProperty(BaseModel):
    """EditProperty

    :param user_key: user_key, defaults to None
    :type user_key: str, optional
    :param team_key: team_key, defaults to None
    :type team_key: str, optional
    :param property_name: property_name, defaults to None
    :type property_name: str, optional
    :param address: address, defaults to None
    :type address: EditAddress, optional
    :param property_type_key: property_type_key, defaults to None
    :type property_type_key: int, optional
    :param address_number1: address_number1, defaults to None
    :type address_number1: str, optional
    :param address_number2: address_number2, defaults to None
    :type address_number2: str, optional
    :param address_direction: address_direction, defaults to None
    :type address_direction: str, optional
    :param address_street: address_street, defaults to None
    :type address_street: str, optional
    :param address_suite: address_suite, defaults to None
    :type address_suite: str, optional
    :param cross_streets: cross_streets, defaults to None
    :type cross_streets: str, optional
    :param for_sale: for_sale, defaults to None
    :type for_sale: bool, optional
    :param for_lease: for_lease, defaults to None
    :type for_lease: bool, optional
    :param owner_principal_key: owner_principal_key, defaults to None
    :type owner_principal_key: str, optional
    :param site_principal_key: site_principal_key, defaults to None
    :type site_principal_key: str, optional
    :param agent_principal_key: agent_principal_key, defaults to None
    :type agent_principal_key: str, optional
    """

    def __init__(
        self,
        user_key: str = None,
        team_key: str = None,
        property_name: str = None,
        address: EditAddress = None,
        property_type_key: int = None,
        address_number1: str = None,
        address_number2: str = None,
        address_direction: str = None,
        address_street: str = None,
        address_suite: str = None,
        cross_streets: str = None,
        for_sale: bool = None,
        for_lease: bool = None,
        owner_principal_key: str = None,
        site_principal_key: str = None,
        agent_principal_key: str = None,
        **kwargs,
    ):
        """EditProperty

        :param user_key: user_key, defaults to None
        :type user_key: str, optional
        :param team_key: team_key, defaults to None
        :type team_key: str, optional
        :param property_name: property_name, defaults to None
        :type property_name: str, optional
        :param address: address, defaults to None
        :type address: EditAddress, optional
        :param property_type_key: property_type_key, defaults to None
        :type property_type_key: int, optional
        :param address_number1: address_number1, defaults to None
        :type address_number1: str, optional
        :param address_number2: address_number2, defaults to None
        :type address_number2: str, optional
        :param address_direction: address_direction, defaults to None
        :type address_direction: str, optional
        :param address_street: address_street, defaults to None
        :type address_street: str, optional
        :param address_suite: address_suite, defaults to None
        :type address_suite: str, optional
        :param cross_streets: cross_streets, defaults to None
        :type cross_streets: str, optional
        :param for_sale: for_sale, defaults to None
        :type for_sale: bool, optional
        :param for_lease: for_lease, defaults to None
        :type for_lease: bool, optional
        :param owner_principal_key: owner_principal_key, defaults to None
        :type owner_principal_key: str, optional
        :param site_principal_key: site_principal_key, defaults to None
        :type site_principal_key: str, optional
        :param agent_principal_key: agent_principal_key, defaults to None
        :type agent_principal_key: str, optional
        """
        if user_key is not None:
            self.user_key = self._define_str("user_key", user_key, nullable=True)
        if team_key is not None:
            self.team_key = self._define_str("team_key", team_key, nullable=True)
        if property_name is not None:
            self.property_name = self._define_str(
                "property_name", property_name, nullable=True
            )
        if address is not None:
            self.address = self._define_object(address, EditAddress)
        if property_type_key is not None:
            self.property_type_key = self._define_number(
                "property_type_key", property_type_key, nullable=True
            )
        if address_number1 is not None:
            self.address_number1 = self._define_str(
                "address_number1", address_number1, nullable=True
            )
        if address_number2 is not None:
            self.address_number2 = self._define_str(
                "address_number2", address_number2, nullable=True
            )
        if address_direction is not None:
            self.address_direction = self._define_str(
                "address_direction", address_direction, nullable=True
            )
        if address_street is not None:
            self.address_street = self._define_str(
                "address_street", address_street, nullable=True
            )
        if address_suite is not None:
            self.address_suite = self._define_str(
                "address_suite", address_suite, nullable=True
            )
        if cross_streets is not None:
            self.cross_streets = self._define_str(
                "cross_streets", cross_streets, nullable=True
            )
        if for_sale is not None:
            self.for_sale = for_sale
        if for_lease is not None:
            self.for_lease = for_lease
        if owner_principal_key is not None:
            self.owner_principal_key = self._define_str(
                "owner_principal_key", owner_principal_key, nullable=True
            )
        if site_principal_key is not None:
            self.site_principal_key = self._define_str(
                "site_principal_key", site_principal_key, nullable=True
            )
        if agent_principal_key is not None:
            self.agent_principal_key = self._define_str(
                "agent_principal_key", agent_principal_key, nullable=True
            )
        self._kwargs = kwargs
