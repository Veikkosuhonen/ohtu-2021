*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Resource  register_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register With Credentials  veikko  veikko123  veikko123
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Register With Credentials  ve  veikko123  veikko123
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Register With Credentials  veikko  v123456  v123456
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Register With Credentials  veikko  veikko123  veikko456
    Registration Should Fail With Message  Password and password confirmation do not match

Login After Succesfull Registration
    Register With Credentials  veikko  veikko123  veikko123
    Go To Login Page
    Login With Credentials  veikko  veikko123
    Login Should Succeed

Login After Failed Registration
    Register With Credentials  ve  veikko123  veikko123
    Go To Login Page
    Login With Credentials  ve  veikko123
    Login Should Fail With Message  Invalid username or password