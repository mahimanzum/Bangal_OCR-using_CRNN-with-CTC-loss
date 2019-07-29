f = open("BCC.txt", "r")
lst = []
st = set()
for x in f:
		
	s = x
	s = s.split(" ")
	for comp in s:
		if(comp != '\n' or comp != ' ' or comp != ''):
			lst.append(comp)
			st.add(comp)
			
print(len(lst))
with open('BCC_out.txt', 'w') as f:
	for item in st:
		it = item
		it = it.replace(" ","")
		it = it.replace("\n","")
		f.write("%s\n" % it)
