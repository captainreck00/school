file1=open("File handling/file1.dat","r+")
file2=open("File handling/file2.dat","a+")

l=file1.readlines()
file2.writelines(l)

