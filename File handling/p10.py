file=open("article.txt",'r+')
l=file.readlines()
print(l)

vowel_l=["a","e","i","o","u"]
vowel_u=["A","E","I","O","U"]

n=""
for i in l:
    n_str=""
    for j in i:
        if j in vowel_l:
            n_str+=j.upper()
        elif j in vowel_u:
            n_str+=j.lower()
        else:
            n_str+=j
    n+=n_str       

file.seek(0)
file.write(n)
           
file.close()


# dsf asdf ato  OOOOfasdf to sdaf ads the adsf aSSDsdf
# asdfWEWQRPASikj to the tABDSXo the adsaf the to tothe asdfWEWQRPASikj
# DAOUe
