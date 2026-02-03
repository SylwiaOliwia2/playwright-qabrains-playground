from playwright.sync_api import Page, expect
from playwright.async_api import Page as AsyncPage, expect as async_expect
import pytest


def test_has_heading(page: Page):
    page.goto("https://practice.qabrains.com/")
    expect(
        page.get_by_role("heading", name="QA Practice Site")
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


def test_login(page: Page):
    page.goto("https://practice.qabrains.com/")
    success_message = page.get_by_role("heading", name="Login Successful")
    
    # before login - no 'Login Successful' message
    expect(success_message).not_to_be_attached()
    
    page.locator("#email").fill("qa_testers@qabrains.com")
    page.locator("#password").fill("Password123")

    login_button = page.get_by_role("button", name="Login")
    with page.expect_navigation():
        login_button.click()

    expect(success_message).to_be_attached()
    expect(success_message).to_be_visible()
