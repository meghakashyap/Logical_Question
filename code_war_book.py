def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return m*n
n=int(input("enter any num="))
m=int(input("enter any num="))
print(paperwork(n,m))