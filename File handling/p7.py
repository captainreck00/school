file=open("File handling/file.dat","r")
k=file.readlines()
file.close()
l=""
for i in k:
    for j in i.strip("\n"):
        if j.isnumeric():
            l+=j

print(l)            

