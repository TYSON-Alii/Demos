from PIL import Image
from math import *
import os, time, random
from colorsys import hsv_to_rgb
rint = random.randint
sz = 50
grid = [[False for _ in range(sz)] for _ in range(sz)]
def print_grid(g):
  for x in range(sz):
    for y in range(sz):
      print(g[y][x], end=' ')
    print()
def count_ne(x, y, g, r):
  count = 0
  for i in range(x-r, x+r+1):
    for j in range(y-r, y+r+1) :
      if i >= 0 and i < sz and j >= 0 and j < sz and g[j][i] is True:
        count += 1
  if g[y][x] is True:
    count -= 1
  return count
def put_cell(x, y):
  global grid
  if x >= 0 and x < sz and y >= 0 and y < sz:
    grid[y][x] = True
def put_ship(x, y):
  put_cell(x, y)
  put_cell(x+1, y+1)
  put_cell(x+2, y+1)
  put_cell(x+2, y)
  put_cell(x+2, y-1)
put_ship(10,10)
gif = []
frame = 40
for i in range(frame):
  im = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
  pix = im.load() 
  cgrid = [row[:] for row in grid]
  for x in range(sz):
    for y in range(sz):
      g = cgrid[y][x]
      c = count_ne(x, y, cgrid, 1)
      if g is True:
        if c not in [2,3]:
          grid[y][x] = False
      elif c in [3]:
          grid[y][x] = True
      pix[x,y] = (0, 0, 0) if grid[y][x] is False else (255, 255, 255)
  gif.append(im)
gif[0].save('out.gif', save_all=True, append_images=gif[1:], optimize=False, duration=100, loop=0) 
