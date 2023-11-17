import requests

def get_cat_fact():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('fact')
    else:
        return None

def get_custom_cat_fact():
    endpoint = input("Введите конечную точку API (например, 'fact', 'breeds'): ")
    url = f'https://catfact.ninja/{endpoint}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    print("Привет! Чтобы получить случайный факт о котах, нажмите 1.")
    print("Для выбора конкретной конечной точки API, нажмите 2.")
    choice = input("Выберите опцию (1 или 2): ")

    if choice == '1':
        fact = get_cat_fact()
        if fact:
            print("Случайный факт о котах:")
            print(fact)
        else:
            print("Не удалось получить факт о котах.")
    elif choice == '2':
        custom_data = get_custom_cat_fact()
        if custom_data:
            print("Данные из выбранной конечной точки:")
            print(custom_data)
        else:
            print("Не удалось получить данные из выбранной конечной точки.")
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()