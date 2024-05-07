from enum import StrEnum
from dataclasses import dataclass
from typing import Union, Optional
from src.proxy_network.geolocation import GeoData


class AttackClassifier(StrEnum):
    Anonymity = "Anonymity"
    Sql_Injection = "Sql Injection"
    Unauthorized_access = "Unauthorized Access"
    Banned_access = "Ongoing ban"
    Banned_Geolocation = "Banned Geolocation"


@dataclass(slots=True)
class LogSettings:
    downloadable: bool


@dataclass(slots=True)
class Log:
    ip: str
    port: int
    creation_date: str


@dataclass(slots=True)
class SecurityLog(Log):
    classifiers: list[AttackClassifier]
    geolocation: GeoData
    malicious_data: Optional[bytes] = None
    metadata: Optional[dict] = None
    
    # TODO: how to download the file (Create a download whole alert when hovering on the log).
    # TODO: Data compression.


@dataclass(slots=True)
class AccessLog(Log):
    pass
    
    # TODO: how to download the file (Create a download whole alert when hovering on the log).
    # TODO: Data compression.


type LogObject = Union[SecurityLog, AccessLog]