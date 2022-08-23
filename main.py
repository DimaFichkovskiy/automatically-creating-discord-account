from string import ascii_letters
import random
import time

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

REGISTER_URL = 'https://discord.com/register'
LOGIN_URL = 'https://discord.com/api/v9/auth/login'


def generate_password():
    password = ''
    for i in range(16):
        password += random.choice(list(ascii_letters))
    return password


def register(email, username, password):
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
    )
    driver.get(REGISTER_URL)
    email_input = driver.find_element(By.NAME, 'email')
    email_input.click()
    email_input.send_keys(email)

    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    day_of_birth = driver.find_element(By.ID, 'react-select-2-input')
    day_of_birth.send_keys(1)

    month_of_birth = driver.find_element(By.ID, 'react-select-3-input')
    month_of_birth.send_keys('january')
    month_of_birth.send_keys(Keys.ENTER)

    year_of_birth = driver.find_element(By.ID, 'react-select-4-input')
    year_of_birth.send_keys(2009)

    button_register = driver.find_element(By.CLASS_NAME, 'button-1cRKG6')
    button_register.click()

    time.sleep(10)
    driver.close()
    driver.quit()


def login(email, password):
    json_data = {
        'login': email,
        'password': password,
    }
    r = requests.post(LOGIN_URL, json=json_data)
    return r.json().get('token')


if __name__ == '__main__':
    email = input('email: ')
    username = input('username: ')

    password = generate_password()
    print(f'password: {password}')

    register(email, username, password)
    token = login(email, password)
    print(f'token: {token}')
