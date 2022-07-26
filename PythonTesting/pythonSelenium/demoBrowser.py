from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
#service_obj = Service("C:/Users/Laxmi.Surampudi/Documents/Vivek/Softwares/chromedriver.exe")
service_obj = Service("C:/Users/Laxmi.Surampudi/selenium_drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

#-- Firefox
#service_obj = Service("C:/Users/Laxmi.Surampudi/selenium_drivers/geckodriver")
#driver = webdriver.Firefox(service=service_obj)

#-- Edge
# service_obj = Service("/Users/rahulshetty/documents/msedgedriver")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
#driver.get("https://rahulshettyacademy.com")
driver.get("https://www.Google.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()

print("finished")
