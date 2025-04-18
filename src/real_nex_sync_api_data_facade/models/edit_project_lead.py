# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "project_status_key": "projectStatusKey",
        "object_key": "objectKey",
        "date_opened": "dateOpened",
        "date_expected": "dateExpected",
        "date_closed": "dateClosed",
        "project_result_key": "projectResultKey",
    }
)
class EditProjectLead(BaseModel):
    """EditProjectLead

    :param published: published, defaults to None
    :type published: bool, optional
    :param project_status_key: project_status_key, defaults to None
    :type project_status_key: int, optional
    :param object_key: object_key, defaults to None
    :type object_key: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    :param amount: amount, defaults to None
    :type amount: float, optional
    :param date_opened: date_opened, defaults to None
    :type date_opened: str, optional
    :param date_expected: date_expected, defaults to None
    :type date_expected: str, optional
    :param date_closed: date_closed, defaults to None
    :type date_closed: str, optional
    :param probability: probability, defaults to None
    :type probability: int, optional
    :param commission: commission, defaults to None
    :type commission: float, optional
    :param project_result_key: project_result_key, defaults to None
    :type project_result_key: int, optional
    :param reason: reason, defaults to None
    :type reason: str, optional
    :param notes: notes, defaults to None
    :type notes: str, optional
    """

    def __init__(
        self,
        published: bool = None,
        project_status_key: int = None,
        object_key: str = None,
        size: float = None,
        amount: float = None,
        date_opened: str = None,
        date_expected: str = None,
        date_closed: str = None,
        probability: int = None,
        commission: float = None,
        project_result_key: int = None,
        reason: str = None,
        notes: str = None,
        **kwargs
    ):
        """EditProjectLead

        :param published: published, defaults to None
        :type published: bool, optional
        :param project_status_key: project_status_key, defaults to None
        :type project_status_key: int, optional
        :param object_key: object_key, defaults to None
        :type object_key: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        :param amount: amount, defaults to None
        :type amount: float, optional
        :param date_opened: date_opened, defaults to None
        :type date_opened: str, optional
        :param date_expected: date_expected, defaults to None
        :type date_expected: str, optional
        :param date_closed: date_closed, defaults to None
        :type date_closed: str, optional
        :param probability: probability, defaults to None
        :type probability: int, optional
        :param commission: commission, defaults to None
        :type commission: float, optional
        :param project_result_key: project_result_key, defaults to None
        :type project_result_key: int, optional
        :param reason: reason, defaults to None
        :type reason: str, optional
        :param notes: notes, defaults to None
        :type notes: str, optional
        """
        if published is not None:
            self.published = published
        if project_status_key is not None:
            self.project_status_key = project_status_key
        if object_key is not None:
            self.object_key = object_key
        if size is not None:
            self.size = self._define_number("size", size, nullable=True)
        if amount is not None:
            self.amount = self._define_number("amount", amount, nullable=True)
        if date_opened is not None:
            self.date_opened = self._define_str(
                "date_opened", date_opened, nullable=True
            )
        if date_expected is not None:
            self.date_expected = self._define_str(
                "date_expected", date_expected, nullable=True
            )
        if date_closed is not None:
            self.date_closed = self._define_str(
                "date_closed", date_closed, nullable=True
            )
        if probability is not None:
            self.probability = self._define_number(
                "probability", probability, nullable=True
            )
        if commission is not None:
            self.commission = self._define_number(
                "commission", commission, nullable=True
            )
        if project_result_key is not None:
            self.project_result_key = project_result_key
        if reason is not None:
            self.reason = self._define_str("reason", reason, nullable=True)
        if notes is not None:
            self.notes = self._define_str("notes", notes, nullable=True)
        self._kwargs = kwargs
