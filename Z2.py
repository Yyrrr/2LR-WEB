def fin(list,colvo):
    list2 = []
    list3 = []
    list5 = []
    for i in range(0,colvo,1):
        if list[i]%2==0:
            list2.append(list[i])
        if list[i]%3==0:
            list3.append(list[i])
        if list[i]%5==0:
            list5.append(list[i])
    return "Делятся на два",list2,"Делятся на три",list3,"Делятся на пять",list5
print("Введите количество элементов:")
colvo= int(input())
list = []
for i in range(0,colvo,1):
    print("Введите ", i ," элемент:")
    list.append(int(input()))
print(fin(list,colvo))