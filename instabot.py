from selenium import webdriver
import time
import user


class Instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('.\chromedriver_win32\chromedriver.exe')
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        self.login()
        self.following()

    def login(self):
        self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input") \
            .send_keys(self.username)
        self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input") \
            .send_keys(self.password)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]") \
            .click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    def following(self):
        self.driver.get("https://www.instagram.com/shafeer_pl/")
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")\
            .click()


if __name__ == '__main__':
    ig_bot = Instabot(user.username, user.password)
