from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time

# prepping selenium environment
opt = Options()
opt.add_experimental_option('detach', True)
path = '/Users/a/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver'
ser = Service(path)
driver = webdriver.Chrome(service=ser, options=opt)

# website url
TEST_URL = 'https://dinerdrip.com/products/zip-up-hoodie'
LIVE_URL = 'https://dinerdrip.com/products/the-everyday-value-tee'

# CHANGE THE URL TO LIVE

driver.get(TEST_URL)

# adding item to cart
# driver.find_element('xpath', '//*[@id="msdrpdd20_msdd"]/div[1]/span[2]').click()
# driver.find_element('xpath', '//*[@id="msdrpdd20_child"]/ul/li[4]/span').click()
driver.find_element('xpath', '//*[@id="product-form-template--16940486557986__main"]/div/button').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="cart-notification-form"]/button').click()

# checkout process
# time.sleep(2)
# driver.find_element('xpath', '//*[@id="cart-subtotal"]/div/input').click()
# time.sleep(2)

# logging in
# username = driver.find_element('xpath', '//*[@id="website_user_login"]')
# username.send_keys('toyea')
# password = driver.find_element('xpath', '//*[@id="website_user_password"]')
# password.send_keys('*********')
# driver.find_element('xpath', '//*[@id="new_website_user"]/input[3]').click()

# checkout cont..
# time.sleep(3)
# driver.find_element('xpath', '//*[@id="cart-subtotal"]/div/input').click()
# time.sleep(1)
# street = driver.find_element('xpath', '//*[@id="website_order_shipping_address_attributes_first_address"]')
# street.send_keys('  ')
# city = driver.find_element('xpath', '//*[@id="website_order_shipping_address_attributes_city"]')
# city.send_keys('')
# driver.find_element('xpath', '//*[@id="website_order_shipping_address_attributes_state_chzn"]/a/span').click()
# search_state = driver.find_element('xpath', '//*[@id="website_order_shipping_address_attributes_state_chzn"]/div/div/input')
# search_state.send_keys('')
# driver.find_element('xpath', '//*[@id="website_order_shipping_address_attributes_state_chzn_o_15"]').click()
# zip_code = driver.find_element('xpath', '//*[@id="website_order_shipping_address_attributes_zip"]')
# zip_code.send_keys('')
# phone = driver.find_element('xpath', '//*[@id="website_order_shipping_contact_attributes_phone"]')
# phone.send_keys('')
# driver.find_element('xpath', '//*[@id="checkout-form"]/div[1]/div/div/input').click()


                                                                                                        # New updated checkout process


# Filling out shipping Information
# time.sleep(1)
email = driver.find_element('xpath', '//*[@id="email"]')
email.send_keys('aadesomoju001@gmail.com')
first_name = driver.find_element('xpath', '//*[@id="TextField0"]')
first_name.send_keys('Akintoye')
last_name = driver.find_element('xpath', '//*[@id="TextField1"]')
last_name.send_keys('Adesomoju')
address = driver.find_element('xpath', '//*[@id="address1"]')
address.send_keys('**** ********* ***')
city = driver.find_element('xpath', '//*[@id="TextField4"]')
city.send_keys('*******')
zipcode = driver.find_element('xpath', '//*[@id="TextField5"]')
zipcode.send_keys('***')
driver.find_element('xpath', '//*[@id="Form0"]/div[1]/div/div/div[2]/div[1]/button').click()
time.sleep(1)

# Selecting Shipping

driver.find_element('xpath', '//*[@id="Form1"]/div[1]/div/div/div[2]/div[1]/button').click()
time.sleep(2)

# Payment Method
# Issue, iframe will not allow multiple characters

card_number = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/iframe')
card_number.send_keys('****')
card_number = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/iframe')
card_number.send_keys('******')
card_number = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/iframe')
card_number.send_keys('***')
card_number = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/iframe')
# card_number.send_keys('')
# card_number = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/iframe')
# card_number.send_keys('')
# card_number = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/iframe')
# card_number.send_keys('')

card_name = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/iframe')
card_name.send_keys('A')
card_name = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/iframe')
card_name.send_keys('Akintoye')
card_name = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/iframe')
card_name.send_keys(' ')
card_name = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/iframe')
card_name.send_keys('Adesomoju')

exp_date = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div/div/iframe')
exp_date.send_keys('**')
exp_date = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div/div/iframe')
exp_date.send_keys('**')

sec_code = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[1]/section[1]/div/fieldset/div[2]/div/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div[1]/iframe')
sec_code.send_keys('***')
