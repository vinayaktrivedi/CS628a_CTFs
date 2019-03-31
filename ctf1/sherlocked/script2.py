key = [84,36,119,16,121,108,164,142]
flag = list("37574122410ddfef6d154075495b91b964154f76485b90be651c42234f54c5b9631442224f5ec1f3")
j=0
i = 0
string = ""
while(i<(len(flag))):
	a = flag[i]
	b = flag[i+1]
	i = i+2
	c = a+b
	x = int(c,16)
	string += chr(key[j%8]^x)
	j = j+1

print(string)