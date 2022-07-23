def factors(a):
    sum=0
    i=1
    s=a**(1/2)
    while(i<=s):
        if(a%i==0):
            if(i!=a/i):
                sum+=i
                sum+=a/i
                print(i,"  ",a/i);
            else:
                sum+=i
                print(i);
        i+=1
    return sum

x=int(input("Enter number: "))
s=factors(x)-(x)
print(s)
print(s == x)
