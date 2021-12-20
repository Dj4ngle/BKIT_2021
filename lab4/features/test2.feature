
Feature: Test
 
    Scenario:Test1
    Given Calculator app is run
    When I input "1", "0" and "0" to calculator
    Then I get result "[0.0]"

    Scenario:Test2
    Given Calculator app is run
    When I input "1", "0" and "-4" to calculator
    Then I get result "[-1.41, 1.41]"

    Scenario:Test3
    Given Calculator app is run
    When I input "1", "-4" and "0" to calculator
    Then I get result "[-2.0, 2.0, 0.0]"