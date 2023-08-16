# Write a program to get roll numbers, names and marks of the students of a class and store these
# details in a file called marks.dat. Process these marks to calculate percentage scored by students and
# save in the file mentioned. Display the data of the file in an appropriate format to view the complete
# details of the students.


def details(file):
    num=int(input("enter the no of students"))
    for i in range(num):
        roll=int(input("enter roll number"))
        name=input("enter name")
        marks=float(input("enter marks"))
        data=str(roll)+","+name+","+str(marks)+"\n"
        file.write(data)

def display(file):
    file.seek(0)
    for i in file.readlines():
        print(i)

file=open("marks.dat","w+")
details(file)

display(file)
file.close()





    


