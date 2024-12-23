from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.gov.il/he/collectors/publications?Type=f2d28b83-ce5f-4ce3-a164-3fd0383b405a"

# Setup the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# Extract content
content = driver.page_source
print(content)

driver.quit()

