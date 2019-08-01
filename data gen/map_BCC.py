import pickle
import random
def save_obj(obj,name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

f = open("BCC_out.txt", "r")
print_list = []
st = set()
for x in f:
    s = x.replace('\n', '')
    s = s.strip()
    if(s not in st):
        st.add(s)
        print_list.append(s)

print(len(print_list))
f.close()
BCC_map = {}
rBCC_map = {}
for i in range(len(print_list)):
    BCC_map[i] = print_list[i]
    rBCC_map[print_list[i]] = i
BCC_map[len(st)] = ' '
rBCC_map[' '] = len(st)
save_obj(BCC_map, "BCC_map")
BCC_map = load_obj("BCC_map")

save_obj(rBCC_map, "rBCC_map")
rBCC_map = load_obj("rBCC_map")

def gen_input(sz = 50000,ln=10):
    f = open("BCC_in.txt", "w")
    for i in range(sz):
        s = ""
        for j in range(ln):
            n = np.random.rand()
            if(n<0.8 or j == 0):
                s = s+random.choice(print_list)
            else:
                s = s+' '
        print(len(s))
        f.write(s+'\n')
    f.close()
gen_input(10, 5)

rd = ""
for j in range(5):
    rd = rd + random.choice(print_list)
for i in rd:
    print(i)

import cv2
def paint_text(text, w, h, rotate=False, ud=False, multi_fonts=False):
    
img = paint_text(rd, w = 128, h = 64)


from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps 
fonts = ImageFont.truetype('SutonnyOMJ.ttf',20, layout_engine=ImageFont.LAYOUT_RAQM)
im = Image.new("RGB",(1000, 1600))
draw = ImageDraw.Draw(im)
draw.text((10, 10),rd, font=fonts)
inverted_image = PIL.ImageOps.invert(im)
name = 'new_name.png'
inverted_image.save(name)

inverted_image = inverted_image.convert('RGB') 
open_cv_image = np.array(inverted_image) 
# Convert RGB to BGR 
open_cv_image = open_cv_image[:, :, ::-1].copy()
print(open_cv_image.shape)






print(BCC_map[2058])














