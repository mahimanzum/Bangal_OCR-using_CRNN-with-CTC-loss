from PIL import Image, ImageDraw, ImageFont
#print(ImageFont)
#fonts = ImageFont.truetype('pubg_font.ttf',50)
#fonts = ImageFont.truetype('SutonnyMJ.ttf',50)
fonts = ImageFont.truetype('SutonnyOMJ.ttf',50, layout_engine=ImageFont.LAYOUT_RAQM)
#/home/mahim/Downloads/SutonnyMJ/SutonnyOMJ.ttf
#fonts = 'SutonnyMJ.ttf'
#print(char)
char = 'দৃষ্টিভঙ্গি '
#char = "HELLO"
print(char)
#char = char.encode('utf-8').decode('utf-8')
#char = "hello world"
print(char)
im = Image.new("RGB",(400, 200))
draw = ImageDraw.Draw(im)

draw.text((10, 90), char, font=fonts)
im.show()
'''
from PIL import Image, ImageDraw
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import glob
import os

font_size = 75
font_paths = sorted(glob.glob('*.ttf'))
print(font_paths)
text = "ইনপুট সরঞ্জামগুলি ব্যবহার করে দেখুন"
print(text)
text = text.encode('utf-8').decode('utf-8')
print(text)
background_color = 180
text_color = 50
color_variance = 60
cv2.namedWindow('display', 0)

for font_path in font_paths:

    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = font.getsize(text)

    ascent, descent = font.getmetrics()
    (width, baseline), (offset_x, offset_y) = font.font.getsize(text)

    # +100 added to see that text gets cut off
    PIL_image = Image.new('RGB', (text_width-offset_x+100, text_height-offset_y), color=0x888888)
    draw = ImageDraw.Draw(PIL_image)
    draw.text((-offset_x, -offset_y), text, font=font, fill=0)

    cv2.imshow('display', np.array(PIL_image))
    k = cv2.waitKey()
    if chr(k & 255) == 'q':
        break

'''


'''

import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
img = np.zeros((200,400,3),np.uint8)
b,g,r,a = 0,255,0,0

## Use cv2.FONT_HERSHEY_XXX to write English.
text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime()) 
cv2.putText(img,  text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b,g,r), 1, cv2.LINE_AA)


## Use simsum.ttc to write Chinese.
fontpath = "kalpurush ANSI.ttf" # <== 这里是宋体路径 
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 80),  "দৃষ্টিভঙ্গি", font = font, fill = (b, g, r, a))
img = np.array(img_pil)

cv2.putText(img,  "--- by Silencer", (200,150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (b,g,r), 1, cv2.LINE_AA)


## Display 
cv2.imshow("res", img);cv2.waitKey();cv2.destroyAllWindows()
'''
