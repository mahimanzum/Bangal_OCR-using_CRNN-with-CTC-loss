import numpy as np
import random


words = []
f = open('dic.txt', 'r')
for x in f:
    s = x.replace('\n', '')
    words.append(s)
print(len(words))    
BASE = ""
def save_obj(obj,name):
    with open(BASE+name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(BASE+name + '.pkl', 'rb') as f:
        return pickle.load(f)
BCC_map = load_obj("BCC_map")
rBCC_map = load_obj("rBCC_map")

def create_mono(size = 90000):
    f = open('mono.txt', 'w')
    for i in range(size):
        out = ""
        prob = np.random.rand();
        if(prob<0.0):
            out = random.choice(words)
        else:
            for j in range(5):
                out = out + BCC_map[np.random.randint(0,len(BCC_map.keys()))]
        f.write(out+'\n')
create_mono()

def create_bi(size = 90000):
    f = open('bi.txt', 'w')
    for i in range(size):
        out1 = ""
        out1 = random.choice(words)
        out2 = ''
        for j in range(5):
            out2 = out2 + BCC_map[np.random.randint(0,len(BCC_map.keys()))]
        if(np.random.rand()<0.0):
            f.write(out1+' '+out2+'\n')
        else:
            f.write(out2+' '+out2+'\n')
create_bi()
