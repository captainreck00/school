def copy_lower(f1,f2):
    file1=open(f1,"r+")
    file2=open(f2,"w+")
    for i in file1.readlines():
        if i[0].islower():
            file2.write(i)


  

