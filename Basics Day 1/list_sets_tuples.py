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
# # fruits[4] = "mango"    # This shows error because you cant add in list like this. Shows index out of range error
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

# fruits = ['apple', 'orange' , 'banana' , 'coconut']
# vegetables = ['bodi', 'saag', 'cauli']
# meat = ['chicken', 'fish' , 'mutton']

# groceries = [fruits , vegetables, meat]

# print(groceries)

# print(groceries[1])

# print(groceries[1][1])



# OR

# groceries = [ ['apple', 'orange' , 'banana' , 'coconut'],
#             ['bodi', 'saag', 'cauli'],
#             ['chicken', 'fish' , 'mutton']]                           # Same thing

# print(groceries)

# print(groceries[1])

# print(groceries[1][1])


# for collection in groceries:
#     for food in collection:
#         print(food)


# We can have lists made up of tuples, tuples made of tuples , tuples made of sets etc.


# Create a 2D keypad 

# num_pad = ( (1, 2, 3), 
#            (4, 5, 6), 
#            (7, 8, 9),
#            ('*', 0 , '#'))


# for row in num_pad:
#     for num in row:
#         print(num, end= " ")
#     print()



# Python Quiz Game

import time

questions = ("1. What is the only planet in our solar system that spins clockwise?",
            "2. Which element has the chemical symbol'Au'?",
            "3. Which city is home to the ancient architectural site of Petra?", 
            "4. What is the hardest natural substance on Earth?", 
            "5. How many strings does a standard violin have?")

options = (("A. Mars","B. Venus","C. Jupiter","D. Neptune"), 
           ("A. Silver","B. Copper","C. Gold","D. Iron"), 
           ("A. Egypt","B. Jordan","C. Greece","D. Turkey"),
           ("A. Quartz","B. Topaz","C. Corundum","D. Diamond"),
           ("A. 4","B. 5","C. 67","D. 8"))

correct_answer = ("B", "C", "B" , "D" , "A")
answers = []
collection_index = 0 
score = 0

for question in questions:
    print('--------------------------------------')
    print(question)

    for option in options[collection_index]:
        print(option)

    user_ans = input("Enter your option (A,B,C,D): ").upper()
    answers.append(user_ans)

    if user_ans == correct_answer[collection_index]:
        score += 1
        print("Correct Answer 😎")

    else:
        print("Wrong Answer 😓")
        print(f"The correct answer is: {correct_answer[collection_index]} ")

    collection_index +=1
    time.sleep(1)

print('--------------RESULTS-------------------------')

print('Your answers : ', end = ' ')
for answer in answers:
    print(answer , end = " ")

print()

print('Correct answer : ', end = " ")
for guesses in correct_answer:
    print(guesses, end= " ")

print()

print(f'Total score : {score} / 5')