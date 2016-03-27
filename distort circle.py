import pygame
from pygame.locals import *

import math

def MIN(a, b):
	""" returns the lowest of two numbers that are passed to it """
	if a <= b:
		return a
	else:
		return b

def main():
	pygame.init()
	
	old_image = pygame.image.load("square grid.png")	# load the image to be distorted
	
	width, height = old_image.get_size()				# find out it's size
	
	centerX = width / 2									# and the center point
	centerY = height / 2
	
	min = MIN(centerX, centerY) * 0.25					# get the range of pixels to distort
	max = MIN(centerX, centerY) * 0.75
	
	new_image = pygame.Surface((width, height))			# create a blank surface the size of the original
	
	for x in range(width):									# cycle through every pixel in the new image
		for y in range(height):
			new_d = math.sqrt((x - centerX)**2 + (y - centerY)**2)		# d = distance of pixel to center
			
			if not min < new_d < max:								# if the distance is not in this range then
				new_image.set_at((x, y), old_image.get_at((x, y)))		# make it the same as the pixel on the old image
			
			else:													# otherwise change the pixel
				phase = (((new_d - min) / (max / min)) - 0.5) * math.pi		# find out how far into the range new_d is, from 0-pi
				
				##### this is the variable to change somehow #####
				old_d = new_d												# calculate the distace of the pixel in the old picture
				
				dir = math.atan2(centerX - x, centerY - y)
				
				old_x = centerX - (math.sin(dir) * old_d)
				old_y = centerY - (math.cos(dir) * old_d)
				
				new_image.set_at((x, y), old_image.get_at((old_x, old_y)))	# set the pixel
	
	pygame.image.save(new_image, "square grid distorted.png")

if __name__ == "__main__":
	main()