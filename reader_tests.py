from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def apple():
    desired_cap = {
        'browserName': 'iPhone',
        'device': 'iPhone XS',
        'realMobile': 'true',
        'os_version': '12',
        'name': 'Bstack-[Python] Sample Test',
        'browserstack.debug' : 'true' 
    }
    
    driver = webdriver.Remote(
        command_executor='http://suryapoddutoori1:VFqXega6vpxQBqUjig6e@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    
    driver.get("https://gb.cs.unc.edu/static/tiny/find.html")
    if not "Find" in driver.title:
        raise Exception("Unable to load gary page!")
    
    elem = driver.find_element_by_xpath("/html/body/form[1]")
    elem.send_keys("Pizza")
    elemsub = driver.find_element_by_xpath("/html/body/form/input[3]") #use xpath to find the element
    print(elemsub.get_attribute('value')) #check if its the search button, it is
    elemsub.click() #click it, this feature does not seem to work on the tests, but works on live tests
    
    elem2 = driver.find_element_by_xpath('/html/body/ul/li/a/h1')
    print(elem2.get_attribute('innerHTML'))
    driver.quit()

def android():
    #Android
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    
    desired_cap = {
        'os_version' : '7.0',
        'device' : 'Samsung Galaxy S8',
        'real_mobile' : 'true',
        'browserstack.local' : 'false', 
        'browserstack.debug' : 'true' 
    }
    
    driver = webdriver.Remote(
        command_executor='http://suryapoddutoori1:VFqXega6vpxQBqUjig6e@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    
    driver.get("https://gb.cs.unc.edu/static/tiny/find.html")
    if not "Find" in driver.title:
        raise Exception("Unable to load gary page!")
    
    elem = driver.find_element_by_xpath("/html/body/form/input[1]")
    elem.send_keys("Pizza")
    elemsub = driver.find_element_by_xpath("/html/body/form/input[3]")
    print(elemsub.get_attribute('value'))
    elemsub.click()
    
    elem2 = driver.find_element_by_xpath('/html/body/ul/li/a/h1')
    print(elem2.get_attribute('innerHTML'))
    driver.quit()

def windows():
    desired_cap = {
        'os' : 'Windows',
        'os_version' : '10',
        'browser' : 'Chrome',
        'browser_version' : '62.0',
        'browserstack.local' : 'false',
        'browserstack.selenium_version' : '3.5.2',
        'browserstack.debug' : 'true'
    }
    
    driver = webdriver.Remote(
        command_executor='http://suryapoddutoori1:VFqXega6vpxQBqUjig6e@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    
    driver.get("https://gb.cs.unc.edu/static/tiny/find.html")
    if not "Find" in driver.title:
        raise Exception("Unable to load gary page!")
    
    elem = driver.find_element_by_xpath("/html/body/form/input[1]")
    elem.send_keys("Pizza")
    elemsub = driver.find_element_by_xpath("/html/body/form/input[3]")
    print(elemsub.get_attribute('value'))
    elemsub.click()
    
    elem2 = driver.find_element_by_xpath('/html/body/ul/li/a/h1')
    print(elem2.get_attribute('innerHTML'))
    driver.quit()

def mac():
    desired_cap = {
        'os' : 'OS X',
        'os_version' : 'Mojave',
        'browser' : 'Safari',
        'browser_version' : '12.0',
        'browserstack.local' : 'false',
        'browserstack.selenium_version' : '3.5.2' 
        'browserstack.debug' : 'true' 
    }
    
    driver = webdriver.Remote(
        command_executor='http://suryapoddutoori1:VFqXega6vpxQBqUjig6e@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    
    driver.get("https://gb.cs.unc.edu/static/tiny/find.html")
    if not "Find" in driver.title:
        raise Exception("Unable to load gary page!")
    
    elem = driver.find_element_by_xpath("/html/body/form/input[1]")
    elem.send_keys("Pizza")
    elemsub = driver.find_element_by_xpath("/html/body/form/input[3]")
    print(elemsub.get_attribute('value'))
    elemsub.click()
    
    elem2 = driver.find_element_by_xpath('/html/body/ul/li/a/h1')
    print(elem2.get_attribute('innerHTML'))
    driver.quit()
