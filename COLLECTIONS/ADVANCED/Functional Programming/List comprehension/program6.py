#print n if char is not vowel and y if vowel
name="luminartechnolab"
vow="aeiou"
lst=["n" if i not in vow else "y" for i in name ]
print(lst)