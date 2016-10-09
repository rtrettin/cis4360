# Remi Trettin
# This loops through all possible key values and decrypts the file
# with each key. The correct key is from the output file named
# count153.dat and 153 in hexadecimal is 99.

from subprocess import call

count = 0
while(count <= 255):
	h = hex(count).split('x')[1]
	s = h + "7e151628aed2a6abf7158809cf4f3c"
	if(count < 16):
		s = "0" + s
	call(["openssl", "enc", "-d", "-aes-128-ecb", "-in", "AESencrypt_view", "-out", "count"+str(count)+".dat", "-K", s])
	count = count + 1
