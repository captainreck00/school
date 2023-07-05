"""Q5. A list containing an even number of elements is passed to a function. The function
must swap the elements with adjacent positions. The main program should print the
updated list accordingly."""


def swap_place(l):
        for i in range(0,len(l)-1,2):
                l[i],l[i+1]=l[i+1],l[i]
        return l


try:
     print(swap_place([0,1,2,3,4,5,6,7,8,9]) )
except:
       print("Invalid list")                      

