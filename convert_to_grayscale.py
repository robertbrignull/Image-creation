import pygame
from pygame.locals import *

def main():
	pygame.init()
	
	image = pygame.image.load("man.jpg")
	
	width, height = image.get_size()
	
	for x in range(width):
		for y in range(height):
			colour = image.get_at((x, y))
			
			grey = ((colour.r * 0.2989) + (colour.g * 0.5870) + (colour.b * 0.1140)) / (0.2989 + 0.5870 + 0.1140)
			
			image.set_at((x, y), (grey, grey, grey))
	
	pygame.image.save(image, "man greyscale.jpg")

if __name__ == "__main__":
	main()