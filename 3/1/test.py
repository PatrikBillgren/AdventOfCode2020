from itertools import count

# Program to emulate enumerate()  
# using count() 
  
# list containing some strings 
my_list =["Geeks", "for", "Geeks"] 
  
# count spits out integers for  
# each value in my list 
for i in zip(count(start = 1,  
                   step = 1), my_list): 
      
    # prints tuple in an enumerated  
    # format 
    print(i)
