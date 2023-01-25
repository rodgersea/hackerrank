import string

word = 'test'
wordheight = []
for x in word:
    wordheight.append(h[string.ascii_lowercase.index(x)])
print(wordheight)

print(max(wordheight)*len(word))
