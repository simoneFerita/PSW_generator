#Semplice script per generare password 
import pyautogui as gui
import time
import random, string

number =  input("Number of password: ")
time.sleep(3)

for i in range(int(number)):
    password = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    message = "".join(random.sample(password, 64))
    gui.typewrite(message)
    gui.press('Enter')