*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  veikko  a2345678
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  veikko  a2345678
    Input Credentials  veikko  12345678
    Output Should Contain  User with username veikko already exists

Register With Too Short Username And Valid Password
    Input Credentials  v  a2345678
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  veikko  a234567
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  veikko  yykaakooneevii
    Output Should Contain  Password must contain at least one character other than a-z