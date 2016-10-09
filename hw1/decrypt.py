# Remi Trettin
# This loops through the 5 files to decrypt using the openssl utility

from subprocess import call

prefix = "AESencrypt_"
output = "AESdecrypt_"
key = "2b7e151628aed2a6abf7158809cf4f3c"
count = 1
while(count <= 5):
	call(["openssl", "enc", "-d", "-aes-128-ecb", "-in", prefix+str(count), "-out", output+str(count), "-K", key])
	count = count + 1
