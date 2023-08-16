def inp():
       print("Enter non numeric character to exit")
       a=input("Enter the number to be appended in list : ")
       b=[]
       while(a.isnumeric()):
              b.append(int(a))
              a=input("Enter the number to be appended in list : ")
       return b

def common(a,b):
       k=[]
       for i in a:
              for j in b:
                     if i==j:
                            k.append(i)
              
       