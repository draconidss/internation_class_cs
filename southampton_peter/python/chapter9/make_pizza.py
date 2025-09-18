# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp

# duplicate function of make_pizza
def make_pizza():
    print("This is a fucntion of make_pizza")

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza()
