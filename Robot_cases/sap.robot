*** Settings ***
Documentation    Suite description
Library  SapGuiLibrary
Library  SikuliLibrary
Library  OperatingSystem
Library  Process

*** Variables ***
${SAPSessionID} 200
${SAPSessionUser} 44544331
${SAPSessionPWD} 1234

*** Test Cases ***
Test title
    [Tags]    Open SAP
    SikuliLibrary.Open Application  C://Program Files (x86)//SAP//FrontEnd//SAPgui//saplgpad.exe
    Sleep  10

*** Keywords ***
Provided precondition
    Setup system under test