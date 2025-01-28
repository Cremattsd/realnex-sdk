# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ContactAddressRole(Enum):
    """An enumeration representing different categories.

    :cvar PRIMARY: "Primary"
    :vartype PRIMARY: str
    :cvar MAILING: "Mailing"
    :vartype MAILING: str
    :cvar WORK: "Work"
    :vartype WORK: str
    :cvar HOME: "Home"
    :vartype HOME: str
    :cvar OTHER: "Other"
    :vartype OTHER: str
    """

    PRIMARY = "Primary"
    MAILING = "Mailing"
    WORK = "Work"
    HOME = "Home"
    OTHER = "Other"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ContactAddressRole._member_map_.values()))
