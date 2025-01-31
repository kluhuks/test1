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
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")  

service = Service("C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe")  
driver = webdriver.Chrome(service=service, options=options)
def scen_1():
    try:
        
        start_time = time.time() 

        
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()
        time.sleep(1)  


        search_box = driver.find_element(By.NAME, "search")

 
        search_box.send_keys("Солнечная система")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)

    finally:
        end_time = time.time() 
        execution_time = end_time - start_time
        

        driver.quit()
        return execution_time

print(f"Время выполнения теста: {scen_1():.2f} секунд")