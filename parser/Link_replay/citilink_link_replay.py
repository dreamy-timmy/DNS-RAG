from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from open_json import append_to_json

import time
import random
import json
import requests  # Для обработки ошибок 429

# Функция для сохранения HTML-кода элемента с заданным классом
def save_html_element(url, target_class):
    """
    Загружает страницу с помощью Selenium, извлекает данные элемента с указанным классом и сохраняет их.

    :param url: URL страницы, которую нужно обработать.
    :param target_class: CSS-класс целевого HTML-элемента для извлечения.
    """
    start_time = time.time()  # Время начала
    # Настройка Selenium WebDriver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-webgl")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")

    # Инициализация WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Загрузка страницы
        print(f"Загрузка страницы: {url}")
        driver.get(url)
        time.sleep(random.randint(4, 8))  # Даем время для загрузки страницы

        # Парсинг HTML-кода страницы
        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        # Поиск элемента с заданным классом
        target_element = soup.find("ul", class_=target_class)
        price = soup.find("span", class_="e1j9birj0 e106ikdt0 app-catalog-8hy98m e1gjr6xo0")
        if target_element and price:
            parse_html_file(target_element, price, url)
        else:
            print(f"Элемент с классом '{target_class}' не найден.")
        
        # Закрытие драйвера после выполнения
        driver.quit()

    except Exception as e:
        print(f"Произошла ошибка при парсинге страницы: {e}")
        driver.quit()

    finally:
        # Время выполнения
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time:.4f} секунд")

def parse_html_file(soup, price, url):
    """
    Парсит HTML-код страницы, извлекая информацию о товарах и их характеристиках.

    :param soup: Объект BeautifulSoup с HTML-кодом страницы.
    :param price: Цена товара, извлеченная из HTML.
    :param url: URL страницы, из которой извлекаются данные.
    """
    items = soup.find_all('li', class_="app-catalog-10ib5jr e1fzyj0h0")
    
    dicrt_h4 = {}

    for item in items:
        h4 = item.find('h4', class_="e1k1l4a50 eml1k9j0 app-catalog-vgrnu3 e1gjr6xo0")
        parameters_and_meanings = {}

        # Извлечение параметров и их значений
        parameters = item.find_all('div', class_="app-catalog-xc0ceg e1ht5hpa5")
        for div_parameter in parameters:
            span_parameter = div_parameter.find('span', class_="e1ht5hpa1 e106ikdt0 app-catalog-fclnc2 e1gjr6xo0")
            if span_parameter:
                parameter_text = span_parameter.text.strip()

            meaning = div_parameter.find('span', class_="e1ht5hpa0 e106ikdt0 app-catalog-1r8w4u1 e1gjr6xo0")
            if meaning:
                meaning_text = meaning.text.strip()
                parameters_and_meanings[parameter_text] = meaning_text    

        # Сохраняем данные в словарь
        h4_text = h4.text.strip()
        dicrt_h4["Цена"] = price.text.strip()
        dicrt_h4[h4_text] = parameters_and_meanings

    product_data.append({
        url: dicrt_h4,
    })    

def make_request_with_retries(url, retries=5, delay=30):
    """
    Функция для обработки ошибки 429 и повторного запроса с задержкой
    """
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            if response.status_code == 429:
                print(f"Ошибка 429 на странице {url}, задержка {delay} секунд")
                time.sleep(delay)
                attempt += 1
                continue
            elif response.status_code != 200:
                print(f"Ошибка {response.status_code}: Не удалось загрузить страницу {url}")
                break
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
            time.sleep(delay)
            attempt += 1
    return None


"""
Основной процесс парсинга:
1. Чтение списка URL-адресов из файла.
2. Последовательная обработка страниц:
   - Загрузка страницы с помощью Selenium.
   - Извлечение характеристик товаров.
   - Сохранение данных в JSON-файл каждые 10 обработанных URL.
3. Обработка ошибок, включая повторные попытки запросов.
"""

# URL и параметры
links = []
product_data = []

# Открытие файла с ссылками
with open('parser/File_save/citilink_product_urls.txt', 'r', encoding='utf-8') as file:
    links = [line.strip() for line in file]
target_class = "app-catalog-rxgulu e1ht5hpa6"

count = 1
len_links = len(links)
# Вызов функции
for url in links[count-1:1001]:
    save_html_element(url + "properties/", target_class)
    print(f"\/\Обработано ссылок {count}\{len_links}")
    if count%10==0:
        print(f"+--------------------+--------------------+--------------------+Прошёл границу в {count}+--------------------+--------------------+--------------------+")
        append_to_json('parser\laptop_specifications\citilink_product_data.json', product_data)
        product_data = []
    count+=1
