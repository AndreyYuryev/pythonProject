*** Settings ***
Documentation    Suite description
Library    SapGuiLibrary
Library    Process

*** Variables ***
${saplogonscreen}    /app/con[0]/ses[0]/wnd[0]

*** Test Cases ***
Test title
    [Tags]    DEBUG
    ${saplogon}=    Start Process  C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplgpad.exe  output_encoding=SYSTEM
    Wait for process    ${saplogon}
    Connect To Session
    Open Connection    XPL System (Development)
    Maximize Window

*** Keywords ***
Provided precondition
    Setup system under test