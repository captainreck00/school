import pickle

name=input("Enter your name")
p=int(input("Enter your marks in physics"))
m=int(input("Enter your marks in maths"))
c=int(input("Enter your marks in chemistry"))
cs=int(input("Enter your marks in CS"))
e=int(input("Enter your marks in english"))
per=(p+e+m+c+cs)/5
d={"name":name,"physics":p,"maths":m,"chemistry":c,"computer":cs}

file=open("marks.dat","ab")

pickle.dump(d,file)

print(pickle.load(file))