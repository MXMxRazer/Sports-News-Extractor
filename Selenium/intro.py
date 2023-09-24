# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime
import os

from selenium.webdriver.support.wait import WebDriverWait

driverPath = "C:/chromedriver-win64/chromedriver.exe"

# TODO: TURN IT INTO MODULAR PROGRAMMING -> OBJECT ORIENTED
# Main Method
def main(website):
    # Initializing Service
    service = Service(executable_path=driverPath)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=service)

    # Display Execution Message
    print("\nExecuting Automation Activities...")

    # Specifying website
    driver.get(website)

    time.sleep(3.5)
    wait = WebDriverWait(driver, 3)
    btn = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-default visible_desktopTablet_only"]')))
    btn.click()

    time.sleep(3)
    wait = WebDriverWait(driver, 2)
    one_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@class="sea-btn btn-default sea-quantity-modal-option"]')))
    one_btn.click()

    time.sleep(2)
    wait = WebDriverWait(driver, 2)
    first_ticket = wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="Sea-TicketRow venue-ticket-list-row venue-ticket-list-row-height venue-ticket-list-row-js venue-ticket-list-mark-col-align-top"]')))
    first_ticket.click()

    time.sleep(2)
    wait = WebDriverWait(driver, 2)
    checkout_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn sea-btn pre-checkout-price-cta"]')))
    checkout_btn.click()

    time.sleep(2)
    wait = WebDriverWait(driver, 2)
    # time.sleep(10000000)
    checkout_email = driver.find_element(by="id", value='email')

    #TODO: CHECKOUT SECTION REMAINING
    # CHECKOUT SECTION
    time.sleep(2)
    wait = WebDriverWait(driver, 2)
    checkout_email.send_keys("example@gmail.com")
    time.sleep(2)
    wait = WebDriverWait(driver, 2)
    checkout_email.send_keys(Keys.ENTER)

    time.sleep(2)
    wait = WebDriverWait(driver, 2)
    payment = driver.find_element(by="id", value="CreditCardTab_AddressSectionModel_BillingName")
    payment.send_keys("kat")


    time.sleep(10)

# Main Method * END *

# Method Executor
def method_executor():
    website = "https://www.vipticketscanada.ca/Metallica-tickets"
    main(website)


# Method Executor * END *

method_executor()
