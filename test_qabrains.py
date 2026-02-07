from playwright.sync_api import Page, expect
import pytest
import re
import os


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


@pytest.mark.api
def test_api_call(page: Page):
    """
    Use reqres.in to test API request (learning purposes).
    """
    response = page.request.get(
        "https://reqres.in/api/users?page=2",
        headers={"x-api-key": os.getenv("X_API_KEY")}
    )
    assert response.ok
    data = response.json()
    assert len(data) > 0


# @pytest.mark.api
# def test_authenticated_api_call(page: Page):
#     """
#     Example workflow of tsting an API endpoint that requires authentication.
    
#     Pattern:
#     1. Authenticate first to get a token
#     2. Use the token in Authorization header for protected endpoints
#     3. Make authenticated API calls
#     """
#     # Step 1: Authenticate to get access token
#     # In real scenario, this would be your actual login endpoint
#     login_url = "https://api.example.com/auth/login"
#     login_credentials = {
#         "username": "test_user",
#         "password": "test_password_123"
#     }
    
#     # Authenticate and get token
#     auth_response = page.request.post(
#         login_url,
#         data=login_credentials
#     )
    
#     # Verify authentication was successful
#     assert auth_response.ok, f"Authentication failed: {auth_response.status}"
    
#     # Extract token from response
#     # Common formats: {"token": "..."}, {"access_token": "..."}, {"authToken": "..."}
#     auth_data = auth_response.json()
#     access_token = auth_data.get("token") or auth_data.get("access_token") or auth_data.get("authToken")
    
#     assert access_token is not None, "Token not found in authentication response"
    
#     # Step 2: Use the token to make authenticated API calls
#     # Common patterns:
#     # - Bearer token: Authorization: Bearer <token>
#     # - API key: X-API-Key: <token>
#     # - Custom header: X-Auth-Token: <token>
    
#     protected_endpoint = "https://api.example.com/users/profile"
    
#     authenticated_response = page.request.get(
#         protected_endpoint,
#         headers={
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json"
#         }
#     )
    
#     # Verify the authenticated request was successful
#     assert authenticated_response.ok, f"Authenticated request failed: {authenticated_response.status}"
    
#     # Verify the response contains expected data
#     user_data = authenticated_response.json()
#     assert "id" in user_data or "username" in user_data, "User data not found in response"
    
#     # Example: Test another protected endpoint
#     users_list_url = "https://api.example.com/users"
#     users_response = page.request.get(
#         users_list_url,
#         headers={"Authorization": f"Bearer {access_token}"}
#     )
    
#     assert users_response.ok
#     users_list = users_response.json()
#     assert isinstance(users_list, list), "Expected list of users"