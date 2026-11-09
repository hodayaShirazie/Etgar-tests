from playwright.sync_api import Page, expect
from .base_page import BasePage
import utilities.config as config


class GooglePasswordPage(BasePage):

    URL = None

    def __init__(self, page: Page):
        super().__init__(page)

        self.password_input = page.get_by_role("textbox", name="Enter your password")

        self.next_button = page.get_by_role("button", name="Next")

    def enter_password(self):
        try:
            expect(self.password_input).to_be_visible()
        except AssertionError:
            page_text = self.page.locator("body").inner_text()
            if "This browser or app may not be secure." in page_text:
                raise AssertionError(
                    "Google blocked this automated browser sign-in. "
                    "Use an approved OAuth flow or a test authentication setup "
                    "instead of entering a Google password through Playwright."
                ) from None
            raise

        self.password_input.fill(config.GMAIL_PASSWORD)

    def click_next(self):
        self.next_button.click()