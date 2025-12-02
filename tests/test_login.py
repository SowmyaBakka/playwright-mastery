import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from playwright.sync_api import Page



def test_successful_login(page,login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "secure" in login_page.page.url

#
# def test_wrong_password(login_page):
#     login_page.login("tomsmith", "wrong")
#     login_page.should_have_error("Your password is invalid!")   # ← fixed text
#
# def test_wrong_username(login_page):
#     login_page.login("", "anything")
#     login_page.should_have_error("Your username is invalid!")   # ← correct text
# def test_page_has_correct_title(login_page):
#     login_page.open()
#     assert login_page.get_page_title()=="The Internet"
def test_successful_login_and_dashboard(page,login_page,secure_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "secure" in login_page.page.url
    secure_page.should_see_success_message()
    secure_page.should_see_secure_heading()

