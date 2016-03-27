import pygame
from pygame.locals import *

def MAX(a, b, c):
	""" returns the highest of three numbers that are passed to it """
	if a >= b and a >= c:
		return a
	elif b >= c:
		return b
	else:
		return c

def MIN(a, b, c):
	""" returns the lowest of three numbers that are passed to it """
	if a <= b and a <= c:
		return a
	elif b <= c:
		return b
	else:
		return c

def convert_RGB_to_HSV(colour):
	r = colour.r / 255.0
	g = colour.g / 255.0
	b = colour.b / 255.0
	
	min = MIN(r, g, b)
	max = MAX(r, g, b)
	
	# value, the V in HSV is whichever rgb value is highest
	v = max
	
	delta = max - min
	
	if max <> 0:
		s = delta / max
	else:
		# therefore r = g = b = 0
		# s = 0 and so hue is undefined
		return -1.0, 0.0, 0.0
	
	if r == max:	# red is the most promenant colour
		h = (g - b) / delta
	elif g == max:	# green is most promenant
		h = (b - r) / delta
	else:			# blue is most promenant
		h = (r - g) / delta
	
	# multiply hue by sixty to get it in degrees
	h *= 60.0
	
	# and make sure it's positive
	if h < 0: h += 360.0
	
	return h, s, v

def main(image_name, save_name, levels):
	pygame.init()
	
	# laod the image we want to get to
	image = pygame.image.load(image_name)
	
	# and find out what size it is
	width, height = image.get_size()
	
	# limit the number of levels to 256
	if levels > 256: levels = 256
	
	# find out the size of one level
	level_height = 256.0 / levels
	
	# loop over all the pixels in the image
	for x in range(width):
		for y in range(height):
			# find the colour of that pixel
			colour = image.get_at((x, y))
			
			# contrain that pixels values to one of the levels
			colour.r = int(colour.r - (colour.r % level_height))
			colour.g = int(colour.g - (colour.g % level_height))
			colour.b = int(colour.b - (colour.b % level_height))
			
			# place that colour onto the new image
			image.set_at((x, y), colour)
	
	pygame.image.save(image, save_name)

if __name__ == "__main__":
	image_name = raw_input("Enter a target image name: ")
	save_name = raw_input("Enter where the output should be save to: ")
	levels = int(raw_input("Enter how many levels to use: "))
	
	main(image_name, save_name, levels)
			