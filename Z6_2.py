b=[]
def dec(func):# верх
    def wrapper(fy):
        a=(func(fy))
        global b
        if(len(b)!=0):
            print("Новое значение:",a," Старое значение:",b)
            b.append(a)
        else:
            print("Функция запущена первый раз, кэш пуст",a)
            b.append(a)
    return wrapper
@dec
def fun(chislo):
    return(chislo)
fun(5)
fun(6)
fun(7)
fun(0)
fun(7)
fun(8)
