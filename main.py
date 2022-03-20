import pygame

pygame.init() 
screen = pygame.display.set_mode((900,300))
pygame.display.set_caption("Momentum")

class cube:
	def __init__(self,colour,width,x,y,mass,vel):
		self.colour = colour;
		self.width = width;
		self.x = x;
		self.y = y;
		self.mass = mass;
		self.vel = vel;
		self.clack = pygame.mixer.Sound('clack.wav');		#must have a clack.wav in your code folder; 
		self.clack.set_volume(0.1)
		self.count = 0;

	def drawcube(self):
		pygame.draw.rect(screen, self.colour, (self.x,self.y, self.width,self.width));

	def move(self):	
		self.x += self.vel;		

	def collide(self, other):
		if not(self.x + self.width < other.x or self.x> other.x + other.width):
			pygame.mixer.Sound.play(self.clack);
			self.count += 0.5;
			print(int(self.count));			
			initv1 = self.vel;
			initv2 = other.vel;
			self.vel = ( ((self.mass - other.mass) / (self.mass + other.mass))*initv1 + ((2*other.mass)/ (self.mass + other.mass))*initv2);		#equation of conserveing momentum for both cubes applied.
			other.vel = ( ( (2*self.mass) / (self.mass + other.mass) )*initv1 + ((other.mass - self.mass)/(self.mass + other.mass))* initv2);			

	def wall(self):
		if self.x < 100:					# In a perfect elastic collision with the wall, the velocity of
			self.vel = self.vel * -1;			# the cube would simply be reversed since the wall will not
			pygame.mixer.Sound.play(self.clack);		# gain any velocity.
			self.count+=1;
			print(int(self.count));




big_cube =   cube((0,200,160), 70, 500, 200, 1,-0.08);			# Change the 5th parameter to change the mass of the big cube.
small_cube = cube((0,160,200), 40, 250, 230, 1,0);			# To get the digits of pi, the mass of the cube should a power of 100
running = True;								#i.e 100^0 = 1; 100^1 = 100; 100^2 = 10000 etc.
									#The power +1 == digits of pi you get
while running:				#running loop of game

	for event in pygame.event.get():
		if event.type == pygame.QUIT:		#being able to close the game
			running = False;


	screen.fill((0,0,0));
	pygame.draw.rect(screen, (255,255,255), (95,0,5,270));
	pygame.draw.rect(screen, (255,255,255), (95,270,900,5));
	big_cube.drawcube();
	big_cube.move();
	small_cube.drawcube();
	small_cube.move();
	small_cube.collide(big_cube);
	big_cube.collide(small_cube);
	small_cube.collide(big_cube);
	small_cube.wall();
	pygame.display.update();



pygame.quit();
