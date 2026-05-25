
# def hello (greeting, title, first , last):

#     print(f"{greeting} , {title} {first} {last}")

# hello(title = "Mr.", greeting="Hello" , last ="Squarepants", first= "Spongebob" )


# print("1","2","3","4","5","6","7", sep = "-")

'''

Arbitrary parameters :

*args = allows us to pass multiple non-key arguments                        (args is a name only it can be anything like *nums)   (tuple)
**kwargs = allows us to pass multiple keyword arguments                      (same)                                               (dictionary)

* = Unpacking operator

'''

# def add (*args):
#     total = 0 
#     for arg in args:
#         total += arg

#     return total

# print(add (1,2,3))


# def display_name(*args):
#     for arg in args:
#         print(arg,end = " ")


# display_name("Mr.", "Harry","James", "Potter")




# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
    


# print_address(street ="Street 10" , apt_no =10, city = "Pokhara", state = "Gandaki", zip ='33101' )

# def shipping_label(*args , **kwargs):

#     for arg in args:
#         print(arg, end=" ")

#     print()

#     # for key, value in kwargs.items():
#     #     print(f"{key} : {value}", end =  " ")


#     if 'appt_no' in kwargs:

#         print(f"{kwargs.get('street')}, {kwargs.get('appt_no')}")
#     else:
#         print(f"{kwargs.get('street')}")

#     print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

# shipping_label("Dr.", "Sponegbob",'Squarepants', "III",
#                street = "Street number 11", appt_no = "#10" , city = 'Pokhara' , state = "Gandaki", zip = "33120")












































