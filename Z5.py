def fin(chislo):
    k=0
    for i in range(2, (chislo//2)+1, 1):
        if (chislo % i == 0):
            return False
    return True
chislo= int(input("Введите число:"))
if (fin(chislo)==True):
    print("Простое")
else:
    print("Сложное")