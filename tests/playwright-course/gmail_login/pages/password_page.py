from playwright.sync_api import Page, expect
from .base_page import BasePage


class GooglePasswordPage(BasePage):

    URL = None

    def __init__(self, page: Page):
        super().__init__(page)

        self.password_input = page.get_by_role("textbox", name="Enter your password")

        self.next_button = page.get_by_role("button", name="Next")

    def enter_password(self, password: str):
        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)

    def click_next(self):
        self.next_button.click()