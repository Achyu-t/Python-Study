import random
import time

options = ["🔔","🍒","7️⃣", "⭐","🍌"]

def placebet(balance):

    while True :
        bet_amount = input("Enter your bet amount: ")

        if not bet_amount.isdigit():
            print("Enter a valid amount!!!")
            continue

        bet_amount = float (bet_amount)
           
        if bet_amount > balance:
            print("You have insufficient funds to place that bet amount. Try different lower amount")
            continue

        if bet_amount < 1:
            print("Minimum bet is 1$ ")

        balance = balance - bet_amount

        print(f"Your remaining amount is: {balance}")

        return bet_amount
       



def rollslot():
    
    return [random.choice(options) for x in range(3)]                # x is a place holder for iteration 

    # roll = []
    # for i in range(3):
    #     roll = roll.append(random.choice(options))
    # return roll

def result(roll):

    print("********************")
    for x in range(3):
        time.sleep(1)
        print("|", roll[x] , end = ' | ', flush = True)
        
    print()   
    print("********************")

def payout(result , bet):
    if result[0] == result [1] == result [2] :

        print("----------------YOU WIN !!!!!!!!-----------------------")
        if result[0] == "🍒":
            payout = bet *5
            
        elif result[0] == "🍌":
            payout = bet *4
            
        
        elif result[0] == "⭐":
            payout = bet *7
            
        
        elif result[0] == "🔔":
            payout = bet *8
            
        
        elif result[0] == "7️⃣":
            payout = bet *10
            
        print(f"Winning amount : $ {payout}")

    elif len(set(result)) == 2:
        print("----------------YOU WIN !!!!!!!!----------------")
        payout = bet*2  
        print(f"Winning amount : $ {payout}")

    else :
        print("---------------  Better Luck Next Time !  ---------------")
        payout = 0

    return payout   




def main():
    
    balance = 100
    print("**************************************************************************************")
    print("---------------------------WELCOME TO LAS BHAKTAPUR JACKPOT---------------------------")
    print("----------------------------------🔔   🍒   7️⃣   ⭐  🍌--------------------------------")
    print("**************************************************************************************")

    while balance > 0 :

        print(f"Your current balance is: ${balance}")
        
        
        bet_amount = placebet(balance)
        
        balance -= bet_amount

        rollresult = rollslot()

        result(rollresult)

        winamount = payout(rollresult , bet_amount)

        balance += winamount

        print(f"Your updated balance is: {balance}")

        if balance > 0:
            stillplay = input("Do you want to continue playing ? : ").lower()

            if stillplay in ('y','yes'):
                continue
            else:
                break

    else :
        print("You donot have necessary funds to continue playing")

if __name__ == '__main__':
    main()