from playwright.sync_api import Page, expect
import re
 
def test_homepage_heading(page: Page):
    page.goto("https://playwright.dev/")

    heading = page.get_by_role("heading", name=re.compile("^Playwright"), level=1)

    expect(heading).to_be_visible()


def test_get_started_navigation(page: Page):

    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()