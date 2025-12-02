from playwright.sync_api import Page, expect
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator("[name='username']")
        self.password = page.locator("[name='password']")
        #self.login_btn = page.get_by_role("button", name="WRONG LOGIN BUTTON NAME")  # ← FIXED THIS LINE
        self.login_btn = page.get_by_text("Login").nth(1)
        self.error_msg = page.locator(".flash.error")
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")
    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def should_have_error(self, text: str):
        expect(self.error_msg).to_contain_text(text)
    def get_page_title(self):
        return self.page.title()
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")