def sky(s=None):
  seed(s)
  ss = 16
  sx, sy = 3*ss, 2*ss
  im = Image.new('RGBA', (sx, sy), (0, 0, 0, 255))
  pix = im.load()
  colors = [hsv(uniform(0, 1), 1, 1) for _ in range(3) ]
  lcol = len(colors)
  lcol1 = lcol - 1
  for i in range(lcol1):
    c1 = colors[i]
    c2 = colors[i+1]
    dv = 1/(sy/lcol1)
    fac = mult(sub(c1, c2), make(dv))
    s = int(i*sy/lcol1)
    e = int((i+1)*sy/lcol1)
    for y in range(s, e):
      for x in range(sx):
        cc = c1 if randint(0,80) != 7 else blend(c1, (255,255,255), 60) 
        pix[x,y] = cast(cc) 
      c1 = sub(c1, fac) 
  return im

gif = []
for _ in range(15):
  gif.append(sky())
gif[0].save("im.gif", 'GIF', append_images=gif[1:], save_all=True, duration=400, loop=0) 
