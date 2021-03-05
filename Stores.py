import time
import os 
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("AMAZON_PASSWORD")

driver = webdriver.Chrome(ChromeDriverManager().install())

class Stores:
    def amazon_buy(i):
        driver.get(i.url)
        try:
            driver.find_element_by_id("buy-now-button")
            print("Item in stock for a price of " + driver.find_element_by_id("price_inside_buybox").text + " and budget set for this item is " + "$" + str(i.max_price))
            if(float(driver.find_element_by_id("price_inside_buybox").text.translate({ord(i):None for i in '$,'})) > i.max_price):
                print("Item is " + "$"+str(round(float(driver.find_element_by_id("price_inside_buybox").text.translate({ord(i):None for i in '$,'}))-i.max_price,2)) + " overpriced")
            else:
                driver.find_element_by_id("buy-now-button").click()
                driver.find_element_by_name("email").send_keys(EMAIL)
                driver.find_element_by_id("continue").click()
                driver.find_element_by_name("password").send_keys(PASSWORD)
                driver.find_element_by_id("signInSubmit").click()
                driver.find_element_by_name("placeYourOrder1").click()
        except NoSuchElementException:
            print ("Item:" + i.product_name + " Store:" + i.store + " Stock: " + 'Not in stock' )
            pass

    def newegg_buy(i):
        driver.get(i.url)
        try:
            driver.find_element_by_class_name("btn-primary")
        except NoSuchElementException:
            return print ("Item:" + i.product_name + " Store:" + i.store + " Stock: " + 'Not in stock' )
    def walmart_buy(i):
        driver.get(i.url)
        try:
            driver.find_element_by_class_name("spin-button-children")
        except NoSuchElementException:
            return print ("Item:" + i.product_name + " Store:" + i.store + " Stock: " + 'Not in stock' )
    def target_buy(i):
        driver.get(i.url)
        try:
            driver.find_element_by_class_name("Button__ButtonWithStyles-y45r97-0")
            return print("trying: "+i.store)
        except NoSuchElementException:
            print("catching: "+i.store)
            return print ("Item:" + i.product_name + " Store:" + i.store + " Stock: " + 'Not in stock' )
    def best_buy(i):
        driver.get(i.url)
        try:
            driver.find_element_by_class_name("btn-primary")
            print("trying: "+i.store)
        except NoSuchElementException:
            print("catching: "+i.store)
            return print ("Item:" + i.product_name + " Store:" + i.store + " Stock: " + 'Not in stock' )
    def gamestop_buy(i):
        driver.get(i.url)
        try:
            driver.find_element_by_class_name("btn-primary")
            print("trying: "+i.store)
        except NoSuchElementException:
            print("catching: "+i.store)
            return print ("Item:" + i.product_name + " Store:" + i.store + " Stock: " + 'Not in stock' )

Stores.newegg_buy = staticmethod(Stores.newegg_buy)
Stores.amazon_buy = staticmethod(Stores.amazon_buy)
Stores.walmart_buy = staticmethod(Stores.walmart_buy)
Stores.target_buy = staticmethod(Stores.target_buy)
Stores.best_buy = staticmethod(Stores.best_buy)
Stores.gamestop_buy = staticmethod(Stores.gamestop_buy)