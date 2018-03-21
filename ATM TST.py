for x in range(3):
    balance = 50000
    pin = int(input("Enter the pin number : "))
    if(pin == 1234):
        withdraw = int(input("Enter the amount to widhdraw : "))
        print("Withdraw  : ",withdraw)
        if(withdraw > 0):
            if(withdraw % 100 == 0):
                if(withdraw < balance):
                     balance = balance - withdraw
                     print("The remaining balance is  : ",balance)
                else:
                     print("Balance is not sufficient")
                     break
            else:
                 print("Withdrawl amount is not multiples of 100")
                 break
        else:
            print("Withdrawl amount should be greater than zero")
        break
    else:
        print("Invalid pin")
else:
    print("ATM is blocked for a day")

print("Thanks")
                
                
