def longest(f):
    file=open(f,'r+')
    l=file.readlines()
    file.close()
    max=l[0].strip("\n")
    for i in l:
        k=i.strip("\n")
        if len(k)>len(max):
            max=k
    return(max)
 
