import requests
from bs4 import BeautifulSoup

url = 'http://example.org'

# Отправка HTTP-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Извлечение HTML-кода
    html_content = response.text

    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлечение значения из тега <title>
    title_tag = soup.find('title')
    if title_tag:
        title_text = title_tag.text
        print(f"Title: {title_text}")
    else:
        print("Title tag not found in the HTML.")
else:
    print(f"HTTP request failed with status code {response.status_code}.")
