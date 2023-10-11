*** Settings ***
Documentation    API Tests
Library    RequestsLibrary

*** Test Cases ***
true_when_x_is_17
    Create Session    session    http://127.0.0.1:5000/
    Check Is Prime    17    True
    
false_when_x_is_36
    Check Is Prime    36    False

true_when_x_is_13219
    Check Is Prime    13219    True


*** Keywords ***
Check Is Prime
    [Arguments]    ${x}    ${expected_result}
    ${resp}    GET On Session    session    /is_prime/${x}
    Should Be Equal As Strings    ${resp.text}     ${expected_result}

    