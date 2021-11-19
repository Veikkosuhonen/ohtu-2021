*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Keywords ***
Register With Credentials
    [Arguments]  ${username}  ${pwd}  ${pwd_confirm}
    Set Username  ${username}
    Set Password  ${pwd}
    Set Password Confirmation  ${pwd_confirm}
    Click Button  Register

Login With Credentials
    [Arguments]  ${username}  ${pwd}
    Set Username  ${username}
    Set Password  ${pwd}
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Login Should Succeed
    Main Page Should Be Open

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}