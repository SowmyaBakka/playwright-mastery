from .base_page import BasePage
from playwright.sync_api import Page, expect

class SecurePage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.success_flash = page.locator(".flash.success")
        self.secure_heading = page.locator("h2",has_text="Secure Area")
        self.logout_button = page.locator("a:has-text('Logout')")
        self.welcome_subtext = page.get_by_text("Welcome to the Secure Area")
    def should_see_success_message(self):
        expect(self.success_flash).to_be_visible()
        expect(self.success_flash).to_contain_text("You logged into a secure area")
    def should_see_secure_heading(self):
        expect(self.secure_heading).to_be_visible()
    def click_logout(self):
        self.logout_button.click()