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
