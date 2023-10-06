import math

def task_1():
    a = [1, 0, 9, 12, 18, 34, 89, 91, 33, 127]
    b = [2, 8, 9, 11, 76, 25, 44]

    print('1.', a[0], ',', a[2], ',', a[-1])
    b.append(7)
    a[4] = 8

    merged = a + b
    print(merged)

    c = a[0:-1] + [100]
    print(c)

def task_2():
    girls = ["Иветта", "Виолетта", "Кассандра", "Вирджиния", "Амелия", "Розамунда", "Янина", "Беатриса"]

    print(girls[1:5])
    print(girls[3:8])
    print(girls[0:2] + girls[3:5])
    print(girls[2:3] + girls[4:5] + girls[5:6])

def task_3():
    L = [12, 3, 8, 125, 10, 98, 54, 199]

    [print(elem) for elem in L]
    print("____________________________")
    [print(math.log(elem)) for elem in L]

def task_4():
    age = [24, 35, 42, 27, 45, 48, 33]

    age2 = list(map(lambda elem: elem ** 2, age))
    print(age2)

    age3 = [None] * len(age)
    for i in range(len(age)):
        age3[i] = age[i] ** 2
    print(age3)

def task_5():
    numbers = [1, 5, 6, 8, 10, 21, 25, 1, 0, -9, 9]

    print('Введите число от 1 до 10')
    k = int(input())
    if (k < 1) | (k > 10):
        print("Ты еблан")
    else:
        print(numbers[k-1])

def star_1():
    L = ['n', 'kkk', 'pp', 'rrrrrrrrrrrr']
    max_len = 0

    for elem in L:
        if (max_len < len(elem)):
            max_len = len(elem)

    for i in range(len(L)):
        elem = L[i]
        difference = max_len - len(elem)
        if difference > 0:
            elem += '_' * difference
        L[i] = elem

    print(L)

def star_2():
    L = ['рауга', 'радость', 'радио', 'радар', "ty"]
    general_part = L[0]

    for elem in L:
        i = 0
        while (i < len(elem)) and (i < len(general_part)) and (elem[i] == general_part[i]):
            i += 1
        general_part = general_part[0:i]

    print(general_part)

def star_3(): #возвращает все подстроки с суммой 5
    L = [1, 2, 3, 4, 0, 1, 0, 1, 5, 4, 3, 4, 1, 1, 1, 0, 0, 1, 1, 1]
    sub_L = []
    index = 0

    for i in range(len(L)):
        sub_L.append(L[i])
        sum = 0
        for elem in sub_L:
            sum += elem

        while sum > 5:
            sum = sum - sub_L.pop(0)
            index += 1
        if sum == 5:
            print(sub_L, index)

def star_3_1(): #возвращает уникальные подстроки без перекрытия элементов
    L = [1, 2, 3, 4, 0, 1, 0, 1, 5, 4, 3, 4, 1, 1, 1, 0, 0, 1, 1, 1]
    sub_L = []
    index = 0

    for i in range(len(L)):
        sub_L.append(L[i])
        sum = 0
        for elem in sub_L:
            sum += elem

        while sum > 5:
            sum = sum - sub_L.pop(0)
            index += 1
        if sum == 5:
            print(sub_L, index)
            index = index + len(sub_L)
            sub_L = []

def calc_distance_rigth(L, i):
    try:
        distance_rigth = abs(L.index(1, i) - i)
    except ValueError:
        distance_rigth = len(L)
    return distance_rigth

def calc_distance_left(L, i):
    try:
        distance_left = abs(L[::-1].index(1, (len(L) - i - 1)) - (len(L) - i - 1))
    except ValueError:
        distance_left = 0
    return distance_left

def star_4():
    #L = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    L = [1]
    try:
        great_index = L.index(0)
    except ValueError:
        print("Свободных мест нет")
        return 0

    max_distance = 0

    for i in range(L.index(0), len(L)):
        if (L[i] == 0):
            if i == 0:
                distance = calc_distance_rigth(L, i)
            elif i == len(L):
                distance = calc_distance_left(L, i)
            else:
                distance_rigth = calc_distance_rigth(L, i)
                distance_left = calc_distance_left(L, i)
                distance = min(distance_rigth, distance_left)
            if max_distance < distance:
                max_distance = distance
                great_index = i
    print("Лучшее место для интроверта -", great_index)

if __name__ == '__main__':
    star_4()
