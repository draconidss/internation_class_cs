# get dictionary key-value
alien_0 = {'color':'green', 'points':5}
print("alien_0['color']: ", alien_0['color'])
print("alien_0['points']: ", alien_0['points'])
# KeyError key 'abc' is not exist
# print("alien_0['abc']: ", alien_0['abc'])

# insert key-value
print("before insert: ", alien_0)
alien_0['name'] = "draco"
print("after insert: ", alien_0)

# modify value
print("before modify: ", alien_0)
alien_0['name'] = "mike"
print("after modify: ", alien_0)

# del key-value
del alien_0['name']
print("after del 'name': ", alien_0)
# KeyError key 'abc' is not exist
# del alien_0['abc']

# use get()
# key exist, use get(key), print value
print("alien_0.get('color'): ", alien_0.get('color')) # green
# key exist, use get(key, default), print value
print("alien_0.get('color', 'default_value'): ", alien_0.get('color', 'default_value')) # green
# key non-exist, use get(key), print None
print("alien_0.get('abc'): ", alien_0.get('abc')) # None
# key non-exist, use get(key, default), print default
print("alien_0.get('abc', 'default_value'): ", alien_0.get('abc', 'default_value')) # default_value

# iteration dictionary
# iteration keys
for key in alien_0:
    print(f"key: {key}")

# iteration key-values
print("alien_0.items():", alien_0.items())
for key_value in alien_0.items():
    print(f"key_value: {key_value}")

# iteration key and value
for key, value in alien_0.items():
    print(f"key: {key}, value: {value}")

print("alien_0.keys():", alien_0.keys())
for key in alien_0.keys():
    print(f"key: {key}")

print("alien_0.values():", alien_0.values())
for value in alien_0.values():
    print(f"value: {value}")