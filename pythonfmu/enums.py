"""FMI enumerations"""
from enum import Enum, IntEnum


class Fmi3Type(Enum):
    integer = 0
    real = 1
    boolean = 2
    string = 3
    enumeration = 4


class Fmi3Causality(Enum):
    parameter = 0
    calculatedParameter = 1
    input = 2
    output = 3
    local = 4
    independent = 5


class Fmi3Initial(Enum):
    exact = 0
    approx = 1
    calculated = 2


class Fmi3Variability(Enum):
    constant = 0
    fixed = 1
    tunable = 2
    discrete = 3
    continuous = 4


class Fmi3Status(IntEnum):
    ok = 0
    warning = 1
    discard = 2
    error = 3
    fatal = 4


class PackageManager(Enum):
    """Enumeration of Python packages manager."""
    pip = "pip"
    conda = "conda"
