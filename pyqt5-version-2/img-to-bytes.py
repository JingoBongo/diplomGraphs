import base64

def pngtostring(filename):
    with open(filename, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    print(converted_string)
    return converted_string

# =================
def stringtopng(converted_string):
    # decodeit = open('newfile.png', 'wb')
    # decodeit.write(base64.b64decode((converted_string)))
    # decodeit.close()
    return base64.b64decode((converted_string))
pngtostring('icon.png')
pngtostring('exit.png')