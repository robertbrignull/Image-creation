import pygame
from pygame.locals import *

import random

def compare_images(working_image, target_image, rect):
	# need the bounds to make sure it doesn't go outside of them
	width, height = target_image.get_size()
	
	# now basically  compare the difference in colour
	# of every pair of pixels on the two surfaces in the desired rect
	
	# the sum of the differences
	d = 0
	
	for x in range(rect.left, rect.right):
		for y in range(rect.top, rect.bottom):
			# onlt do the comparison if it's within the picture's bounds
			if 0 <= x < width and 0 <= y < height:
				# get the colour of both pixels
				colour1 = working_image.get_at((x, y))
				colour2 = target_image.get_at((x, y))
				
				# and add on the difference squared to d
				d += abs(colour1.r - colour2.r)
				d += abs(colour1.g - colour2.g)
				d += abs(colour1.b - colour2.b)
	
	# now do the final calculation by dividing by the number of pixels times by 3
	# to get the average variation in colour
	rank = (d) / (rect.width * rect.height * 3.0)
	
	return rank

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
		# get a random colour
		colour = (random.random()*255, random.random()*255, random.random()*255)
		
		# and create a random circle
		surf = None
		size = (random.random()*30) + 1
		surf = pygame.Surface((size*2, size*2))
		pygame.draw.circle(surf, colour, (size, size), size)
		surf.set_alpha(100)
		surf.set_colorkey((0, 0, 0))
		rect = pygame.Rect((random.random()*(width + size*2)) - size, (random.random()*(height + size*2)) - size, size*2, size*2)
		
		# create a new test image
		test_image.blit(working_image, (0, 0))
		
		# and draw the rectangle onto the test image
		test_image.blit(surf, rect)
		
		# find out how far each image is from the target
		working_rank = compare_images(working_image, target_image, rect)
		test_rank = compare_images(test_image, target_image, rect)
		
		print counter, test_rank, working_rank
		
		# if the test image is closer to the target then keep it
		if test_rank < working_rank:
			working_image.blit(surf, rect)
			working_rank = test_rank
	
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