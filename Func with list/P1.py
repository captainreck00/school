def inp():
       print("Enter non numeric character to exit")
       a=input("Enter the number to be appended in list : ")
       b=[]
       while(a.isnumeric()):
              b.append(int(a))
              a=input("Enter the number to be appended in list : ")
       return b

def even_odd(a):
       e=[]
       o=[]
       for i in a:
              if i%2==-0:
                     e.append(i)
              else:
                     o.append(i)
       return [e,o]              

k=inp()
print(even_odd(k))                            

     

