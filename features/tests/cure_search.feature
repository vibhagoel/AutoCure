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