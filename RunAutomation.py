import pyautogui
import time
import os
import threading
import random
import json

min_wait = 0.2
max_wait = 1.5
automation_story = None

def _wait():
	t = random.uniform(min_wait, max_wait)
	print(f"waiting for {t} sec..")
	time.sleep(t)

def Open_Genymotion():
	t = threading.Thread(target=lambda : os.system("scrcpy"))
	t.start()
	
def Press_Key(key_name):
	pyautogui.press(key_name)

def Click(x, y):
	pyautogui.click(x=x, y=y)

def Type_String(text):
	for i in text:
		pyautogui.press(i) 
		
def Load_Automation_File(name):
	global automation_story
	with open(name, 'r') as f:
		data = f.read()
		automation_story = json.loads(data)

def Print_Story():
	global automation_story
	print(automation_story)

def Run_Story():
	global automation_story
	for i in automation_story:
		print(i)
		_wait()

Load_Automation_File("test.json")

Run_Story()

# phone_number = input("enter number:\n")


