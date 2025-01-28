# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .user_fields import UserFields
from .user_data_fields import UserDataFields
from .logical_fields import LogicalFields


@JsonMap(
    {
        "capital_markets": "capitalMarkets",
        "user_fields": "userFields",
        "user_data_fields": "userDataFields",
        "logical_fields": "logicalFields",
    }
)
class EditContactAgent(BaseModel):
    """EditContactAgent

    :param area: area, defaults to None
    :type area: str, optional
    :param listings: listings, defaults to None
    :type listings: str, optional
    :param reference: reference, defaults to None
    :type reference: str, optional
    :param other: other, defaults to None
    :type other: str, optional
    :param offices: offices, defaults to None
    :type offices: bool, optional
    :param apartments: apartments, defaults to None
    :type apartments: bool, optional
    :param hotels: hotels, defaults to None
    :type hotels: bool, optional
    :param industrial: industrial, defaults to None
    :type industrial: bool, optional
    :param investments: investments, defaults to None
    :type investments: bool, optional
    :param land: land, defaults to None
    :type land: bool, optional
    :param leasing: leasing, defaults to None
    :type leasing: bool, optional
    :param residential: residential, defaults to None
    :type residential: bool, optional
    :param retail: retail, defaults to None
    :type retail: bool, optional
    :param capital_markets: capital_markets, defaults to None
    :type capital_markets: bool, optional
    :param user_fields: user_fields, defaults to None
    :type user_fields: UserFields, optional
    :param user_data_fields: user_data_fields, defaults to None
    :type user_data_fields: UserDataFields, optional
    :param logical_fields: logical_fields, defaults to None
    :type logical_fields: LogicalFields, optional
    """

    def __init__(
        self,
        area: str = None,
        listings: str = None,
        reference: str = None,
        other: str = None,
        offices: bool = None,
        apartments: bool = None,
        hotels: bool = None,
        industrial: bool = None,
        investments: bool = None,
        land: bool = None,
        leasing: bool = None,
        residential: bool = None,
        retail: bool = None,
        capital_markets: bool = None,
        user_fields: UserFields = None,
        user_data_fields: UserDataFields = None,
        logical_fields: LogicalFields = None,
        **kwargs,
    ):
        """EditContactAgent

        :param area: area, defaults to None
        :type area: str, optional
        :param listings: listings, defaults to None
        :type listings: str, optional
        :param reference: reference, defaults to None
        :type reference: str, optional
        :param other: other, defaults to None
        :type other: str, optional
        :param offices: offices, defaults to None
        :type offices: bool, optional
        :param apartments: apartments, defaults to None
        :type apartments: bool, optional
        :param hotels: hotels, defaults to None
        :type hotels: bool, optional
        :param industrial: industrial, defaults to None
        :type industrial: bool, optional
        :param investments: investments, defaults to None
        :type investments: bool, optional
        :param land: land, defaults to None
        :type land: bool, optional
        :param leasing: leasing, defaults to None
        :type leasing: bool, optional
        :param residential: residential, defaults to None
        :type residential: bool, optional
        :param retail: retail, defaults to None
        :type retail: bool, optional
        :param capital_markets: capital_markets, defaults to None
        :type capital_markets: bool, optional
        :param user_fields: user_fields, defaults to None
        :type user_fields: UserFields, optional
        :param user_data_fields: user_data_fields, defaults to None
        :type user_data_fields: UserDataFields, optional
        :param logical_fields: logical_fields, defaults to None
        :type logical_fields: LogicalFields, optional
        """
        if area is not None:
            self.area = self._define_str("area", area, nullable=True)
        if listings is not None:
            self.listings = self._define_str("listings", listings, nullable=True)
        if reference is not None:
            self.reference = self._define_str("reference", reference, nullable=True)
        if other is not None:
            self.other = self._define_str("other", other, nullable=True)
        if offices is not None:
            self.offices = offices
        if apartments is not None:
            self.apartments = apartments
        if hotels is not None:
            self.hotels = hotels
        if industrial is not None:
            self.industrial = industrial
        if investments is not None:
            self.investments = investments
        if land is not None:
            self.land = land
        if leasing is not None:
            self.leasing = leasing
        if residential is not None:
            self.residential = residential
        if retail is not None:
            self.retail = retail
        if capital_markets is not None:
            self.capital_markets = capital_markets
        if user_fields is not None:
            self.user_fields = self._define_object(user_fields, UserFields)
        if user_data_fields is not None:
            self.user_data_fields = self._define_object(
                user_data_fields, UserDataFields
            )
        if logical_fields is not None:
            self.logical_fields = self._define_object(logical_fields, LogicalFields)
        self._kwargs = kwargs
