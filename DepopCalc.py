bundle = input('Is this a bundle? ') 
def program(bundle): 

    if bundle == 'no' or bundle == 'n': 
        pass 
        Item = float(input('How much was the item? '))
        fee = float(input('How much was the fee? '))
        ActualPrice = float(input('What was the Original Price of the item? ')) 
        Calculations = float(Item - fee) - ActualPrice  
        print(f'Profit: ${Calculations:.2f}')
    elif bundle == "y" or bundle == "yes": 
        bundle_price_list = []
        bundle_num = int(input("How much are in the bundle? ")) 
        for i in range(1, bundle_num + 1): 
            bundle_price =  float(input("How much did you sell them for? "))  
            bundle_price_list.append(bundle_price)
        Actual_Price_List = []  
        for c in range(1, bundle_num + 1): 
            Actual_Price = float(input("How much did you buy each item for? "))  
            Actual_Price_List.append(Actual_Price)
        fee = float(input("How much was the fee for the bundle? ")) 
        Shipping = float(input("How much was shipping? "))
        formula_list = [] 
        for i in range (bundle_num):
            List_up  = Actual_Price_List[i]
            List_up2 = bundle_price_list[i]
            formula = (List_up2 - List_up - fee/bundle_num - Shipping/bundle_num) 
            formula_list.append(formula) 
        for i, emp in enumerate(formula_list, start=1):  
            print(f"Profit for item {i}: ${round(emp, 2)}")
program(bundle)
        




    


    
    




 


    
        
   
