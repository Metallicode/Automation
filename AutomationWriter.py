from pynput.mouse import Listener
from pynput import keyboard
import datetime 
import json

story = []
story_name = input("enter story name: \n")

def on_click(x, y, button, pressed):
	if pressed is True:
		d = dict(x=x, y=y, button=str(button), time=str(datetime.datetime.now()))
		story.append(d)

def on_press(key):
	try:
		if hasattr(key, 'char'):
			d = dict(x=None, y=None, button=str(key.char), time=str(datetime.datetime.now()))
		else:
			d = dict(x=None, y=None, button=str(key), time=str(datetime.datetime.now()))
		story.append(d)
		if key.char == '`':
			with open(f'{story_name}.json','w') as f:
				f.write(json.dumps(story))
				print("file created!\n")

	except Exception as e:
		print(e)

				
listener1 = keyboard.Listener(on_press=on_press)
listener1.start()

with Listener(on_click=on_click) as listener:
	listener.join()
	

