# Remi Trettin

# function to split input into 4-byte blocks
def chunks(l, n):
	n = max(1, n)
	return (l[i:i+n] for i in xrange(0, len(l), n))

# hash function
def hash(input):
	inputHex = ':'.join(x.encode('hex') for x in input) #convert input into hex bytes
	hexList = inputHex.split(":")
	length = len(hexList)

	# check if input bytes is multiple of 4
	if(length % 4 != 0):
		offset = 4 - (length % 4)
		counter = 0
		while(counter < offset):
			hexList.append('30')
			counter = counter + 1
	# split into chunks
	obj = chunks(hexList, 4)
	obj = list(obj)
	counter = 0
	while(counter < len(obj)):
		obj[counter][0] = "0x" + obj[counter][0]
		obj[counter][1] = "0x" + obj[counter][1]
		obj[counter][2] = "0x" + obj[counter][2]
		obj[counter][3] = "0x" + obj[counter][3]
		counter += 1

	outputList = []
	outer = 0
	inner = 0
	while(inner < 4):
		while(True):
			r = hex(int(obj[outer][inner], 16) ^ int(obj[outer+1][inner], 16) ^ int(obj[outer+2][inner], 16))
			outputList.append(r)
			outer = 0
			break
		inner += 1

	output = ""
	for i in outputList:
		i = hex(int(i, 16)).split('x')[1]
		output += i

	return output

val = hash("abcdefghijklmnopqrstuvwxyz")
print val
