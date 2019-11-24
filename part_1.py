#pip install selenium before start the procces
#Class 4
#1
import time
from selenium import webdriver
# url = webdriver.Chrome(executable_path="C:\\Users\\Taspa\\Downloads\\chromedriver_win32\\chromedriver.exe")
# url.get("https://.walla.co.il")
url = webdriver.Chrome(executable_path="C:\\Users\\Taspa\\Downloads\\chromedriver_win32\\chromedriver.exe")
#2 A
url.get("https://ynet.co.il")
time.sleep(6)
url.refresh()
#2 B
