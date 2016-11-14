gs0 = fl[0].glyphs
gs1 = fl[1].glyphs
for g in gs0:
	if len(g.unicodes) != 0 and g.unicode >= 0x4e00:
		glyph1_index = fl[1].FindGlyph(g.unicode)
		if glyph1_index != -1:
			g.mask = Glyph(gs1[glyph1_index])
fl.UpdateFont(1)