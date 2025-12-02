# 2. Update your conftest.py — add this at the very top (above everything)
import pytest
from pytest_playwright.pytest_playwright import playwright, context, page, browser
from pathlib import Path
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from playwright.sync_api import Page

# Create folders once
Path("screenshots").mkdir(exist_ok=True)
Path("videos").mkdir(exist_ok=True)
Path("traces").mkdir(exist_ok=True)

# ONLY run tracing when we say --tracing=on in command line
@pytest.fixture(autouse=True)
def auto_setup(page):
    page.set_viewport_size({"width": 1600, "height": 900})
    yield
    # Nothing here — we control tracing from command line only
@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.navigate("https://the-internet.herokuapp.com/login")
    return lp
@pytest.fixture
def secure_page(page: Page):
    return SecurePage(page)