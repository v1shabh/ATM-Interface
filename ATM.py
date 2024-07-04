name = input("plz enter your name : ")
print(name,"Hello JI")


message = ""
""



print("message")
task = int(input("plz enter your option:"))
available_amount=5000

if task >=1 and task <=3:
    print("welc")


    #check balance
    if task ==1:
         print("your available balance is:", available_amount)

    #deposite bal
    elif task ==2:
        deposite_amount= int(input("plz enter your deposite amount:"))
        if deposite_amount>=500:
            available_amount+=deposite_amount
            print("u have successfully deposited amount",deposite_amount )
            print("your avaialbale bal",available_amount)

        else:
            print("plz enter more than 500 rupeess")   

    #withdrawn
    else:
        withdrawn_amount=int(input("enter amount to withdrawn:"))
        if withdrawn_amount<= available_amount:
            available_amount=available_amount-withdrawn_amount
            
            print("current balance:", available_amount)

        else:
            print("You have no suffcient balnce in account ")
               


else:
    print("correct enter option between 1 - 3")    
