def prime(b):
    for i in range(2,b):
        if(b%i==0):
            return False
    return True


def factors(a):
    sum=0
    i=1
    s=a**(1/2)
    while(i<=s):
        if(a%i==0):
            if(i!=a/i):
                if(prime(i)and prime(a//i)):
                    print(a, " = ", i, " * ", a//i)
                #print(i,"  ",a/i);
            else:
                if(prime(i)):
                    print(a, " = ", i, " * ", i)
                #print(i);
        i+=1

x=int(input("Enter number: "))
factors(x)
