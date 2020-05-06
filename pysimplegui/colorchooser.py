#!/usr/bin/env python

import io
import base64
from PIL import Image
import PySimpleGUI as sg

width = 128
height = 128
imgtk = None

def framebuf_to_tk(fb, w, h):
	# create PIL image
	img = Image.new('RGB', (w, h))
	px = img.load()

	# copy framebuf to PIL image
	# TODO: use frombytes() or frombuffer()
	for y in range(h):
		for x in range(w):
			px[x,y] = fb[y*w + x]

	# PIL -> gif -> string
	gif = None
	with io.BytesIO() as output:
		img.save(output, format="GIF")
		gif = output.getvalue()

	# gif string -> base64
	return base64.b64encode(gif)

if __name__ == '__main__':
	# create framebuffer
	i=0
	framebuf = [None] * width * height
	for y in range(height):
		for x in range(width):
			framebuf[i] = (0,0,0)
			i += 1
	# create Tk-compatible image	
	imgtk = framebuf_to_tk(framebuf, width, height)

	sgImage = sg.Image(data=imgtk, size=(width,height))
	gui_rows = [[sg.Text('Color Chooser')],  
				[sg.T('')],
				[sg.Slider(range=(0,255), default_value=255, orientation='h')],
				[sg.Slider(range=(0,255), default_value=0, orientation='h')],
				[sg.Slider(range=(0,255), default_value=0, orientation='h')],
				[sg.Quit(button_color=('black', 'orange'))],
				[sgImage]
				]  
	  
	window = sg.Window('Color Chooser', auto_size_text=True).Layout(gui_rows)  
	  
	while (True):  
		# This is the code that reads and updates your window  
		event, valuesDict = window.Read(timeout=100)  
		print(valuesDict)
		if event == None:
			print('None event')
		elif event == '__TIMEOUT__':
			#print('TIMEOUT event')
			pass
		elif event == 'Quit':
			print('Quit event')
			break
		elif event == 'Forward':
			print('FORWARD!')
		else:
			print('unknown event: ', event)

		if valuesDict:
			[r,g,b] = map(int, valuesDict.values())
			print("new rgb: (%d,%d,%d)" % (r,g,b))

			i=0
			for y in range(height):
				for x in range(width):
					framebuf[i] = (r,g,b)
					i += 1
			imgtk = framebuf_to_tk(framebuf, width, height)
			sgImage.Update(data=imgtk)
 
	window.Close() # Don't forget to close your window!
