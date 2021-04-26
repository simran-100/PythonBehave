Feature: Duplicate

    Background:
        Given I set base REST API url and headers correctly

    Scenario Outline: API E2E Example which should fail
        Given I Set posts api endpoint to tatics endpoint
        When set the body of request to contents of the <File name>
        And perfrom post
        Then I receive valid HTTP response code as <Code>
        And validate error is <ErrorCode>
        Then Extract Message

    Examples: Corrects
        | File name  | Code | ErrorCode |
        | ETOE1.json | 200  | True      |
        | ETOE2.json | 200  | True      |   

