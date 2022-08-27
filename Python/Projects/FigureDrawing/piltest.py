from PIL import Image


img = Image.open("C:\\Users\\jason\\Desktop\\Art\\Art Ref\\sample pack new\\DSC06393.jpg")

new_height = 1000
new_width = new_height / img.height * img.width
new_size = img.resize((int(new_width), int(new_height)))
print(new_size)
img.show()