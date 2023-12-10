def cen():
    c=float(input("enter the temperature value in celsius :"))
    f=c*(9/5)+32
    print("value in Fahrenheit is {0:0.2f}".format(f))
def far():
    f=float(input("Enter the temperature value in Fahrenheit :"))
    c=( f-32 )*( 5/9 )
    print("value in Celsius is {0:0.2f}:".format(c))
    
def main_menu():
    print("Enter your choice ,")
    print("1: Fahrenheit 2 Celsius")
    print("2: Celsius 2 Fahrenheit")
    choice=int(input())
    if(choice==1):
        far()
    elif(choice==2):
        cen()
    else:
        print("invalid option selected !")

main_menu()