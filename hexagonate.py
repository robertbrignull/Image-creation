import pygame
from pygame.locals import *

import math

def main():
	""" this program turns an image into a stain glass effect
	by drawing hexagons all over the image and filling them with
	block colours """
	
	pygame.init()
	
	# the image to hexagonate
	image = pygame.image.load("countryside.jpg")
	
	# the size of the image being modified
	# don't need to make a second image, all work is done on the original
	im_width, im_height = image.get_size()
	
	# the size of each individual hexagon
	hex_width = im_width / 80
	hex_height = hex_width * (math.sqrt(3) / 2)
	
	# need to keep an offset as two columns of hexagons next to each
	# other are not in line with each other, one is a bit further down
	height_offset = 0.0
	
	# need to do the big loop twice, first colouring the hexagons,
	# then drawing the edges, done this way to stop colours overlapping
	
	# fist put in the colour
	for x in range(int(im_width / hex_width)+2):
		for y in range(int(im_height / hex_height)+2):
			if 0 <= (hex_width * x) < im_width and 0 <= ((hex_height * y) + height_offset) < im_height:
				colour = image.get_at((hex_width * x, (hex_height * y) + height_offset))
				pygame.draw.polygon(image, colour, [((hex_width * x) + (hex_width / 2.0), (hex_height * y) + height_offset),
													((hex_width * x) + (hex_width / 4.0), (hex_height * y) + (hex_height / 2.0) + height_offset),
													((hex_width * x) - (hex_width / 2.0), (hex_height * y) + (hex_height / 2.0) + height_offset),
													((hex_width * x) - (hex_width / 1.35), (hex_height * y) + height_offset),
													((hex_width * x) - (hex_width / 2.0), (hex_height * y) - (hex_height / 2.0) + height_offset),
													((hex_width * x) + (hex_width / 4.0), (hex_height * y) - (hex_height / 2.0) + height_offset)])
		
		# change the offset so that the next column are drawn in place
		if height_offset == 0.0:
			height_offset = hex_height / 2.0
		else:
			height_offset = 0.0
	
	# then draw the edges
	height_offset = 0.0
	for x in range(int(im_width / hex_width)+2):
		for y in range(int(im_height / hex_height)+2):
			# only need to draw the bottom and right hand side lines of each hexagon
			# bottom edge
			pygame.draw.line(image, (0, 0, 0), ((hex_width * x) - (hex_width / 2.0), (hex_height * y) + (hex_height / 2.0) + height_offset), 
											   ((hex_width * x) + (hex_width / 4.0), (hex_height * y) + (hex_height / 2.0) + height_offset), 2)
			# bottom right edge
			pygame.draw.line(image, (0, 0, 0), ((hex_width * x) + (hex_width / 4.0), (hex_height * y) + (hex_height / 2.0) + height_offset), 
											   ((hex_width * x) + (hex_width / 2.0), (hex_height * y) + height_offset), 2)
			# bottom left edge
			pygame.draw.line(image, (0, 0, 0), ((hex_width * x) + (hex_width / 2.0), (hex_height * y) + height_offset),
											   ((hex_width * x) + (hex_width / 4.0), (hex_height * y) - (hex_height / 2.0) + height_offset), 2)
		
		# change the offset so that the next column are drawn in place
		if height_offset == 0.0:
			height_offset = hex_height / 2.0
		else:
			height_offset = 0.0
	
	pygame.image.save(image, "countryside hexagonate.jpg")

if __name__ == "__main__":
	main()