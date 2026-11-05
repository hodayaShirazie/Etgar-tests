from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage
import pages.google_login_page as google_login_page
import pages.password_page as password_page
import utilities.config as config
import re



@pytest.mark.smoke
def test_gmail_login(page: Page, request):
    sign_in = LoginPage(page)
    sign_in.open()

    with page.expect_popup() as popup_info:
        sign_in.navigate_to_login()

    login_page = popup_info.value

    expect(login_page).to_have_url(
        re.compile(r"^https://accounts\.google\.com/")
    )

    google_login = google_login_page.GoogleLoginPage(login_page)
    
    # Enter email
    google_login = google_login_page.GoogleLoginPage(login_page)
    google_login.enter_email(config.GMAIL_EMAIL)
    google_login.click_next()

    # # Enter password
    # password = password_page.GooglePasswordPage(login_page)
    # password.enter_password(config.GMAIL_PASSWORD)
    # password.click_next()


