import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(1)
        buscar_por_xpath=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(1)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


