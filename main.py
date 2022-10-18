import math
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.TAG_NAME, "button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element(By.ID, "input_value").text
xinput = math.log(abs(12*math.sin(int(x))))
answer = browser.find_element(By.ID, "answer")
answer.send_keys(xinput)
browser.find_element(By.TAG_NAME, "button").click()
time.sleep(30)
browser.quit()


