####№1
###def getListMult(numN):
###    list = []
###    listMult = [list.append(i) for i in range(1, numN+1) if numN % i == 0]
###    return list


###def primeNum(numN):
###    primeList = []
###    for i in range(2, numN):
###        while numN % i == 0:
###            numN /= i
###            primeList.append(i)
###    return primeList

###numN = int(input("N: "))
###list1 = getListMult(numN)
###print(f'factors  {numN} : {list1}')
###list2 = primeNum(numN)
###print(f'prime factors of N {numN} :{list2}')
######№2
##list_1 = ['«Сливочное»', '«Бурёнка»', '«Вафелька»', '«Сладкоежка»']
##list_2 = ['«Сливочное»', '«Вафелька»', '«Сладкоежка»']

##list_difference = []
##for element in list_1:
##    if element not in list_2:
##        list_difference.append(element)

##print(list_difference)
###########№3
#from math import pi

#d = int(input("Введите число для заданной точности числа Пи:\n"))
#print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
##№4

