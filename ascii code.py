# 
my_dict = {}


for i in range(97, 97 + 26):
    
    my_dict[chr(i)] = i


print(my_dict)

# Program to find the ASCII value of the given character

my_dict = input("Enter a alphabet:")
print("The ASCII value of '" + my_dict + "' is", ord(my_dict))
