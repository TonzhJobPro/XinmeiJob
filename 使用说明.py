import win32api

def u2g(string):
	return string.decode('utf-8').encode('gbk')

result_str = ''

result_str = ''
result_str += (u2g('1. ѡ����������Shift�� + ����������ڲ�: ѡ������')+ '\r\n\r\n')
result_str += (u2g('2. ������������c�� + ��shift����ѡ��������') + '\r\n')
result_str += (u2g('\t �����꣬����ѡ�����������λ��') + '\r\n\r\n')
result_str += (u2g('3.�������䣺��a�� + ��shift����ѡ��������') + '\r\n')
result_str += (u2g('\t Ȼ��up��or��down��or��left��or��right����') + '\r\n')
result_str += (u2g('\t ʵ�֡��ϡ�or���¡�or����or���ҡ�,����') + '\r\n\r\n')
result_str += (u2g('4.���ȷֲ�����f�� + ��shift����ѡ��������')  + '\r\n')
result_str += (u2g('\t Ȼ��up��or��down������ֱ���ȷֲ���')  + '\r\n')
result_str += (u2g('\t ��left��or��right����ˮƽ���ȷֲ���') + '\r\n\r\n')
win32api.MessageBox(0, result_str, u2g('��������ʹ��˵��'))