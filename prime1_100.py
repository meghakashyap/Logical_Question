j=1
while j<=100:
    i = 1
    c=0
    while i<=j:
        if j%i==0:
            c+=1
        i+=1
    if c==2:
        print(j,"prime")  
    j+=1
  

i=1
while i<=100:
    j=2
    c=0
    while j<i:
        if i%j==0:
            c+=1
        j+=1
    if c==0:
        print("prime num",i)
    i+=1

#2nd way