# 1st input no_of soldier
# 2nd for weapon hae each soliders
# luck even num of weaponjmuy6y7
# unlucky odd num of weapon
# if even count > odd ( Ready for battel)
# else (Not ready)

soldiers = int(input("Enter the number of soldiers="))
even = 0
odd = 0
while soldiers>0:
    weapon = int(input("enter the number of weapon each soldiers have ="))
    if weapon % 2==0:
        even+=1
    else:
        odd+=1
    soldiers-=1
if even>odd:
    print("You are Ready")
else:
    print("not ready")