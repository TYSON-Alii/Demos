import pygame
import math, random

pygame.init()

width, height = 500, 500
class v2:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  x, y = 0, 0
class Circle:
  def __init__(self, cen):
    self.center = cen
    self.l = float(random.randint(20, 85))
    self.r = 0
    self.w = random.uniform(-0.5, 0.5)
    self.pos = v2(0, 0)
  center = None
  l = 0
  r = 0
  w = 0
  pos = v2(0, 0)
  def cal(self):
    self.pos.x = self.center.x + self.l * math.cos(self.r)
    self.pos.y = self.center.y + self.l * math.sin(self.r)
    self.r += self.w
    pygame.draw.circle(screen, (0, 0, 255), (self.pos.x, self.pos.y), 5)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
lines = []
base_c = Circle(v2(250,250)) 
circles = [base_c]
for i in range(1):
  circles.append(Circle(circles[-1].pos))
last_c = circles[-1]
while True:
  screen.fill((255, 255, 255))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.fill((255, 255, 255))
  if len(lines) > 2:
    pygame.draw.aalines(screen, (255, 0, 0), False, lines)
  for c in circles:
    c.cal()
  lines.append((last_c.pos.x,last_c.pos.y))
  pygame.display.flip()
  clock.tick(30) 
