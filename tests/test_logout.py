import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from playwright.sync_api import Page, expect


def test_successful_logout(page,login_page,secure_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "secure" in login_page.page.url
    secure_page.should_see_success_message()
    secure_page.should_see_secure_heading()
    secure_page.click_logout()
    expect(login_page.page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(login_page.page.get_by_role("heading",name="Login Page")).to_be_visible()

