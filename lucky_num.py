# cook your dish here
T = int(input("enter the number="))
i = 0
while i<T:
    digit = input("enter the lottery number=")
    if len(digit)==3:
        if "7" in digit:
            print("YES")
        else:
            print("NO")
    else:
        print("Error")
    i+=1


# second way
T = int(input("enter the number="))
i = 1
while i<=T:
    res = ""
    A,B,C= input("enter the lottery number=").split()
    if "7" in  [A,B,C] :
        print("Yes")
    else:
        print("NO")

    i+=1