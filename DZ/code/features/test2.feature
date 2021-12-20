Feature: Test summary
    Scenario: test summary for making check with 1 2 3
        Given ordering food with answers in bot milk product - 1 meat and fish - 2 bakery product - 3
        When we form summary of check
        Then check should be with correct price 670
    Scenario: test summary for making check with 2 1 3
        Given ordering food with answers in bot milk product - 2 meat and fish - 1 bakery product - 3
        When we form summary of check
        Then check should be with correct price 310


