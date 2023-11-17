import requests

def get_agents():
    url = 'https://valorant-api.com/v1/agents'
    response = requests.get(url)
    
    if response.status_code == 200:
        agents_data = response.json()
        for agent in agents_data['data']:
            print(f"Имя персонажа: {agent['displayName']}")
            print(f"Имя агента: {agent['developerName']}")
            print(f"Описание: {agent['description']}")
            print("--------------------")
    else:
        print("Ошибка при получении данных об агентах")

def get_maps():
    url = 'https://valorant-api.com/v1/maps'
    response = requests.get(url)
    
    if response.status_code == 200:
        maps_data = response.json()
        for map_info in maps_data['data']:
            print(f"Имя карты: {map_info['displayName']}")
            print(f"Описание: {map_info['narrativeDescription']}")
            print("--------------------")
    else:
        print("Ошибка при получении данных о картах")

def get_weapons():
    url = 'https://valorant-api.com/v1/weapons'
    response = requests.get(url)
    
    if response.status_code == 200:
        weapons_data = response.json()
        for weapon in weapons_data['data']:
            print(f"Название оружия: {weapon['displayName']}")
            print(f"Тип: {weapon['category']}")
            print("--------------------")
    else:
        print("Ошибка при получении данных об оружии")

def get_events():
    url = 'https://valorant-api.com/v1/events'
    response = requests.get(url)
    
    if response.status_code == 200:
        events_data = response.json()
        for event in events_data['data']:
            print(f"Название события: {event['displayName']}")
            print(f"Дата начала: {event['startTime']}")
            print(f"Дата окончания: {event['endTime']}")
            print("--------------------")
    else:
        print("Ошибка при получении данных о событиях")

get_agents()
get_maps()
get_weapons()
get_events()
