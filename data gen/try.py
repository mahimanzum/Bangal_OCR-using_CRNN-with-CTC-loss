
import cv2
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps 
fonts = ImageFont.truetype('SutonnyOMJ.ttf',20, layout_engine=ImageFont.LAYOUT_RAQM)
char = 'দৃষ্টিভঙ্গি '
idx = 3
f = open("BCC_out.txt", "r")
char2 = ""
c = 0
print_list = []
for x in f:
	c+=1
	comb = x
	comb = comb.replace('\n', '')
	char2 += str(comb)
	print_list.append(comb)
	#print(char2)
	if(c == 5):
		break
char2 =  print_list[idx]
print(char2)
im = Image.new("RGB",(1000, 1600))
im2 = Image.new("RGB",(1000, 1600))
draw = ImageDraw.Draw(im)
draw.text((10, 10), char2, font=fonts)
#im.show()
#im.save('new_name.png')
inverted_image = PIL.ImageOps.invert(im)
name = 'new_name.png'
inverted_image.save(name)

img = cv2.imread(name,cv2.IMREAD_COLOR)
print(img.shape)
x = 8
y = 8
w = 0
h = 0
draw_txt = ImageDraw.Draw(im2)
width, height = fonts.getsize(print_list[idx])
#width, height = draw_txt.textsize(print_list[i], font=fonts)
cv2.rectangle(img, (x,y), (x+width,y+height+2), (200, 0,255), 1)	
x = x+width
#y = y+height
print(width, height)

#cv2.imshow('image',img)
cv2.imwrite(name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

