*** Settings ***
Documentation    Suite description
Library    SapGuiLibrary
Library    Process

*** Variables ***
${saplogonscreen}    /app/con[0]/ses[0]/wnd[0]
${command}  'C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\sapshcut.exe -system=XPL -client=200 -desc=XPL System (Development) -user=44544331 -pw=UnVkXHbQF3m3!'

*** Test Cases ***
Open SAP
    ${cmd} =	Join Command Line	--option	C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\sapshcut.exe -system=XPL -client=200 -desc=XPL System (Development) -user=44544331 -pw=UnVkXHbQF3m3!
    Run Process    cmd=${cmd}
    Maximize Window


*** Keywords ***
Provided precondition
    Setup system under test