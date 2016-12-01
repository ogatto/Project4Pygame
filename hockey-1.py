import pygame
import random

pygame.init()

max_width = 500
max_height = 700

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

		# move puck based on key press
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
		self.rect.centerx = max_width/2
		self.rect.bottom = max_height - 55
		self.speed = [4,-4]


	def update(self):
		# update Puck x and y directions
		self.rect.left += self.speed[0]
		self.rect.top  += self.speed[1]

		# check boundary conditions
		if self.rect.left <= 0:
			self.rect.left = 0
			self.speed[0] = -self.speed[0]
		elif self.rect.left >= max_width:
			self.rect.left = max_width
			self.speed[0] = -self.speed[0]

		if self.rect.top <= 0:
			self.rect.top = 0
			self.speed[1] = -self.speed[1]
		elif self.rect.top >= max_height:
			self.rect.top = max_height
			self.speed[1] = -self.speed[1]

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

# class Hockey
class Hockey():
	def __init__(self):
		# set up the hockey rink
		self.game_display = pygame.display.set_mode((max_width, max_height))
		self.ice_rink = pygame.image.load('ice.bmp')
		self.ice_rink = pygame.transform.scale(self.ice_rink, (max_width, max_height))
		pygame.display.set_caption('AIR HOCKEY')

		# initalize paddle, puck, and net
		self.paddle = Paddle()
		self.puck = Puck()
		self.net = Net()

		# add sprites
		self.all_sprites = pygame.sprite.Group()
		self.all_sprites.add(self.paddle)
		self.all_sprites.add(self.puck)
		self.all_sprites.add(self.net)

	def run(self):
		gameExit = False
		while not gameExit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True

			self.game_display.blit(self.ice_rink, (0,0))
			#m_display.blit(block_m, (0,0))

			self.all_sprites.update()
			self.all_sprites.draw(self.game_display)

			pygame.display.flip()

if __name__ == "__main__":
    Hockey().run()
