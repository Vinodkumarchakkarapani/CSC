import time
import os
# from appium import webdriver
# from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
# from appium import webdriver
import properties as properties

# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_arguments('--incognito')
# web_driver=webdriver.chrome(chrome_options=chrome_options)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# web_driver = webdriver.Chrome(options=options)

# serv = Service("C:/Users/vinow/PycharmProjects/Sharepoint/Sharepoint/Drivers/chromedriver.exe")

# web_driver = webdriver.Chrome(executable_path='C:/Users/vinow/PycharmProjects/Sharepoint/Sharepoint/Drivers/chromedriver.exe')
serv = Service("C:/Users/vinod/PycharmProjects/CSC/Drivers/chromedriver.exe")

web_driver = webdriver.Chrome(service=serv)

cur_dir = os.getcwd()


# def message():
#     driver.find_element(By.XPATH, "//android.widget.TextView[@text='Vk']").click()
#     sms = driver.find_element(By.ID, "com.android.messaging:id/message_text").text
#     print(sms)
#     msg = sms
#     N = 8
#     print(msg)
#     length = len(msg)
#     OTP = msg[length - N:]
#     print(OTP)


#
# def open_notifications():
#     web_driver.open_notifications()
#
#
# def clear_notifications():
#     webdriver.clear_notifications()
#
# def open_notifications(self):
#     self.driver.open_notifications()
#     try:
#         notification = self.driver.find_element_by_id("com.android.systemui:id/clear_notifications")
#         if notification.is_displayed():
#             notification.click()
#             # return EnterPhoneNumber(self.driver)
#     except Exception as e:
#         print(e)
#         self.driver.press_keycode(4)
#
# def open_notifications(self):
#     self.driver.open_not

# def get_otp(self):
#     try:
#         self.driver.open_notifications()
#         time.sleep(3)
#         message_text = self.driver.find_elements_by_id("android:id/message_text")
#         size = len(message_text)
#         print("Size =" + str(size))
#         for i in range(0, 3):
#             time.sleep(2)
#             if len(self.otp) == 0:
#                 self.otp = self.otp_loop(size, message_text)
#             else:
#                 print("OTP Found")
#                 break
#         if len(self.otp) < 6:
#             print("---- Failed to retrieve OTP ----")
#             self.driver.press_keycode(4)
#             return ""
#         else:
#             self.otp = self.extract_otp(self.otp)
#         if len(self.otp) == 0:
#             Assert.fail("OTP not received")
#         else:
#             print("OTP is: " + self.otp)
#
#
# web_driver.openNotifications();
# driver_path = "C:/Users/vinow/PycharmProjects/Sharepoint/Sharepoint/Drivers/chromedriver.exe"
# web_driver = webdriver.Chrome(driver_path)

def open_browser(url):
    web_driver.get(url)
    web_driver.maximize_window()


# def open_browser(url):

# webdriver.Chrome()
def page_refresh():
    web_driver.refresh()


# def wait_and_find_app(element, locator):
#     try:
#         if locator == 'ID':
#             waitElement = WebDriverWait(d, 120).until(
#                 EC.presence_of_element_located((By.ID, element)))
#         elif locator == 'XPATH':
#             waitElement = WebDriverWait(web_driver, 120).until(
#                 EC.presence_of_element_located((By.XPATH, element)))
#         elif locator == 'CSS':
#             WebDriverWait(web_driver, 120).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, element)))
#
#     except:
#         print("No element present for the locator " + element)
#
#     return waitElement


def wait_and_find(element, locator):
    try:
        if locator == 'ID':
            waitElement = WebDriverWait(web_driver, 120).until(
                EC.presence_of_element_located((By.ID, element)))
        elif locator == 'XPATH':
            waitElement = WebDriverWait(web_driver, 120).until(
                EC.presence_of_element_located((By.XPATH, element)))
        elif locator == 'CSS':
            WebDriverWait(web_driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element)))

    except:
        print("No element present for the locator " + element)

    return waitElement


def wait_and_find_elements_list(element, locator):
    if locator == 'ID':
        waitElements = WebDriverWait(web_driver, 30).until(
            EC.presence_of_all_elements_located((By.ID, element)))
    elif locator == 'XPATH':
        waitElements = WebDriverWait(web_driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, element)))
    return waitElements


def string_equals(string1, string2):
    return string1 == string2


def is_displayed(element):
    return web_driver.find_element(By.XPATH, element).is_displayed()


def is_selectByallvisibletext(element, locator):
    try:
        if locator == 'ID':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_all_elements_located((By.ID, element)))
        elif locator == 'XPATH':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, element)))
        elif locator == 'CSS':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_element_located(By.CSS_SELECTOR, element))
    except:
        print("No element present for the locator " + element)

    return visiblealltext


def is_selectByvisibletext(element, locator):
    try:
        if locator == 'ID':
            visibletext = WebDriverWait(web_driver, 30).until(
                Select.select_by_visible_text((By.ID, element)))
        elif locator == 'XPATH':
            visibletext = WebDriverWait(web_driver, 30).until(
                Select.select_by_visible_text((By.XPATH, element)))
        elif locator == 'CSS':
            visibletext = WebDriverWait(web_driver, 30).until(Select.select_by_visible_text(By.CSS_SELECTOR, element))
    except:
        print("No element present for the locator " + element)

    return visibletext


def login_to_moonshot(username, password):
    # wait_and_find(properties.user_name_textbox, 'XPATH').send_keys(username)
    # wait_and_find(properties.password_textbox, 'XPATH').send_keys(password)
    # time.sleep(5)
    wait_and_find(properties.login_button, 'XPATH').click()


def pop_up_username(username):
    # handles = web_driver.window_handles
    # web_driver.switch_to.window(handles[1])

    wait_and_find(properties.pop_up_username, 'XPATH').send_keys(username)
    wait_and_find(properties.pop_up_submit_button, 'XPATH').click()
    # wait_and_find(properties)


def pop_up_password(username):
    # handles = web_driver.window_handles
    # web_driver.switch_to.window(handles[1])

    wait_and_find(properties.pop_up_pass, 'XPATH').send_keys(username)
    time.sleep(5)
    wait_and_find(properties.pop_up_submit, 'XPATH').click()


def wait_find(element, locator):
    try:
        if locator == 'ID':
            waitElement = WebDriverWait(web_driver, 30).until(
                EC.text_to_be_present_in_element((By.ID, element)))
        elif locator == 'XPATH':
            waitElement = WebDriverWait(web_driver, 30).until(
                EC.text_to_be_present_in_element((By.XPATH, element)))
        elif locator == 'CSS':
            WebDriverWait(web_driver, 30).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, element)))

    except:
        print("No element present for the locator " + element)

    return waitElement


def pop_up_button():
    # handles = web_driver.window_handles
    # web_driver.switch_to.window(handles[1])
    wait_and_find(properties.pop_up_button, 'XPATH').click()


def text_me_button(otp):
    # wait_and_find()
    # wait_and_find(properties.text_me_new_codes, 'XPATH').click()
    # time.sleep(30)
    wait_and_find(properties.otp_textbox, 'XPATH').send_keys(otp)


def sign_in_button():
    wait_and_find(properties.pop_up_button, 'XPATH').click()
    time.sleep(3)
    wait_and_find(properties.sign_click, 'XPATH').click()


def contract_button():
    time.sleep(10)
    wait_and_find(properties.create_contract_button, 'XPATH').click()
    wait_and_find(properties.submit_button, 'XPATH').click()
    alert_prompt = Alert(web_driver)
    print(alert_prompt.text)
    alert_prompt.accept()


def save_as_draft_button():
    time.sleep(5)
    wait_and_find(properties.save_as_draft, 'XPATH').click()
    alert_prompt = Alert(web_driver)
    print(alert_prompt.text)
    alert_prompt.accept()


def ws_office_dropdown():
    wait_and_find(properties.ws_office, 'XPATH').click()
    wait_and_find(properties.ws_office_dropdown, 'XPATH').click()
    # wait_and_find(properties.ws_office_dropdown,'XPATH').click()


def client_name(name):
    wait_and_find(properties.client_name, 'XPATH').send_keys(name)
    wait_and_find(properties.client_name_select, 'XPATH').click()
    # time.sleep(5)


def client_name_textbox(name):
    wait_and_find(properties.client_name_textbox, 'XPATH').send_keys(name, Keys.ENTER)
    # time.sleep(5)


def enter():
    # actions = ActionChains(web_driver)
    wait_and_find(properties.client_name_textbox, 'XPATH').send_keys(Keys.ENTER)


def select_primary_client():
    wait_and_find(properties.primary_client_contact, 'XPATH').click()
    wait_and_find(properties.select_primary_client_contact, 'XPATH').click()


def select_contract_term():
    wait_and_find(properties.select_contract_term, 'XPATH').click()
    wait_and_find(properties.select_contract_term_year, 'XPATH').click()


def select_contract_date():
    wait_and_find(properties.select_contract_start_date, 'XPATH').click()
    wait_and_find(properties.contract_start_date, 'XPATH').click()


def select_management_coverage(text):
    wait_and_find(properties.select_add_coverages, 'XPATH').click()
    wait_and_find(properties.select_management_coverage, 'XPATH').send_keys(text, Keys.ENTER)

    # action = ActionChains(web_driver)
    # wait_and_find(properties.client_name_select, 'XPATH').action.key_down(Keys.CONTROL).perform()
    # # perform the operation
    # action.key_down(Keys.CONTROL).send_keys('F').key_down(Keys.CONTROL).perform()
    # # wait_and_find(properties.client_name_select,'XPATH').send_keys(keys.DOWN)
    # # wait_and_find(properties.client_name_select,'XPATH').send_keys(keys.ENTER)
    # wait_and_find(properties.submit_button,'XPATH').click()


def fees_offset_commission_textbox(text):
    wait_and_find(properties.fees_offset_commission_textbox, 'XPATH').send_keys(text)


def select_commericial_signer():
    wait_and_find(properties.commericial_contract_signer, 'XPATH').click()
    wait_and_find(properties.select_commericial_contract_signer, 'XPATH').click()


def select_stc_radio_button():
    wait_and_find(properties.stc_radio_button, 'XPATH').click()


def submit_button():
    wait_and_find(properties.submit_button, 'XPATH').click()


def employee_benefits_coverage(text):
    wait_and_find(properties.employee_benefits_coverage_button, 'XPATH').click()
    wait_and_find(properties.employee_benefits_coverage, 'XPATH').send_keys(text, Keys.ENTER)


def fees_offset_EB(text):
    wait_and_find(properties.eb_fees_offset_commission_textbox, 'XPATH').send_keys(text)


def select_employee_benefit_signer():
    wait_and_find(properties.employee_benefits_signer, 'XPATH').click()
    wait_and_find(properties.select_employee_benefits_signer, 'XPATH').click()


def select_sow_document():
    wait_and_find(properties.sow_dropdown, 'XPATH').click()
    wait_and_find(properties.select_sow_domben_dropdown, 'XPATH').click()


def scroll_up():
    # time.sleep()
    web_driver.execute_script('window.scrollTo(0,200)')


def scroll_down():
    web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


def ready_for_docusign_link():
    wait_and_find(properties.ready_for_docusign_link, 'XPATH').click()


def rescind_button():
    wait_and_find(properties.rescind_button, 'XPATH').click()
    wait_and_find(properties.confirmation_no, 'XPATH').click()
    wait_and_find(properties.rescind_button, 'XPATH').click()
    wait_and_find(properties.confirmation_yes, 'XPATH').click()
    time.sleep(3)
    wait_and_find(properties.edit_close_button, 'XPATH').click()
    wait_and_find(properties.confirmation_close_yes, 'XPATH').click()
    wait_and_find(properties.close_button, 'XPATH').click()


def rescinded_link():
    wait_and_find(properties.rescind_link, 'XPATH').click()
    wait_and_find(properties.edit_button, 'XPATH').click()
    wait_and_find(properties.rescind_submit_button, 'XPATH').click()


def all_contract_button():
    wait_and_find(properties.all_contract_button, 'XPATH').click()
