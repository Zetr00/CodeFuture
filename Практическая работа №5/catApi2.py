import requests
from PIL import Image
from io import BytesIO

def get_cat_images(query=None, params=None):
    url = 'https://cataas.com/cat'
    if query:
        url += f'/{query}'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.content
    else:
        return None

def display_image(image_data):
    if image_data:
        image = Image.open(BytesIO(image_data))
        image.show()
    else:
        print("Не удалось получить изображение.")

def main():
    print("Привет! Чтобы получить фотографию кота, нажмите 1.")
    print("Для получения фотографии с дополнительными параметрами, нажмите 2.")
    choice = input("Выберите опцию (1 или 2): ")

    if choice == '1':
        image_data = get_cat_images()
        display_image(image_data)
    elif choice == '2':
        query = input("Введите запрос (например, 'funny', 'cute'): ")
        params = {'filter': query}
        image_data = get_cat_images(params=params)
        display_image(image_data)
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()
