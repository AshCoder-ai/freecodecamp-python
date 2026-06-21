"""
User Configuration Manager Module.

This module provides functions to manage user settings stored in a dictionary.
It supports adding, updating, deleting, and viewing settings, handling case-insensitive
key matching.

This is a certification project submission.
"""

test_settings = {"Theme": "Dark", "Notifications": "On", "Volume": "High"}


def add_setting(setting_dict, kv_tuple):
    """
    Add a new setting to the configuration dictionary.

    Args:
        setting_dict (dict): The dictionary containing user settings.
        kv_tuple (tuple): A tuple containing the key and value (key, value) to be added.

    Returns:
        str: A message indicating the success or failure of the operation.
    """
    k, v = kv_tuple
    k = k.lower()
    v = v.lower()

    for keys in setting_dict.keys():
        if k == keys.lower():
            return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    else:
        setting_dict[k] = v
        return f"Setting '{k}' added with value '{v}' successfully!"


def update_setting(setting_dict, kv_tuple):
    """
    Update an existing setting in the configuration dictionary.

    Args:
        setting_dict (dict): The dictionary containing user settings.
        kv_tuple (tuple): A tuple containing the key and new value (key, value).

    Returns:
        str: A message indicating the success or failure of the update operation.
    """
    k, v = kv_tuple
    k = k.lower()
    v = v.lower()

    for keys in setting_dict.keys():
        if k == keys.lower():
            setting_dict[keys] = v
            return f"Setting '{k}' updated to '{v}' successfully!"
    else:
        return f"Setting '{k}' does not exist! Cannot update a non-existing setting."


def delete_setting(setting_dict, key):
    """
    Delete a setting from the configuration dictionary.

    Args:
        setting_dict (dict): The dictionary containing user settings.
        key (str): The key of the setting to delete.

    Returns:
        str: A message indicating whether the deletion was successful or the setting was not found.
    """
    key = key.lower()

    for k in setting_dict.keys():
        if key == k.lower():
            setting_dict.pop(k)
            return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(setting_dict):
    """
    Format and return all current settings in the configuration dictionary.

    Args:
        setting_dict (dict): The dictionary containing user settings.

    Returns:
        str: A formatted string listing all settings, or a message indicating no settings are available.
    """
    if setting_dict == {}:
        return f"No settings available."
    else:
        result = "Current User Settings:\n"

        for i, j in setting_dict.items():
            result += f"{i.capitalize()}: {j}\n"
        return result


# Test cases for the functions
print(test_settings)
print(add_setting(test_settings, ("Language", "English")))
print(add_setting(test_settings, ("THEME", "Dark")))
print(add_setting(test_settings, ("volume", "medium")))
print("\n")
print(update_setting(test_settings, ("notifications", "off")))
print(update_setting(test_settings, ("Theme", "light")))
print("\n")
print(delete_setting(test_settings, "volume"))
print("\n")
print(view_settings(test_settings))
