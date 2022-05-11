import base64

print("Ingrese el path de la imagen")
link = input()

with open(link, "rb") as image2string:
	converted_string = base64.b64encode(image2string.read())
print(converted_string)

with open('ImagenCodificada.txt' , "wb") as file:
	file.write(converted_string)