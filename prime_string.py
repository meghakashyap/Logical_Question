even= []
odd=[]
user = input("enter anything :-")
i = 0
c=1
while i<len(user):
    print(user[i])
    if c%2==0:
        even.append(ord(user[i]))
    else:
        odd.append(ord(user[i]))
    i+=1
    c+=1
x = 0
even_sum = 0
odd_sum = 0
while x<len(even):
    even_sum += even[x]
    odd_sum += odd[x]
    absolute = even_sum - odd_sum
    x+=1

i = 2
while (i<absolute):
    if (absolute%i == 0):
        print(absolute, 'is not a casual string')
        break
    i = i + 1
else:
    print(absolute, 'its a prime string')