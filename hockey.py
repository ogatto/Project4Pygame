import pygame
from pygame import *
from pygame.sprite import *
from pygame.mixer import *
import random

pygame.init()
print("Author: Owen Gatto")
pygame.mixer.music.load('nhl_organ.wav')
pygame.mixer.music.play(loops =-1)

max_width = 500
max_height = 700

game_display = pygame.display.set_mode((max_width, max_height))
ice_rink = pygame.image.load('ice.bmp')
ice_rink = pygame.transform.scale(ice_rink, (max_width, max_height))
pygame.display.set_caption('AIR HOCKEY')


class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 50
		self.height = 50

		self.image = pygame.image.load('paddle.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.centerx = max_width/2
		self.rect.bottom = max_height - 10


	def update(self):
		keys = pygame.key.get_pressed()

		# move paddle based on key press
		if keys[pygame.K_LEFT]:
			self.rect.x -= 5
		if keys[pygame.K_RIGHT]:
			self.rect.x += 5

		# check boundary condition
		if self.rect.right > max_width:
			self.rect.right = max_width
		if self.rect.left < 0:
			self.rect.left = 0


class Puck(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 30
		self.height = 30

		self.image = pygame.image.load('puck.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.center = (max_width/2, max_height - 55)
		self.direction = [4,-4]



	def update(self):
		# update Puck x and y directions
		left, top = self.rect.center
		left += self.direction[0]
		top += self.direction[1]

		# check boundary conditions
		if left <= 0:
			left = 0
			self.direction[0] = -self.direction[0]
		elif left >= max_width:
			left = max_width
			self.direction[0] = -self.direction[0]

		if top <= max_height-620:
			top = max_height-620
			self.direction[1] = -self.direction[1]		

		elif top >= max_height:
			top = max_height
			self.direction[1] = -self.direction[1]	

		self.rect.center = left, top

	def changedirection(self):
		bottom = self.rect.center[1]
		if bottom >= max_height - 55:
			self.direction[1] = -self.direction[1]


class Net(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 80
		self.height = 80

		self.image = pygame.image.load('net.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.centerx = max_width/2
		self.rect.top = max_height - 675

		self.speed = 5
		self.score = 0
		
		self.state = 0

		self.collidedetect = False

	def update(self):
		# update Net position
		self.rect.x += self.speed

		# check boundary conditions
		if self.rect.right > max_width:
			self.rect.right = max_width
			self.speed = -self.speed

		elif self.rect.left < 0:
			self.rect.left = 0
			self.speed = -self.speed

	def detect_score(self):
		self.score += 1
		if self.score >= 50:
			self.score = 50
			self.state = 1	
			
all_sprites = pygame.sprite.Group()

paddle = Paddle()
puck = Puck()
net = Net()

paddle.add(all_sprites)
puck.add(all_sprites)
net.add(all_sprites)



gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	
	#put rink in background
	game_display.blit(ice_rink, (0,0))
	
	#update all sprites and draw on screen
	all_sprites.update()
	all_sprites.draw(game_display)

	#display score
	if net.state == 0:
		default_font = pygame.font.get_default_font()
		font = pygame.font.Font(default_font, 50)
		msg = font.render("Score  "+str(net.score), True, (0,0,0))
		game_display.blit(msg, (125,350))

	#display message
	if net.state == 1:
		default_font = pygame.font.get_default_font()
		font = pygame.font.Font(default_font, 50)
		msg = font.render("Congratulations!", True, (0,0,0))
		msg_2 = font.render("You Won!", True, (0,0,0))
		msg_3 = font.render("Score  "+str(net.score), True, (0,0,0))
		game_display.blit(msg_3, (125,350))
		game_display.blit(msg, (45, 200))
		game_display.blit(msg_2, (125,500))



	#if paddle and puck collide, change direction
	if pygame.Rect.colliderect(paddle.rect, puck.rect):
		puck.changedirection()

		
	#if puck and net collide, detect the score.		
	if pygame.Rect.colliderect(puck.rect, net.rect) and net.collidedetect == False:
		net.detect_score()
		net.collidedetect = True

	if puck.rect.center[1] >= 100:
		net.collidedetect = False
			
	

	pygame.display.flip()
pygame.quit()
quit()


