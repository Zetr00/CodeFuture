try:
    month = int(input("Введите номер месяца вашего рождения (1-12): "))
    if 1 <= month <= 12:
        if 3 <= month <= 5:
            season = "весной"
            description = "Птицы пели прекрасные песни."
        elif 6 <= month <= 8:
            season = "летом"
            description = "Солнце светило ярче, чем когда-либо."
        elif 9 <= month <= 11:
            season = "осенью"
            description = "Урожай был невероятным."
        else:
            season = "зимой"
            description = "За окном падал белый снег."

        months = [
            "январе", "феврале", "марте", "апреле", "мае", "июне",
            "июле", "августе", "сентябре", "октябре", "ноябре", "декабре"
        ]
        month_name = months[month - 1]

        print(f"Вы родились в {month_name} {season}. {description}")
    else:
        print("Неверно введен номер месяца. Введите число от 1 до 12.")
except ValueError:
    print("Неверный формат ввода. Пожалуйста, введите целое число от 1 до 12.")
