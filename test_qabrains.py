from playwright.sync_api import Page, expect
import pytest
import re


def test_has_heading(page: Page):
    page.goto("https://practice.qabrains.com/")
    expect(
        page.get_by_role("heading", name="QA Practice Site")
    ).to_be_visible()

def test_has_caption(page: Page):
    page.goto("https://practice.qabrains.com/")
    expect(
        page.get_by_text("User Authentication")
        ).to_be_visible()


def test_button_submit(page: Page):
    page.goto("https://practice.qabrains.com/")
    submit_button = page.get_by_role("button", name="Submit")
    cancel_button = page.get_by_role("button", name="Cancel")
    
    # submit disablet when page is loaded
    expect(submit_button).to_be_disabled()
    expect(cancel_button).not_to_be_attached()

    # provide some test in textarea
    textarea = page.get_by_placeholder("Write Comment...")
    textarea.fill("This is a test")

    # submit button should be enabled
    expect(submit_button).to_be_enabled()

    expect(cancel_button).to_be_attached()
    expect(cancel_button).to_be_visible()
    expect(cancel_button).to_be_enabled()


@pytest.mark.login
def test_login_button(page: Page):
    page.goto("https://practice.qabrains.com/")
    success_message = page.get_by_role("heading", name="Login Successful")
    
    # before login - no 'Login Successful' message
    expect(success_message).not_to_be_attached()
    
    page.get_by_label("Email").fill("qa_testers@qabrains.com")
    page.get_by_label("Password").fill("Password123")
    # page.locator("#password").fill("Password123") # NOTE: also correct

    login_button = page.get_by_role("button", name="Login")
    with page.expect_navigation():
        login_button.click()

    expect(success_message).to_be_attached()
    expect(success_message).to_be_visible()

    expect(page).to_have_url(re.compile(".*logged=true"))


@pytest.mark.login
def test_login_enter(page: Page):
    page.goto("https://practice.qabrains.com/")
    success_message = page.get_by_role("heading", name="Login Successful")
    
    # before login - no 'Login Successful' message
    expect(success_message).not_to_be_attached()
    
    email = page.get_by_label("Email")
    password = page.get_by_label("Password")

    email.fill("qa_testers@qabrains.com")
    password.fill("Password123")
    password.press("Enter")

    expect(page).to_have_url(re.compile(".*logged=true"), timeout=5000)
    
    expect(success_message).to_be_attached()
    expect(success_message).to_be_visible()