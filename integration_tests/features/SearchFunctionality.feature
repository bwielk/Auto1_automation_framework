# Created by bwiel at 16/03/2019
Feature: Search cars on Auto1

  Scenario: Sorting search results
    Given results are filtered by first registration year - 2015
    When the results are sorted by price in descending order
    Then the results are filtered by first registration - 2015
    And the results are sorted in descending order by price

