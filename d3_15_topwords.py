texts = ["a a b", "b c c c"]
text=" ".join(texts)

print(text)
counts={}
words=text.split()
for i in words:
    counts[i]=counts.get(i,0)+1
pairs=[]
for i in counts:
    pairs.append((counts[i],i))
pairs.sort()
pairs.reverse()
for j in range(3):
    print(pairs[j])
 
