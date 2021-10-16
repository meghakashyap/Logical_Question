num =int(input("enter hoe many coustomers are in line="))            
k = 0
i =1
list_time=[]
cous = []
while i<=num:
    order,prepratin = input("Your order andprepration time is =").split()
    time = int(order)+int(prepratin)
    list_time.append(time)
    a=list_time.sort()
    i+=1
    
print(list_time)

