from selenium.webdriver.common.keys import Keys

import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-speed', default='min')

    return parser


def get_chrome_options():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')

    return chrome_options


if __name__ == '__main__':
    parser = create_parser()
    driver = webdriver.Chrome(config.WEB_DRIVER_PATH, options=get_chrome_options())
    direction = parser.parse_args(sys.argv[1:])
    if direction.speed == 'min':
        print('Setting minimum speed')
    elif direction.speed == 'max':
        print('Setting maximum speed')
    driver.set_window_position(20, 20)
    driver.set_window_size(1000, 500)
    driver.implicitly_wait(180)

    try:
        driver.get('https://my.yota.ru/selfcare/login?goto=https%3A%2F%2Fmy.yota.ru%3A443%2Fdevices')
        login = driver.find_element_by_id('authLoginText')
        password = driver.find_element_by_id('authPasswordLogin')
        button = driver.find_element_by_css_selector('.js-auth-login-button > button.b-button')
        login.clear()
        login.send_keys('norzes@mail.ru')
        password.send_keys('12345678')
        button.click()
        decreaseButton = driver.find_element_by_css_selector('.decrease a')
        increaseButton = driver.find_element_by_css_selector('.increase a')
        print('Authorization was successful')
        print('Progress: [', end='')
        for i in range(0, 11):
            if direction.speed == 'min':
                decreaseButton.click()
            elif direction.speed == 'max':
                increaseButton.click()
            sleep(0.5)
            print('=', end='')
        print(']')
        offerButton = driver.find_element_by_css_selector('.main-offer a.btn')
        offerButton.click()
        print('Applying: [', end='')
        for i in range(0,10):
            print('=', end='')
            sleep(0.5)
        print(']')
        print('Done!')
    except Exception as e:
        driver.close()
        driver.quit()

    driver.close()
    driver.quit()
