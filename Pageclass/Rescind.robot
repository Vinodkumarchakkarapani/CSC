*** Settings ***
Library     SeleniumLibrary
Library     Selenium2Library
#Library     properties
#Library     Lib
Library     Collections

Library     ../Py/properties.py
Library    ../Py/library.py

Resource    ../Py/library.py
Resource    ../Objects/Object.robot

*** Variables ***

*** Keywords ***
Open the browser
    [Arguments]
    library.open browser    ${url}
login Sharepoint application
    [Arguments]                   ${microsoft_username}        ${microsoft_password}

    library.pop_up_username           ${microsoft_username}
    sleep    3
    library.pop up password           ${microsoft_password}
    sleep  15
    library.Pop Up Button
Rescind flow
#    library.Ready For Docusign Link
#    library.Rescind Button
    library.Rescinded Link
    sleep   10

