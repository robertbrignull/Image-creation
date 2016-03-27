import pygame
from pygame.locals import *

import math

def main(image_name, x, y):
	pygame.init()
	
	# the original image that will be blurred
	old_image = pygame.image.load(image_name)
	
	# the size of the original and final image
	width, height = old_image.get_size()
	
	# the final image, will have many
	new_image = pygame.Surface((width, height))
	
	# how many blurs to do
	max_blurs = 50
	
	for i in range(max_blurs):
		# each blur will be larger and less opaque than the last
		# only one point on all of the images will line up, the point (x, y)
		
		# the scale of the image that will be blitted
		scale = 1.0 + ((i * 1.0) / max_blurs)
		
		# scale the image, on a scale from the first blur at 1.0 to the last blur near 2.0
		surf = pygame.transform.scale(old_image, (width * scale, height * scale))
		
		# make the image semi-opaque, on a scale from the first blur at 100% to the last blur near 0%
		surf.set_alpha(255.0 * ((max_blurs - i) / (max_blurs * 1.0)))
		
		# these are the offsets for when blitting the images
		# this makes the point indicated by the player match up on all the images
		offset_x = x - (x * scale)
		offset_y = y - (y * scale)
		
		new_image.blit(surf, (offset_x, offset_y))
	
	image_name = image_name.split(".")
	save_name = image_name[0] + " blurred." + image_name[1]
	
	pygame.image.save(new_image, save_name)

if __name__ == "__main__":
	image_name = raw_input("Enter the name of an image to blur: ")
	
	point = raw_input("Enter the point to blur from, format 'x, y': ")
	point = point.split(", ")
	
	x = int(point[0])
	y = int(point[1])
	
	main(image_name, x, y)