from __future__ import print_function

a = "5D>>DFB@FD;DDBB5D>>DFB@FD;DDBB5D>>DFB@FD;DDBB5D>>DFB@FD;DDBB5D>>DFB@FD;DDBB5D>>DFB@FD;DDBB5D>>DFB@FD;DDBB5D>>DFB@FD;D"
num = []
for i in range(len(a)):
	num.append(ord(a[i])-ord('>'))

print(num)
