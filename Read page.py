from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\dhruv\\chromedriver")
driver.get("https://en.wikipedia.org/wiki/Communism")

elem = driver.find_element_by_css_selector("#mw-content-text > div > p:nth-child(8)")
print(elem.text)

#get entire page:
#elem2 = driver.find_element_by_css_selector('html')
#print(elem2.text)

driver.quit()