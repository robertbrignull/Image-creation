import pygame
from pygame.locals import *

def blur(old_image, (x, y)):
	# the size of the original and final image
	width, height = old_image.get_size()
	
	# the final image, will have many
	new_image = pygame.Surface((width, height))
	
	# how many blurs to do
	max_blurs = 4
	
	for i in range(max_blurs):
		# each blur will be larger and less opaque than the last
		# only one point on all of the images will line up, the point (x, y)
		
		# the scale of the image that will be blitted
		scale = 1.0 + ((i * 0.2) / max_blurs)
		
		# scale the image, on a scale from the first blur at 1.0 to the last blur nearer 1.2
		surf = pygame.transform.scale(old_image, (width * scale, height * scale))
		
		# make the image semi-opaque, on a scale from the first blur at 100% to the last blur near 0%
		surf.set_alpha(255.0 * ((max_blurs - i) / (max_blurs * 1.0)))
		
		# these are the offsets for when blitting the images
		# this makes the point indicated by the player match up on all the images
		offset_x = x - (x * scale)
		offset_y = y - (y * scale)
		
		new_image.blit(surf, (offset_x, offset_y))
	
	return new_image

def main(image_name):
	pygame.init()
	
	old_image = pygame.image.load(image_name)
	
	window = pygame.display.set_mode((1280, 800), FULLSCREEN)
	
	running = 1
	while running:
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				running = 0
		
		x, y = pygame.mouse.get_pos()
		
		new_image = blur(old_image, (x, y))
		
		window.blit(new_image, (0, 0))
		
		pygame.display.update()

if __name__ == "__main__":
	#image_name = raw_input("Enter the name of an image to blur: ")
	image_name = "countryside small.jpg"
	main(image_name)