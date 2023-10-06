import re

def task_1():
    L = []
    Sum = 0

    print("Введите длину списка:")
    try:
        n = int(input())
    except:
        print("Длина списка должна быть целым числом")
        return 0

    for i in range(n):
        print("L[", i, "] = ", sep="", end="")
        L.append(input())

    for i in range(len(L)):
        try:
            Sum += int(L[i])
        except ValueError:
            Sum += -1
    if Sum == -1 * len(L):
        print("Элементы списка нельзя суммировать")
    else:
        print(Sum)

def foo(d):
  d.update({'new_key':'with_map'})
  return d

def task_2():
    L = [{"Кот": "Фунтик"}, {"Питон": "Жизнь"}, {"Настя": "Солнышко ^^"}]

    L = list(map(foo, L))
    print(L)

def task_3():
    a = [-1, 2, -3, 4, 5]

    a = list(filter(lambda x: x > 0, a))
    print(a)

def foo_in_task_4(a, b):
  c = []
  for i in range(len(a)):
    if a[i] > b[i]:
      c.append(0)
    else:
      c.append(1)
  return c

def task_4(a, b):
    return list(map(lambda x, y: 0 if x > y else 1, a, b))

def simple_generator(val):
   while val > 0:
       val = val / 2
       yield val

def task_5():
    gen_iter = simple_generator(100)
    i = 10
    while i > 0:
        try:
            print(next(gen_iter))
        except StopIteration:
            print("StopIteration")
            return 0

def task_6():
    str = "anf 17u fkjgktjg 123 gvbnn 81 jfjgj 12/n"
    a = re.findall(r' 1\d*' , str)
    print(list(map(lambda x: x.strip(), a)))

if __name__ == '__main__':
    task_6()
