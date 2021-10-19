
def func(chislo):
    temp = chislo
    perevernytoe =0
    while (temp!=0):
        perevernytoe = (perevernytoe *10) + (temp % 10)
        temp=temp//10
    if(chislo==perevernytoe):
        return True
    else:
        return False
x = int(input("введи число: "))
if(func(x)==True):
    print("Палиндром")
else:
    print("Не палиндром")
