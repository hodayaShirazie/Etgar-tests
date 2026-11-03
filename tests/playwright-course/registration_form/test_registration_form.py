"""
Hodaya Shirazie
21390778-5
"""

from playwright.sync_api import Page, expect
from consts import PLAYWRIGHT_DOCS_URL, REGISTRATION_FORM
import re

GITHUB_FORM_URL = "https://github.com/yashago/hadasim-qa-pytest/blob/9bcef875b222092b4f32c3599b7773e5d1aca48b/tests/playwright/src/playwright_registration_form.html"
FILE_PATH = f"https://htmlpreview.github.io/?{GITHUB_FORM_URL}"

def test_registration_form(page: Page):

    page.goto(FILE_PATH)
    # printAccessibilityTree(page)
    # page.pause()

    fillInFullForm(page)
    validateResetForm(page)
    fillInFullForm(page)
    validateSubmitForm(page)

def test_header(page: Page):
    page.goto(FILE_PATH)

    # validateRegistrationLink(page)
    validateNavigationLink(page, "Registration", "region", "Registration details")

    # validatePreferencesLink(page)
    validateNavigationLink(page, "Preferences", "heading", "Preferences")

    validateHelpLink(page)

    validatePlaywrightDocsLink(page)

def fillInFullForm(page):

    fillInFirstName(page, "John")

    fillInLastName(page, "Doe")

    fillInEmail(page, "Hodaya.Shirazie@gmail.com", "alex@example.com")

    fillInEmailConfirmation(page, "Hodaya.Shirazie@gmail.com")

    fillInPassword(page, "HodayaShirazie12345")

    fillInPhoneNumber(page, "+972-54-4746095")

    fillInDateOfBirth(page, "2003-09-16")

    selectCountry(page, "United States")

    fillInCity(page, "Beer-Sheva")

    fillInPersonalWebsite(page, "https://www.hodayaShirazie.com")

    selectGender(page, "Female")

    selectOccupation(page, "Software Developer")

    fillInShortIntroduction(page, "this is me telling you about myself.")

    selectYearsOfExperience(page, "6+ years")

    selectFavoriteBrowser(page, "Chromium")

    checkWhichTopicIntrestsYou(page, ("Test automation", "API testing"))

    selectPreferredContactMethod(page, "Email")

    checkMonthlyNewsletter(page, True)

    checkTermsAndConditions(page, True)

def printAccessibilityTree(page):
    pageAccesibility = page.locator("body").aria_snapshot()
    print(f"pageAccesibility: {pageAccesibility}")

def fillInFirstName(page, firstName):
    #By role, preferred method
    page.get_by_role("textbox", name="First name").fill(firstName)
    
    # #By label, preferred method
    # page.get_by_label("First name").fill("Doe")

    # #By placeholder, good option if the placeholder is unique and descriptive
    # page.get_by_placeholder("e.g. Alex").fill("John")

    # #By locator, good option if the locator is unique and descriptive
    # page.locator("#firstName").fill("Doe")

    # #By locator, Usually unnecessary
    # page.locator('input[id="firstName"]').fill("John")
    # page.fill('input[name="firstName"]', "Doe")

def fillInLastName(page, lastName):
    page.get_by_role("textbox", name="Last name").fill(lastName)

def fillInEmail(page, email, placeholder):
    emailField = page.get_by_role("textbox", name="Email address *", exact=True)

    expect(emailField).to_have_attribute("placeholder", placeholder)

    emailField.fill(email)

def fillInEmailConfirmation(page, emailConfirmation):
    page.get_by_role("textbox", name="Confirm email address").fill(emailConfirmation)

def fillInPassword(page, password):
    page.get_by_role("textbox", name="Password").fill(password)

def fillInPhoneNumber(page, phoneNumber):
    page.get_by_role("textbox", name="Phone number").fill(phoneNumber)

def fillInDateOfBirth(page, dateOfBirth):
    #By label, preferred method
    datePicker = page.get_by_label("Date of birth")
    datePicker.fill(dateOfBirth)
    datePicker.scroll_into_view_if_needed()
    datePicker.highlight()  

def selectCountry(page, country):
    countrySelect = page.get_by_role("combobox", name="Country")
    countrySelect.select_option(country)
    countrySelect.scroll_into_view_if_needed()
    countrySelect.highlight()

def fillInCity(page, city):
    page.get_by_role("textbox", name="City").fill(city)

def fillInPersonalWebsite(page, personalWebsite):
    page.get_by_role("textbox", name="Personal website").fill(personalWebsite)

def selectGender(page, gender):
    page.get_by_role("radio", name=gender).check()

def selectOccupation(page, occupation):
    occupationSelect = page.get_by_role("combobox", name="Occupation")
    occupationSelect.select_option(occupation)
    occupationSelect.scroll_into_view_if_needed()
    occupationSelect.highlight()

def fillInShortIntroduction(page, shortIntroduction):
    page.get_by_role("textbox", name="Short introduction").fill(shortIntroduction)

def selectYearsOfExperience(page, yearsOfExperience):
    yearsOfExperienceSelect = page.get_by_role("combobox", name="Years of experience")
    yearsOfExperienceSelect.select_option(yearsOfExperience)
    yearsOfExperienceSelect.scroll_into_view_if_needed()
    yearsOfExperienceSelect.highlight()

def selectFavoriteBrowser(page, favoriteBrowser):
    favoriteBrowserSelect = page.get_by_role("combobox", name="Favorite browser")
    favoriteBrowserSelect.select_option(favoriteBrowser)
    favoriteBrowserSelect.scroll_into_view_if_needed()
    favoriteBrowserSelect.highlight()

def checkWhichTopicIntrestsYou(page, topic):
    for topicName in topic:
        page.get_by_role("checkbox", name=topicName).check()

def selectPreferredContactMethod(page, contactMethod):
    page.get_by_role("radio", name=contactMethod).check()

def checkMonthlyNewsletter(page, isChecked):
    monthlyNewsletterCheckbox = page.get_by_role("checkbox", name="Subscribe to the monthly QA newsletter")
    if isChecked:
        monthlyNewsletterCheckbox.check()
    else:
        monthlyNewsletterCheckbox.uncheck()

def checkTermsAndConditions(page, isChecked):
    termsAndConditionsCheckbox = page.get_by_role("checkbox", name="I agree to the terms and conditions")
    if isChecked:
        termsAndConditionsCheckbox.check()
    else:
        termsAndConditionsCheckbox.uncheck()


def validateSubmitForm(page):
    submitButton = page.get_by_role("button", name="Submit registration")

    expect(submitButton).to_be_visible()
    expect(submitButton).to_be_enabled()

    submitButton.click()

    successMessage = page.get_by_text(
        "Registration submitted!",
        exact=True
    )
    expect(successMessage).to_be_visible()

    closeButton = page.get_by_role("button", name="Close")
    expect(closeButton).to_be_visible()
    expect(closeButton).to_be_enabled()

# This function replaces the "validatePreferencesLink" and "validateRegistrationLink" functions
# since they share the same logic and can be generalized to work for any navigation link and section.
def validateResetForm(page):
    fillInFirstName(page, "Hodaya")

    firstNameField = page.get_by_role("textbox", name="First name")
    expect(firstNameField).to_have_value("Hodaya")

    resetButton = page.get_by_role("button", name="Reset form")
    expect(resetButton).to_be_visible()
    expect(resetButton).to_be_enabled()
    resetButton.click()

    resetMessage = page.get_by_text(
        "The form has been reset. All fields are cleared.",
        exact=True
    )
    expect(resetMessage).to_be_visible()

    expect(firstNameField).to_have_value("")

# def validateRegistrationLink(page):
#     registrationLink = page.get_by_role("link", name="Registration")
#     expect(registrationLink).to_be_visible()
#     expect(registrationLink).to_be_enabled()

#     registrationLink.click()

#     expect(page).to_have_url(re.compile(r"#registration$"))

#     registrationSection = page.get_by_role("region", name="Registration details")
#     expect(registrationSection).to_be_visible()

# def validatePreferencesLink(page):
    # preferencesLink = page.get_by_role("link", name="Preferences")
    # expect(preferencesLink).to_be_visible()
    # expect(preferencesLink).to_be_enabled()

    # preferencesLink.click()

    # expect(page).to_have_url(re.compile(r"#preferences$"))

    # preferencesSection = page.get_by_role("region", name="Preferences")
    # expect(preferencesSection).to_be_visible()

def validateNavigationLink(page, linkName, sectionRole, sectionName):
    navigationLink = page.get_by_role("link", name=linkName)
    expect(navigationLink).to_be_visible()
    expect(navigationLink).to_be_enabled()

    navigationLink.click()

    expect(page).to_have_url(re.compile(f"#{linkName.lower()}$"))

    section = page.get_by_role(sectionRole, name=sectionName)
    expect(section).to_be_visible()

def validateHelpLink(page):
    helpLink = page.get_by_role("link", name="Help")
    helpLink.scroll_into_view_if_needed()
    helpLink.highlight()
    helpLink.click()

    # printAccessibilityTree(page)
    dialog = page.get_by_role("dialog", name=REGISTRATION_FORM["modalHeaderText"])
    expect(dialog).to_be_visible()
    expect(dialog.get_by_role("heading", level=2, name=REGISTRATION_FORM.get("modalHeaderText"))).to_be_visible()

    dialogOkButton = dialog.get_by_role("button", name=REGISTRATION_FORM.get("modalButtonText"))
    expect(dialogOkButton).to_be_visible()
    expect(dialogOkButton).to_be_enabled()
    dialogOkButton.click()

def validatePlaywrightDocsLink(page):
    docsLink = page.get_by_role("link", name="Playwright documentation")

    expect(docsLink).to_be_visible()
    expect(docsLink).to_be_enabled()

    with page.expect_popup() as newPage:
        docsLink.click()

    newTab = newPage.value

    expect(newTab).to_have_url(PLAYWRIGHT_DOCS_URL)