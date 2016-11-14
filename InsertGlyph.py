glyphs0 = fl.font.glyphs
g0 = Glyph(glyphs0[22512])
for g in glyphs0:
	if len(g.unicodes) != 0:
		for i in range(len(g.unicodes)):
			if 0x4dff < g.unicodes[i] < 0xa000:
				r0 = g.GetBoundingRect()
				width0 = r0.width
				if width0 < 1000:
					g.Insert(g0.nodes)
fl.UpdateFont()