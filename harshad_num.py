num = int(input("enter any number="))
a = num
i = 0
while i<=num:
    rem = num%10
    sum = rem+num
    num = num //10
    i+=1
if a%sum==0:
    print(a,"is a harshad number")
else:
    print("not a harshad number")

j = 1
while j<=1000:
    sum = 0
    i = 1
    a = i
    while i<= j:
        rem = i%10
        sum = rem+i
        i = i//10
        i+=1
    if a%sum==0:
        print(a,"is a harshad number")
    else:
        print("not a harshad number")
    j+=1


d ={"a":1,"b":2,"a":3}
print(d)