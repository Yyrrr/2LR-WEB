c = []
counter = []
n = 0

def dec(function):
    def wrapper(chislo):
        if len(c) != 0 :
            if counter[0] == 0 :
                c.pop(0)
                counter.pop(0)
            print (c)
            for i in range (len(c)):
                counter[i] -= 1
        c.append(function(chislo))
        counter.append(n)
    return wrapper

@dec
def fun(chislo):
    return chislo
n = int(input("Как долго хранить кэш?"))
fun(1)
fun(2)
fun(3)
fun(4)
fun(5)
fun(6)