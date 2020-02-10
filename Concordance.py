example_txt = "there is no god only suffering"

lst = example_txt.split()

dct = {}


for word in lst:
    if word in dct:
        dct[word] += 1
    else:
        dct[word] = 1

        
for entry in sorted(dct):
    print(entry,dct[entry])
