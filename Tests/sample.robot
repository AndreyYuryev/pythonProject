*** Settings ***
Documentation    Suite description
...              Test documentation
Library         SapGuiLibrary
Library         Process

*** Variables ***
${path}         C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplgpad.exe
${systemname}   XPL System (Development)
${userid}       44544331
${userpswd}     UnVkXHbQF3m3!

*** Test Cases ***
Login to SAP system
    Open SAPlogon
    Login to System

*** Keywords ***
Open SAPlogon
    [Documentation]  Execute saplogon
    ${saplogon}=    Start Process  ${path}  alias=process1
    Sleep  5
    Connect To Session
    Open Connection    ${systemname}
    Maximize Window
    Take Screenshot

Login to System
    [Documentation]  Log in
    Input Text  wnd[0]/usr/txtRSYST-BNAME  ${userid}
    Input Password  wnd[0]/usr/pwdRSYST-BCODE  ${userpswd}
    Send Vkey  0
