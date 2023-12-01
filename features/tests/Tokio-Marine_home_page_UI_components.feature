# Created by Ricky Mekonen at 11/29/2023
Feature: # Tokio Marine home page UI components
  # User can open the home page  https://www.tmhcc.com/en-us and see UI components and can interact with them

  Scenario: User can open https://www.tmhcc.com/en-us and see header-one menu and can interact with them
    Given Open https://www.tmhcc.com/en-us home page
    Then Verify user can see the 10 header menu
    And Verify user can click on all 10 header menu and a correct page is display
#
  Scenario: User can open https://www.tmhcc.com/en-us and see header-two elements and can interact with them
    Given Open https://www.tmhcc.com/en-us home page
    When Click on the search icon to navigate away from the home page
    Then Verify clicking on the logo takes user to the home page
    When Click on the search icon
    And Populate the search field with test
    And Click on the search submit icon
    Then Verify search results are displayed
    When Click on the language button
    Then Verify user can change language
