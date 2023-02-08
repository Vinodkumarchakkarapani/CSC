*** Settings ***
#Documentation
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     properties
#Library     Lib
Library     Collections

Library     ../Py/properties.py
Library    ../Py/library.py
#Library     ../Pageclass/Appium.robot
#Library     ../Py/Capabilities.py
Resource    ../Pageclass/Appium.robot
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
#    library.Pop Up Button
    sleep  15
#   library.Text Me Button  otp
 Enter OTP value in Textbox
#    [Arguments]     ${var1}
    library.Text Me Button  ${var1}
#    library.Text Me Button

#    Input Text    xpath: //*[@id='auth_methods']/fieldset/div/div/input    ${number_only}
#    library.Text Me Button    text

    library.Sign In Button

#    library.Pop Up Button
