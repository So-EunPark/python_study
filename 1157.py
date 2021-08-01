s = input().upper()
alphabet=[0 for i in range(26)]
for i in range(len(s)):
    index=ord(s[i])-65
    alphabet[index] += 1

m=max(alphabet)
t=[i for i,v in enumerate(alphabet) if v==m ]
if len(t)>1:
    print('?')
else:
    print(chr(alphabet.index(max(alphabet))+65))
