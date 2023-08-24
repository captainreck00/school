file=open("article.txt",'r+')
l=file.readlines()
file.close()
vowel_l=["a","e","i","o","u"]
vowel_u=["A","E","I","O","U"]
n_str=""
for i in l:
    for j in i:
        if j in vowel_l:
            n_str+=j.upper()
        elif j in vowel_u:
            n_str+=j.lower()
        else:
            n_str+=j

print(n_str)            

