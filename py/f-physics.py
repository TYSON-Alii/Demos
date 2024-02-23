import pygame
from math import *
from random import *
pygame.init()
def F(x): x = x/10-20; return 10*(cos(x) - x**2/20 + 40)
def dF(x): x = x/10-20; return 10*(-sin(x)/10 - 2*x/200)
def G(x): x = x/20-15; return -100*(sin(x)/x if x != 0 else 1) + 300
def dG(x): x = x/20-15; return (-100*(cos(x)*x/20-sin(x)/20)/x**2) if x != 0 else 0
def H(x): return -(x/20-10)**2 + 300
def dH(x): return -2*(x/20-10)/20
Func = F # function
dFunc = dF # derivative the function
width, height = 500, 500
class v2:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  x, y = 0, 0
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
lines = []
g = 981.0
dt = 0.001*2
class Top:
  def __init__(self):
    pass
  x, y = 110.0, 0.0
  v = v2(0.0,0.0)
  a = v2(0.0,g)
  b = 1/3
  ka, kv = 0.97, 0.97
  def cal(self):
    fy = Func(self.x)
    θ = 0
    if self.y >= fy:
      self.y = fy
      fd = dFunc(self.x)
      θ = atan(fd)
      self.a.x *= self.ka
      self.v.x *= self.kv
      V = sqrt(self.v.x**2 + self.v.y**2)
      self.v.x += V * sin(θ) * self.b
      self.v.y -= V * cos(θ) * self.b
    self.a.x = g * sin(θ)
    self.v.x += self.a.x * dt
    self.v.y += self.a.y * dt
    self.x += self.v.x * dt
    self.y += self.v.y * dt
    pygame.draw.circle(screen, (255,34,45), (self.x, self.y), 10)
for i in range(0, width):
	lines.append((i, Func(i)))
top = Top()
while True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          top.x, top.y = event.pos[0], event.pos[1]
          top.v = v2(0.0,0.0)
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.fill((255, 255, 255))
  pygame.draw.aalines(screen, (0, 0, 233), False, lines)
  top.cal()
  pygame.display.flip()
  clock.tick(90)
