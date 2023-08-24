import os
file="File handling/file.dat"
if os.path.isfile(file):
    data=open(file,"r+")
    print(len(data.readlines()))