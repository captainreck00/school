import csv

excel_header=["Ad No","Name","Class"]
excel_content=[[4242,'Vaibhav',12],[4242,'Vaibhav',12],[4242,'Vaibhav',12],[4242,'Vaibhav',12],[4242,'Vaibhav',12]]

with open("/workspaces/school/File handling csv/student.csv","w",newline="") as file:
    file_writer=csv.writer(file,delimiter=",")
    file_writer.writerow(excel_header)
    file_writer.writerows(excel_content)

def record_counter():
    with open("/workspaces/school/File handling csv/student.csv") as f:
        file_content=csv.reader(f)
        count=0
        for i in file_content:
            count+=1
            for j in i:
                print(j,end=",")
                print("\n")


record_counter()