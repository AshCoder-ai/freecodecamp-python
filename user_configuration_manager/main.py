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

