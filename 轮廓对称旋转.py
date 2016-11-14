import math, os,sys

def get_AA_cos_sin(a1,a2):#返回向量夹角cosa,sina
	#设两个向量分别为a=（x1，y1）,b=(x2,y2)，其夹角为α，
	#因为ab=|a||b|cosα，
	#所以cosα=ab/|a||b|=（x1y1+x2,y2）/(根号（x1^2+y1^2）根号（x2^2+y1^2）)
	cosa = (a1.x*a2.x+a1.y*a2.y)/(math.sqrt(a1.x*a1.x+a1.y*a1.y)*\
	math.sqrt(a2.x*a2.x+a1.y*a1.y))
	
	sina = math.sqrt(1-cosa*cosa)
	return cosa,sina

	
def GetConBoundBox(ns1):
    min_x = ns1[0].point.x
    max_x = ns1[0].point.x
    min_y = ns1[0].point.y
    max_y = ns1[0].point.y
    for n in xrange(1,len(ns1)):
        pt = ns1[n].point
        if pt.x < min_x:
            min_x = pt.x
        if pt.x > max_x:
            max_x = pt.x
        if pt.y < min_y:
            min_y = pt.y
        if pt.y > max_y:
            max_y = pt.y
    rect = Rect(Point(min_x, min_y), Point(max_x, max_y))
    return rect

def mid_point(node1,node2): #返回两点的中点
	return Point((node1.x+node2.x)/2.0,(node1.y+node2.y)/2.0)
def getVector(p1,p2):
	x = p2.x -p1.x
	y = p2.y -p1.y
	return Point(x, y)

	
g = fl.glyph
nlist = []
for n in g.nodes:
	if n.selected != 0:
		nlist.append(n)
if 	len(nlist)>0:	
	#对称选中轮廓
	r = GetConBoundBox(nlist)
	x_mid_v = (r.ll.x+r.ur.x)/2
	point_mid = mid_point(r.ll,r.ur)
	for n in nlist:
		n.point.Assign(Point(2*x_mid_v-n.x,n.y))

	#m = Matrix(math.cos(math.pi/xit), math.sin(math.pi/xit), -math.sin(math.pi/xit), math.cos(math.pi/xit), 0, -0)
	#旋转对称轮廓
	g_new = Glyph(1,nlist)
	g_new.Shift(Point(-1*point_mid.x,-1*point_mid.y))
	a1 = getVector(point_mid,Point(r.ur.x,r.ll.y))
	a2 = getVector(point_mid,r.ur)
	cosa,sina = get_AA_cos_sin(a1,a2)
	print cosa,sina
	m = Matrix(cosa,sina,-sina,cosa,0,0)
	g_new.Transform(m)
	g_new.Shift(point_mid)

	g.DeleteSelected()
	g.Insert(g_new)
	fl.UpdateGlyph()