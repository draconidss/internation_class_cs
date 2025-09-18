def describe_pet(pet_name, animal_type='dog'):
# def describe_pet(animal_type='dog', pet_name): # Error
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

print("describe_pet('willie'): ")
describe_pet('willie')

print("\ndescribe_pet('a', 'b'): ")
describe_pet('a', 'b')

print("\ndescribe_pet(animal_type='a', pet_name='b'): ")
describe_pet(animal_type='a', pet_name='b')

# describe_pet(animal_type='b') # Error

def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age != None:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', "")
print(musician)
musician = build_person('jimi', 'hendrix')
print(musician)






# function definite
def verifing(unconfirmed_users):
    confirmed_users = []
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        # print(f"Verifying user: {current_user.title()}")
        confirmed_users.append(current_user)
        # print("\nThe following users have been confirmed:")

    return confirmed_users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = verifing(unconfirmed_users[:])
print(confirmed_users)
print(unconfirmed_users)