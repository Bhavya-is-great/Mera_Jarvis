from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver =  webdriver.Chrome() 

driver.get("https://bard.google.com/?hl=en")
sleep(4)

try:
    driver.find_element(by = By.XPATH,value="/html/body/chat-app/side-navigation/mat-sidenav-container/mat-sidenav-content/main/welcome-window/div/landing-page-variant-a/div/div/div/button/span[3]").click
    print("Button Clicked")
    sleep(4)
except:
    print("**KEY NOT FOUND**")