from behave import *
import time


@given("I am on the login page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)


@when("I enter a correct username")
def step_impl(context):
    user_name = context.browser.get_username_element()
    user_name.send_keys("tomsmith")
    time.sleep(1)


@when("I enter a correct password")
def step_impl(context):
    password = context.browser.get_password_element()
    password.send_keys("SuperSecretPassword!")
    time.sleep(1)


@then("I click on the login button")
def step_impl(context):
    login_button = context.browser.get_login_button()
    login_button.click()
    time.sleep(1)


@given('I am on login page')
def step_impl(context):
    context.login_page.go_page_home()


@when('I enter {input_field} {value}')
def step_impl(context, input_field, value):
    if value != "None":
        context.login_page.send_value_to_input_fields(input_field, value)


@when('I press login button')
def step_impl(context):
    context.login_page.press_login_button()


@then('I will be redirected to the secure page')
def step_impl(context):
    assert context.browser.get_current_url() == context.secure_page.URL


@then('A message containing the text "{text_message}" appears')
def step_impl(context, text_message):
    assert text_message in context.login_page.get_flash_message_text()


@then('I will remain on the login page')
def step_impl(context):
    assert context.browser.get_current_url() == context.login_page.URL


@given('All steps in scenario "Login with valid/invalid credentials" are done')
def step_impl(context):
    context.execute_steps(u'''
      Given I am on login page
      When I enter "username" tomsmith
      And I enter "password" something!342
      And I press login button
      Then I will remain on the login page
      And A message containing the text "Your password is invalid!" appears
    ''')
