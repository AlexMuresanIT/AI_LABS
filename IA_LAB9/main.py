def numar_palindrom(x):
    y=0
    while x!=0:
        y=y*10+x%10
        x=x//10
    return y

x=int(input("Introdu un numar:"))
y=numar_palindrom(x)
if y==x:
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")