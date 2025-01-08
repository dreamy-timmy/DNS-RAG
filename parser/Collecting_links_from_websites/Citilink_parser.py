from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random

product_urls = []

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
# Инициализация WebDriver с использованием менеджера драйверов
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for page_num in range(1, 22):  # От 1 до 22
    url = f"https://www.citilink.ru/catalog/noutbuki/?p={page_num}"
    print(f"Загружается страница {page_num} по URL: {url}")
    
    driver.get(url)
    time.sleep(random.randint(5, 12))  # Даем время для загрузки страницы

    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Находим все элементы <a> с нужным классом
    links = soup.find_all("a", class_="app-catalog-9gnskf")
    print(f"Найдено {len(links)} ссылок на странице {page_num}")

    # Извлекаем ссылки из атрибута href
    for link in links:
        product_page_url = link.get('href')
        if product_page_url:
            full_url = "https://www.citilink.ru" + product_page_url + "properties/"  # Преобразуем относительную ссылку в абсолютную
            product_urls.append(full_url)

    print(f"Парсинг страницы {page_num} завершен. Перехожу к следующей.")
    print("+----------------------------------------------------------+")

driver.quit()

# Сохраняем результат в файл
with open('parser/File_save/citilink_product_urls.txt', 'a') as file:
    for line in product_urls:
        file.write(f"{line}\n")

print("Ссылки сохранены в файл 'parser/File_save/citilink_product_urls.txt'")
