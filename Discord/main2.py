from Userinfo import password,username
from soundstotxt import liste
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

class Discord:
    def __init__(self,username,password,liste):
        self.browser = wd.Chrome()
        self.username = username
        self.password = password
        self.liste = liste

    def singIn(self):
        self.browser.get("https://discord.com/login")
        time.sleep(2)
        usernameInput = self.browser.find_element(By.NAME,"email")
        passwordInput = self.browser.find_element(By.NAME,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        # self.browser.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
        time.sleep(5)
        self.goSettings()
        time.sleep(1)
        self.voiceDowload()

    def goSettings(self):
        self.browser.get("https://discord.com/channels/320479122910347265/723914979639558154")
        time.sleep(5)
        self.browser.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/nav/div[1]').click()
        time.sleep(1)
        self.browser.find_element(By.XPATH,'//*[@id="guild-header-popout-settings"]').click()
        time.sleep(1)
        self.browser.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/nav/div/div[5]').click()

    def voiceDowload(self):
        
        for name in self.liste: 
            time.sleep(1)
            self.browser.find_element(By.XPATH,'//*[@id="soundboard-tab"]/div/div[2]/div[1]/div[2]/button').click()
            time.sleep(1)

            voiceNameInput = self.browser.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/input')
            voiceInput = self.browser.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/button/div/input')
        
        
            voiceInput.send_keys(f"C:/Users/saykı/Desktop/Code/Pyhton Klasör/Python_Camping/selenium/Discord/sounnds/{name}")
            voiceNameInput.send_keys(f"{name}")
            time.sleep(1)
            self.browser.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/button[1]').click()
            time.sleep(1)



discord = Discord(username,password,liste)



while True:
    discord.singIn()
    if "y" == input():
        break