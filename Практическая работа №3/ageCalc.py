def days_lived(year_of_birth):
    from datetime import datetime

    current_year = datetime.now().year
    current_age = current_year - year_of_birth

    days_lived = 0

    for year in range(year_of_birth, current_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days_lived += 366
        else:
            days_lived += 365

    return days_lived, current_age


if __name__ == "__main__":
    year_of_birth = int(input("Введите год рождения: "))

    total_days_lived, current_age = days_lived(year_of_birth)
    print(f"Прожито дней: {total_days_lived}")
    print(f"Полный возраст: {current_age}")
