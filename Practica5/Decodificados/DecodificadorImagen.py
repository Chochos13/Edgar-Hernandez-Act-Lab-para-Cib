import base64

file = open('mystery_img1.txt','rb')
byte = file.read()
file.close()

decodeit = open('mystery_img1.jpg','wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()