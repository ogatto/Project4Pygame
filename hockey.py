import pygame
from pygame import *
from pygame.sprite import *
import random

pygame.init()

width = 513
height = 700

game_display = pygame.display.set_mode((width, height))
ice_rink = pygame.image.load('ice.bmp')
ice_rink = pygame.transform.scale(ice_rink, (width, height))

#puck
puck_diameter = 18
puck_radius = int(puck_diameter / 2)
max_puck_x = width - puck_diameter
max_puck_y = height - puck_diameter

class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 80
		self.height = 80

		self.image = pygame.image.load('paddle.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.centerx = width/2
		self.rect.bottom = height - 10

		self.live = 5
		self.score = 0	

	def update(self):
		keys = pygame.key.get_pressed()
		self.speed = 0

		if keys[pygame.K_LEFT]:
			self.speed -= 5
		if keys[pygame.K_RIGHT]:
			self.speed += 5	
		self.rect.x += self.speed
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.left < 0:
				self.rect.left = 0	


sprites_list = pygame.sprite.Group()			
paddle = Paddle()
sprites_list.add(paddle)

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	
	game_display.blit(ice_rink, (0,0))
	sprites_list.update()
	sprites_list.draw(game_display)
	
	pygame.display.flip()
pygame.quit()
quit()
