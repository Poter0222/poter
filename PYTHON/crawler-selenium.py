import selenium
from selenium import webdriver
driver=webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver")
driver.get("https://www.google.com/?hl=zh-tw")
q = driver.find_element_by_name("q")
q.send_keys("觀音高中")
from selenium.webdriver.common.keys import Keys
q.send_keys(Keys.RETURN)