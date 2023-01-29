#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


lst = [ ]
n = int(input("Enter number of elements : "))  #here i entered 4 i.e it takes 8 numbers as input to make list of 4list in a list..
  
for i in range(0, n):
    element = [input(), input()]
    lst.append(element)
      
print("the list we entered:",lst)              # prints the list u entered


def last(n):
    return n[-1] 
  
def sort(tuples):                       # it sorts the given list
    return sorted(tuples, key=last)
  
print("sorted_lst:",sort(lst))             #prints the list in the increasing order

