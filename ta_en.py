import tkinter as tk
from selenium import webdriver
import time


def englishtotamilapi(s):
   op = webdriver.ChromeOptions()
   op.add_argument('headless')
   driver = webdriver.Chrome(options=op)
   driver.get('http://www.google.com/')
   search_box = driver.find_element_by_name('q')
   search_box.send_keys(str(s)+" meaning in tamil")
   search_box.submit()
   search_box = driver.find_element_by_class_name("hrcAhc")
   r = search_box.text
   driver.quit()
   return r
    
   
def tamiltoenglishapi(s):
   op = webdriver.ChromeOptions()
   op.add_argument('headless')
   driver = webdriver.Chrome(options=op)
   driver.get('http://www.google.com/')
   search_box = driver.find_element_by_name('q')
   search_box.send_keys(str(s)+" meaning in english")
   search_box.submit()
   search_box = driver.find_element_by_class_name("hrcAhc")
   r = search_box.text
   driver.quit()
   return r   


