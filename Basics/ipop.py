# x = 'Alice'
# y = 'bob'
# print(x+y)

# z = x*5
# print(z)



# Boolean: All theconditons below return False 

'''  
[] (empty list)
{} (empty dict)
() (empty tuple)
'' (empty string)
0
None
False

'''

# So :  if [] :
#           print('a')

#       else:
#          print('b')                              This expression prints b.
                

# print('Hello world')

# myName = input('what is your name')

# print ('Nice to meet you, ' + myName)

# print(f'Your name has length:',{len(myName)})

# print('What is your age: ')
# age = input()

# print(f'Oh you are {age} years old')

# print ('You will be '+ str(int((age))+1 ) + ' next year')


# name = input('Enter your name: ')
#  age = int (input('Enter your age: '))
#  newPatient = bool(input('Are you a new patient? Type True or False: '))

# print(f'The patient name is: {name}. They are {age} years old. Their new patient status is {newPatient}')

# colour = input("Enter your favorite colour: ")

# print("My name is " + name + ". My favorite colour is " + colour)


# weight = int(input('Enter your weight: '))
# height = float(input('Enter your height: '))

# hwr = weight * height
# print(hwr)


# age= input()

# int (age)

# print (age)



# abcd = ''' HI 

# I am doing very well

# How are yo udoing in your life '''

# print (abcd)

# stringnumber1 = 'My name is Panda'

# print(stringnumber1[0])  # M
# print(stringnumber1[5])   # m
# print(stringnumber1[-1])  # a
# print(stringnumber1[-5])  # P

# stringnumber1 = 'My name is Panda'

# print(stringnumber1[1:-2])   # y name is Pan


# stringnumber1 = 'My name is Panda'
# print(stringnumber1[1:])                # y name is Panda

# stringnumber1 = 'My name is Panda'
# print(stringnumber1[1:-2])


# first = 'Panda'
# second = ' prasad'

# msg = f'The guys name is {first} and his family name is {second}'

# print (msg)

# course = 'Hi I am PaPnda'
# print(course.replace('P','J'))

# name = 'hi I am PaNda'
# print (name.title())
# print('Panda' in name)

# print (2^3) : XOR 
# x = 5
# x+= 3
# print (x)


# x= -3.4 
# print(round(x))
# print(abs(x))


# import math 

# print (math.ceil(2.9))
# print (math.floor(2.9))


# is_hot = False
# is_cold =  False
# if is_hot == 1 and is_cold == 0:
#     print("Today is hot")

# elif is_cold and not is_hot:
#     print(('Today is cold'))

# elif is_hot and is_cold:
#     print("Today is both hot and cold")

# else :
#     print ('It is neither')


# price = 1000000


# credit = input('Is your credit good? (True or False) : ').lower() == 'true'
# bool(credit)
# if credit:
#     Downpayment = 0.1* price
#     print(f'Your downpayment amount is {Downpayment}')

# else:
#     print(f'Your downpayment amount is {price *0.2 }')



# name : int = 10
# print(name)


# name_len = len(input('Enter your name: '))

# if name_len < 3 :
#     print('Name atleast must be 3 charcters. ')

# elif name_len >= 50 :
#     print('Name must be less than 50 charcters.')


# if name_len < 3 or name_len >= 50 :
#     print('Name must be between 3 and 50 characters.')

# else :
#     print('The name is fine')

# print("Python" " is" " programming language")



# weight = input("Enter the weight to convert in kgs or lbs with unit: ").lower()
# indexx = weight.find(' ')

# weight_num = float(weight[:indexx])

# if weight[indexx + 1] == 'l' :
#     print(f'Converted weight in kgs is {weight_num * 0.453592}')

# elif weight[indexx + 1] == 'k':
#     print(f'Converted weight in lbs is {weight_num*2.20462}')

# else:
#     print('Wrong Units')



# p = int (2)

# q = float (2.5)

# print(p*q)


# i =1
# user_inp = int(input("Enter your guess number: "))
# num = 16

# while user_inp != num and i <= 3 :

#     i= i+1
#     user_inp = int(input("The guess is incorrect, Guess Another: "))

#     if user_inp == num:
#         print("You guessed the correct number")
#         break
#     elif i ==3 and user_inp != num:
#         print("Too many tries")
#         break
# else :
#     print ("The guess is correct!!")



# user_inp = input().lower()
# if user_inp == 'start' : car_started = True 
# elif user_inp == 'stop' : car_started = False

# while not car_started:
#     print('The car is already at still at the start.')
#     user_inp = input().lower()
#     if user_inp == 'start' : car_started = True

# else:

#     while user_inp != "quit":


#         if car_started:
#             print("The car started.... Ready to go")
            
#             user_inp = input().lower()

#             if user_inp == 'start': car_started = True
#             elif user_inp == 'stop': car_started = False  

#             while car_started :
#                 print('Car already started !!!!')
#                 user_inp = input().lower()   
#             continue 


#         elif not car_started:
#             print('Car stopped')
#             user_inp = input().lower()
            
#             if user_inp == 'start': car_started = True
#             elif user_inp == 'stop': car_started = False 

#             while not car_started:
#                 print('Car is in still position.')
#                 user_inp = input().lower()
#             continue

        
#         else:
#             print('wrong command....')
#             user_inp = input().lower()

#             if car_started :
#                 while user_inp == 'start':
#                     print('Car already started !!!!')
#                     user_inp = input().lower()
#                 continue

#             if not car_started:
#                 while user_inp== user_inp == 'stop':
#                     print('Car is in still position.')
#                     user_inp = input().lower()
#                 continue


#     else:
#         quit()


# n= 5

# print("Positive" if n > 0 else "Negative")
# result = 'Even' if n%2 == 0 else 'odd'
# print(result)     
                                    
# name = "panda china"
# cap= name.capitalize()
# print(cap  )

# name = '123'
# print(name.isdigit())

# phone_num = '9823440432'
# print(phone_num.count("4"))

# nums = [1,2,3,4,5]

# for num in nums:
#     if num==3:
#         break

#     else:
#         print("Loop complete")


#----------------------------------------------------------------------------------------------------------------------------------------------#

# import time

# timer = int (input('Enter time to countdown: ')
#                )
# for x in reversed(range(1, timer+1)):

#     time.sleep(1)
#     print(x)
    

# print ('Times up')


# import time

# timer = int (input('Enter time to countdown: ')
#                )
# for x in range(timer, 0 ,-1):

#     time.sleep(1)
#     print(x)
    

# print ('Times up')


# import time

# timer = input("Enter time to count down in seconds: ")

# timer= int(timer)

# for x in range (timer, 0 , -1):

#     seconds = x % 60
#     minutes = (x // 60) % 60
#     hours = (x // 3600) % 24

#     time.sleep(1)
#     print(f'{hours:02}:{minutes:02}:{seconds:02}')

# print("Times up ")


# num1 = 5.6443
# num2= 3.141569
# num3 = 2.2223
# num4 = -56.34
# num5 = 69450678

# print(f'{num1:.3f}')

# print(f'{num2:3}')     
# print(f'{num3:<10}')

# print(f'{num2:>10}')

# print(f'{num3:+}')


# print(f'{num2:=}')

# print(f'{num1:}')

# print(f'{num5:,}')


#----------------------------------------------------------------------------------------------------------------------------------------------#


# NESTED LOOPS

# for x in range(1,5):
#     print(f'{x} : ',end= "")
#     for y in range (1,10):

#         print(y, end = "")

#     print()
# print('END')


# # print a rectangle

# rows = int(input('Enter number of rows: '))
# columns = int(input('Enter number of columns: '))
# symbol = input("Enter symbol you want to use: ")

# for x in range(0,rows):

#     for y in range(columns):
#         print(f"{symbol}", end = "")

#     print()    


#----------------------------------------------------------------------------------------------------------------------------------------------#


# Random Numbers in Python :


# import random

# print(random.randint(1,6))                        

# low = 4 
# high = 100 

# guess = random.randint(low,high)

# print(guess)



# random_float = random.random()   # gives random float betn 0 and 1 
# print(random_float)


# random_float = random.random(high , low)  This gives error because it doesnot take any argument



# options = ('rock' , 'paper' , 'scissors')

# option = random.choice(options)

# print(option)

# cards = ['A' , "2" , '3' , '4' , '5' , '6' , '7' , '8'  , '9' , '10' , 'J' , 'Q' , 'K' ]

# random.shuffle(cards)

# print(cards)




#----------------------------------------------------------------------------------------------------------------------------------------------#


# Number guessing game: 

# import random 

# print('---------Random Number Guessing Game---------------')



# METHOD 1 without isdigit()

# print('Game quits if user types q in input or user guesses correctly.')

# lowest = 1
# highest = 100

# random_number = random.randint(lowest, highest)


# while True: 

#     user_guess = input("Enter your guess : ")

#     if user_guess.lower() == 'q':
#         break

#     elif int(user_guess) == random_number:
#         print(f"Correct guess. The number was {random_number}")
#         break
    
#     elif int(user_guess) > random_number :
#         print("The number is lower. Guess again !!!")
    
#     elif int(user_guess) < random_number:
#         print('The number is higher. Guess again !!!')

#     elif int(user_guess)  < 1 or user_guess > 100 :
#         print('The number is between 0 and 100') 





# METHOD 2 with isdigit()

    
# lowest = 1
# highest = 100

# random_number = random.randint(lowest, highest)

# print(f"Guess a number between {lowest} and {highest} or press q to quit")

# i= 0

# while True:
#     guess = input("Enter your guess: ")
#     i += 1
    

#     if guess.isdigit() :

#         guess = int(guess)

#         if guess < lowest or guess > highest:
#             print(f"Guess out of range. Try another number between {lowest} and {highest}")
#             continue
        
#         elif guess == random_number:
#             print(f"Correct guess. The random number was {guess}.")
#             print(f"The total number of tries:  {i}")
#             break

#         elif guess > random_number :
#             print("The number is lower. Guess again !!!")
    
#         elif guess < random_number:
#             print('The number is higher. Guess again !!!')

#     elif guess.lower() == 'q' :
#         break
    
#     else:
#         print("Enter valid numerical value. ")
#         continue


#----------------------------------------------------------------------------------------------------------------------------------------------#

# Rock paper scissors game

# import random
# print("Lets play rock paper scissors")
# print('User can type either rock , paper or scissors')

# options = ('Rock', 'Paper', 'Scissors')

# play = True

# while play:

#     computer_answer = random.choice(options)

#     user_input = input("Enter your input: ")

#     if user_input.capitalize() in options :

#         print(f"Your choice is: {user_input}")
#         print(f'Computer choice is: {computer_answer} ')

#         user_input = user_input.lower()
#         computer_answer = computer_answer.lower()



# #---------------------------------------------------------------Works but below option is more clean and short---------------------------------------------------------
#         # if user_input == "rock":
#         #     if computer_answer == 'paper':
#         #         print("You loose")
#         #         break
#         #     elif computer_answer == 'scissors':
#         #         print("You win")
#         #         break
#         #     else :
#         #         print("Same answer. Try again")
#         #         

#         # if user_input == "paper":
#         #     if computer_answer == 'scissors':
#         #         print("You loose")
#         #         break
#         #     elif computer_answer == 'rock':
#         #         print("You win")
#         #         break
#         #     else :
#         #         print("Same answer. Try again")
#         #                 

#         # if user_input == "scissors":
#         #     if computer_answer == 'rock':
#         #         print("You loose")
#         #         break
#         #     elif computer_answer == 'paper':
#         #         print("You win")
#         #         break
#         #     else :
#         #         print("Same answer. Try again")
#         #         
# #----------------------------------------------------------------------------------------------------------------------------------------------------------------

#         if user_input == computer_answer:                             # More cleaner approch
#             print("Its a tie. Try again")
#             continue

#         elif user_input == 'rock' and computer_answer == 'scissors':
#             print("You win")
            

#         elif user_input == 'paper' and computer_answer == 'rock':
#             print("You win")
            

#         elif user_input == 'scissors' and computer_answer == 'paper':
#             print("You win")
            
#         else: 
#             print("You loose")
            
#         if not input("Do you want to play again? Press 'y' if YES : ").lower() == 'y': 
#             play = False


#     else:
#         print("Wrong value . Only choose between rock, paper and scissors")

    
#----------------------------------------------------------------------------------------------------------------------------------------------#

# MEMBERSHIP OPERATORS : in and not in   ( Return true or false (boolean) ) 

# word = "PANDA"

# letter = input("Guess a letter in secret word: ")

# if letter in word:
#     print("The letter is present in word")

# else: 
#     print("The letter is not present")



# grades = { "Cunha":"A" , "Mbeumo":"B"  , "Sesko":"C" ,"Bruno":"D"}

# student = input("Enter the student you want to search: ")

# if student in grades:
#     print(f'{student} is in grade {grades[student]}')

# else:
#     print(f'{student} was not found in school data')




# EXERCISE - 2 FOR MEMBERSHIP OPERATOR

# email = "abcd@hotmail.com"

# if "@" and "." in email:
#     print("Vaid email")

# else:
#     print("Emaill provided is invalid")





#----------------------------------------------------------------------------------------------------------------------------------------------#

# LIST COMPREHENSION : Concise way to create lists in Python which is compact and easier to read than traditional loops. 


# doubles = []

# for value in range(1,11):
#     doubles.append(value*2)

# print(doubles)

# Faster method:  Syntax: variabe = [expression for loop condition]

# double = [x*2 for x in range(1,11) ]
# print(double)


# Exercise 

# fruits = ['apples', 'banana' , 'coconut', 'mango']
# print(fruits)
# x= True
# cap_fruits = [abcd.upper() for abcd in fruits if x==True]
# print(cap_fruits)

# ini_fruits = [x[0] for x in fruits]
# print(ini_fruits)



# abcd = 1,2,3,4

# print(abcd , type(abcd))


# pqrs = 7,8,89,10

# print(abcd, pqrs , "My name is Raj")

# numbers  = [1,-2,3,-4,5,-6]

# positive_num = [num for num in numbers if num >= 0 ]

# print(positive_num)



#----------------------------------------------------------------------------------------------------------------------------------------------#

 

# Switch cases   (MATCH CASE)

# def day_of_week(day):
#     match day :
#         case 1:
#             return "Sunday"
#         case 2:
#             return "Monday"
#         case 3:
#             return "Tuesday"
#         case 4:
#             return "Wednesday"
#         case 5:
#             return "Thursday"
#         case 6:
#             return "Friday"
#         case 7:
#             return "Saturday"

# print(day_of_week(3))





# def is_weekend(day):
#     match day :
#         case 'Sunday' | 'Saturday' | '':
#             return True
#         case "Monday" | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
#             return False


# print(is_weekend('Tuesday'))

#----------------------------------------------------------------------------------------------------------------------------------------------#


# Modules:


# import math

# print(math.pi)


# import math as history

# print(history.pi)





# from math import pi

# print(pi)





# from math import e 

# print(e)


# a,b,c,d,e = 1,2,3,4,5


# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)
# print(e ** e)           # Using from can casue such naming conflicts. Here both e from math and e variable are same . So the progeam chooses the newest provided e and ignore the one from math module.


# Create a module:


# import wronglearn as w

# print(w.area(5))

# print(w.circumference(5))

# print(w.cube(5))

# print(w.square(5))


#----------------------------------------------------------------------------------------------------------------------------------------------#


# a = ['apple', 'banana', 'guava']
# b = ['9','8','8','7','5','4','2']
# c = [9,8,8,7,5,4,2]

# for i in a:
#     print(i, end = '-')
# print()

# print("-".join(b))

# print('-'.join(map(str,c)))


# print(*a, sep = '*')


#----------------------------------------------------------------------------------------------------------------------------------------------#


# API

# import requests


# base_url = 'https://pokeapi.co/api/v2/'

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
#     print(response)

#     if response.status_code ==200:
#         pokemon_data = response.json()
#         return pokemon_data

#     else:
#         print(f"Failed to retreive data {response.status_code}")

# pokemon_name = "goodra"

# pokemon_info = get_pokemon_info(pokemon_name)


# if pokemon_info:
#     print(f"{pokemon_info['name'].capitalize()}")
#     print(f"{pokemon_info['height']}")












































































































































# Dice roller

# import random



# cars = ["a", 'b','c']

# trend = []

# for c in cars:
#     if c == 'a' or 'c':
#         trend.append(c)

# print(trend)