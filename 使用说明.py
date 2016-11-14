import win32api

def u2g(string):
	return string.decode('utf-8').encode('gbk')

result_str = ''

result_str = ''
result_str += (u2g('1. 选择轮廓：“Shift” + 鼠标点击轮廓内部: 选中轮廓')+ '\r\n\r\n')
result_str += (u2g('2. 复制轮廓：“c” + “shift”，选择轮廓；') + '\r\n')
result_str += (u2g('\t 点击鼠标，复制选中轮廓到点击位置') + '\r\n\r\n')
result_str += (u2g('3.轮廓对其：“a” + “shift”，选择轮廓；') + '\r\n')
result_str += (u2g('\t 然后“up”or“down”or“left”or“right”，') + '\r\n')
result_str += (u2g('\t 实现“上”or“下”or“左”or“右”,对齐') + '\r\n\r\n')
result_str += (u2g('4.均匀分布：“f” + “shift”，选择轮廓；')  + '\r\n')
result_str += (u2g('\t 然后“up”or“down”，垂直均匀分布；')  + '\r\n')
result_str += (u2g('\t “left”or“right”，水平均匀分布；') + '\r\n\r\n')
win32api.MessageBox(0, result_str, u2g('轮廓对齐使用说明'))