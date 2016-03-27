import pygame
from pygame.locals import *

def main(image_name):
	pygame.init()
	
	image = pygame.image.load(image_name)
	
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
	
	image_name = image_name.split(".")
	save_name = image_name[0] + " edge detected." + image_name[1]
	
	pygame.image.save(new_image, save_name)

if __name__ == "__main__":
	image_name = raw_input("Enter the name of an image: ")
	
	main(image_name)