a = int(input('Введите начальную дистанцию: '))
b = int(input('Введите конечную дистанцию: '))
t = int(0)
while a < b:
    a = a + a * 0.1
    t += 1
    if a >= b:
        print('Через', t, 'дней мы выйдем на дистанцию', b)

