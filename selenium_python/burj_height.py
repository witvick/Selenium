
from selenium.webdriver.common.by import By
from selenium import webdriver

# Launch the Chrome browser and navigate to the webpage
driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

# Find the "Burj Khalifa" row in the table and get the height value
burj_khalifa_row = driver.find_element(By.XPATH,"//tr[contains(.,'Burj Khalifa')]")

burj_khalifa_height = burj_khalifa_row.find_element(By.XPATH,".//td[3]").text

# Verify that the height of Burj Khalifa is 829m
assert burj_khalifa_height == "829m"


# Verify that the height of Burj Khalifa is 829m
#assert burj_khalifa_height == "869m", f"Expected height to be '869m', but got '{burj_khalifa_height}'"


# Close the browser
driver.quit()