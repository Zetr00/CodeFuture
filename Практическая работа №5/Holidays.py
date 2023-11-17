import requests

def get_holidays(country_code):
    url = f'https://date.nager.at/Api/v2/NextPublicHolidays/{country_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_holidays(holidays):
    if holidays:
        print("Праздники и даты:")
        for holiday in holidays:
            print(f"{holiday['name']} - {holiday['date']}")
    else:
        print("Не удалось получить данные о праздниках.")

def main():
    print("Привет! Этот скрипт позволяет получить список праздников по стране.")
    country_code = input("Введите код страны (например, 'US' для США, 'GB' для Великобритании): ")

    holidays = get_holidays(country_code)
    display_holidays(holidays)

if __name__ == "__main__":
    main()
