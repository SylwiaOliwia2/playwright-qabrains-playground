# import pytest
# from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv() 

# @pytest.fixture(scope="session")
# def browser_type_launch_args(browser_type_launch_args):
#     """Display test in prowser in slow motion for visibility."""
#     return {
#         **browser_type_launch_args,
#         "headless": False,
#         "slow_mo": 1000  # 1 second delay between actions
#     }


# @pytest.fixture(autouse=True)
# def setup_page(page: Page):
#     """Global setup: navigate to TodoMVC before each test."""
#     page.goto('https://demo.playwright.dev/todomvc')
#     yield
