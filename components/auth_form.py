from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class AuthLocators:
    def __init__(self):
        self.root = '//div[@class="auth"]'
        self.email_field = '//input[@id="emailAuth"]'
        self.chat_btn = '//a[@href="/chats"]'
        self.password_field = '//input[@id="passAuth"]'
        self.submit_btn = '//button[@id="entBtnAuth"]'
        self.profile_btn = '//a[@href="/profile"]'
        self.login_btn = '//a[@href="/auth"]'
        self.error_field = '//div[@class="error error_limit-width error_center"]'
        self.registration_link = '//div[@class="input-data-card__link"]'
        self.incorrect_error_field = '//span[@class="error"]'


class AuthForm(BaseComponent):
    def __init__(self, driver):
        super(AuthForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = AuthLocators()

    def set_email(self, email: str):
        """
        Вводит логин в окне авторизации
        :param email: email пользователя
        """
        user_email = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.email_field))
        )
        user_email.send_keys(email)

    def set_password(self, pwd: str):
        """
        Вводит пароль в окне авторизации
        :param pwd: пароль пользователя
        """
        password = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.password_field))
        )
        password.send_keys(pwd)

    def submit(self):
        """
        Завершает авторизацию
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit_btn))
        )
        submit.click()

    def wait_for_mainpage(self):
        """
        Ождиает пока не откроется главная страница
        """
        try:
            WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.locators.profile_btn)
            )
            WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.locators.chat_btn)
            )
            return True
        except NoSuchElementException:
            return False

    def top_error(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.locators.error_field)))
            return True
        except TimeoutException:
            return False

    def check_any_error(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.incorrect_error_field)))

    def click_href_reg(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.registration_link))
        )
        element.click()

    def is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.login_btn)))
            return True
        except:
            return False
