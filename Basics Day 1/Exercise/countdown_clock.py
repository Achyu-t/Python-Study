import time

timer = input("Enter time to count down in seconds: ")

timer= int(timer)

for x in range (timer, 0 , -1):

    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600) % 24

    time.sleep(1)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')

print("Times up ")