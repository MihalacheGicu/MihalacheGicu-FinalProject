from behave import *
import time


@given("I access the home page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)


@when("I click the link for Add/Remove Elements")
def step_impl(context):
    add_remove_elements = context.browser.get_add_remove_link()
    add_remove_elements.click()
    time.sleep(2)


@then("I am redirected to the 'add_remove_elements' page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/add_remove_elements/"
    assert redirect_link == expected_url
    time.sleep(2)


@when("I click the link for checkbox 2")
def step_impl(context):
    checkbox_link = context.browser.get_checkboxes_link()
    checkbox_link.click()
    time.sleep(2)


@then("I am redirected to the 'checkbox' page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/checkboxes"
    assert redirect_link == expected_url
    time.sleep(2)


@when("I click Endless Scrolling")
def step_impl(context):
    infinite_scroll = context.browser.get_infinite_scroll()
    infinite_scroll.click()
    time.sleep(2)


@then("I am on Endless Scrolling page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/infinite_scroll"
    assert redirect_link == expected_url
    time.sleep(2)


@when("I click the link for Form authentication")
def step_impl(context):
    form_link = context.browser.get_form_authentication_link()
    form_link.click()
    time.sleep(2)


@then("I am redirected to the 'Form authentication' page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/login"
    assert redirect_link == expected_url
    time.sleep(2)


@given(u'I am on home page')
def step_impl(context):
    context.home_page.go_page_home()


@when(u'I press {name} link')
def step_impl(context, name):
    context.home_page.go_to(name)


@then(u'I am redirected to {name_of} page')
def step_impl(context, name_of):
    assert context.browser.get_current_url() == f"https://the-internet.herokuapp.com/{name_of}"


@then(u'The title text is {page_title}')
def step_impl(context, page_title):
    if page_title == "Login Page":
        assert context.login_page.get_page_header_text() == page_title
    elif page_title == "Forgot Password":
        assert context.forgot_pwd_page.get_page_header_text() == page_title
    elif page_title == "Dropdown List":
        assert context.drop_down_page.get_page_header_text() == page_title
    elif page_title == " Secure Area":
        assert context.secure_page.get_page_header_text == page_title
