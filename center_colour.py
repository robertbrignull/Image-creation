import pygame
from pygame.locals import *

import random

def main(target_name, working_name = None):
	""" works by choosing random points and drawing rectangles onto
	the working image of that colour of the target image at the center point
	"""
	
	pygame.init()
	
	# laod the image we want to get to
	target_image = pygame.image.load(target_name)
	
	width, height = target_image.get_size()
	
	# scale if it won't fit onto the screen
	if width > 1280:
		target_image = pygame.transform.scale(target_image, (1280, int(height * (1280.0 / width))))
	elif height > 800:
		target_image = pygame.transform.scale(target_image, (int(width * (800.0 / height)), 800))
	
	width, height = target_image.get_size()
	
	# if no working image is specified, make a new one
	if working_name == None:
		working_image = pygame.Surface(target_image.get_size())
		working_image.fill((0, 0, 0))
	# else load a pre-made working image
	else:
		working_image = pygame.image.load(working_name)
		working_image = pygame.transform.scale(working_image, target_image.get_size())
	
	# into the main loop
	for counter in range(100000):
		# get a random point
		posX = int(random.random()*width)
		posY = int(random.random()*height)
		
		# find out the colour at that point
		colour = target_image.get_at((posX, posY))
		
		# generate a random size for our shape
		size = random.random()*25
		
		# now create the surface
		surf = pygame.Surface((size*2, size*2))
		pygame.draw.circle(surf, colour, (size, size), size)
		surf.set_alpha(100)
		surf.set_colorkey((0, 0, 0))
		
		# now blit that surface to the working image
		working_image.blit(surf, (posX - size, posY - size))
	
	# save the resulting image
	pygame.image.save(working_image, "working image.jpg")

if __name__ == "__main__":
	target_name = raw_input("Enter a target image name: ")
	working_name = raw_input("Enter a working image name, enter 'None' to make a new image: ")
	
	if working_name == "None":
		main(target_name)
	else:
		main(target_name, working_name)