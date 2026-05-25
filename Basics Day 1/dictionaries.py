# Dictionaries are a collection of {key : value} pairs . They are ordered and changeable and no duplicates are allowed. Eg: {Roll1 : Ram}

capitals = {"Nepal":"Kathmandu" ,
             "USA" : "Washington DC",
             "China" : "Beijing",
             "Japan" : "Tokyo"}


# print(dir(capitals))  

# print(capitals.get("USA"))

# print(capitals.get("India"))


# if capitals.get("Russia"):
#     print("The capital country pair exists in the dictionary")

# else:
#     print("The capital country pair doesnot exist in the dictionary")



# capitals.update({"Germany": "Berlin"})

# print(capitals)


# capitals.update({"USA" : "Israel"})
# print(capitals)


# capitals.pop("USA")
# print(capitals)

# capitals.popitem()     # Removes the latest key value pair that was added
# print(capitals)

# capitals.clear()
# print(capitals)



# keyss = capitals.keys()
# print(keyss)

# for keys in keyss:
#     print(keys)



# values = capitals.values()

# print(values)


# for value in values:
#     print(value)



# items = capitals.items()

# print(items)

# for key,value in capitals.items():

#     print(f"{key} : {value} ")



# Food STALL program :

menu = {"Momo" : 150,
         "Chowmein" : 160,
         "Chicken Roll" : 200,
         "Keema Noodles" : 190,
         "Sausage" : 40,
         "Drumstick" : 50
  
        }

cart = []

total = 0 

index = 0 


print('-------------MENU-------------')
for key,value in menu.items():
    print(f"{key:15} : Rs.{value:.2f}")

print('-------------------------------')

while True:

    food = input("Select an item to add to cart or press q to quit: ")

    if food.lower() == 'q':
        break
    
    elif menu.get(food) is not None:

        cart.append(food)

    else:
        print("The item is not present in the menu. Please select a different option.")

print('-------------------------------')
print('Your Order List: ')
for food_item in cart:
    total +=  menu.get(food_item)
    print(food_item, end = ' ')

print()

print(f"Your total amount is Rs. {total}")

print('-------------------------------')