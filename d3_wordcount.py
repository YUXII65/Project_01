text="The cat, and the Dog .and THE bird!"
text=text.lower()
text=text.replace(","," ")
text=text.replace("."," ")
text=text.replace("!"," ")
words=text.split()
print(words)
counts={}
for w in words:
    counts[w]=counts.get(w,0)+1
print(counts)
pairs=[]
for w in counts:
    pairs.append((counts[w],w))
pairs.sort()
pairs.reverse()

for p in  pairs:
    if p[0]>1:
        print(p[1]+"出现"+str(p[0])+"次")
    
