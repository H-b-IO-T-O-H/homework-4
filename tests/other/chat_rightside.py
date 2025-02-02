import unittest

from pages.chat_page import ChatPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from scenario.auth import auth_as_employer_has_comp
from tests.default_setup import default_setup


class ChatRightSide(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.TEST_MSG = "привет2"
        self.TEST_MSG2 = "привет"
        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.chatPage = ChatPage(self.driver)

    def test_send_by_button(self):
        auth_as_employer_has_comp(self)
        self.chatPage.open()
        self.chatPage.click_on_another_chat(0)
        self.chatPage.click_on_send_msg(self.TEST_MSG)
        text = self.chatPage.get_last_msg()
        self.assertEqual(text,self.TEST_MSG)
        self.chatPage.click_on_send_msg_by_enter(self.TEST_MSG2)
        text1 = self.chatPage.get_last_msg()
        self.assertEqual(text1, self.TEST_MSG2)

    def tearDown(self):
        self.driver.quit()
