
"""
Hodaya Shirazie
21390778-5
"""

from playwright.sync_api import Page
import pytest
from pages.registrantion_page import RegistrationPage
from pathlib import Path
from datetime import datetime


def test_registration_form(page: Page, request):

    registration = RegistrationPage(page)

    registration.open()

    registration.fillInFullForm()

    registration.validateResetForm()

    registration.fillInFullForm()

    registration.validateSubmitForm()

    takeScreenshot(page, request)

@pytest.mark.smoke
@pytest.mark.regression
def test_header(page: Page):

    registration = RegistrationPage(page)

    registration.open()

    # validateRegistrationLink(page)
    registration.validateNavigationLink("Registration", "region", "Registration details")

    # validatePreferencesLink(page)
    registration.validateNavigationLink("Preferences", "heading", "Preferences")

    registration.validateHelpLink()

    registration.validatePlaywrightDocsLink()

    # registration.validateNativeDialog()

    # registration.validatePlaywrightGetDocs()


def test_iframe(page: Page):

    registration = RegistrationPage(page)

    registration.testIFrame()


def takeScreenshot(page, request):

    screenshotsDir = Path(__file__).parent.parent / "Screenshots"
    screenshotsDir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fileName = f"{request.node.name}_{timestamp}.png"

    screenshotPath = screenshotsDir / fileName
    page.screenshot(path=str(screenshotPath), full_page=True)
