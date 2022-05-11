import base64

file = open('ResultadosNmapSegmentoRed.txt','rb')
byte = file.read()
file.close()

decodeit = open('encoded_msg.txt','wb')
decodeit.write(base64.b64encode((byte)))
decodeit.close()