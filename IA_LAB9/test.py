from main import numar_palindrom

x=int(input("Introdu un numar:"))
y=numar_palindrom(x)
if x==y:
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")