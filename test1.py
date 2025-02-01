import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import driver_config
import config

class TestWikiSearch(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.driver = driver_config.get_driver()
    
    def test_search_wikipedia(self):
        """Тест поиска на Wikipedia"""
        start_time = time.time()
        
        self.driver.get("https://www.wikipedia.org/")
        self.driver.maximize_window()
        time.sleep(1)
        
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        
        search_box.send_keys("Солнечная система")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения теста: {execution_time:.2f} секунд")
        

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
        self.assertIn("Солнечная система", self.driver.title)

    def tearDown(self):
        """Закрытие браузера после каждого теста"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()