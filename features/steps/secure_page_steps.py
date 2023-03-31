from behave import *
import time


@given("I connect with correct user and password")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)
    user_name = context.browser.get_username_element()
    user_name.send_keys("tomsmith")
    password = context.browser.get_password_element()
    password.send_keys("SuperSecretPassword!")
    login_button = context.browser.get_login_button()
    login_button.click()


@when("Check if the  message: ' You logged into a secure area!' is displayed")
def step_impl(context):
    secure_area_message = context.browser.get_alert_secure_area().text
    expected_message = "You logged into a secure area!"
    assert expected_message in secure_area_message
    time.sleep(1)


@then("I click the logout button")
def step_impl(context):
    logout_button = context.browser.get_logout_bt()
    logout_button.click()
    time.sleep(1)


@given('I am on the secure page')
def step_impl(context):
    context.secure_page.go_page_home()


@when('Page finish loading')
def step_impl(context):
    context.secure_page.go_page_home()
    time.sleep(1)


@when('I press logout button')
def step_impl(context):
    context.secure_page.press_logout_button()


@given('A message containing the text "{text_message}" appears')
def step_impl(context, text_message):
    assert text_message in context.secure_page.get_flash_message_text()


@when('I press x button on the message')
def step_impl(context):
    context.secure_page.press_x_message_button()


@then('Message will not be displayed')
def step_impl(context):
    assert context.login_page.get_flash_message_text() is False
