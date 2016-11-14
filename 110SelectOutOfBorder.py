glyphs = fl.font.glyphs
fl.Unselect()
i = 0
for g in glyphs:
	if len(g.unicodes) != 0:
		#if 0x4dff < g.unicode < 0x9fa6:
		max_x = 0
		min_x = 1000
		max_y = -150
		min_y = 850
		node_list = g.nodes
		for item in node_list:
			if item.x > max_x:
				max_x = item.x
			if item.x < min_x:
				min_x = item.x	
			if item.y > max_y:
				max_y = item.y
			if item.y < min_y:
				min_y = item.y	
		if min_x < 0 or max_x > 900 or min_y < -150 or max_y > 850:
			print str(hex(g.unicode)) + ' out of border: ' + str(min_x) + " " + str(max_x) + " " + str(min_y) + " " + str(max_y)
			fl.Select(g.index)
			i = i + 1
print i

