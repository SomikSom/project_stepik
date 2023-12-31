from selenium.webdriver.common.by import By

from pages.locators import MainPageLocators
from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"



def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()      # выполняем метод страницы — переходим на страницу логина


