# LIST

# fruits = [ "apple" , "orange" , "banana", "coconut"]

# print(fruits)

# print(fruits[:3:2])

# for fruit in fruits:
#     print(fruit)


# print(dir(fruits))
# print(help(fruits))           To get description of methods available for collection

# print(len(fruits))

# print("apple" in fruits)          # Find values in a list

# fruits[0] = 'pineapple'
# # fruits[4] = "mango"    # This shos error because you cant add in list like this. Shows index out of range error
# print(fruits)


# fruits.append('mango')       # This is correct way to add
# print(fruits)

# fruits.remove("pineapple")
# print(fruits)


# fruits.insert(2,"pineapple")


# fruits.sort()


# fruits.reverse()

# fruits.clear()

# print(fruits.index("coconut"))

# print(fruits.count("mango"))

# print(fruits)












# SETS

# len and find ( "apple" in fruits) are used in same way in sets just as list


# fruits = {"apple" , "orange" , "banana", "coconut", "apple"}

# print(fruits)

# fruits.add("mango")
# fruits.add("pineapple")
# print(fruits)

# fruits.remove("apple")
# print(fruits)

# fruits.pop()
# print(fruits)





# TUPLES

# len and find ( "apple" in fruits) are used in same way in tuples just as in list and sets

# fruits = ("apple" , "orange" , "banana", "coconut", "apple")

# print(fruits.index('apple'))   # Gives first occurance

# print(fruits.count('apple'))


# for fruit in fruits:
#     print (fruit)



# okaya = [1,2,3,4,5]

# print(okaya)

# print(type(okaya))

# okaya = float(okaya)

# print(okaya)

# print(type(okaya))





# SHOPPING CART PROBLEM

# foods = []
# prices = []

# total = 0 

# while True:
#     food = input("Enter a food to buy (OR Press q to quit the line): ")



#     if food.lower() == 'q':
#         break
    
#     else:
#         price = float(input(f"Enter price of {food}: $"))
#         foods.append(food)
#         prices.append(price)


# print("-----YOUR CART-----")


# ''' 
# for food in foods:
#     print(food, end = ' ')


# for price in prices:
#     total += price

# print()
# print(f'Your total is {total}')

# '''


# total = 0 
# for x in range (len(foods)) :

#     total += prices[x]

#     print(foods[x], end = " ")

# print()
# print(f'Your total is: {total}')




# num_list = [1,5,6,8,7]
# largest = num_list[0]

# for x in num_list:

#     if x > largest:
#         largest = x

# print(f'The largest element in set is: {largest}')

    








# 2D Collections





