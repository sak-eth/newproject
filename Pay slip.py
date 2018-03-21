emp_no = int(input("Enter employee number  : "))
emp_name = input("Enter employee name  : ")
emp_sal = int(input("Enter employee salary : "))
ta = (10*emp_sal)/100
print("travel allowances is  : ",ta)
da = (15*emp_sal)/100
print("daily allowances is   : ",da)
hra = (20*emp_sal)/100
print("house rent allowances : ",hra)
total_allowances = ta+da+hra
print("toatal allowances     : ",total_allowances)
gross_salary = emp_sal + total_allowances
print("gross salary is       : ",gross_salary)
input()
