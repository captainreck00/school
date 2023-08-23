file1=open("File handling/file.dat","r+")
k=file1.readlines()
l=""
for i in k:
    l=l+i
print(i)    