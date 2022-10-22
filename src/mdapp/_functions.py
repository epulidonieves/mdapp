"""A set of functions just for emulate a module in a real library."""

from typing import Any


def value_to_bool(value: Any) -> bool:
    """A dummy bool converter.

    :param value: Param to convert
    :return: Boolean representation of value
    """
    return bool(value)
