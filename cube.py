import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite



class Cube(Sprite):
	
	
	def __init__(self, x, y):
		# инициализация кубов
		Sprite.__init__(self)
		
		#Куб
		self.image = pygame.image.load(Path('images','level1_image','cube_forest.png'))
		self.rect = pygame.Rect(x, y, 73, 73)

	
	# Изменения картинки куба для уровня пещера
	def change_cube_cave(self):
		self.image = pygame.image.load(Path('images','level2','cube_cave.png'))