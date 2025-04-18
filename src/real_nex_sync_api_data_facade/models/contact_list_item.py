# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address
from .history import History
from .object_group_list_item import ObjectGroupListItem


@JsonMap(
    {
        "user_key": "userKey",
        "team_key": "teamKey",
        "full_name": "fullName",
        "first_name": "firstName",
        "last_name": "lastName",
        "web_site": "webSite",
        "do_not_call": "doNotCall",
        "do_not_email": "doNotEmail",
        "do_not_fax": "doNotFax",
        "do_not_mail": "doNotMail",
        "mailing_address": "mailingAddress",
        "last_activity": "lastActivity",
        "object_groups": "objectGroups",
    }
)
class ContactListItem(BaseModel):
    """ContactListItem

    :param key: key, defaults to None
    :type key: str, optional
    :param user_key: user_key, defaults to None
    :type user_key: str, optional
    :param team_key: team_key, defaults to None
    :type team_key: str, optional
    :param full_name: full_name, defaults to None
    :type full_name: str, optional
    :param first_name: first_name, defaults to None
    :type first_name: str, optional
    :param last_name: last_name, defaults to None
    :type last_name: str, optional
    :param salutation: salutation, defaults to None
    :type salutation: str, optional
    :param greeting: greeting, defaults to None
    :type greeting: str, optional
    :param title: title, defaults to None
    :type title: str, optional
    :param investor: investor, defaults to None
    :type investor: bool, optional
    :param tenant: tenant, defaults to None
    :type tenant: bool, optional
    :param agent: agent, defaults to None
    :type agent: bool, optional
    :param vendor: vendor, defaults to None
    :type vendor: bool, optional
    :param personal: personal, defaults to None
    :type personal: bool, optional
    :param prospect: prospect, defaults to None
    :type prospect: bool, optional
    :param work: work, defaults to None
    :type work: str, optional
    :param fax: fax, defaults to None
    :type fax: str, optional
    :param mobile: mobile, defaults to None
    :type mobile: str, optional
    :param home: home, defaults to None
    :type home: str, optional
    :param email: email, defaults to None
    :type email: str, optional
    :param web_site: web_site, defaults to None
    :type web_site: str, optional
    :param do_not_call: do_not_call, defaults to None
    :type do_not_call: bool, optional
    :param do_not_email: do_not_email, defaults to None
    :type do_not_email: bool, optional
    :param do_not_fax: do_not_fax, defaults to None
    :type do_not_fax: bool, optional
    :param do_not_mail: do_not_mail, defaults to None
    :type do_not_mail: bool, optional
    :param address: address, defaults to None
    :type address: Address, optional
    :param mailing_address: mailing_address, defaults to None
    :type mailing_address: Address, optional
    :param last_activity: last_activity, defaults to None
    :type last_activity: History, optional
    :param object_groups: object_groups, defaults to None
    :type object_groups: List[ObjectGroupListItem], optional
    """

    def __init__(
        self,
        key: str = None,
        user_key: str = None,
        team_key: str = None,
        full_name: str = None,
        first_name: str = None,
        last_name: str = None,
        salutation: str = None,
        greeting: str = None,
        title: str = None,
        investor: bool = None,
        tenant: bool = None,
        agent: bool = None,
        vendor: bool = None,
        personal: bool = None,
        prospect: bool = None,
        work: str = None,
        fax: str = None,
        mobile: str = None,
        home: str = None,
        email: str = None,
        web_site: str = None,
        do_not_call: bool = None,
        do_not_email: bool = None,
        do_not_fax: bool = None,
        do_not_mail: bool = None,
        address: Address = None,
        mailing_address: Address = None,
        last_activity: History = None,
        object_groups: List[ObjectGroupListItem] = None,
        **kwargs,
    ):
        """ContactListItem

        :param key: key, defaults to None
        :type key: str, optional
        :param user_key: user_key, defaults to None
        :type user_key: str, optional
        :param team_key: team_key, defaults to None
        :type team_key: str, optional
        :param full_name: full_name, defaults to None
        :type full_name: str, optional
        :param first_name: first_name, defaults to None
        :type first_name: str, optional
        :param last_name: last_name, defaults to None
        :type last_name: str, optional
        :param salutation: salutation, defaults to None
        :type salutation: str, optional
        :param greeting: greeting, defaults to None
        :type greeting: str, optional
        :param title: title, defaults to None
        :type title: str, optional
        :param investor: investor, defaults to None
        :type investor: bool, optional
        :param tenant: tenant, defaults to None
        :type tenant: bool, optional
        :param agent: agent, defaults to None
        :type agent: bool, optional
        :param vendor: vendor, defaults to None
        :type vendor: bool, optional
        :param personal: personal, defaults to None
        :type personal: bool, optional
        :param prospect: prospect, defaults to None
        :type prospect: bool, optional
        :param work: work, defaults to None
        :type work: str, optional
        :param fax: fax, defaults to None
        :type fax: str, optional
        :param mobile: mobile, defaults to None
        :type mobile: str, optional
        :param home: home, defaults to None
        :type home: str, optional
        :param email: email, defaults to None
        :type email: str, optional
        :param web_site: web_site, defaults to None
        :type web_site: str, optional
        :param do_not_call: do_not_call, defaults to None
        :type do_not_call: bool, optional
        :param do_not_email: do_not_email, defaults to None
        :type do_not_email: bool, optional
        :param do_not_fax: do_not_fax, defaults to None
        :type do_not_fax: bool, optional
        :param do_not_mail: do_not_mail, defaults to None
        :type do_not_mail: bool, optional
        :param address: address, defaults to None
        :type address: Address, optional
        :param mailing_address: mailing_address, defaults to None
        :type mailing_address: Address, optional
        :param last_activity: last_activity, defaults to None
        :type last_activity: History, optional
        :param object_groups: object_groups, defaults to None
        :type object_groups: List[ObjectGroupListItem], optional
        """
        if key is not None:
            self.key = self._define_str("key", key, nullable=True)
        if user_key is not None:
            self.user_key = user_key
        if team_key is not None:
            self.team_key = self._define_str("team_key", team_key, nullable=True)
        if full_name is not None:
            self.full_name = self._define_str("full_name", full_name, nullable=True)
        if first_name is not None:
            self.first_name = self._define_str("first_name", first_name, nullable=True)
        if last_name is not None:
            self.last_name = self._define_str("last_name", last_name, nullable=True)
        if salutation is not None:
            self.salutation = self._define_str("salutation", salutation, nullable=True)
        if greeting is not None:
            self.greeting = self._define_str("greeting", greeting, nullable=True)
        if title is not None:
            self.title = self._define_str("title", title, nullable=True)
        if investor is not None:
            self.investor = investor
        if tenant is not None:
            self.tenant = tenant
        if agent is not None:
            self.agent = agent
        if vendor is not None:
            self.vendor = vendor
        if personal is not None:
            self.personal = personal
        if prospect is not None:
            self.prospect = prospect
        if work is not None:
            self.work = self._define_str("work", work, nullable=True)
        if fax is not None:
            self.fax = self._define_str("fax", fax, nullable=True)
        if mobile is not None:
            self.mobile = self._define_str("mobile", mobile, nullable=True)
        if home is not None:
            self.home = self._define_str("home", home, nullable=True)
        if email is not None:
            self.email = self._define_str("email", email, nullable=True)
        if web_site is not None:
            self.web_site = self._define_str("web_site", web_site, nullable=True)
        if do_not_call is not None:
            self.do_not_call = do_not_call
        if do_not_email is not None:
            self.do_not_email = do_not_email
        if do_not_fax is not None:
            self.do_not_fax = do_not_fax
        if do_not_mail is not None:
            self.do_not_mail = do_not_mail
        if address is not None:
            self.address = self._define_object(address, Address)
        if mailing_address is not None:
            self.mailing_address = self._define_object(mailing_address, Address)
        if last_activity is not None:
            self.last_activity = self._define_object(last_activity, History)
        if object_groups is not None:
            self.object_groups = self._define_list(object_groups, ObjectGroupListItem)
        self._kwargs = kwargs
