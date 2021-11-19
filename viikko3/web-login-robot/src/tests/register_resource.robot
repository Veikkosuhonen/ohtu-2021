*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Keywords ***
Register With Credentials
    [Arguments]  ${username}  ${pwd}  ${pwd_confirm}
    Set New Username  ${username}
    Set New Password  ${pwd}
    Set New Password Confirmation  ${pwd_confirm}
    Click Button  Register

Set New Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set New Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set New Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}