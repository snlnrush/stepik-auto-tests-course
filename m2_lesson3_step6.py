from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    page = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(page)
    
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    
    new_window_name = browser.window_handles[1]
    
    browser.switch_to.window(new_window_name)    
    
    x_obj = browser.find_element_by_id('input_value')
    x = x_obj.text
    
    y = calc(x)
    
    input = browser.find_element_by_id("answer")    
    input.send_keys(y)
    
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
