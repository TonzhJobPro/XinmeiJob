for g in fl.font.glyphs:
	if len(g.unicodes)>0 and (g.unicode<0x3000 or g.unicode > 0xa000):
		continue
	for i in range(g.GetContoursNumber()):
		if g.isContourClockwise(i) == 0:
			g.ReverseContour(i)
fl.UpdateFont()