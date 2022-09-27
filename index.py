#https://github.com/danpush/t-rex-game-bot/blob/master/TRexBot.js
from selenium import webdriver
import tensorflow as tf
import keyboard

options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('./chromedriver/chromedriver.exe', options= options)
driver.implicitly_wait(2)
driver.get('https://dino-chrome.com/')

## Runner.instance_.horizon.obstacles.length > 0 : 장애물 존재 여부
## Runner.instance_.activated : 게임 실행 여부


is_playing = driver.execute_script("return Runner.instance_.activated;")
if(is_playing):
    pass