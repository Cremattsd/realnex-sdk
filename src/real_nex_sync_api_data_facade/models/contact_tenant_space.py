# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "space_key": "spaceKey",
        "lease_commencement": "leaseCommencement",
        "sq_ft": "sqFt",
        "lease_expiry": "leaseExpiry",
        "rent_per_sqft": "rentPerSqft",
        "lease_term": "leaseTerm",
        "rent_per_mo": "rentPerMo",
        "cam_per_sqft": "camPerSqft",
        "lease_type": "leaseType",
        "effective_rent": "effectiveRent",
    }
)
class ContactTenantSpace(BaseModel):
    """ContactTenantSpace

    :param space_key: space_key, defaults to None
    :type space_key: str, optional
    :param suite: suite, defaults to None
    :type suite: str, optional
    :param floor: floor, defaults to None
    :type floor: str, optional
    :param lease_commencement: lease_commencement, defaults to None
    :type lease_commencement: str, optional
    :param sq_ft: sq_ft, defaults to None
    :type sq_ft: float, optional
    :param increases: increases, defaults to None
    :type increases: str, optional
    :param lease_expiry: lease_expiry, defaults to None
    :type lease_expiry: str, optional
    :param rent_per_sqft: rent_per_sqft, defaults to None
    :type rent_per_sqft: float, optional
    :param options: options, defaults to None
    :type options: str, optional
    :param lease_term: lease_term, defaults to None
    :type lease_term: str, optional
    :param rent_per_mo: rent_per_mo, defaults to None
    :type rent_per_mo: float, optional
    :param cam_per_sqft: cam_per_sqft, defaults to None
    :type cam_per_sqft: float, optional
    :param lease_type: lease_type, defaults to None
    :type lease_type: str, optional
    :param effective_rent: effective_rent, defaults to None
    :type effective_rent: float, optional
    :param tia: tia, defaults to None
    :type tia: str, optional
    """

    def __init__(
        self,
        space_key: str = None,
        suite: str = None,
        floor: str = None,
        lease_commencement: str = None,
        sq_ft: float = None,
        increases: str = None,
        lease_expiry: str = None,
        rent_per_sqft: float = None,
        options: str = None,
        lease_term: str = None,
        rent_per_mo: float = None,
        cam_per_sqft: float = None,
        lease_type: str = None,
        effective_rent: float = None,
        tia: str = None,
        **kwargs
    ):
        """ContactTenantSpace

        :param space_key: space_key, defaults to None
        :type space_key: str, optional
        :param suite: suite, defaults to None
        :type suite: str, optional
        :param floor: floor, defaults to None
        :type floor: str, optional
        :param lease_commencement: lease_commencement, defaults to None
        :type lease_commencement: str, optional
        :param sq_ft: sq_ft, defaults to None
        :type sq_ft: float, optional
        :param increases: increases, defaults to None
        :type increases: str, optional
        :param lease_expiry: lease_expiry, defaults to None
        :type lease_expiry: str, optional
        :param rent_per_sqft: rent_per_sqft, defaults to None
        :type rent_per_sqft: float, optional
        :param options: options, defaults to None
        :type options: str, optional
        :param lease_term: lease_term, defaults to None
        :type lease_term: str, optional
        :param rent_per_mo: rent_per_mo, defaults to None
        :type rent_per_mo: float, optional
        :param cam_per_sqft: cam_per_sqft, defaults to None
        :type cam_per_sqft: float, optional
        :param lease_type: lease_type, defaults to None
        :type lease_type: str, optional
        :param effective_rent: effective_rent, defaults to None
        :type effective_rent: float, optional
        :param tia: tia, defaults to None
        :type tia: str, optional
        """
        if space_key is not None:
            self.space_key = self._define_str("space_key", space_key, nullable=True)
        if suite is not None:
            self.suite = self._define_str("suite", suite, nullable=True)
        if floor is not None:
            self.floor = self._define_str("floor", floor, nullable=True)
        if lease_commencement is not None:
            self.lease_commencement = self._define_str(
                "lease_commencement", lease_commencement, nullable=True
            )
        if sq_ft is not None:
            self.sq_ft = self._define_number("sq_ft", sq_ft, nullable=True)
        if increases is not None:
            self.increases = self._define_str("increases", increases, nullable=True)
        if lease_expiry is not None:
            self.lease_expiry = self._define_str(
                "lease_expiry", lease_expiry, nullable=True
            )
        if rent_per_sqft is not None:
            self.rent_per_sqft = self._define_number(
                "rent_per_sqft", rent_per_sqft, nullable=True
            )
        if options is not None:
            self.options = self._define_str("options", options, nullable=True)
        if lease_term is not None:
            self.lease_term = self._define_str("lease_term", lease_term, nullable=True)
        if rent_per_mo is not None:
            self.rent_per_mo = self._define_number(
                "rent_per_mo", rent_per_mo, nullable=True
            )
        if cam_per_sqft is not None:
            self.cam_per_sqft = self._define_number(
                "cam_per_sqft", cam_per_sqft, nullable=True
            )
        if lease_type is not None:
            self.lease_type = self._define_str("lease_type", lease_type, nullable=True)
        if effective_rent is not None:
            self.effective_rent = self._define_number(
                "effective_rent", effective_rent, nullable=True
            )
        if tia is not None:
            self.tia = self._define_str("tia", tia, nullable=True)
        self._kwargs = kwargs
