print("===================================")
print("=====WElcome to the Calculator=====")
print("===================================")
def add(no1,no2):
    ans=no1+no2
    print("++++++++++++++++++++++++++++++++++")
    print(no1,"+",no2,"=",ans)
    print("++++++++++++++++++++++++++++++++++")
def sub(no1,no2):
    ans=no1-no2
    print("---------------------------------")
    print(no1,"-",no2,"=",ans)
    print("---------------------------------")
def mul(no1,no2):
    ans=no1*no2
    print("**********************************")
    print(no1,"*",no2,"=",ans)
    print("**********************************")
def div(no1,no2):
    ans=no1/no2
    print("///////////////////////////////////")
    print(no1,"/",no2,"=",ans)
    print("///////////////////////////////////")
choice = 0
while choice != 5:
    print("===================================")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("===================================")
    choice=int(input("Enter your Choice:"))
    print("===================================")
    if choice == 5:
        print("Exiting the Calculator, Goodbye!")
    elif choice in [1, 2, 3, 4]:
        no1=int(input("Enter First number:"))
        no2=int(input("Enter second number:"))
        if choice==1:
            add(no1,no2)
        elif choice==2:
            sub(no1,no2)
        elif choice==3:
            mul(no1,no2)
        elif choice==4:
            div(no1,no2)
    else:
        print("Invalid choice, Please try again.")
    print("===================================")
