import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


#options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")
#driver = webdriver.Chrome(options=options)
#.get("https://www.taglit.info/")


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    sleep(2)

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.taglit.info/")


def test_user_login(browser):
   # browser.get("https://www.taglit.info/")
    browser.find_element(By.ID, "accept-btn").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, ".Login").click()
    browser.find_element(By.ID, "signup-tab-btn").click()
    browser.find_element(By.ID, "email-signup-btn").click()
    browser.find_element(By.ID, "email-signup-btn").click()
    browser.find_element(By.XPATH, '//label[contains(text(), "Given Name(s)")]').send_keys("Gabriella Brown")
    browser.find_element(By.NAME, "last_name").send_keys("TEST")
    browser.find_element(By.XPATH, '//input[@name="birth_date"]').send_keys("01/01/2003")
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys("gabriella.brown@example.com")











