import pygame
from pygame.locals import *

import random

def main(target_name, working_name, save_name, iterations):
	pygame.init()
	
	# laod the image we want to get to
	target_image = pygame.image.load(target_name)
	
	# and find out what size it is
	width, height = target_image.get_size()
	
	# if no working image is specified, make a new one
	if working_name == None:
		working_image = pygame.Surface(target_image.get_size())
		working_image.fill((0, 0, 0))
	# else load a pre-made working image
	else:
		working_image = pygame.image.load(working_name)
		working_image = pygame.transform.scale(working_image, target_image.get_size())
	
	# and create a new blank test_image the same size as the target
	test_image = pygame.Surface(target_image.get_size())
	
	# into the main loop
	for counter in range(iterations):
		# get a random point
		posX = int(random.random()*width)
		posY = int(random.random()*height)
		
		# find out the colour at that point on both images
		target_colour = target_image.get_at((posX, posY))
		working_colour = target_image.get_at((posX, posY))
		
		# create a new colour that is between the two
		test_colour = ((random.random()*(target_colour.r - working_colour.r)) + working_colour.r,
					   (random.random()*(target_colour.g - working_colour.g)) + working_colour.g,
					   (random.random()*(target_colour.b - working_colour.b)) + working_colour.b)
		
		# generate a random size for our shape
		size = random.random()*25
		
		# now create the surface
		surf = pygame.Surface((size*2, size*2))
		pygame.draw.circle(surf, test_colour, (size, size), size)
		surf.set_alpha(100)
		surf.set_colorkey((0, 0, 0))
		
		# now blit that surface to the working image
		working_image.blit(surf, (posX - size, posY - size))
	
	# save the resulting image
	pygame.image.save(working_image, save_name)

if __name__ == "__main__":
	target_name = raw_input("Enter a target image name: ")
	working_name = raw_input("Enter a working image name, enter 'None' to make a new image: ")
	save_name = raw_input("Enter where the output should be save to: ")
	iterations = int(raw_input("Enter how many iterations to do: "))
	
	if working_name == "None":
		working_name = None
	
	main(target_name, working_name, save_name, iterations)