from selenium import webdriver
import time
import os


try: 
    page = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(page)
    
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Man')
    
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Bigman')
    
    input3 = browser.find_element_by_name('email')
    input3.send_keys('man@bigman.com')
    
    download = browser.find_element_by_name('file')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file_m2lesson2step8.txt')           # добавляем к этому пути имя файла 
    download.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
