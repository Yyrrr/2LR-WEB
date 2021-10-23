def func(chislo,stepen):
    a=1#начальное число 
    b=(1/stepen)*((stepen-1)*a+(chislo/(a**(stepen-1))))# cледующее число
    while(abs(b-a)>0.1):
        a=b
        b=(1/stepen)*((stepen-1)*a+(chislo/(a**(stepen-1))))
    return b
chislo = int(input("введи число:"))
stepen = int(input("введи степень:"))
print(func(chislo,stepen))