from browser import Browser
from pages.drop_down_page import DropDownPage
from pages.forgot_pwd_page import ForgotPasswordPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def before_all(context):
    print("Setting the browser for testing!!")
    context.browser = Browser()

    context.home_page = HomePage(context.browser.driver)
    context.login_page = LoginPage(context.browser.driver)
    context.forgot_pwd_page = ForgotPasswordPage(context.browser.driver)
    context.secure_page = SecurePage(context.browser.driver)
    context.drop_down_page = DropDownPage(context.browser.driver)


def after_all(context):
    context.browser.close()
