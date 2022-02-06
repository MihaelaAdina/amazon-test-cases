# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# inherit TestCase Class and create a new test class
class AmazonProduct(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test case method. It should always start with test_
    def test_search_for_iphone(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("https://www.amazon.com/ref=nav_logo")

        select_searchbar = driver.find_element(By.ID, 'twotabsearchtextbox')
        self.assertEqual(select_searchbar.tag_name, 'input')

        select_searchbar.send_keys('iphone charger' + Keys.ENTER)

        # aici se electeaza al 4-lea element si se da click pe el
        driver.find_element(By.XPATH, '(//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]/a)[4]').click()

        select_products = Select(driver.find_element(By.ID, 'quantity'))
        select_products.select_by_value('2')

        self.assertEqual(select_products.first_selected_option.text, '2')

        driver.find_element(By.ID, 'add-to-cart-button').click()

        driver.find_element(By.ID, 'nav-cart').click()

        delete_button = driver.find_element(By.XPATH, '(//div[@class="a-row sc-action-links"]/span/span/input[@data-action="delete"])')
        delete_button.click()

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()






