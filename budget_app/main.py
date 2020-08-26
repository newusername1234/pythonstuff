from budget import Category,create_spend_chart
from unittest import main

food = Category('Food')
food.deposit(1000,'initial deposit')
food.withdraw(10.15,'groceries')
print(food.get_balance())

clothing = Category('Clothing')
food.transfer(50,clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = Category('Auto')
auto.deposit(1000,'initial deposit')
auto.withdraw(15)

print(food)
print('')
print(clothing)
print('')
print(create_spend_chart([food,clothing,auto]))

# main(module='test_module',exit=False)