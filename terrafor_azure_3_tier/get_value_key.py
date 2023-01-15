def get_value_recursive(dictionary, key):
    if isinstance(dictionary, dict):
        if key in dictionary:
            print("key in dictionary")
            value = dictionary[key]
            if isinstance(value, dict):
                return get_value_recursive(value, key)
            else:
                
                return value
                print("here for 1st dictionaey")
        else:
            print("2nd loop")
            for k, v in dictionary.items():
                value = get_value_recursive(v, key)
                if value is not None:
                    print("here for next dcit")
                    return value
                    print ("last line")
    return None

# Example usage
#obj = {"a": {"b": {"c": "d"}}, "e": {"f": {"g": "h"}}}
obj = {"a": {"b": {"c": "d"}}}
print(get_value_recursive(obj, "b")) # Output: "d"
print(get_value_recursive(obj, "g")) # Output: "h"
