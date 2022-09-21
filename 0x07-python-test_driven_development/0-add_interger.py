#!/usr/bin/python3
"""Defines an addition interger function"""


def add_interger(a, b =98):
    """Returns tha addition of a and b
    float intergers are typecasted to and int before addidion
    Raises:
        TypeError: if either a or b is ont and interger or float
    """
    if(not isinstance(a, int) and not isinstance(a,float)):
        raise TypeError("a must be an interger")
    if(not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an interger")
    return (int(a) + int(b))
