from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://login.skype.com/login?client_id=578134&redirect_uri=https%3A%2F%2Fweb.skype.com')

driver.find_element_by_id('username').send_keys('silvinho485@gmail.com')

driver.find_element_by_id('username').send_keys(Keys.ENTER)

driver.implicitly_wait(2)

driver.find_element_by_id('i0118').send_keys('$Ilvio141091')

driver.find_element_by_id('i0118').send_keys(Keys.ENTER)

driver.implicitly_wait(10)

driver.find_element_by_partial_link_text('Amigos preguntones').click()

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "chatInputAreaWithQuotes"))
)

print element

# textArea = driver.find_element_by_id('textarea-bindings')

element.send_keys('Message send through selenium webdriver')

driver.find_element_by_id('chatInputAreaWithQuotes').send_keys('Message send through selenium webdriver') 

driver.find_element_by_id('chatInputAreaWithQuotes').send_keys(Key.ENTER)
