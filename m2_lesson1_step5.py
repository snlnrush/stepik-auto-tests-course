from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    page = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(page)

    # Получаем значение Х для вычисления формулы
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    # Ваш код, который заполняет обязательные поля    
    input = browser.find_element_by_id("answer")
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
