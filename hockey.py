import pygame
from pygame import *
from pygame.sprite import *
import random

pygame.init()

width = 500
height = 700

game_display = pygame.display.set_mode((width, height))
ice_rink = pygame.image.load('ice.bmp')
ice_rink = pygame.transform.scale(ice_rink, (width, height))

#-----ADD BLOCK M-----$
# width2 = 250
# height2 = 350

# m_display = pygame,display.set_mode((width2, height2))
# block_m = pygame.image.load('BlockM.bmp')
# block_m = pygame.transform.scale(block_m, (width2, height2))



class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 50
		self.height = 50

		self.screen = pygame.display.set_caption('AIR HOCKEY') #will need to be moved

		self.image = pygame.image.load('paddle.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.centerx = width/2
		self.rect.bottom = height - 10


	def update(self):
		keys = pygame.key.get_pressed()
		self.speed = 0

		#create response to key press
		if keys[pygame.K_LEFT]:
			self.speed -= 5
		if keys[pygame.K_RIGHT]:
			self.speed += 5	
		
		#update position of the rectangle
		self.rect.x += self.speed

		#thresholds of movement (cant go past border)
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.left < 0:
				self.rect.left = 0	

	

class Puck(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 30
		self.height = 30

		self.image = pygame.image.load('puck.bmp')
		self.image = transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.centerx = width/2
		self.rect.bottom = height - 55
		 

	def update(self):
		keys = pygame.key.get_pressed()
		#self.speed = 0
		
		if keys[pygame.K_SPACE]:
			self.speed = 4
			self.rect.left += self.speed
			self.rect.top  += -self.speed

		if self.rect.top < 0:
			self.rect.top = 0
			#self.speed = -4
			#self.rect.top -= self.speed	

		if self.rect.right > width:
			self.rect.right = width
			self.rect.right +
		if self.rect.left < 0:
			self.rect.left = 0	



			#need a way to reverse position at an angle. Also make the ball move at random angle.

	#Add code that makes the puck move when space bar is pressed
	#will function like a brick breaker game

class Net(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 80
		self.height = 80

		self.image = pygame.image.load('net.bmp')
		self.image = transform.scale(self.image, (self.width, self.height)) 

		self.rect = self.image.get_rect()
		self.rect.centerx = width/2
		self.rect.top = height - 675

	#def update(self):	
	#Add code that makes the net move back and forth and a constant rate
	#if the puck collides with net, gain score of 1
	#if the puck passes by the paddle, opponent gains a score of 1


all_sprites = pygame.sprite.Group()
#pucks = pygame.sprite.Group()
#nets = pygame.sprite.Group()

paddle = Paddle()
puck = Puck()
net = Net()

all_sprites.add(paddle)
all_sprites.add(puck)
all_sprites.add(net)

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	
	game_display.blit(ice_rink, (0,0))
	#m_display.blit(block_m, (0,0))

	all_sprites.update()
	all_sprites.draw(game_display)
	
	pygame.display.flip()
pygame.quit()
quit()
