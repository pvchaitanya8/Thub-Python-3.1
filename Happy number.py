def sum(a):
    s=0
    while(a):
        s+=(a%10)**2
        a//=10
    return s

def happy(x):
    while(True):
        if (x<=9):
            if(x==1 or x==7):
                return True
            else:
                return False
        x=sum(x)

c=int(input())
print(happy(c))
