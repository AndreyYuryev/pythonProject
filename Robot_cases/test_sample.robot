*** Settings ***
Documentation    Suite description
Library    SapGuiLibrary
Library    Process
Library    UserLib.py

*** Variables ***


*** Test Cases ***
Open SAPlogon
    ${saplogon}=    Start Process  C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplgpad.exe  alias=process1
    Sleep  5
    Connect To Session
    Open Connection    XPL System (Development)
    Maximize Window
    Take Screenshot
    Input Text  wnd[0]/usr/txtRSYST-BNAME  44544331
    Input Password  wnd[0]/usr/pwdRSYST-BCODE  UnVkXHbQF3m3!
    Send Vkey  0
    ${title}=  Get Window Title  wnd[0]
    Is first  ${title}

*** Keywords ***
Provided precondition
    Setup system under test