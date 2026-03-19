# Add Two Numbers in Python
# Author:Xiong An Kang
# Using a function
# function to add two numbers
def add(a,b):
	res=float(a)+float(b)
	return res
# takinguser input
a=input("First number:")
b=input("Second number:")
# calling function
res=add(a,b)
print("The answer is:")
print(res)
