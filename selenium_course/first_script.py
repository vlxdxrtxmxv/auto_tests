from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:

    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    # price = WebDriverWait(browser, 12).until(
    #     EC.text_to_be_present_in_element((By.ID, "price"), "100")
    # )
    #
    # button = browser.find_element(By.ID, "book")
    # button.click()
    #
    # x = browser.find_element(By.ID, "input_value").text
    # expr = math.log(abs(12*math.sin(int(x))))
    #
    # answer = browser.find_element(By.ID, "answer")
    # answer.send_keys(str(expr))
    #
    # # Отправляем заполненную форму
    # button = browser.find_element(By.ID, "solve")
    # button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()