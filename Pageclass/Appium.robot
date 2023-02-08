*** Settings ***
Library    AppiumLibrary
#Library    SeleniumLibrary
#Library    library
Library    String
#Library    Selenium2Library

#Resource    Objects/Object.robot
#Resource
*** Variables ***
${APPIUM_SERVER}    http://localhost:4723/wd/hub
${PLATFORM_NAME}    Android
${DEVICE_NAME}    3695d818
#${APP}    ${CURDIR}\\Sample Android App Login Test_v4.0_apkpure.com.apk
${APP_PACKAGE}    com.android.messaging
${APP_ACTIVITY}    com.android.messaging.ui.conversationlist.ConversationListActivity
#${message_application}  "//android.widget.TextView[@text='Vk']"
#*** Test cases ***
#Mobile Test
#    Launch Mobile Application
${number_only}=      

*** Keywords ***
#launch Sharepoint Application
#    Open Browser    ${url}
#    Input Text    "//*[@id='i0116']    ${microsoft_username}
#    click

Launch Mobile Application
    Open Application    ${APPIUM_SERVER}
    ...    platformName=${PLATFORM_NAME}
    ...    deviceName=${DEVICE_NAME}
#    ...    app=${APP}
    ...    appPackage=${APP_PACKAGE}
    ...    appActivity=${APP_ACTIVITY}
        Sleep    30

        Click Element    xpath=//android.widget.TextView[@text='Vk']
        Sleep    15
        ${message}=    Get Element Attribute    id=com.android.messaging:id/message_text   text
        Log To Console    ${message}
        ${number_only}     Evaluate    "${message}".split(" ")[7]
        Log To Console    ${number_only}
        ${var1}=    Set Variable    ${number_only}
        Set Global Variable    ${var1}

#def text_me_button(otp):
    # wait_and_find()
    # wait_and_find(properties.text_me_new_codes, 'XPATH').click()
    # time.sleep(30)



#        otp= ${number_only}
#        ${otp}=  Split String    ${message}
#        Log To Console    ${otp}[2
#    Str = ${message}
#    N = 8
#    print(Str)
#    length = len(Str)
#    Str2 = Str[length - N:]
#    print(Str2)