from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class ResumeCreateFormLocators:
    def __init__(self):
        self.root = "(//div[@class ='page-name'])"

        self.title = "//*[@id='title']"
        self.description = '//textarea[@id="description"]'
        self.place = '//input[@id="place"]'
        self.skills = '//textarea[@id="skills"]'
        self.salary_min = '//input[@id="salary_min"]'
        self.salary_max = '//input[@id="salary_max"]'
        self.surname = '//input[@id="surname"]'
        self.name = '//input[@id="name"]'
        self.email = '//input[@id="email"]'

        self.job_date = '(//div[@class="job-container"])/div[1]'
        self.job_name = '(//div[@class="job-container"])/div[3]'
        self.job_position = '(//div[@class="job-container"])/div[2]'

        self.submit = '//button[text()="Сохранить"]'
        self.browse_image_btn = '//input[@id="sum-img-load"]'
        self.add_experience_btn = '//div[@class="btn-add-exp"]'
        self.experience_container = '//div[@class="job"]'

        self.error_title = '(//span[@class="error"])[1]'
        self.error_surname = '(//span[@class="error"])[2]'
        self.error_name = '(//span[@class="error"])[3]'
        self.error_email = '(//span[@class="error"])[4]'
        self.error_description = '(//span[@class="error"])[5]'
        self.error_place = '(//span[@class="error"])[6]'
        self.error_skills = '(//span[@class="error"])[7]'
        self.error_salary = '(//span[@class="error"])[8]'
        self.error_common = '(//span[@class="error"])[9]'


class ResumeCreateForm(BaseComponent):
    def __init__(self, driver):
        super(ResumeCreateForm, self).__init__(driver)
        self.locators = ResumeCreateFormLocators()

        self.error_message_input = 'Поле обязательно для заполнения.'
        self.error_message_email = 'Укажите email.'
        self.error_message_common = 'Что-то пошло не так. Попробуйте позже.'

    def set_input(self, locator: str, data: str):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        ).send_keys(data)

    def submit_resume(self):
        self.click_locator(self.locators.submit)

    def clear_contact_data(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.surname))
        ).clear()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.name))
        ).clear()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.email))
        ).clear()

    def wait_for_resume_page(self):
        self.wait.until(
            EC.url_matches("https://studhunt.ru/resume")
        )

    def is_error_input(self, locator: str, error_message):
        try:
            _ = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, locator), error_message)
            )
            return True
        except TimeoutException:
            return False

    def load_image(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.browse_image_btn))
        ).send_keys('test_data/big_img.png')

    def open_popup_add_experience(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.add_experience_btn))
        ).click()

    def check_experience_exist(self):
        try:
            self.driver.find_element_by_xpath(self.locators.experience_container)
            return True
        except NoSuchElementException:
            return False

    def get_job_date(self):
        date = self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.job_date)
        ).text
        return date.split('_')

    def get_job_name(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.job_name)
        ).text

    def get_job_position(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.job_position)
        ).text

    def set_title(self, title: str):
        self.set_input(self.locators.title, title)

    def set_description(self, description: str):
        self.set_input(self.locators.description, description)

    def set_place(self, place: str):
        self.set_input(self.locators.place, place)

    def set_skills(self, skills: str):
        self.set_input(self.locators.skills, skills)

    def set_salary_min(self, salary: str):
        self.set_input(self.locators.salary_min, salary)

    def set_salary_max(self, salary: str):
        self.set_input(self.locators.salary_max, salary)

    def set_email(self, email: str):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.email))
        ).clear()
        self.set_input(self.locators.email, email)

    def is_title_error(self):
        return self.is_error_input(self.locators.error_title, self.error_message_input)

    def is_description_error(self):
        return self.is_error_input(self.locators.error_description, self.error_message_input)

    def is_place_error(self):
        return self.is_error_input(self.locators.error_place, self.error_message_input)

    def is_skills_error(self):
        return self.is_error_input(self.locators.error_skills, self.error_message_input)

    def is_salary_error(self, error_message):
        return self.is_error_input(self.locators.error_salary, error_message)

    def is_surname_error(self):
        return self.is_error_input(self.locators.error_surname, self.error_message_input)

    def is_name_error(self):
        return self.is_error_input(self.locators.error_name, self.error_message_input)

    def is_email_error(self):
        return self.is_error_input(self.locators.error_email, self.error_message_email)

    def is_common_error(self, error_message=None):
        if error_message is None:
            error_message = self.error_message_common
        return self.is_error_input(self.locators.error_common, error_message)
