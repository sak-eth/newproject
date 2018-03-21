for x in range(3):
    balance = 50000
    pin = int(input("Enter the pin number : "))
    if(pin == 1234):
        for y in range(2):
            withdraw = int(input("Enter the amount to widhdraw : "))
            print("Withdraw  : ",withdraw)
            if(withdraw > 0):
                if(withdraw % 100 == 0):
                    if(withdraw < balance):
                        balance = balance - withdraw
                        print("The remaining balance is  : ",balance)
                        break
                    else:
                        print("Balance is not sufficient")
                else:
                    print("Withdrawl amont is given wrong")
            else:
                print("Withdrawl amount is less than zero")
        else:
            print("Re-try again with correct balance")
        break
    else:
        print("Invalid pin")
else:
    print("Account is blocked for a day")

print("Thanks")
input()
                
                
