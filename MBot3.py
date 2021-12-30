from keyauth import api
import asyncio
import time
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire import webdriver
import json
import aiohttp
import os
import sys
import os.path
import platform
from datetime import datetime

from cfg import *
keyauthapp = api("BotPython", "u6NQ037Tro", "3730042d70cce8b2fb0e8edb6d1e80f3f46c091c9c60b49dcc6a5bc4fbc5f200","1.0")

print("Initializing")
keyauthapp.init()

key = input('Enter your license: ')
keyauthapp.license(key)

print("\nUser data: ") 
print("Username: " + keyauthapp.user_data.username)
print("IP address: " + keyauthapp.user_data.ip)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Expires at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))

results = []

def getAuctionPage():
    url = f'https://www.binance.com/ru/nft/goods/blindBox/detail?productId={product_id}&isOpen=true&isProduct=1'
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath('//button[text()="Сделать ставку"]').click()  # buy btn

    print("CLICKED")
    time.sleep(2)


def clickConfirm():
    search = driver.find_elements_by_xpath('//button[text()="Сделать ставку"]')[1]
    ActionChains(driver).move_to_element(search).click().perform()

    print('CONFIRMED')

    time.sleep(2.5)

    for request in driver.requests:

        if str(request.url) == 'https://www.binance.com/bapi/nft/v1/private/nft/nft-trade/order-create':
            cookies = request.headers['cookie']
            csrftoken = request.headers['csrftoken']
            deviceinfo = 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6Ijg1OCwxNTI1IiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiODEzLDE1MjUiLCJzeXN0ZW1fdmVyc2lvbiI6IldpbmRvd3MgNyIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoiZW4tVVMiLCJ0aW1lem9uZSI6IkdNVCs2IiwidGltZXpvbmVPZmZzZXQiOi0zNjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImxpc3RfcGx1Z2luIjoiIiwiY2FudmFzX2NvZGUiOiIyOWI5YmU4MyIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwoUikgSEQgR3JhcGhpY3MgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wKSIsImF1ZGlvIjoiMzUuNzM4MzI5NTkzMDkyMiIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJBc2lhL0FsbWF0eSIsImRldmljZV9uYW1lIjoiRmlyZWZveCBWOTMuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6Ijg3YmY0OTA2ZDU3NDc4ZTE0NjAwMzQwYmY3MWUyYTUzIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTYyOTEzODQ2NTA4NHBCVTJIS2JOeWhjRWRKRkpHMGksMTYyOTk4Mjk5NzgwMnBPQWVDMGRmcldqUUZxV2NZTmEsMTYyOTk4NTIzMTY3MXlndGlyOFhBOWZWWW93TWFRRDcifQ=='
            useragent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'

            xNftCheckbotSitekey = request.headers['x-nft-checkbot-sitekey']
            xNftCheckbotToken = request.headers['x-nft-checkbot-token']
            xTraceId = request.headers['x-trace-id']
            xUiRequestTrace = request.headers['x-ui-request-trace']

            return {
                'Host': 'www.binance.com',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'clienttype': 'web',
                'x-nft-checkbot-token': xNftCheckbotToken,
                'x-nft-checkbot-sitekey': xNftCheckbotSitekey,
                'x-trace-id': xTraceId,
                'x-ui-request-trace': xUiRequestTrace,
                'content-type': 'application/json',
                'cookie': cookies,
                'csrftoken': csrftoken,
                'device-info': deviceinfo,
                'user-agent': useragent
            }

    return {}


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://binance.com/ru/nft")
a = input('Залогинтесь и нажмите Enter: ')

getAuctionPage()





def get_tasks(session):
    url = 'https://www.binance.com/bapi/nft/v1/private/nft/mystery-box/purchase'
    tasks = []

    for i in range(0, requestsNumber):
        tasks.append(asyncio.create_task(session.post(url, data=json.dumps(requests_payload), ssl=False)))

    # tasks.extend([asyncio.create_task(session.post(url, data = json.dumps(js), ssl=False))] * 100)
    print(len(tasks))
    return tasks


async def get_symbols(headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = get_tasks(session)
        print(time.time())
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.text())


def startSsc(headers):
    try:
        return asyncio.get_event_loop().run_until_complete(get_symbols(headers))
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop().run_until_complete(get_symbols(headers))


while True:
    ts = time.time()
    if saleTime>ts:
        print(f'{saleTime-ts} - осталось секунд')
    if saleTime-ts < 13.0:
        break

headers = clickConfirm()


while True:
    ts = time.time()
    if saleTime>ts:
        print(f'{saleTime-ts} - осталось секунд')
    if saleTime<ts:
        startSsc(headers)
        break


for r in results:
    if len(r)>250:
        print('blocked')
    else:
        print(r)

q = input()
