# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ObjectGroupListItem(BaseModel):
    """ObjectGroupListItem

    :param key: key, defaults to None
    :type key: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, key: str = None, name: str = None, **kwargs):
        """ObjectGroupListItem

        :param key: key, defaults to None
        :type key: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if key is not None:
            self.key = self._define_str("key", key, nullable=True)
        if name is not None:
            self.name = self._define_str("name", name, nullable=True)
        self._kwargs = kwargs
