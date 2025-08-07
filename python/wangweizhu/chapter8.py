def print_name():
    """aaa"""
    print("wwz")
print_name()

# wrong arguments
def describe_pet(pet_name, age, animal_type='dog'):
    str = f"pet_name: {pet_name}, age: {age}, animal_type: {animal_type}"
    return str

return_value = describe_pet("harry", 10)
print(return_value) # pet_name: harry, animal_type: dog
# describe_pet(pet_name='harry') # pet_name: harry, animal_type: dog
# describe_pet("harry", "cat") # pet_name: harry, animal_type: cat
# describe_pet(pet_name="harry", animal_type="cat") # pet_name: harry, animal_type: cat
# describe_pet(animal_type="cat", pet_name="harry") # pet_name: harry, animal_type: cat

# None
def build_person(first_name, last_name, age=None):
    person = {
        "first": first_name,
        "last_name": last_name
        }
    if age:
        person["age"] = age
    return person

print(build_person("first_name", "last_name", 10))

# while with function
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\n Please tell me your name")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     if f_name == "":
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("formatted_name: ", formatted_name)

def verify_users(unconfirmed_users,confirmed_users):
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print(f"Verifying user:{current_user.title()}")
        confirmed_users.append(current_user)
    
def show_verified_users(confirmed_users):
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user)


unconfirmed_users = ["a","b","c"]
confirmed_users = []
print(f"unconfirmed_users= {unconfirmed_users}")
print(f"confirmed_users= {confirmed_users}")
verify_users(unconfirmed_users,confirmed_users)
show_verified_users(confirmed_users)
print(f"unconfirmed_users= {unconfirmed_users}")
print(f"confirmed_users= {confirmed_users}")
