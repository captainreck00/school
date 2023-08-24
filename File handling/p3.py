file1=open("File handling/file.dat","r+")
k=file1.readlines()
file1.close()
l=""
for i in k:
    i=i.strip('\n')
    l=l+i
print(l)    