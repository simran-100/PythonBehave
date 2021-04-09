Feature: End 2 End Rest API testing POC2

    Background:
        Given I set base REST API url and headers correctly

    Scenario: API E2E Example
        Given I Set posts api endpoint to tatics endpoint
        When set the body of request to contents of the ETOE1.json
            And perfrom post
        Then I receive valid HTTP response code as 200
            And validate error is True
         Then Extract Message
