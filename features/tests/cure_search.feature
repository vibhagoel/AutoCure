# Created by shekh at 4/22/2023
Feature: CureSkin Search Test
  # Enter feature description here

  Scenario: Search results UI is correct
    Given Open CureSkin Page
    And Close pop-up displayed
    When Click on CureSkin search icon
    And Enter Cure in search box
    And Click on Search For button
    Then Verify search result UI is correct


  Scenario: User delete an item from the cart
    Given Open CureSkin Page
    And Close pop-up displayed
    When Click on CureSkin search icon
    And Enter Cure in search box
    And Click on Search For button
    And Add Item to the cart
    And Click on View Cart
    Then Verify 1 Items added to the cart
    And Delete First Item from the cart
    And Verify text Your cart is currently empty is displayed on empty cart