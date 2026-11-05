import re
from playwright.sync_api import Page, expect
from pathlib import Path

"""
    A few exercises to try:
    Find the button using its role and name.
    Click it and verify the confirmation text.
    Find the email input using its placeholder.
    Fill in the password field.
    Select United Kingdom from the dropdown.
    Select Premium.
    Check the terms checkbox.
    Submit the form and verify the confirmation.
    Click the Details link and verify that a new tab opens.
    Verify the headline and paragraph on the new page.
"""




def test_get_started_navigation(page: Page):

    # page.goto("file:///C:/Users/etgar_atida/test_practice/tests/playwright-course/playwright-selectors.html")
    html_path = Path(__file__).parent / "playwright-selectors.html"
    page.goto(html_path.as_uri())

    # 1. Find the button using its role and name
    page.get_by_role("button", name="Open Details").click()

    # 2. Verify the confirmation text
    expect(
        page.get_by_text("Button clicked! This text appeared after the click.")
    ).to_be_visible()

    # 3. Find the email input using its placeholder
    page.get_by_placeholder("name@example.com").fill("test@example.com")

    # 4. Fill in the password field
    page.get_by_label("Password").fill("hodaya1234!")

    # 5. Select United Kingdom from the dropdown
    page.get_by_label("Choose a country").select_option(label="United Kingdom")

    # 6. Select Premium
    page.get_by_label("Premium").check()

    # 7. Check the terms checkbox
    page.get_by_label("I agree to the terms").check()

    # 8. Submit the form and verify the confirmation
    page.get_by_role("button", name="Submit Form").click()

    expect(page.get_by_text("Form submitted successfully!")).to_be_visible()

    # 9. Click the Details link and verify that a new tab opens
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Go to Details Page").click()

    new_page = popup_info.value

    # 10. Verify the headline and paragraph on the new page
    expect(
        new_page.get_by_role("heading", name="Welcome to the Details Page")
    ).to_be_visible()

    expect(
    new_page.get_by_text(
        re.compile(
            "This page was opened by clicking a link.",
            re.IGNORECASE
        )
    )
).to_be_visible()

    


