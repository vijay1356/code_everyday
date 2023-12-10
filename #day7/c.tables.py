#Printing the tables of given number

number=int(input("tables of "))
i=1
while(i>0):
    print(number,"X",i,"=",(number*i))
    i=i+1
    if i==11:
        break
    else:
        continue