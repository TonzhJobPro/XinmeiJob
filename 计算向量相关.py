#-*- coding: utf-8 -*-

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

	
def compare_rect(r1,r2):#比较矩形
	if r1.ll.x==r2.ll.x and r1.ur.x==r2.ur.x:
		return True
	return False

	
def lenghts(node1, node2): #返回连点之间的长度
	x = node1.x - node2.x
	y = node1.y -node2.y
	return math.sqrt(x*x+y*y)

def mid_point(node1,node2): #返回两点的中点
	return Point((node1.x+node2.x)/2.0,(node1.y+node2.y)/2.0)
		
def get_Point_intersection(line1,line2): #输入两直线，返回交点
	a1 = line1[0]
	b1 = line1[1]
	c1 = line1[2]
	a2 = line2[0]
	b2 = line2[1]
	c2 = line2[2]
	x = (b1*c2-b2*c1)/(a1*b2-a2*b1)
	y = (a1*c2-a2*c1)/(b1*a2-b2*a1)
	return Point(x,y)
		
def get_StraightLines(p,v): #输入点和向量，返回过点直线
	a = v.y
	b = -v.x
	c = v.x*p.y -p.x*v.y
	return [a,b,c]

def is_vertical(v1,v2): #判断垂直
	return True if (v1.x*v2.x+v1.y*v2.y) == 0 else False

def is_parallel(v1,v2): #判断平行
	#print v1, v2
	#print abs(math.atan((v1.y/v1.x-v2.y/v2.x)/(1+v1.y/v1.x*v2.y/v2.x)))
	if (v1.x*v2.y-v1.y*v2.x) == 0:
		return True
	elif v1.x == 0 or v2.x ==0:	
		a = math.pi/2 if v1.x == 0 else abs(math.atan(v1.y/v1.x))
		b = math.pi/2 if v2.x == 0 else abs(math.atan(v2.y/v2.x))
		if abs(a-b) < math.pi/9:
			return True
	elif (1+v1.y/v1.x*v2.y/v2.x) == 0:
		return False
	elif abs(math.atan((v1.y/v1.x-v2.y/v2.x)/(1+v1.y/v1.x*v2.y/v2.x)))<math.pi/9:
	#abs((0 if v1.y == 0 else math.atan(abs(v1.y/v1.x)))-(0 if v2.y == 0 else math.atan(abs(v2.y/v2.x)))) < math.pi/10: 
		return True
	return False

def getVector(p1,p2):
	x = p2.x -p1.x
	y = p2.y -p1.y
	return Point(x, y)	

def get_vertical_vector(v): #返回垂直向量
	return Point(v.y, -v.x)

def get_shif_points(p1,p2): #计算偏移量
	return Point(p1.x-p2.x, p1.y-p2.y)
def p_add_p(p1,p2):
	return Point(p1.x+p2.x,p1.y+p2.y)
def check_point_in_Con(p, con_p_list):
	#判断点在轮廓内， con_p_list 为轮廓点列表，表尾插入第一个点
	con_p_list.append(con_p_list[0])
	temp = 0
	#print type(p)
	px = p.x
	py = p.y
	flag = False
	for i in range(len(con_p_list)-1):
		sx = con_p_list[i+1].x
		sy = con_p_list[i+1].y
		tx = con_p_list[i].x
		ty = con_p_list[i].y
		if (py == ty and px == tx) or (py == sy and px == sx):
			return True
		if (py==ty and py ==sy and px < max(sx,tx) and px > min(sx,tx)):
			return True
		if (py > sy and py <= ty) or (py <= sy and py > ty):
			x = sx + (py - sy) * (tx - sx) / (ty - sy)
			if abs(x - px) < 1:
				return True
			if x > px:
				#print x
				flag = not flag
	return flag

def get_Dingbifen_Point(p1,p2,r): #返回定比分点，P1P=r*PP2
	x = int((r*p2.x+p1.x)/(r+1))
	y = int((r*p2.y+p1.y)/(r+1))
	return Point(x,y)

def get_x_fendian(p1,p2,x): #返回线段上过给定X的点
	y = int(((x-p2.x)*p1.y+(p1.x-x)*p2.y)/(p1.x-p2.x))
	return Point(x,y)
def get_y_fendian(p1,p2,y): #返回线段上过给定Y的点
	x = int(((y-p2.y)*p1.x+(p1.y-y)*p2.x)/(p1.y-p2.y))
	return Point(x,y)