import asyncio
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from selenium import webdriver
import re

adresa = "192.168.2.112"
ofset = 0


def get_result(adres):
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--headless")
    print(options)

    browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options, service_args=["--verbose", "--log-path=chromedirver.log"])
    browser.get('https://'+adres+':8443/#/login/?referrer=https%3A%2F%2F192.168.2.112%3A8443%2Fapp%2Feu.saimos.edge.count%2Fstats')

    # loginElement = browser.find_element_by_xpath("//input[@aria-label='Username']")
    loginElement = browser.find_element_by_id("Login_username")
    loginElement.send_keys('bojan')
    # passwordElement = browser.find_element_by_xpath("//input[@aria-label='Password']")
    passwordElement = browser.find_element_by_id("Login_password")
    passwordElement.send_keys('Bojana2512')

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


class CountConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected ")
        await self.send({
            "type": "websocket.accept"
        })
        boki = 0
        while True:
            boki = get_result(adresa)
            await asyncio.sleep(1)
            await self.send({
                "type": "websocket.send",
                "text": str(boki)
            })

    async def websocket_disconnect(self, event):
        print("Disconnected ", event)
        await self.send({
            "type": "websocket.disconnect"
            })

        raise StopConsumer()

    async def websocket_receive(self, event):
        print("received: ", event)