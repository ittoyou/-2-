#coding=utf-8
import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)#常量
CREATE_ENEMY_EVENT = pygame.USEREVENT #敌机事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1 #子弹事件常量
#爆炸销毁图片
bg1 = pygame.image.load('./images/enemy0_down1.png')
bg2 = pygame.image.load('./images/enemy0_down2.png')
bg3 = pygame.image.load('./images/enemy0_down3.png')
bg4= pygame.image.load('./images/enemy0_down4.png')

#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()

#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):#父类 大写

    def __init__(self,image,speed=1):
        super(GameSprite,self).__init__()#调用父类方法
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y +=self.speed
#背景精灵
class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		imagename = './images/background.png'
		super(BackGroundSprite,self).__init__(imagename)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super(BackGroundSprite,self).update()#调用父类
		#把移除屏幕的背景放到屏幕上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height	
class EnemySprite(GameSprite): #敌机精灵

	def __init__(self):
		imagename = './images/enemy-1.gif'

		super(EnemySprite,self).__init__(imagename)
		self.speed = random.randint(1,5)#随机速度
		max = SCREEN_RECT.width - self.rect.width#最大值 防止飞机在屏幕外
		
		self.rect.x = random.randint(0,max)
		self.rect.bottom = 0#平滑出现
		self.down_index = 0#敌机销毁图片索引
	
	def update(self):
		super(EnemySprite,self).update()
		if self.rect.top >= SCREEN_RECT.height:#销毁敌机
			#print("销毁了...")
			self.kill()

class HeroSprite(GameSprite): #英雄精灵
	def __init__(self):
		imagename ='./images/hero1.png'
		super(HeroSprite,self).__init__(imagename,0)
		#max = SCREEN_RECT.height - self.rect.bottom#防止飞机飞出屏幕外

		self.speed = 0
		self.bullet_group = pygame.sprite.Group()#创建子弹精灵组
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.height - 60

	def update(self):
		# super().update() 
		self.rect.x += self.speed  
		self.rect.y += self.speed1
			
		if self.rect.left <= 0:
			self.rect.left = 0

		if self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
	'''
	def moveUp(self):
		self.y-=20
	def moveDown(self):
		self.y+=20
	'''
	
	def fire(self):
		bullet = BulletSprite()
		bullet.rect.x = self.rect.centerx
		bullet.rect.bottom = self.rect.top 

		bullet1 = BulletSprite()
		bullet1.rect.x = self.rect.centerx-35
		bullet1.rect.bottom = self.rect.top+30 

		bullet2 = BulletSprite()
		bullet2.rect.x = self.rect.centerx+35
		bullet2.rect.bottom = self.rect.top+30 
		self.bullet_group.add(bullet1)
		self.bullet_group.add(bullet2)
		self.bullet_group.add(bullet)
		     

    

#子弹精灵
class BulletSprite(GameSprite):
    def __init__(self):
        imagename = "./images/bullet1.png"
        super(BulletSprite,self).__init__(imagename,-10)

    def update(self):
        super(BulletSprite,self).update() 
	
        
        #子弹飞出屏幕要销毁
        if self.rect.bottom <= 0:
            self.kill()                   
class Source(pygame.sprite.Sprite):
	def __init__(self):
		super(Source,self).__init__()
	def update(self):
		super(Source,self).update()
		if self.rect.bottom < 0:
			self.kill()
