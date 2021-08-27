from selenium import webdriver
from datetime import datetime
import time
money = None
buy_cursor = None
buy_grandma = None
buy_factory = None
buy_mine = None
buy_shipment = None
buy_alchemy = None
buy_portal = None
buy_time_machine = None
cps = None
runtime = 30

laptop_driver = "/Users/Kamiklza/PycharmProjects/chromedriver"

driver = webdriver.Chrome(executable_path=laptop_driver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

def get_item_value():
    global money, buy_cursor, buy_grandma, buy_factory, buy_mine, buy_shipment, buy_alchemy, buy_portal, buy_time_machine, cps
    money = int(driver.find_element_by_id("money").text)
    buy_cursor = int(driver.find_element_by_css_selector("#buyCursor b").text.split("-")[1].strip())
    buy_grandma = int(driver.find_element_by_css_selector("#buyGrandma b").text.split("-")[1].strip())
    buy_factory = int(driver.find_element_by_css_selector("#buyFactory b").text.split("-")[1].strip())
    buy_mine = int(driver.find_element_by_css_selector("#buyMine b").text.split("-")[1].strip().replace(",", ""))
    buy_shipment = int(driver.find_element_by_css_selector("#buyShipment b").text.split("-")[1].strip().replace(",", ""))
    buy_alchemy = int(driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b').text.split("-")[1].strip().replace(",", ""))
    buy_portal = int(driver.find_element_by_css_selector("#buyPortal b").text.split("-")[1].strip().replace(",", ""))
    buy_time_machine = int(driver.find_element_by_xpath('//*[@id="buyTime machine"]/b').text.split("-")[1].strip().replace(",", ""))
    cps = float(driver.find_element_by_id("cps").text.split(":")[1].strip())


def buy_items():
    global money, buy_cursor, buy_grandma, buy_factory, buy_mine, buy_shipment, buy_alchemy, buy_portal, buy_time_machine
    if money >= buy_time_machine:
        driver.find_element_by_xpath('//*[@id="buyTime machine"]/b').click()
    elif money >= buy_portal:
        driver.find_element_by_css_selector("#buyPortal b").click()
    elif money >= buy_alchemy:
        driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b').click()
    elif money >= buy_shipment:
        driver.find_element_by_css_selector("#buyShipment b").click()
    elif money >= buy_mine:
        driver.find_element_by_css_selector("#buyMine b").click()
    elif money >= buy_factory:
        driver.find_element_by_css_selector("#buyFactory b").click()
    elif money >= buy_grandma:
        driver.find_element_by_css_selector("#buyGrandma b").click()
    else:
        driver.find_element_by_css_selector("#buyCursor b").click()

def final_result():
    money = int(driver.find_element_by_id("money").text)
    cps = float(driver.find_element_by_id("cps").text.split(":")[1].strip())
    return money, cps

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes
is_on = True
while is_on:
    cookie.click()
    if time.time() > timeout:
        get_item_value()
        buy_items()
        timeout = time.time() + 5
    if time.time() > five_min:
        is_on = False

print(final_result())







# while True:
#     cookie.click()
#     time.sleep(5)
#     buy_cursor = driver.find_element_by_css_selector("#buyCursor b")