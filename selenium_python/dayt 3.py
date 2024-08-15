import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demo.opencart.com/")
driver.maximize_window()
time.sleep(10)
# Click on "My Account" to open the dropdown menu

shping_kart = driver.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[4]/a/span')
time.sleep(5)
shping_kart.click()

# my_account = driver.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]')
# act=ActionChains(driver)
# act.move_to_element(my_account).perform()
# my_account.click()
# time.sleep(10)


my_account2 = driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/div/a/i[2]')
my_account2.click()
register_link = driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a")
register_link.click()
time.sleep(20)
# )
#



