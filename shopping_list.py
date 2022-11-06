#first start by creating an empty data structure(dictionary)

shopping_list_data_types = {}
shopping_history_dictionary = []

#variable used to check if while loop condition is met using bool

stop = False

while not stop:
#start input of the name of the shopping list
    name = input("Enter shopping items:\n ")
#input of the quantity of the item
    quantity = input("enter the quantity:\n ")
#input of the price of the item
    price = input("enter price:\n ")

#bring the created empty data structure(dictionary)
shopping_list_data_types = {"shopping list item ": name, "quantity": int(quantity), 'cost': float(price)}
#bring the created empty history data structure
shopping_history_dictionary.append(shopping_list_data_types)
#ask user if he has finished shopping list

fininal_question = input("would you like a enter another item on the list?\n Type 'c' to continue entering or 'q' to finish:\n ")
if fininal_question == 'q':
    stop = True
else:
    stop = False
#make variable for the total price ! make sure its outside the loop
total_price = 0

for item in shopping_history_dictionary:
#calculate the total price store in a new variable
    total_cost = item["quantity"] * item["price"]
    total_price += total_cost
#output information use place holders %d(int) %s(str) %f(float)
    print("%d %s @ $ %f ea $%f" %(item['quantity'], item['name'],item["price"], total_price))
    total_cost = 0
print("Total price is: $%f" % total_price)





