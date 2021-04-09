Feature: Duplicate

    Background:
        Given I set base REST API url and headers correctly

    Scenario: API E2E Example which should fail
        Given I Set posts api endpoint to tatics endpoint
        When set the body of request to contents of the ETOE1.json
            And perfrom post
        Then I receive valid HTTP response code as 201
            And validate error is True
         Then Extract Message
