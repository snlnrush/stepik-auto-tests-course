from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    page = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(page)
    
    x_obj = browser.find_element_by_id("input_value")
    x = x_obj.text
    
    y = calc(x)
    
    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)
    
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element_by_css_selector("[value='robots']")
    radiobox.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
