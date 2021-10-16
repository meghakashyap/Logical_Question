i = 1
c = 0
num = int(input("enter any num="))
while i<=num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print("prime")
else:
    print("no")



