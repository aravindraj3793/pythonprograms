#print string without vowels
name="apple"
n=""
vow="aeiouAEIOU"
for i in name:
    if i not in vow:
        vow+=i
        print(i)
        