from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.set_rotation(180)

red = [255, 0, 0]  # Red
white = [255, 255, 255]  # White
blue= [0, 0 ,50]
green = [0 , 50, 0]


while('true'):
	sense.show_message("we zijn nmd boys", text_colour=red, back_colour=white)
	sense.show_message("we zijn nmd boys", text_colour=white, back_colour=blue)
	sense.show_message("we zijn nmd boys", text_colour=white, back_colour=green)


	
