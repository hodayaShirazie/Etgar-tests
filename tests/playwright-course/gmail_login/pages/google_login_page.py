from playwright.sync_api import Page, expect
from .base_page import BasePage


class GoogleLoginPage(BasePage):

    URL = None

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_role("textbox", name="Email or phone")
        self.next_button = page.get_by_role("button", name="Next")

    def enter_email(self, email: str):
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)

    def click_next(self):
        self.next_button.click()