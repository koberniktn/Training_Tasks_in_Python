def walk(trains, event):
    passenge_found = False
    i = 0
    name = event.get("passenger", None)
    distance = event.get("distance", None)

    if (name == None) or (distance == None):
        print("Недостаточно данных")
        return -1
    for train in trains:
        cars = train["cars"]
        while i < len(cars) and passenge_found == False:
            if name in cars[i]["people"]:
                passenge_found = True
                cars[i]["people"].remove(name)
                if i + distance + 1 > len(cars) or i + distance < 0:
                    print("Пассажир ушел за пределы поезда :(")
                    return -1
                cars[i + distance]["people"].append(name)
            i += 1

    if passenge_found == False:
        print("По поезду передвигается неопознанный пассажир")
        return -1

    return(trains)

def switch(trains, event):
    train_from, train_to, amount = event["train_from"], event["train_to"], event["cars"]
    buff = []

    for train in trains:
        if train["name"] == train_from:
            if amount > len(train["cars"]):
                print("Попытка отцепить слишком много вагонов")
                return -1
            for i in range(amount):
                buff.append(train["cars"].pop())

    if buff == []:
        print("From_train не найден")
        return -1

    for train in trains:
        if train["name"] == train_to:
            train["cars"].exstend(buff[::-1])
            return(trains)

    return -1

def process(data):
    trains, events, result = data['trains'], data['events'], data['result']
    car_res = data["result"]["car"]
    for event in events:
        if event.get("type") == "walk":
            trains = walk(trains, event)
            if trains == -1:
                print(-1)
                return -1
        if event.get("type") == "switch":
            trains = switch(trains, event)
            if trains == -1:
                print(-1)
                return -1

    for train in trains:
        for car in train["cars"]:
            if car["name"] == car_res:
                result = len(car["people"])
                print(result)
                if result == data["result"]["amount"]:
                    print("It is true")
                else:
                    print("Not correct!!!")
                return result
