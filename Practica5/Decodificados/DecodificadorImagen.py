import base64

def decodificadorimg(link):
	file = open(link,'rb')
	byte = file.read()
	file.close()

	decodeit = open(link,'wb')
	decodeit.write(base64.b64decode((byte)))
	decodeit.close()