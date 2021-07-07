from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import ElementClickInterceptedException

import time

CHROME_DRIVER_PATH = "E:\chromedriver_win32\chromedriver"
INSTAGRAM_USERNAME = "YOUR INSTAGRAM USERNAME"
INSTAGRAM_PASSWORD = "YOUR INSTAGRAM PASSWORD"
SIMILAR_ACCOUNT = "python.learning"
INSTAGRAM_URL = "https://www.instagram.com/"

class InstaFollower:

    def __init__(self, path):
        self.driver =webdriver.Chrome(executable_path=path)
        self.driver.set_window_size(1310, 720)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(3)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(INSTAGRAM_USERNAME)
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)



    def find_followers(self):
        """ Find the followers of the account you want to follow """
        self.driver.get(f"{INSTAGRAM_URL}{SIMILAR_ACCOUNT}")
        time.sleep(5)
        # Find the followers button and click it
        followers_popup = self.driver.find_element_by_css_selector('header a')
        followers_popup.click()
        # print(followers_popup.text)
        time.sleep(2)
        # Holds the div in which the followers are appearing
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(3):
            """ Scroll down the followers list """
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        """ Follows the find users """
        # Locate the follow buttons of the all the users in followers list
        follow_btns = self.driver.find_elements_by_css_selector('.PZuss button')
        # Go through each button and if button text is follow then click on it
        for btn in follow_btns:
            if btn.text == 'Follow':
                time.sleep(1)
                btn.click()
                rand_time = random.randint(2, 40)  # Creates a random int to be use as time
                print(rand_time)
                time.sleep(rand_time)  # wait for the time until click on the next button

                time.sleep(1)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()


