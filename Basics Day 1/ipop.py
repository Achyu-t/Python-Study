# x = 'Alice'
# y = 'bob'
# print(x+y)

# z = x*5
# print(z)



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



user_inp = input().lower()
if user_inp == 'start' : car_started = True 
elif user_inp == 'stop' : car_started = False

while not car_started:
    print('The car is already at still at the start.')
    user_inp = input().lower()
    if user_inp == 'start' : car_started = True

else:

    while user_inp != "quit":


        if car_started:
            print("The car started.... Ready to go")
            
            user_inp = input().lower()

            if user_inp == 'start': car_started = True
            elif user_inp == 'stop': car_started = False  

            while car_started :
                print('Car already started !!!!')
                user_inp = input().lower()   
            continue 


        elif not car_started:
            print('Car stopped')
            user_inp = input().lower()
            
            if user_inp == 'start': car_started = True
            elif user_inp == 'stop': car_started = False 

            while not car_started:
                print('Car is in still position.')
                user_inp = input().lower()
            continue

        
        else:
            print('wrong command....')
            user_inp = input().lower()

            if car_started :
                while user_inp == 'start':
                    print('Car already started !!!!')
                    user_inp = input().lower()
                continue

            if not car_started:
                while user_inp== user_inp == 'stop':
                    print('Car is in still position.')
                    user_inp = input().lower()
                continue


    else:
        quit()
      
                                    


