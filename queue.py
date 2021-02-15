def person(f):
    global count
    while f:
        event = input('\x1B[36mНовый посетитель или выдача посылки?: \x1B[0m')
        if event != '-':
            if len(f) == 9:
                covid(f)
            elif len(f) % 10 == 1:
                print(f"\x1B[37mПеред вами {len(f)} посетитель\x1B[0m")

            elif len(f) % 10 == 2 or len(f) % 10 == 3 or len(f) % 10 == 4:
                print(f"\x1B[37mПеред вами {len(f)} посетителя\x1B[0m")

            else:
                print(f"\x1B[37mПеред вами {len(f)} посетителей\x1B[0m")
            f.append(event)
            print(f)  # чтобы проверить количество людей в очереди
        else:
            vydacha(f)
        continue
    return f


def vydacha(f):
    global count
    recipient = f[0]
    print(f"\x1B[1;35mПосылка выдана {recipient}. Хорошего дня!\x1B[0m")
    count += 1
    if count % 10 == 5:
        print('\x1B[31;1;40mУ нас перерыв!\x1B[0m')
        print(count)  # там ли выдает реплику
    if count % 10 == 6:
        print("\x1B[1;31;40mУ нас санобработка!\x1B[0m")
        print(count)  # там ли выдает реплику
    if count % 10 == 7:
        print("\x1B[1;31;40mДа откуда вы все взялись?! Обед!\x1B[0m")
        print(count)  # там ли выдает реплику
    f.pop(0)
    if len(f) % 10 == 2 or len(f) % 10 == 3 or len(f) % 10 == 4:
        print(f"\x1B[37mВ очереди осталось {len(f)} человека\x1B[0m")
    elif len(f) % 10 == 1:
        print(f"\x1B[37mВ очереди остался {len(f)} человек\x1B[0m")
    else:
        print(f"\x1B[37mВ очереди осталось {len(f)} человек\x1B[0m")


def no_queue(f):
    while not f:
        event = input("Кто-то еще пришел?: ")
        if event != '-':
            f.append(event)
        else:
            print("Посылку отдавать некому")
            no_queue(f)
            continue
    return f


def covid(f):
    global count
    while len(f) >= 9:
        event = input("\x1B[1;34mСлушаю? \x1B[0m")
        if event != '-':
            print(f"\x1B[1;41;30mТут уже {len(f)} человек, ждите на улице.\x1B[0m")
            covid(f)
        else:
            vydacha(f)

            continue
    return f


print("\x1B[1;34;40mВас приветствует Почта России! Мы не очень дружелюбные, но выбора у вас нет.\x1B[0m")
queue = []
count = 0
while True:
    if queue:
        person(queue)
    else:
        no_queue(queue)
