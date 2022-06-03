yearofbirth = 1
while yearofbirth != 1799:
    yearofbirth = int(input("Введите год рождения А.С.Пушкина от Р.Х.: "))

    if yearofbirth == 1799:
        print("Верно!")
        dayofbirth = 1
        while dayofbirth != "6 июня":
            dayofbirth = input("Введи его день Рождения: ")
            if dayofbirth == "6 июня":
                print("Верно!")
            else:
                print("Неверный день рождения")
    else:
        print("Неверный год рождения")