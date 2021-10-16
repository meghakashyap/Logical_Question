def shipping_service():
    curreny = "INR"
    if country_code.upper() == "UK" :
        if weight_in_kg < 5:
            cost = 5 
            if  "123" in product_code:
                charge = 1.2
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            elif "234" in product_code:
                charge = 1.5
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            else:
                print("Shipping Cost is ",cost*(1+0.18),curreny)

        elif weight_in_kg >= 5:
            cost = 15
            if  "123" in product_code:
                charge = 1.2
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            elif "234" in product_code:
                charge = 1.5
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            else:
                print("Shipping Cost is ",cost*(1+0.18),curreny)
   

    elif country_code.upper() == "US":
        if weight_in_kg < 10 :
            cost = 5
            if  "123" in product_code:
                charge = 1.2
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            elif "234" in product_code:
                charge = 1.5
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            else:
                print("Shipping Cost is ",cost*(1+0.18),curreny)

        elif weight_in_kg>=10: 
            cost = 15
            if  "123" in product_code:
                charge = 1.2
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            elif "234" in product_code:
                charge = 1.5
                print("Shipping Cost is",cost*charge*(1+0.18),curreny)
            else:
                print("Shipping Cost is ",cost*(1+0.18),curreny)
    else:
        print("Shipping Cost Not Applicable")


country_code = input("Please Enter Your Country Code (ex-US,UK,etc.) :-")
product_code = input("Enter the product code(code lenght should be more than 3 and less than 8) :-")
weight_in_kg = float(input("Enter the weight of product in kg:-"))
shipping_service()  
