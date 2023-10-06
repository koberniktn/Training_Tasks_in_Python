import math
from collections import Counter

def task_1():
    str = "Елки-палки, сколько елей здесь лежит"
    counter = 0

    for i in range(len(str)):
        if i == 0:
            if (str[i] == "Е"):
                counter += 1
        elif (str[i] == "е") and (str[i-1] == " "):
            counter += 1
    print(counter)

def task_1_smart():
    str = "Елки-палки, сколько елей здесь лежит"
    counter = 0

    for word in str.split():
        if word[0].lower() == 'е':

            counter += 1
    print(counter)

def task_2():
    str = " Road         u river  wood         ."
    counter = 0
    i = 0
    if str[i] != " ":
        counter += 1
    while str[i] != ".":
        if (str[i] == " ") and (str[i+1].isalpha()):
            counter += 1
        i += 1
    print(counter)

def task_2_smart():
    str = " Road         u river  wood         ."
    print(len(str.replace(".", "").split()))

def task_3():
    str = "fff^:fef:%    uY:   %%:7  "
    counter = 0
    for s in str:
        if s == ":":
            counter += 1
    str = str.replace(":", "%")
    print(str)
    print(counter)

def task_4():
    L = [1, 4, 5, 6, 3, 4, 6, 8, 9, 1]
    max_elem = max(L)
    print(max_elem)

    L = [None]*10
    sum = 0
    for i in range(10):
        L[i] = input()
        if int(L[i]) > 5:
            sum += int(L[i])
    print(sum)

def task_5_1():
    mas = []
    print("Введите число элементов и затем сами элементы")
    N = int(input())

    for i in range(N):
        mas.append(int(input()))
    print(min(mas))
    print(mas[::-1])

def task_5_2():
    A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    B = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    buffer = B
    B = A
    A = buffer

    print(A)
    print(B)

def task_8(n):
    print([n-1, n+1])

def task_9():
    str = "В лесу родилась ёлочка В лесу она росла"
    buff = ""
    res = []
    for i in range(len(str)):
        if str[i] == " ":
            res.append(buff)
            buff = ""
        else:
            buff += str[i].lower()
    res.append(buff)
    print(res)

def task_9_smart():
    str = "В лесу родилась ёлочка В лесу она росла"

    for word in str.split():
        print(word)

def my_log(numbers):
    log_of_numbers = []
    for elem in numbers:
        if elem > 0:
            log_of_numbers.append(math.log(elem))
        else:
            log_of_numbers.append(None)
    print(log_of_numbers)

def all_sort(num):
    buff = ""
    res = []
    for i in range(len(num)):
        if num[i] == ",":
            res.append(int(buff))
            buff = ""
        elif num[i] != " ":
            buff += num[i]
    res.append(int(buff))
    res.sort()
    print(res)

def task_12():
    words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]
    words_clean = []
    for elem in words:
        words_clean.append(elem.lower().strip())
    print(words_clean)

def task_13_1(str):
    letters = []
    words_counter = 0
    for i in range(len(str)):
        if str[i].isalpha():
            letters.append(str[i].lower())
        elif i != 0 and str[i] == " " and str[i-1].isalpha():
            words_counter += 1
    if str[-1].isalpha():
        words_counter += 1
    letters = set(letters)
    print("Количество слов =", words_counter)
    print("Количество уникальных букв =", len(letters))

    return letters

def task_13_2():
    str_1 = task_13_1("ПП рр оо ")
    str_2 = task_13_1("про про з")

    str_inter = str_1.intersection(str_2)
    print("Количество общих уникальных букв =", len(str_inter))
    print(str_inter)

def ts_13_s(str, i):
    words = str.split()
    count = Counter()
    print("Количество слов", i, "строки =", len(words))
    for word in words:
        count.update(map(lambda x: x.lower(), word))
    print("Количество уникальных букв =", len(count))
    return(count)

def task_13_smart():
    str_1 = ts_13_s("ПП рр оо ", 1)
    str_2 = ts_13_s("про про з", 2)

    str_inter = set(str_1.keys()).intersection(set(str_2.keys()))
    print("Количество общих уникальных букв =", len(str_inter))
    print(str_inter)


def repeat_task_1():
    correct_password = False
    true_password = "Qwerty"
    while not correct_password:
        print("Enter password: ")
        password = str(input())
        if password == true_password:
            correct_password = True
            print("Login success")
        else:
            print("Incorrect password, try again!")

def repeat_task_2():
    numbers = [3, 7, 11, 23, 18, 48, 81]
    print("Enter number")
    num = int(input())
    if numbers.count(num):
        print("Есть совпадение")
    else:
        print("Совпадений не найдено")

def repeat_task_3(num):
    num = str(num)
    num_new = num.replace(" ", "")
    num_new = num_new.replace("-", "")
    print(num_new)

def star_2():
    L = [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1]
    is_one = False
    index = 0
    max_len = 0
    counter = 0
    for i in range(len(L)):
        if L[i] == 1:
            if not is_one:
                is_one = True
                index = i
            counter += 1
        else:
            if is_one and counter > max_len:
                max_len = counter
            is_one = False
            counter = 0
    if counter > max_len:
        max_len = counter
    print("len =", max_len, ", index =", index)

def star_1():
    L = [[1, 2], [1, 2, 3, 6, 7], [1, 2, 3, 6], [1, 2, 3, 4]]
    new_L = []

    for i in range(len(L)):
        L[i] = set(L[i])

    for i in range(len(L)):
        buff = L[i]
        for j in range(len(L)):
            if i != j:
                buff = buff.difference(L[j])
        new_L.append(list(buff))
    print(new_L)

def star_3():
    str = " Привет привет       привет     при вет "
    words = []
    latters = {}
    start = 0

    for i in range(1, len(str)):
        if str[i] == " " and str[i-1].isalpha():
            if str[start:i].find("е") > 0:
                words.append(str[start:i].replace(" ", ""))
            start = i
    if str[-1].isalpha() and str[start:].find("е") > 0:
        words.append(str[start:].replace(" ", ""))

    for i in range(len(words)):
        for j in range(len(words[i])):
            if latters.get(words[i][j].lower()):
                latters[words[i][j].lower()] += 1
            else:
                latters[words[i][j].lower()] = 1
    print(words)

def star_3_smart():
    str = " Привет привет       привет     при вет "
    counter = Counter()
    for word in str.split():
        if 'е' in word:
            counter.update(map(lambda x: x.lower(), word))
    for letter in counter:
        print(letter, '=', counter[letter])


def star_4():
    str = "hhhhhhhhh          hhhhhhhhhh"
    str = str.strip()
    i = 0
    while i < len(str) - 1:
        if i != 0 and str[i] == str[i - 1]:
            str = str[:i-1] + str[i+1:]
            i -= 2
        i += 1
    if len(str) >= 2 and str[-1] == str[-2]:
        str = str[:len(str) - 2]
    print(str)

def star_5():
    str = "(              {[}   ]  )"
    str = str.replace(" ", "")
    dic = {"(": ")", "[": "]", "{": "}"}
    stak = [" "]

    for i in range(len(str)):
        if str[i] == dic.get(stak[-1], " "):
            stak.pop()
        else:
            stak.append(str[i])
    if stak[-1] == " ":
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    task_13_smart()
    task_13_2()
