import time
from PIL import Image
import pytesseract

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://randevu.nvi.gov.tr/")
assert "Randevu" in driver.title
elements=driver.find_elements(By.CLASS_NAME, "fs10")
for element in elements:
    if(element.text == "PASAPORT"):
        element.click()
        print("pasaport tıklandı")
        break

time.sleep(2)
driver.find_element(By.XPATH, "//*[contains(text(), 'kabul ediyorum')]").click()
print("kabul ediyorum tıklandı")
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="pasaport"]/div/div/div/div[3]/div/button').click()
print("seç tıklandı")
adiniz = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/form/div[2]/div[1]/div[1]/div/input')
adiniz.send_keys("rana")
print("adınız yazıldı")
captcha=driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/form/div[2]/div[1]/div[6]/div/div/img')
with open('captcha.png', 'wb') as file:
    file.write(captcha.screenshot_as_png)
time.sleep(1)
captcha=pytesseract.image_to_string(Image.open('captcha.png'))
alengirli=driver.find_element(By.XPATH, '//*[@id="divKisi"]/div[1]/div[6]/div/input')
alengirli.send_keys(captcha)
print("captcha :", captcha)
print("captcha yazıldı")