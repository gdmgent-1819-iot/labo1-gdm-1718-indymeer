from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
sense.clear()

while('true'):
	for x in range(8):
		for y in range(8):
			color = (randint(0,255), randint(0,255), randint(0,255) )
			match = (randint(0,1))
			if match == 0:
				sense.set_pixel(x,y,0,0,0)
				sense.set_pixel((7-x),y,0,0,0)

			else: 
				sense.set_pixel(x,y,color)
				sense.set_pixel((7-x),y,color)

	
	time.sleep(2)


