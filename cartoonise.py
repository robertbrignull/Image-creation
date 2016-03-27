import pygame
from pygame.locals import *

def edge_detect(image):
	width, height = image.get_size()
	
	new_image = pygame.Surface((width, height))
	
	for x in range(width):
		for y in range(height):
			center_colour = image.get_at((x, y))
			
			if x < width - 1:
				right_colour = image.get_at((x + 1, y))
			else:
				right_colour = center_colour
			
			if y < height - 1:
				bottom_colour = image.get_at((x, y + 1))
			else:
				bottom_colour = center_colour
			
			center_grey = (center_colour.r * 0.2989) + (center_colour.g * 0.5870) + (center_colour.b * 0.1140)
			right_grey = (right_colour.r * 0.2989) + (right_colour.g * 0.5870) + (right_colour.b * 0.1140)
			bottom_grey = (bottom_colour.r * 0.2989) + (bottom_colour.g * 0.5870) + (bottom_colour.b * 0.1140)
			
			gradient = abs(((right_grey - center_grey) + (bottom_grey - center_grey)) / 2.0)
			
			gradient *= 5
			
			if gradient > 255:
				gradient = 255
			
			new_image.set_at((x, y), (gradient, gradient, gradient))
	
	return new_image

def main():
	##################################################################
	##                                                              ##
	##   This script cartoonises an image, I changes it to blocks   ##
	##   of colour separated with black lines.                      ##
	##   It works by first performing an edge detecting algorithm   ##
	##   on the image to produce a new image of gradients, it       ##
	##   then goes through that image and separates it into         ##
	##   sections of little change of gradient. These different     ##
	##   bits are then drawn onto a new image using the average     ##
	##   colour for that section of the image.                      ##
	##   Finally the edge detected image is drawn onto the final    ##
	##   image to provide the black lines and emphasise the many    ##
	##   different sections of the image.                           ##
	##                                                              ##
	##################################################################
	
	pygame.init()
	
	source_image = pygame.image.load("countryside.jpg")
	
	width, height = source_image.get_size()
	
	result_image = pygame.Surface((width, height))
	
	print "pre loading done"
	
	# perform the edge detection
	edged_image = edge_detect(source_image)
	
	print "edge detection done"
	
	# create a list containing a integer for each pixel
	# groups are then allocated to pixels by changing the value of their integer
	# these loops will turn 'pixels' into a 2D list
	pixels = []
	for x in range(width):
		pixels.append([])
		for y in range(height):
			pixels[x].append(-1)
	
	print "pixels list created"
	
	# go through the list once putting in zeros for pixels that will be black
	for x in range(width):
		for y in range(height):
			color = edged_image.get_at((x, y))
			if color.r > 30.0:
				pixels[x][y] = 0
	
	print "pixels list populated with zeros"
	
	# now create another list containing colors for each of the pixel groups
	groups = [(0, 0, 0)]
	
	# now draw the final image by looking at each pixel, determining its group
	# and therefore its color and then drawing it.
	for x in range(width):
		for y in range(height):
			if pixels[x][y] == -1:
				color = (255, 255, 255)
			else:
				color = groups[pixels[x][y]]
			
			result_image.set_at((x, y), color)
	
	pygame.image.save(result_image, "countryside cartoon.jpg")

if __name__ == "__main__": main()