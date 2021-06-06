from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    page = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(page)
    
    num1_obj = browser.find_element_by_id("num1")
    num1 = num1_obj.text
    num2_obj = browser.find_element_by_id("num2")
    num2 = num2_obj.text
    
    sum_x = str(sum(int(x) for x in (num1, num2)))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_x) 
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
