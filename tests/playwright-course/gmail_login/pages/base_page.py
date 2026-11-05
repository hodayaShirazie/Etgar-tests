from playwright.sync_api import Page
import utilities.config as config

class BasePage:
    URL = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.URL is None:
            raise NotImplementedError(f"{type(self).__name__} must define URL")
        self.page.goto(self.URL)