import base64

file = open('encoded_msg.b64','rb')
byte = file.read()
file.close()

decodeit = open('encoded_msg.txt','wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()