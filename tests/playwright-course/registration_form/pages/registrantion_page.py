
"""
Hodaya Shirazie
21390778-5
"""

from playwright.sync_api import Page, expect
from utilities.consts import PLAYWRIGHT_DOCS_URL, REGISTRATION_FORM
import re


GITHUB_FORM_URL = "https://github.com/yashago/hadasim-qa-pytest/blob/main/tests/playwright/src/playwright_registration_form.html"
FILE_PATH = f"https://htmlpreview.github.io/?{GITHUB_FORM_URL}"


class RegistrationPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(FILE_PATH)

    def fillInFullForm(self):

        self.fillInFirstName("John")
        self.fillInLastName("Doe")
        self.fillInEmail("Hodaya.Shirazie@gmail.com", "alex@example.com")
        self.fillInEmailConfirmation("Hodaya.Shirazie@gmail.com")
        self.fillInPassword("HodayaShirazie12345")
        self.fillInPhoneNumber("+972-54-4746095")
        self.fillInDateOfBirth("2003-09-16")
        self.selectCountry("United States")
        self.fillInCity("Beer-Sheva")
        self.fillInPersonalWebsite("https://www.hodayaShirazie.com")
        self.selectGender("Female")
        self.selectOccupation("Software Developer")
        self.fillInShortIntroduction("this is me telling you about myself.")
        self.selectYearsOfExperience("6+ years")
        self.selectFavoriteBrowser("Chromium")
        self.checkWhichTopicIntrestsYou(("Test automation", "API testing"))
        self.selectPreferredContactMethod("Email")
        self.checkMonthlyNewsletter(True)
        self.checkTermsAndConditions(True)

    def printAccessibilityTree(self):
        pageAccesibility = self.page.locator("body").aria_snapshot()
        print(f"pageAccesibility: {pageAccesibility}")

    def fillInFirstName(self, firstName):
        # By role, preferred method
        firstNameField = self.page.get_by_role("textbox", name="First name")
        firstNameField.fill(firstName)

        # screenshotsDir = Path(__file__).parent.parent / "Screenshots"
        # firstNameField.screenshot(path=str(screenshotsDir / "firstNameField.png"))
        # page.screenshot(path=str(screenshotsDir / "firstNameFieldFULL.png"),full_page=True)

    def fillInLastName(self, lastName):
        self.page.get_by_role("textbox", name="Last name").fill(lastName)

    def fillInEmail(self, email, placeholder):
        emailField = self.page.get_by_role(
            "textbox",
            name="Email address *",
            exact=True
        )

        expect(emailField).to_have_attribute("placeholder", placeholder)
        emailField.fill(email)

    def fillInEmailConfirmation(self, emailConfirmation):
        self.page.get_by_role(
            "textbox",
            name="Confirm email address"
        ).fill(emailConfirmation)

    def fillInPassword(self, password):
        self.page.get_by_role("textbox", name="Password").fill(password)

    def fillInPhoneNumber(self, phoneNumber):
        self.page.get_by_role("textbox", name="Phone number").fill(phoneNumber)

    def fillInDateOfBirth(self, dateOfBirth):
        # By label, preferred method
        datePicker = self.page.get_by_label("Date of birth")
        datePicker.fill(dateOfBirth)
        datePicker.scroll_into_view_if_needed()
        datePicker.highlight()

    def selectCountry(self, country):
        countrySelect = self.page.get_by_role("combobox", name="Country")
        countrySelect.select_option(country)
        countrySelect.scroll_into_view_if_needed()
        countrySelect.highlight()

    def fillInCity(self, city):
        self.page.get_by_role("textbox", name="City").fill(city)

    def fillInPersonalWebsite(self, personalWebsite):
        self.page.get_by_role(
            "textbox",
            name="Personal website"
        ).fill(personalWebsite)

    def selectGender(self, gender):
        self.page.get_by_role("radio", name=gender).check()

    def selectOccupation(self, occupation):
        occupationSelect = self.page.get_by_role(
            "combobox",
            name="Occupation"
        )
        occupationSelect.select_option(occupation)
        occupationSelect.scroll_into_view_if_needed()
        occupationSelect.highlight()

    def fillInShortIntroduction(self, shortIntroduction):
        self.page.get_by_role(
            "textbox",
            name="Short introduction"
        ).fill(shortIntroduction)

    def selectYearsOfExperience(self, yearsOfExperience):
        yearsOfExperienceSelect = self.page.get_by_role(
            "combobox",
            name="Years of experience"
        )
        yearsOfExperienceSelect.select_option(yearsOfExperience)
        yearsOfExperienceSelect.scroll_into_view_if_needed()
        yearsOfExperienceSelect.highlight()

    def selectFavoriteBrowser(self, favoriteBrowser):
        favoriteBrowserSelect = self.page.get_by_role(
            "combobox",
            name="Favorite browser"
        )
        favoriteBrowserSelect.select_option(favoriteBrowser)
        favoriteBrowserSelect.scroll_into_view_if_needed()
        favoriteBrowserSelect.highlight()

    def checkWhichTopicIntrestsYou(self, topic):
        for topicName in topic:
            self.page.get_by_role("checkbox", name=topicName).check()

    def selectPreferredContactMethod(self, contactMethod):
        self.page.get_by_role("radio", name=contactMethod).check()

    def checkMonthlyNewsletter(self, isChecked):
        monthlyNewsletterCheckbox = self.page.get_by_role(
            "checkbox",
            name="Subscribe to the monthly QA newsletter"
        )

        if isChecked:
            monthlyNewsletterCheckbox.check()
        else:
            monthlyNewsletterCheckbox.uncheck()

    def checkTermsAndConditions(self, isChecked):
        termsAndConditionsCheckbox = self.page.get_by_role(
            "checkbox",
            name="I agree to the terms and conditions"
        )

        if isChecked:
            termsAndConditionsCheckbox.check()
        else:
            termsAndConditionsCheckbox.uncheck()

    def validateSubmitForm(self):
        submitButton = self.page.get_by_role(
            "button",
            name="Submit registration"
        )

        expect(submitButton).to_be_visible()
        expect(submitButton).to_be_enabled()

        submitButton.click()

        successMessage = self.page.get_by_text(
            "Registration submitted!",
            exact=True
        )
        expect(successMessage).to_be_visible()

        closeButton = self.page.get_by_role("button", name="Close")
        expect(closeButton).to_be_visible()
        expect(closeButton).to_be_enabled()

    def validateResetForm(self):
        self.fillInFirstName("Hodaya")

        firstNameField = self.page.get_by_role(
            "textbox",
            name="First name"
        )
        expect(firstNameField).to_have_value("Hodaya")

        resetButton = self.page.get_by_role("button", name="Reset form")
        expect(resetButton).to_be_visible()
        expect(resetButton).to_be_enabled()
        resetButton.click()

        resetMessage = self.page.get_by_text(
            "The form has been reset. All fields are cleared.",
            exact=True
        )
        expect(resetMessage).to_be_visible()

        expect(firstNameField).to_have_value("")

    def validateNavigationLink(self, linkName, sectionRole, sectionName):
        navigationLink = self.page.get_by_role("link", name=linkName)
        expect(navigationLink).to_be_visible()
        expect(navigationLink).to_be_enabled()

        navigationLink.click()

        expect(self.page).to_have_url(re.compile(f"#{linkName.lower()}$"))

        section = self.page.get_by_role(sectionRole, name=sectionName)
        expect(section).to_be_visible()

    def validateHelpLink(self):
        helpLink = self.page.get_by_role("link", name="Help")
        helpLink.scroll_into_view_if_needed()
        helpLink.highlight()
        helpLink.click()

        # printAccessibilityTree(self.page)
        dialog = self.page.get_by_role(
            "dialog",
            name=REGISTRATION_FORM["modalHeaderText"]
        )
        expect(dialog).to_be_visible()

        expect(
            dialog.get_by_role(
                "heading",
                level=2,
                name=REGISTRATION_FORM.get("modalHeaderText")
            )
        ).to_be_visible()

        dialogOkButton = dialog.get_by_role(
            "button",
            name=REGISTRATION_FORM.get("modalButtonText")
        )
        expect(dialogOkButton).to_be_visible()
        expect(dialogOkButton).to_be_enabled()
        dialogOkButton.click()

    def validatePlaywrightDocsLink(self):
        docsLink = self.page.get_by_role(
            "link",
            name="Playwright documentation"
        )

        expect(docsLink).to_be_visible()
        expect(docsLink).to_be_enabled()

        with self.page.expect_popup() as newPage:
            docsLink.click()

        newTab = newPage.value

        expect(newTab).to_have_url(PLAYWRIGHT_DOCS_URL)

    def validateNativeDialog(self):
        def handle_dialog(dialog):
            print("Dialog message:", dialog.message)

            self.page.pause()

            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.page.get_by_role(
            "link",
            name="Native confirm dialog"
        ).click()

        # self.page.once("dialog", lambda dialog: dialog.dismiss())
        # self.page.get_by_role("link", name="Native confirm dialog").click()

    def validatePlaywrightGetDocs(self):
        # self.page.pause()
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role(
                "link",
                name="Playwright documentation"
            ).click()

            popup = popup_info.value

        expect(popup).to_have_url("https://playwright.dev/")
        expect(
            popup.get_by_role("heading", name="Playwright CLI")
        ).to_be_visible()

    def testIFrame(self):
        self.open()

        googleMapsLink = self.page.get_by_role("link", name="Google Map")
        expect(googleMapsLink).to_be_visible()
        googleMapsLink.click()

        googleMapsFrame = self.page.frame_locator(
            'iframe[title="Google Map showing Tel Aviv, Israel"]'
        )

        expect(googleMapsFrame.locator("body")).to_be_visible()

        with self.page.expect_popup() as popup_info:
            self.page.evaluate("""
                window.open(
                    'https://www.google.com/maps?q=Tel+Aviv,+Israel',
                    '_blank'
                )
            """)

        popup = popup_info.value
        expect(popup).to_have_url(
            re.compile(r"https://www.google.com/maps")
        )
