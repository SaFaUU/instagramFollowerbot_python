import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

DRIVER_PATH = "C://Selenium/chromedriver.exe"

# Add your email and password of instagram account you want to use
EMAIL = "..."
PASSWORD = "..."

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.instagram.com/")
time.sleep(3)

email = driver.find_element(By.XPATH,
                            "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH,
                               "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(5)

# The account want to follow
driver.get("https://www.instagram.com/landgrenwilliam/")
time.sleep(3)

followers_click = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div")
followers_click.click()
time.sleep(3)
followers_window = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
for num in range(1, 100):
    print(num)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_window)
    time.sleep(1)
all_person = driver.find_elements(By.CSS_SELECTOR, 'li button')
for single_person in all_person:
    try:
        single_person.click()
        time.sleep(1)
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except selenium.common.exceptions.ElementClickInterceptedException:
        cancel = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
        cancel.click()
