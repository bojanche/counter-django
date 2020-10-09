from selenium import webdriver
import time


adresa = "<camera_ip>"


def get_result(adresa):
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--headless")
    print(options)

    browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    browser.get('https://'+adresa+':8443/#/login/?referrer=%2Fapp%2Feu.saimos.edge.count%2Fstats')

    loginElement = browser.find_element_by_xpath("//input[@aria-label='Username']")
    loginElement.send_keys('admin')
    passwordElement = browser.find_element_by_xpath("//input[@aria-label='Password']")
    passwordElement.send_keys('admin')

    loginButton = browser.find_element_by_class_name("v-btn__content")
    loginButton.click()
    try:
        entry = browser.find_element_by_class_name("enter").text
        entry = int(re.search(r'\d+', entry).group())
        leave = browser.find_element_by_class_name("leave").text
        leave = int(re.search(r'\d+', leave).group())
    except:
        entry = 0
        leave = 0
    finally:
        browser.quit()
    browser.quit()
    return entry-leave