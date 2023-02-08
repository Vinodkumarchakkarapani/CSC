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

Create an new contract

    library.Contract Button
    library.Save As Draft Button
    library.Ws Office Dropdown
    library.Client Name             ${client_name}
#    sleep   10
    library.Client Name Textbox    ${client_name}
#    library.enter
    sleep   3
    library.Select Primary Client
    library.Select Contract Term
    library.Select Contract Date
    library.Select Management Coverage    ${Management_coverage}
    library.Fees Offset Commission Textbox    ${Fees_offset_commission}
    library.Employee Benefits Coverage    ${Domestic_benefits}
    library.Fees Offset EB       ${EB_fee_offset_commission}
    sleep   5
    library.Select Employee Benefit Signer
    library.Select Commericial Signer
    library.Select Stc Radio Button
    sleep  3
    library.Scroll Down
    sleep   5
    library.Select Sow Document
    library.Submit Button
    sleep  10
#    Press Keys  "//div[@class='Select__value-container css-1hwfws3']"   DOWN



