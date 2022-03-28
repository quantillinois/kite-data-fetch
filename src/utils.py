"""
List of common utlities and subroutines to be used across files
"""

import os


def read_env(variable_name):
    """Takes in a variable_name, and reads its value from the environment
    In case it is null, it raises an exception, which we can decide what to do with

    Args:
        variable_name (string): The variable name to get from the env config
    """
    value = os.getenv(variable_name)
    if value is None:
        raise LookupError("Did not find the following env variable")
    return value
