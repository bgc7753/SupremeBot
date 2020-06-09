from selenium import webdriver
from config import keys
import pyautogui
import time

browser = webdriver.Firefox()
browser.get(keys['product_url'])

def checkout():
    print('Adding to Checkout')
    # Add to Cart
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input').click()
    time.sleep(1)
    # Go to Checkout
    browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/a[2]').click()
    # Name
    browser.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
    # Email
    browser.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
    # Telephone
    browser.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['tel'])
    # Address
    browser.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['address'])
    # Apartment
    browser.find_element_by_xpath('//*[@id="oba3"]').send_keys(keys['apt'])
    # Zip
    browser.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip'])
    # City
    browser.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    # State auto filled
    # Country autofilled
    # CC Number
    browser.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys['number'])
    # CC Exp Month
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[1]/option[{}]'.format(keys["cc_month"])).click()
    # # CC Exp Year
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[2]/option[{}]'.format(keys["cc_year"])).click()
    # # CC CVV
    browser.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['cc_cvv'])
    # # I have read and agree
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p[2]/label/div/ins').click()
    # # Process Payment

def main():
    checkout()

main()