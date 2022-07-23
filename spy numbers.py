def fun(a):
    s=0
    p=1
    while(a):
        s+=a%10
        p*=a%10
        a=a/10
    print(s==p)
        
x=int(input("Enter number: "))
fun(x)
