import urllib.parse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    BASE_URL = 'https://studhunt.ru/'
    PATH = ''

    def __init__(self, driver, container):
        self.driver = driver
        self.container = container

    def open(self, query='') -> None:
        if query != '':
            self.PATH += query
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def is_open(self) -> bool:
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self.container)))
        except TimeoutException:
            return False
        return True

    def wait_for_page_open(self):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, self.container)))
