#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


   

lst = [ ]
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    element = [input(), input()]
    lst.append(element)
      
print(lst)

def last(n):
    return n[-1] 
  
def sort(tuples):
    return sorted(tuples, key=last)
  
print("sorted_lst:",sort(lst))
