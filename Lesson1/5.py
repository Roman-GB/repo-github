prib = int(input('Введите выручку фирмы: '))
izd = int(input('Введите издержки фирмы: '))
s = int(input('Укажите численность сотрудников: '))
if prib > izd:
    ost = int(prib - izd)
    k = int(ost / s)
    print('Фирма рентабельна, прибыль', ost)
    print('Выручка на одного сотрудника равна: ', k)
else: print ('Фирма убыточна')
