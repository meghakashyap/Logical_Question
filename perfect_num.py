num = int(input("enter any number :="))
i =1
sum = 0
while i<num:
    if num%i ==0:
        sum+=i
    i+=1
if sum == num:
    print("perfect number",num)
else:
    print("not perfect number",num)



i = 1
while i<=100:
    sum = 0
    j =1
    sum = 0
    while j<i:
        if i%j ==0:
            sum+=j
        j+=1
    if sum == i:
        print("perfect number",i) 
    i+=1
                      