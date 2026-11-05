from playwright.sync_api import Page
from .base_page import BasePage
# from tests.playwright.consts import FILE_PATH, REGISTRATION_FORM
import re
import utilities.config as config


class LoginPage(BasePage):
    URL = config.GMAIL_URL


    def __init__(self, page: Page):
        super().__init__(page)
        self.signin_button = page.get_by_role("link", name="כניסה ל-Gmail")


    def navigate_to_login(self):
        self.signin_button.click()
