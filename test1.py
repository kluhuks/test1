from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")  # Отключение песочницы
options.add_argument("--disable-dev-shm-usage")  # Исправление для Linux
options.add_argument("--disable-gpu")  # Отключение GPU (иногда помогает)

service = Service("C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe")  # Укажи путь к ChromeDriver
driver = webdriver.Chrome(service=service, options=options)
def scen_1():
    try:
        
        start_time = time.time()  # Запуск таймера

        # Открытие главной страницы Википедии
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()
        time.sleep(1)  # Даем время на загрузку страницы

        # Поиск строки поиска
        search_box = driver.find_element(By.NAME, "search")

        # Ввод ключевого слова и нажатие Enter
        search_box.send_keys("Солнечная система")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)  # Ожидание загрузки результатов

    finally:
        end_time = time.time()  # Завершение таймера
        execution_time = end_time - start_time
        
        # Закрытие браузера
        driver.quit()
        return execution_time

print(f"Время выполнения теста: {scen_1():.2f} секунд")