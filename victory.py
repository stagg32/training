"""
Кевин Митник - г.р.1963,  Альберт Эйнштейн - г.р.1879, Роджер Желязны - г.р.1937
Альберт Кинг - г.р.1923, Стив Джобс - г.р.1955, Гордон Фримен - г.р.1971
"""
decision = "да"
while decision == "да":
    rightanswer = int(0)
    wronganswer = int(0)

    print("Привет! Знаешь ли ты год рождения героев данной викторины?")
    mitnik = input("Напиши год рождения программиста Кевина Митника: ")
    if mitnik == "1963":
        rightanswer += 1
    else:
        wronganswer += 1
    albert = input("Напиши год рождения физика Альберта Эйнштейна: ")
    if albert == "1879":
        rightanswer += 1
    else:
        wronganswer += 1
    rojer = input("Напиши год рождения писателя Роджера Желязны: ")
    if rojer == "1937":
        rightanswer += 1
    else:
        wronganswer += 1
    albertking = input("Напиши год рождения музыканта Альберта Кинга: ")
    if albertking == "1923":
        rightanswer += 1
    else:
        wronganswer += 1
    steve = input("Напиши год рождения изобретателя Стива Джобса: ")
    if steve == "1955":
        rightanswer += 1
    else:
        wronganswer += 1
    gordon = input("Напиши год рождения физика-мастера монтировки Гордона Фримена: ")
    if gordon == "1971":
        rightanswer += 1
    else:
        wronganswer += 1

    print("Количество правильных ответов - ", rightanswer)
    print("Количество неправильных ответов - ", wronganswer)
    print("Процент правильных ответов - ", format(float(rightanswer*100/6), ".3g"))
    print("Процент неправильных ответов - ", format(float(wronganswer*100/6), ".3g"))
    decision = input("Сыграем еще?(да/нет): ")

print("До скорого!")