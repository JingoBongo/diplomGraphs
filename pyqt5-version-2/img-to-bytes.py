import base64


with open("icon.png", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())
print(converted_string)

# =================

decodeit = open('newfile.png', 'wb')
decodeit.write(base64.b64decode((converted_string)))
decodeit.close()