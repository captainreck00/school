myfile = open("marks.dat","a+")
stnum = int(input("Enter number of students: "))
for i in range(stnum):
    Name = input("Enter name: ")
    M = int(input("Enter marks in math: "))
    E = int(input("Enter marks in english: "))
    CS = int(input("Enter marks in cs: "))
    P = int(input("Enter marks in physics: "))
    C = int(input("Enter marks in chemistry: "))
    TM =M+E+CS+P+C
    Per = (TM/5)
    l = ["Name:",Name, "\n", "Math:",str(M), "\n", "Eng:",str(E),"\n","CS:",str(CS),"\n","Phy:",str(P),"\n","Chem:",str(C),"\n","Total Marks:",str(TM),"\n","Per:",str(Per), "\n"]
    myfile.writelines(l)
myfile.seek(0)
str0 = myfile.readlines()
print(str0)