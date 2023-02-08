*** Settings ***
#Library     AppiumLibrary
Library     SeleniumLibrary
Library     Selenium2Library
#Library     properties
#Library     Lib
Library     Collections

Library     ../Py/properties.py
Library    ../Py/library.py
#Library     ../Py/library.py

Resource    ../Py/library.py
Resource    ../Objects/Object.robot

*** Variables ***
#${APPIUM_SERVER}    http://localhost:4723/wd/hub
#${PLATFORM_NAME}    Android
#${DEVICE_NAME}    3695d818
##${APP}    ${CURDIR}\\Sample Android App Login Test_v4.0_apkpure.com.apk
#${APP_PACKAGE}    com.android.messaging
#${APP_ACTIVITY}    com.android.messaging.ui.conversationlist.ConversationListActivity

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
    library.Select Commericial Signer
    library.Select Stc Radio Button
    library.Submit Button
    sleep  10
#    Press Keys  "//div[@class='Select__value-container css-1hwfws3']"   DOWN



