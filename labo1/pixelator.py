from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
sense.clear()


while('true'):
	for x in range(0,8):
			for y in range(0,8):
				r = randint(0,255)
				g = randint(0,255)
				b = randint(0,255)
				color = (r, g, b)
				sense.set_pixel(y,x,color) 
				sense.clear()
				if y != 0:
					sense.set_pixel(y,x,color) 
				time.sleep(0.2)

				
				
	time.sleep(2)

	
