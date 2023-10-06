def task_1():
    rept = {"python": " питон", "anaconda": "анаконда", "tortoize": " черепаха"}
    rept["snake"] = "змея"

    buff = rept.pop("tortoize", None)
    rept["tortoise"] = buff

    for key, value in rept.items():
        print(value.strip(), "на английском будет", key.strip())

def task_2():
    cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
    fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

    dic = dict(list(zip(cnt, fh)))
    print(dic)

def task_3():
    L_1 = ["Ann", "Tim", "Sam", "T"]
    L_2 = [12, 23, 17]

    if len(L_1) == len(L_2):
        dic = dict(list(zip(L_1, L_2)))
    else:
        print("Списки имеют разную длину")
        dic = dict()
    print(dic)

def task_4(): #было бы неплохо оптимизировать
    remarks = {'namе': 'Kyzya', 'subject': 'Python', 'mark':4}
    journal = {'Ivanov': {'Math':4, 'Physics':5}, 'Sidorov': {'Java':5}}

    name = remarks.get('namе')
    subject = remarks.get('subject')
    mark = remarks.get('mark')

    student_dic = journal.get(name, None)

    if student_dic != None:
        if student_dic.get(subject, None) != None:
            if student_dic[subject] == mark:
                print("Оценка по дисциплине", subject,"уже существует")
            else:
                journal[name][subject] = mark
                print("Оценка добавлена")
        else:
            journal[name][subject] = mark
            print("Оценка и предмет добавлены")
    else:
        journal[name] = {subject: mark}
        print("Ученик, ценка и предмет добавлены")
    print(journal)

def task_5():
    dic = [{'product': 'shirt', 'number': 10}, {'product': 'jeans', 'number': 5}, {'product': 'shuffle', 'number': 4}]
    max_count = 0
    product = ""

    for elem in dic:
        if elem['number'] >= max_count:
            max_count = elem['number']
            product = elem['product']
    print(product)

if __name__ == '__main__':
    task_5()
