list=['sharda',1,20.30,55,5.7,0,'suman']
i = 0
data = []
while i<len(list):
    if type(list[i]) == int or type(list[i]) == float:
        data.append(list[i])
    i += 1
print(data)
#seperate data type
# int float nd string it should be come  in seperate list


