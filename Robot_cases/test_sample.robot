*** Settings ***
Documentation    Suite description
Library    SapGuiLibrary

*** Variables ***
${saplogonscreen}    /app/con[0]/ses[0]/wnd[0]

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Connect To Session
    Open Connection    <connection_name>
    Provided precondition
    When action
    Then check expectations

*** Keywords ***
Provided precondition
    Setup system under test