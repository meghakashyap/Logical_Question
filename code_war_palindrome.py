def is_palindrome(string):
    check=[]
    i=-1
    while i>=(-len(string)):
        check.append(string[i])
        i-=1
    k=0
    while k<len(string):
        if string[k]==check[k]:
            return True
        else:
            return False
        k+=1
        
        
print(is_palindrome("anna"))