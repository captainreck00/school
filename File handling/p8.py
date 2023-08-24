def copy(f1,f2):
    file1=open(f1,"r+")
    file2=open(f2,"w+")
    for i in file1:
        if i[0]!="@":
            file2.write(i)
    file1.close()
    file2.close()      

copy("File handling/file.dat","file2.dat")