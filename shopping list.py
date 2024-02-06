#Exerscise 2
'''Shopping List: Write a program to manage a shopping list. Use variables to store item names, 
quantities, and prices. Calculate the total cost of items and check if you have enough budget'''

#program
budget = int(input("enter budget:"))

item_names = [input("enter items name:")]
quantities = int(input("enter quantity:"))
price_of_each_item = int(input("enter price of each item:"))

total_cost_of_items = quantities * price_of_each_item

if total_cost_of_items <= budget :
    print(f"{total_cost_of_items}$  total cost is in your budget")
else:
    print(f"{total_cost_of_items}$  total cost is out of your budget")