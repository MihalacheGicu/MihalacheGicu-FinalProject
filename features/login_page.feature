Feature: Login Page

   @smoke
   Scenario: Try login test
    Given I am on the login page
    When I enter a correct username
    And I enter a correct password
    Then I click on the login button

   @smoke
  Scenario: Verify logout button
    Given I am on Secure area page after a valid login
    When I click the logout button
    Then I see the logout message


    @smoke
    Scenario Outline: Login with valid/invalid credentials
      Given I am on login page
      When I enter "username" <username>
      And I enter "password" <password>
      And I press login button
      Then I will <action> the <page_name> page
      And A message containing the text "<text_message>" appears

    Examples: Login with invalid credentials

      |username|password            |text_message                  |action          |page_name|
      |tomsmith|SuperSecretPassword!|You logged into a secure area!|be redirected to|secure   |
      |tomsmith|something           |Your password is invalid!     |remain on       |login    |
      |tomsmith|423432452           |Your password is invalid!     |remain on       |login    |
      |tomsmith|something!342       |Your password is invalid!     |remain on       |login    |
      |tomsmith|None                |Your password is invalid!     |remain on       |login    |
      |None    |SuperSecretPassword!|Your username is invalid!     |remain on       |login    |
      |username|SuperSecretPassword!|Your username is invalid!     |remain on       |login    |
      |13213213|SuperSecretPassword!|Your username is invalid!     |remain on       |login    |
      |username|something           |Your username is invalid!     |remain on       |login    |


