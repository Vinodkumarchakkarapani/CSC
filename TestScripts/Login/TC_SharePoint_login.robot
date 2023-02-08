*** Settings ***
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     selenium
#Library     ../../Py/library.py
Library     ../../Py/library.py

#Resource     ../../Pageclass/Sharepoint_login.robot
#Resource      ../../Pageclass/Rescind.robot
Resource       ../../Pageclass/Practice_leader.robot
Resource    ../../Objects/object.robot
Resource    ../../Pageclass/Appium.robot
#Resource     ../../Pageclass/Employee_benefit.robot
*** Test Cases ***

TC_01_login with valid credentials for sharepoint

    Open the browser
    login Sharepoint application          ${microsoft_username}        ${microsoft_password}
    Launch Mobile Application       
    Enter OTP value in Textbox

#    Create an new contract
#    Rescind flow

