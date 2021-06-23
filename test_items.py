import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_cart_button(browser):
    browser.get(page)    
    button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='submit'].btn.btn-lg.btn-primary.btn-add-to-basket")))    
    assert button, 'Button not found!'
    time.sleep(30)
