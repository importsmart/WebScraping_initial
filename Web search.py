from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\dhruv\\chromedriver")
driver.get("https://www.flipkart.com/")

#elem = driver.find_element_by_css_selector("body > div.main > ul:nth-child(16) > li:nth-child(1) > a")
#elem.click()

#elems = driver.find_elements_by_css_selector('p')
#paragraphs
#print(len(elems))

searchElem = driver.find_element_by_css_selector("#container > div > div._3ybBIU > div._1tz-RS > div._3pNZKl > div.Y5-ZPI > form > div > div > input")
searchElem.send_keys('Catan')
searchElem.submit()

#driver.back()
#driver.fresh(
driver.quit()