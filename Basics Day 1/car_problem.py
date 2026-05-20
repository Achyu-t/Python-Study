car_started = False

user_inp = input().lower()

while user_inp == 'stop':
    print('The car is still at start.')
    user_inp = input().lower()

while user_inp != 'quit':

    if user_inp == 'start':
        if  car_started :
            print('The car is already running')

        else:
            print('Car started.... Ready to go!!!!')
            car_started = True

    elif user_inp == 'stop':
        if  car_started :
            print('Car stopped')
            car_started = False
        else:
            print('Car is already in still position')

    else:
        print('Wrong command')


    user_inp = input().lower()

else:
    quit()