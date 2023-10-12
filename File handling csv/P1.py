import csv
with open("/workspaces/school/File handling csv/Employee.csv") as file:
    content=csv.reader(file)
    for i in content:
        print(i)