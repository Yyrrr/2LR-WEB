def func(chislo):
    temp = abs(chislo)
    perevernytoe =0
    while (temp!=0):
        perevernytoe = (perevernytoe *10) + (temp % 10)
        temp=temp//10
    if(chislo<0):
        perevernytoe=perevernytoe*-1
    return perevernytoe
chislo = int(input("введи число:"))
print(func(chislo))