units = int(input("Number of units used  : "))
def bill():
    s_gst = 8.25
    c_gst = 3.92
    discount = 0.89
    print("per unit cost                 : ",cost)
    total = units*cost
    print("total                         : ",total)
    print("s_gst                         : ",s_gst)
    print("c_gst                         : ",c_gst)
    s_gst = (8.25*total)/100
    c_gst = (3.92*total)/100
    total = s_gst + c_gst + total
    print("after tax                     : ",total)
    print("discount                      : ",discount)
    discount = (0.89*total)/100
    total = total - discount
    print("Final bill amount             : ",total)
if(0<=units<=25):
     print("the number of units used      : ",units)
     cost = 3.25
     bill()
elif(26<=units<=50):
    print("the number of units used      : ",units)
    cost = 4.85
    bill()
elif(51<=units<=100):
    print("the number of units used      : ",units)
    cost = 6.18
    bill()

elif(units>100):
    print("the number of units used      : ",units)
    cost = 9.45
    bill()
else:
    print("enter correct number of units")

print("               thanks              ")
input()
