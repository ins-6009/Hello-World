from selenium import webdriver         # import webdriver package
driver =  webdriver.Firefox()             # initial a firefox: driver
driver.maximize_window()               # maximize browser
driver.get("https//www.google.com")    # open a url by get method
# driver.quit()                          # close and quit browser
