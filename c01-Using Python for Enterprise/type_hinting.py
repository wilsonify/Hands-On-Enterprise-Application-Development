"""
these are broken, can you tell?
"""
from typing import Dict


def get_name_string1(name):
    return name['first_name'] + name['last_name']


def get_name_string2(name: Dict[str, str]) -> str:
    return name['first_name'] + name['last_name']


username = "Joe Cruze"
print(get_name_string2(username))
print(get_name_string1(username))
