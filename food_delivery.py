import random,json

details={}
delivery_exe = ["DE1","DE2","DE3","DE4","DE5"]
executive = random.choice(delivery_exe) 
print(executive)

def booking_handle():
    list=[]

    delivery_charge = 50
    allowance = 10
    dict={}
    
    for i in range(0,number):

        coustumer_id = int(input("enter your coustomer id="))
        order = int(input("enter your order how much you want="))
        restaurant = input("enter the restaurant name A,B,C,D,E=")
        Destination = input("Please enter you destination=")
        time = int(input("enter the booking time="))
        
        print("****************************************")
        print("Booking_id:=",coustumer_id,"\n")
        print("your oder booking time:=",time,"\n")
        print("your order will reach at:=",time,":",30,"\n")
        print("your delivery executive is:=",executive,"\n")
        print("****************************************")

        if (order >1):

            amount=delivery_charge+allowance
            print("your delievery charge:=",delivery_charge+5,"Allowance:=10\nToatl:=",delivery_charge+5+allowance)      
        else:
            amount=delivery_charge
            print("Toatl delievery charge(include allowance):=",delivery_charge+allowance)
        
        dict["Executive"] = executive
        dict["Earn"] = amount
        
    if dict["Executive"]==executive:
        dict["Earn"]+=amount

        
    list.append(dict)
    with open("delivery.json","a+") as info:
        json.dump(list,info,indent=4)
    print(list)
    

number=int(input("enter the number="))


def delivery_executive():

    charge=booking_handle()
    coustmer_data = []
    file = open("delivery.json","r")
    convert_data = json.load(file)

    for i in range(0,len(convert_data)):
        for index in convert_data[i]:
            print(index)

            if convert_data[i]["Executive"] == executive:
                if convert_data["Earn"]>100:
                    print("Now you can Take rest")

                else:
                    print("you have to work hard")

 
    if executive in delivery_exe:
        coustmer_data.append(executive)
        coustmer_data.append(charge-10)
    
    print(coustmer_data)
    

    return executive

delivery_executive()



