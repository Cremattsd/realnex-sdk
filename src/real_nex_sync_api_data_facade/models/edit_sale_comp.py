# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .edit_comp_property import EditCompProperty
from .edit_comp_contact import EditCompContact


@JsonMap(
    {
        "user_key": "userKey",
        "team_key": "teamKey",
        "property_key": "propertyKey",
        "buyer_principal_key": "buyerPrincipalKey",
        "seller_principal_key": "sellerPrincipalKey",
        "procuring_principal_key": "procuringPrincipalKey",
        "listing_principal_key": "listingPrincipalKey",
        "buyer_contact": "buyerContact",
        "seller_contact": "sellerContact",
        "procuring_contact": "procuringContact",
        "listing_contact": "listingContact",
    }
)
class EditSaleComp(BaseModel):
    """EditSaleComp

    :param user_key: user_key, defaults to None
    :type user_key: str, optional
    :param team_key: team_key, defaults to None
    :type team_key: str, optional
    :param property_key: property_key, defaults to None
    :type property_key: str, optional
    :param buyer_principal_key: buyer_principal_key, defaults to None
    :type buyer_principal_key: str, optional
    :param seller_principal_key: seller_principal_key, defaults to None
    :type seller_principal_key: str, optional
    :param procuring_principal_key: procuring_principal_key, defaults to None
    :type procuring_principal_key: str, optional
    :param listing_principal_key: listing_principal_key, defaults to None
    :type listing_principal_key: str, optional
    :param property: property, defaults to None
    :type property: EditCompProperty, optional
    :param buyer_contact: buyer_contact, defaults to None
    :type buyer_contact: EditCompContact, optional
    :param seller_contact: seller_contact, defaults to None
    :type seller_contact: EditCompContact, optional
    :param procuring_contact: procuring_contact, defaults to None
    :type procuring_contact: EditCompContact, optional
    :param listing_contact: listing_contact, defaults to None
    :type listing_contact: EditCompContact, optional
    """

    def __init__(
        self,
        user_key: str = None,
        team_key: str = None,
        property_key: str = None,
        buyer_principal_key: str = None,
        seller_principal_key: str = None,
        procuring_principal_key: str = None,
        listing_principal_key: str = None,
        property: EditCompProperty = None,
        buyer_contact: EditCompContact = None,
        seller_contact: EditCompContact = None,
        procuring_contact: EditCompContact = None,
        listing_contact: EditCompContact = None,
        **kwargs,
    ):
        """EditSaleComp

        :param user_key: user_key, defaults to None
        :type user_key: str, optional
        :param team_key: team_key, defaults to None
        :type team_key: str, optional
        :param property_key: property_key, defaults to None
        :type property_key: str, optional
        :param buyer_principal_key: buyer_principal_key, defaults to None
        :type buyer_principal_key: str, optional
        :param seller_principal_key: seller_principal_key, defaults to None
        :type seller_principal_key: str, optional
        :param procuring_principal_key: procuring_principal_key, defaults to None
        :type procuring_principal_key: str, optional
        :param listing_principal_key: listing_principal_key, defaults to None
        :type listing_principal_key: str, optional
        :param property: property, defaults to None
        :type property: EditCompProperty, optional
        :param buyer_contact: buyer_contact, defaults to None
        :type buyer_contact: EditCompContact, optional
        :param seller_contact: seller_contact, defaults to None
        :type seller_contact: EditCompContact, optional
        :param procuring_contact: procuring_contact, defaults to None
        :type procuring_contact: EditCompContact, optional
        :param listing_contact: listing_contact, defaults to None
        :type listing_contact: EditCompContact, optional
        """
        if user_key is not None:
            self.user_key = self._define_str("user_key", user_key, nullable=True)
        if team_key is not None:
            self.team_key = self._define_str("team_key", team_key, nullable=True)
        if property_key is not None:
            self.property_key = self._define_str(
                "property_key", property_key, nullable=True
            )
        if buyer_principal_key is not None:
            self.buyer_principal_key = self._define_str(
                "buyer_principal_key", buyer_principal_key, nullable=True
            )
        if seller_principal_key is not None:
            self.seller_principal_key = self._define_str(
                "seller_principal_key", seller_principal_key, nullable=True
            )
        if procuring_principal_key is not None:
            self.procuring_principal_key = self._define_str(
                "procuring_principal_key", procuring_principal_key, nullable=True
            )
        if listing_principal_key is not None:
            self.listing_principal_key = self._define_str(
                "listing_principal_key", listing_principal_key, nullable=True
            )
        if property is not None:
            self.property = self._define_object(property, EditCompProperty)
        if buyer_contact is not None:
            self.buyer_contact = self._define_object(buyer_contact, EditCompContact)
        if seller_contact is not None:
            self.seller_contact = self._define_object(seller_contact, EditCompContact)
        if procuring_contact is not None:
            self.procuring_contact = self._define_object(
                procuring_contact, EditCompContact
            )
        if listing_contact is not None:
            self.listing_contact = self._define_object(listing_contact, EditCompContact)
        self._kwargs = kwargs
