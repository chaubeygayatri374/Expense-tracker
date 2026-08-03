expenseslist=[]
print("------Welcome to Expense tracker------")
while True:
    print("------menu------")
    print("1. Add Expense.")
    print("2. view all expense.")
    print("3. view total money spend.")
    print("4. Exit.")
    choice=int(input("Enter your choice-"))
    if(choice==1):
        date=input("Enter date=")
        category=input("which type of expense you have done like in food,cloth please enter=")
        description=input("enetr more about your expense=")
        amount=float(input("Enter total amount="))
        expense={"date":date,"category":category,"description":description,"amount":amount}
        expenseslist.append(expense)
        print("\n Expense is added succesfully")
    elif(choice==2):
        if(len(expenseslist)==0):
            print("Nothing is there.......")
        else:
            print("Printing your expense.....")
            count=1
            for eachexpenese in expenseslist:
                print(f"count of expenese:{count}-->{eachexpenese['date']},{eachexpenese['category']},{eachexpenese['description']},{eachexpenese['amount']}")
                count=count+1
    elif(choice==3):
        total=0
        for eachamount in expenseslist:
            total=total+eachamount["amount"]
        print("\n total expense=",total)
    
    elif(choice==4):
        print("thank you")
        break
    else:
        print("Enter correct option")
                
