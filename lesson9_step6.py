import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
time.sleep(2)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
time.sleep(1)
read = browser.find_element(By.ID, "input_value")
read = read.text
read = int(read)
input = browser.find_element(By.ID, "answer")
input.send_keys(calc(read))

button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
