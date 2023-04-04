Feature: Home page

  Background:
    Given I access the home page


  Scenario: Redirect to Add/Remove Elements
    When I click the link for Add/Remove Elements
    Then I am redirected to the 'add_remove_elements' page

  Scenario: Redirect to Checkboxes link
    When I click the link for checkbox 2
    Then I am redirected to the 'checkbox' page

  @scroll_page
  Scenario: Check Endless Scrolling page
    When I click Endless Scrolling
    Then I am on Endless Scrolling page

  Scenario: Redirect to Form authentication link
    When I click the link for Form authentication
    Then I am redirected to the 'Form authentication' page


  @smoke
  Scenario Outline: Home page links works correctly
    When I press <name_link> link
    Then I am redirected to <name_page> page
    And The title text is <page_title>

    Examples:
    |name_link           |name_page      |page_title     |
    |Form Authentication |login          |Login Page     |
    |Forgot Password     |forgot_password|Forgot Password|
    |Dropdown            |dropdown       |Dropdown List  |
