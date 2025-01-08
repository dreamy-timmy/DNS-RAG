from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random

# Список для хранения ссылок на карточки товаров
product_urls = []

# Настройка Selenium WebDriver
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")  # Отключаем GPU
options.add_argument("--disable-webgl")  # Отключаем WebGL
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Инициализация WebDriver с использованием менеджера драйверов
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Функция парсинга страниц
def parse_dns_notebooks(start_page, end_page):
    for page_num in range(start_page, end_page + 1):
        url = f"https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?p={page_num}"
        print(f"Загружается страница {page_num} по URL: {url}")
        
        # Открываем страницу
        driver.get(url)
        time.sleep(random.randint(5, 12))  # Задержка для имитации активности пользователя

        # Получаем HTML-код страницы
        soup = BeautifulSoup(driver.page_source, 'lxml')

        # Находим все элементы <a> с нужным классом
        links = soup.find_all("a", class_="catalog-product__name ui-link ui-link_black")

        # Извлекаем ссылки из атрибута href
        if links:
            for link in links:
                product_page_url = link.get('href')
                if product_page_url:
                    full_url = "https://www.dns-shop.ru" + product_page_url  # Преобразуем относительную ссылку в абсолютную
                    product_urls.append(full_url)
            print(f"Найдено {len(links)} ссылок на странице {page_num}")
        else:
            print(f"Не удалось найти ссылки на странице {page_num}")

        print(f"Парсинг страницы {page_num} завершен. Перехожу к следующей.\n")
        print("+----------------------------------------------------------+")

# Задаем диапазон страниц для парсинга от 1 до 55
parse_dns_notebooks(start_page=1, end_page=55)

# Закрываем браузер
driver.quit()

# Сохраняем результат в файл
output_file = 'parser/File_save/dns_product_urls.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for url in product_urls:
        file.write(f"{url}\n")

print(f"Парсинг завершен. Ссылки сохранены в файл '{output_file}'")
