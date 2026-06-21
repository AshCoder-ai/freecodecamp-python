test_settings = {"Theme": "Dark", "Notifications": "On", "Volume": "High"}


def add_setting(setting_dict, kv_tuple):
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
    key = key.lower()

    for k in setting_dict.keys():
        if key == k.lower():
            setting_dict.pop(k)
            return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
