import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('test_pages', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
#@pytest.mark.parametrize('test_pages', ['236895', '236896'])
def test_guest_should_see_login_link(browser, test_pages):
    link = f"https://stepik.org/lesson/{test_pages}/step/1"
    browser.get(link)
    
    answer = str(math.log(int(time.time())))    
    
    # Вводим ответ в нужное поле
    input = browser.find_element_by_css_selector('[class="ember-text-area ember-view textarea string-quiz__textarea"]')
    input.send_keys(answer)    
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
        
    text_obj = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    
    text = text_obj.text
    
    print(text)    
    
    assert text == 'Correct!', f"Вместо 'Correct!' получено '{text}'"
