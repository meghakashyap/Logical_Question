list1 =[]
for i in range(int(input("enter How many students are there="))):
    list2=[]
    name = input("Enter the name=")
    score = float(input("Enter the score="))
    list2.append(name)
    list2.append(score)
    list1.append(list2)
marks = []
for x in list1:
    for y in x:
        if type(y)==float:
            marks.append(y)
            lowest = min(marks)
            print(lowest)

        