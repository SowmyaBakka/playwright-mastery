import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from playwright.sync_api import Page, expect


def test_login_with_mocked_api(page,login_page,secure_page):
    page.route("**/secure",lambda route: route.fulfill(status=200,body="<h2>Secure Area</h2><div class='flash success'>You logged into a secure area!</div><a href='/logout'>Logout</a>"))
    page.route("**/logout",lambda route:route.fulfill(status=200,body="<h2>Login Page</h2><div class='flash success'>You logged out!</div>"))
    page.route("**/*.{png,jpg,jpeg,css,js}", lambda route: route.abort())
    login_page.open()
    login_page.login("tomsmith","SuperSecretPassword!")
    secure_page.should_see_secure_heading()
    secure_page.should_see_success_message()
    secure_page.click_logout()
    #expect(page.locator(".flash.success")).to_contain_text("You logged out")
