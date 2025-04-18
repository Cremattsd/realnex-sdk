# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .user_fields import UserFields
from .user_data_fields import UserDataFields
from .logical_fields import LogicalFields


@JsonMap(
    {
        "user_fields": "userFields",
        "user_data_fields": "userDataFields",
        "logical_fields": "logicalFields",
    }
)
class EditProjectDetails(BaseModel):
    """EditProjectDetails

    :param user_fields: user_fields, defaults to None
    :type user_fields: UserFields, optional
    :param user_data_fields: user_data_fields, defaults to None
    :type user_data_fields: UserDataFields, optional
    :param logical_fields: logical_fields, defaults to None
    :type logical_fields: LogicalFields, optional
    """

    def __init__(
        self,
        user_fields: UserFields = None,
        user_data_fields: UserDataFields = None,
        logical_fields: LogicalFields = None,
        **kwargs,
    ):
        """EditProjectDetails

        :param user_fields: user_fields, defaults to None
        :type user_fields: UserFields, optional
        :param user_data_fields: user_data_fields, defaults to None
        :type user_data_fields: UserDataFields, optional
        :param logical_fields: logical_fields, defaults to None
        :type logical_fields: LogicalFields, optional
        """
        if user_fields is not None:
            self.user_fields = self._define_object(user_fields, UserFields)
        if user_data_fields is not None:
            self.user_data_fields = self._define_object(
                user_data_fields, UserDataFields
            )
        if logical_fields is not None:
            self.logical_fields = self._define_object(logical_fields, LogicalFields)
        self._kwargs = kwargs
