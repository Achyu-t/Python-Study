# Exception : Event that interrupts flow of a program. There are many different types of exception. 


try:
    number =int( input("Enter a number: "))

    print(1/number)

except ZeroDivisionError :
    print("You cant divide by 0 IDIOT !!!!")

except ValueError :
    print("Enter a number you dumbass")


# except Exception as e:                 # Another way to handle exception especially if you dont know what exception might occur
#     print(e)


# Another way to do is  :     except Exception :
#                                 print("Something went wrong")
                               
# This is a bad practice because it catches all exceptions. It is best to give user idea of what actual error it is . Genrally used as a last resort.


finally :                                           # Always executed regardless of exception or not.
    print("Do some cleanup here")