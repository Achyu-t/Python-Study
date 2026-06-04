'''Multithreading is used to perform multiple tasks concurrently. Good for I/O bound tasks like reading files or fetching data from APIs threading.'''

# Syntax :   threading.Thread(target = my_function)

import threading
import time

def walk_dog(first_name , last_name):
    time.sleep(10)
    print(f"You finish walking {first_name} {last_name} 🦮")

def take_out_trash():
    time.sleep((3))
    print("You take out the trash. 🚮")

def get_mail():
    time.sleep(6)
    print("You get the mail. 💌")

task1 = threading.Thread(target = walk_dog, args = ("Meowth" , "James"))
task1.start()

task2 = threading.Thread(target = take_out_trash)
task2.start()

task3 = threading.Thread(target = get_mail)
task3.start()

task1.join()
task2.join()
task3.join()

print("All tasks are complete")