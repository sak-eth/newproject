s1 = int(input("enter 1st sub marks : "))
s2 = int(input("enter 2nd sub marks : "))
s3 = int(input("enter 3rd sub marks : "))
total = (s1+s2+s3)
print("total : ",total)
average = (s1+s2+s3)/3
print("average : ",average)
if(s1<35):
    print("Fail in subject one")
else:
    print("passs in subject one")
if(s2<35):
    print("Fail in subject two")
else:
    print("passs in subject two")
if(s3<35):
    print("Fail in subject three")
else:
    print("passs in subject three")
if(s1>=s2 and s1>=s3):
    print("s1 is high")
if(s2>=s3 and s2>=s1):
    print("s2 is high")
if(s3>=s1 and s3>=s2):
    print("s3 is high")
if(s1<=s2 and s1<=s3):
    print("s1 is low")
if(s2<=s3 and s2<=s1):
    print("s2 is low")
if(s3<=s1 and s3<=s2):
    print("s3 is low")
input()
    
