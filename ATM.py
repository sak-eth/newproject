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
        else:
            print("Withdrawl amont is given wrong")
    else:
        print("Withdrawl amount is less than zero")
else:
    print("Invalid pin")
print("Thanks")
                
                
