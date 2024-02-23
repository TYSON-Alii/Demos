from PIL import Image
from colorsys import hsv_to_rgb
from random import *
import time
def limit(c, mx=1, stop=False):
  if c < 0:
    return 0 if stop else limit(c+mx)
  elif c > mx:
    return mx if stop else limit(c-mx)
  return c
def hsv(h, s, v):
  c = hsv_to_rgb(h, s, v)
  return (int(c[0]*255), int(c[1]*255), int(c[2]*255), 255)
uf = uniform
rint = randint
def fallin_star(yem=None):
  seed(yem)
  w = rint(30,50)
  im = Image.new('RGBA', (6,w), (0, 0, 0, 0))
  pix = im.load()
  mcol = uf(0,1)
  cols = [limit(mcol+i/12) for i in range(3)]
  seed()
  for x in range(6):
    for y in range(w):
      prob = 1 - (y/w)**2 - abs(3-x)*y/(3*w)
      col = (0,0,0,0)
      if rint(0,100) < prob*100:
        c = int(y/w*len(cols))
        ch = c+choice([-1,0,0,1])
        ch = limit(ch, len(cols)-1, True)
        col = hsv(cols[ch], 1, 1) 
      pix[x,y] = col
  pix[5,0] = pix[0,0] = (0,0,0,0)
  for x in [2,3]:
    for y in [1,2]:
      pix[x,y] = (255,255,255,255)
  return im

while True:
  yem = random()
  for _ in range(1,20):
    im = fallin_star(yem)
    im.save("im.png")
    time.sleep(0.1)
