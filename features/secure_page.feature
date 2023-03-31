Feature: Secure Page

  Scenario: Verify correct login and logout
    Given I connect with correct user and password
    When Check if the  message: ' You logged into a secure area!' is displayed
    Then I click the logout button


  Scenario: Secure page right redirect
    Given I am on the secure page
    When Page finish loading
    Then A message containing the text "You logged into a secure area!" appears
    And The title text is Secure Area


  Scenario: Secure page logout successfully
    Given I am on the secure page
    When I press logout button
    Then I am redirected to login page
    And A message containing the text "You logged out of the secure area!" appears
    And The title text is "Login Page"




