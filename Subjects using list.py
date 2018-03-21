#WAP TO READ SUBJECT MARKS AND PRINT TOTAL AVERAGE HIGHEST LOWEST AND PASS AND FAIL

marks = []
min_marks = [35]
for x in range(1,7):
    print("Enter the subject : ", x , "marks")
    sub = int(input())
    marks.append(sub)
print(marks)
print(min_marks)
print("Total marks are : ",sum(marks))
print("Average marks are : ",sum(marks)/len(marks))
print("Maximum marks in a subject is : ",max(marks),"in subject : ",marks.index(max(marks)))
print("Minimum marks in a subject is : ",min(marks),"in subject : ",marks.index(min(marks)))
for y in marks:
    for z in min_marks:
        if y<=z:            
            print("the failed subject marks : ", y ,"in subject : ",marks.index(y))
for y in marks:
    for z in min_marks:
        if y>=z:           
            print("the passed subject marks : ", y ,"in subject : ",marks.index(y))
print("Thanks")
input()
