#!/usr/bin/env python
#Simple program to turn zip files into images and images into zip files
#Written by Koppany Horvath, c 2017
#Under the MIT license, do whatever you want, but I'm not liable for anything
import pygame, math, sys
from pygame.locals import *

fimg = sys.argv[1]
to = sys.argv[2]

if to == "zip":
	img = pygame.image.load(fimg)
	w,h = img.get_size()
	d = ""

	for y in xrange(h):
		for x in xrange(w):
			c = img.get_at((x,y))
			for z in xrange(3): d += chr(c[z])

	f = open(fimg+".zip","wb")
	f.write(d)
	f.close()
else:
	f = open(fimg,"rb")
	img = f.read()
	f.close()
	c = 0

	def getByte():
		global c, img
		if c < len(img):
			t = ord(img[c])
			c += 1
			return t
		else: return 0

	s = int(math.sqrt(len(img)/3.0)+1)

	surf = pygame.Surface((s,s))

	for y in xrange(s):
		for x in xrange(s):
			p = [0,0,0]
			for z in xrange(3): p[z] = getByte()
			surf.set_at((x,y),p)

	pygame.image.save(surf,fimg+"."+to)