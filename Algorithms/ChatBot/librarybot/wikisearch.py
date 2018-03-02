#!/bin/python2

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://pt.wikipedia.org')
driver.find_element_by_id('searchInput').send_keys('Guitarra')
driver.find_element_by_id('searchButton').click()
