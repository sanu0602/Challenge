def get_value(obj, key):
    for k, v in obj.items():
        if k == key:
            return v
        if isinstance(v, dict):
            value = get_value(v, key)
            if value is not None:
                return value
    return None
object = {"a": {"b": {"c": "d"}}}
user_input_key = input("Enter the key: ")
value = get_value(object, user_input_key)
if value:
    print(f"The value for key '{user_input_key}' is: {value}")
else:
    print(f"The key '{user_input_key}' was not found in the nested dictionary")
