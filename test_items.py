from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_user_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button"), f"No 'Add to Basket' button found!"

