import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button1 = browser.find_element(By.ID, "book").click()

read1 = browser.find_element(By.ID, "input_value")
read1 = read1.text
read1 = int(read1)
input = browser.find_element(By.ID, "answer")
input.send_keys(calc(read1))
button_end = browser.find_element(By.ID, "solve").click()