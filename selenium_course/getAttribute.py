import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.ID, 'treasure')
    x = x_el.get_attribute('valuext')
    print(x)
    y = calc(x)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(y)

    option = browser.find_element(By.ID, "robotCheckbox")
    option.click()

    radioButton = browser.find_element(By.ID, 'robotsRule')
    radioButton.click()

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()