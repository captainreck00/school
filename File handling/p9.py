file=open("article.txt","r")
l=file.readlines()
file.close()
c_to=0
c_the=0
for i in l:
    k=(i.lower()).split(" ")
    c_to+=k.count("to")
    c_the+=k.count("to")
print(c_to,c_the)    

 
    
        
