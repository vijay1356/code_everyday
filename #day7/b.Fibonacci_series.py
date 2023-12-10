a=0
b=1
x=0
while(a<20):
    x=a+b           #instead
    a=b             # a , b=b , a+b
    b=x
    print(b)