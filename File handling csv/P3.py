import csv
a=[['Takla associations','Hazaribagh'],['LMaoa','Noida'],["Hecker","Jamatara"],["Ghado ka tabela","Delhi"]]

with open("/workspaces/school/File handling csv/NGO.csv","w",newline="") as file:
    file_writer=csv.writer(file,delimiter=",") 
    file_writer.writerows(a)

def count_loc():
    