import pickle
import random
def save_obj(obj,name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
BCC_map = load_obj("BCC_map")
rBCC_map = load_obj("rBCC_map")

val = 0
for i in BCC_map.keys():
    if(len(BCC_map[i])>5):
        #print(BCC_map[i])
        val = max(val,len(BCC_map[i]))
        for j in BCC_map[i]:
            print(j+' ', end = '')
        print(" = "+BCC_map[i])
print(val)

s= ''
actual = []
for j in range(78, 90, 1):
    n = random.randint(0, 3000)
    s = s + BCC_map[n]
    actual.append(n)
print(s)
'''
i = 0
print(BCC_map[78])
print(s[0:6])
print(BCC_map[78] == s[0:6])
for j in range(i, len(s)):
    print(i, j)
    if(s[i:j] in BCC_map):
        print(i, j, s[i:j])
'''
BCC_map = load_obj("BCC_map")
rBCC_map = load_obj("rBCC_map")
def dcd(text):
    i = 0
    j = 0
    far = 9
    out  = []
    while(i<len(text)):
        #print(i)
        j = min(i+far, len(text))
        found = True
        while(text[i:j] not in rBCC_map):
            #print('j = ', j)
            #print(text[i:j])
            #print(i, " ", j)
            j-=1
            if(j == i):
                i = i+1
                #print('comes inside, i = ', str(i))
                found = False
                break
        if found:
            out.append(rBCC_map[text[i:j]])
            i = j
        #print(out)  
    return out
#print(actual)

def encd(lst):
    s = ''
    for val in lst:
        s  = s+BCC_map[val]
    return s
st = "সংস্কৃতিসংকট"
lst = dcd(st)
print(st)
print(encd(lst))


cnt = 0
f = open('dic.txt', 'r')
for x in f:
    s = str(x)
    s = s.replace('\n', '')
    if(encd(dcd(s)) != s):
        cnt+=1
        print(s+ " turns into -> "+ encd(dcd(s)))
print(cnt)


#print(rBCC_map['অ'])
#print(rBCC_map.keys())


punc = ['া', ' ', 'ি', ' ', 'ী', ' ', 'ু', ' ', 'ূ', ' ', 'ৃ', ' ', 'ে', ' ', 'ৈ', ' ', 'ো', ' ', 'ৌ']
punc = punc[::2]
print(punc)
punc.append(' ')
for i in s:
    if(i != 'ক'):
        punc.append(i)
print(punc)
s2 = 'স্কৃ স্থা স্থি য়্যা স্থু স্বৈ ন্থ স্থ্য স্প্রি স্থী স্থূ স্থ ন্থি ন্থা গ্ল্যা গ্ল্যা র্শ্ব ন্থা য়া প্নো স্থৈ স্পৃ ষ্নু ল্লো স্প্রে স্প্যা র্দ্র ম্ভৃ ন্থী শ্লো শ্বৈ শ্রী র্ঙ্গ র্দ্ধ ষ্ক্ স্ত্ স্ত্ব স্লো র্ঙ্গ র্জ্ঞ র্তৃ র্ত্ম র্ত্রী র্দৃ র্দ্ধ র্দ্ব র্ধ্ব র্বৃ স্থে স্থৌ অ্যা ফ্যা র্ভ্র  স্মৈ দ্বৈ দ্দ্ব দ্ধৃ দ্ধ্য ত্রৈ দ্দৃ জ্যৈ ক্ষৌ ক্রৌ রো শ্রৌ অ দ্ভ্র দ্ভ্রা ষ্ন ন্ট্রি'

comp = set()
ss = s2.split(' ')
for vals in ss:
    n = vals
    for j in punc:
        n = n.replace(j, '')
    comp.add(n)
print(comp)


f = open("add_comp.txt", 'w')
for vals in comp:
    for pc in punc:
        out = vals+pc
        f.write(out+' ')
for p in punc:
    f.write(p+' ')
print(punc)

f.close()

for i in gg:
    print(i+' ', end = '')
    
    
gg = "অক্সিডাইজ়"
print(gg[9:])
     
'''
স্কৃ স্থা স্থি য়্যা স্থু স্বৈ ন্থ স্থ্য স্প্রি স্থী স্থূ স্থ ন্থি ন্থা গ্ল্যা গ্ল্যা র্শ্ব ন্থা য়া প্নো স্থৈ স্পৃ ষ্নু ল্লো স্প্রে স্প্যা র্দ্র ম্ভৃ ন্থী শ্লো শ্বৈ শ্রী র্ঙ্গ র্দ্ধ ষ্ক্ স্ত্ স্ত্ব স্লো র্ঙ্গ র্জ্ঞ র্তৃ র্ত্ম র্ত্রী র্দৃ র্দ্ধ র্দ্ব র্ধ্ব র্বৃ 
স্থে স্থৌ অ্যা ফ্যা র্ভ্র  স্মৈ দ্বৈ দ্দ্ব দ্ধৃ দ্ধ্য ত্রৈ দ্দৃ জ্যৈ ক্ষৌ ক্রৌ রো শ্রৌ অ দ্ভ্র দ্ভ্রা ষ্ন ন্ট্রি

'''
    