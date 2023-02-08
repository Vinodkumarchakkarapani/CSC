
from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap ={
    "platformName": "Android",
    "deviceName": "3695d818",
    "appPackage": "com.android.messaging",
    "appActivity": "com.android.messaging.ui.conversationlist.ConversationListActivity"

}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//android.widget.TextView[@text='Vk']").click()
sms=driver.find_element(By.ID,"com.android.messaging:id/message_text").text
print(sms)
# def textbox

Str = sms
N = 8
print(Str)
length = len(Str)
Str2 = Str[length - N:]
print(Str2)

















































































# import os
# from subprocess import PIPE, run
#
#
# def out(command):
#     result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
#     return result.stdout
#
#
# get_current_device = out("adb devices").split("attached")[1].split("device")[0].strip()
# cur_dir = os.getcwd()
#
#
# desired_cap_b2b = {
#     "appium:deviceName": "Android Emulator",
#     "platformName": "Android",
#     "appium:app": cur_dir + "/APK/GrabB2B.apk",
#     "appium:automationName": "UIAutomator2",
#     "appium:platformVersion": "11",
#     "appium:appActivity": "com.grab.grabrider.Activity.MainActivity",
#     "appium:appPackage": "com.grab.grabrider",
#     "appium:udid": get_current_device,
#     "appium:uiautomator2ServerInstallTimeout": "25000"
# }
# #
# # desired_cap={
# #     "deviceName": "3695d818",
# #     "platformName": "Android"
# # }
# # driver.open_notifications()
# #
# # try:
# #     notification = driver.find_element_by_id("com.android.systemui:id/clear_notifications")
# #
# #     if notification.is_displayed():
# #         notification.click()
# #         return EnterPhoneNumber(driver)
# #
# # except Exception as e:
# #     print(e)
# #     driver.press_keycode(4)
# #
