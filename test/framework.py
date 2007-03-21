from Tkconstants import *
from random      import randint, seed, choice
import Tkinter, os
import canvasvg
import thread

D = 400
def coord():
	return randint(0, D)

def random_color():
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	return "#%02x%02x%02x" % (r, g, b)

def test(canv, name, pretty=False):
	doc = canvasvg.SVGdocument()
	for element in canvasvg.convert(doc, canv):
		doc.documentElement.appendChild(element)

	doc.documentElement.setAttribute('width',  str(D))
	doc.documentElement.setAttribute('height', str(D))

	f = open(name + '.svg', 'w')
	if pretty:
		f.write(doc.toprettyxml())
	else:
		f.write(doc.toxml())
	f.close()
	os.system("inkview %s.svg" % name)
	raise SystemExit


root = Tkinter.Tk()
canv = Tkinter.Canvas(width=D, height=D, bg="#ffffff")
canv.pack()

seed(100)
