#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_Pair(arr, n, sum):
    print("Answer Of Q1 started here")
    count = 0 
 #To check all possible pairs
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count=count+1
                print("(",arr[i], ",", " ",arr[j], ")", sep = "")
    return count
 
arr = [1, 5, 7, -1, 5,9,4,3]
n = len(arr)

sum = 8
print("Number of pairs is",
      find_Pair(arr, n, sum))

#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseArray(arr, start, end):
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end =end-1
 
arr = [1, 2, 3, 4, 5, 6]
print("\nAnswer Of Q2 started here")
print("Given Array is ",arr)
reverseArray(arr, 0, len(arr)-1)
print("Reversed Array is ",arr)

#Q3. Write a program to check if two strings are a rotation of each other?
def checkRotation(s1, s2): 
    temp = '' 
   # Check if lengths of two strings are equal or not 
    if len(s1) != len(s2): 
        return False
# storing concatenated string 
    temp = s1 + s1 
    if s2 in temp: 
        return True 
    else: 
        return False
  

string1 = "HELLO"
string2 = "LOHEL"

print("\nAnswer Of Q3 started here")
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")

#Q4. Write a program to print the first non-repeated character from a string?

NO_OF_CHARS = 256
def get_char_count(string):
	count = [0] * NO_OF_CHARS
	for i in string:
		count[ord(i)]+=1
		return count

def first_non_repeating_character(string):
	count = get_char_count(string)
	index = -1
	k = 0
	for i in string:
		if count[ord(i)] == 1:
			index = k
			break	
	k += 1
	return index
print("\nAnswer Of Q4. started here...")
string = input("Enter the string :")
index = first_non_repeating_character(string)
if index==1:
	print ("All the characters are repetitive")
else:	
	print ("First non-repeating character is ", string[index] )


#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print( "Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
# Driver code
print("\nAnswer Of Q5. started here...")
n = 3
TowerOfHanoi(n,'A','B','C') 

#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

s = "*-A/BC-/AKL"
print("\nAnswer of Q6 Starts Here...")
# Stack for storing operands
stack = []
operators = set(['+', '-', '*', '/', '^'])
# Reversing the order
s = s[::-1]
for i in s:
    # if token is operator
    if i in operators:
        # pop 2 elements from stack
        a = stack.pop()
        b = stack.pop()
        # concatenate them as operand1 +
        # operand2 + operator
        temp = a+b+i
        stack.append(temp)
    # else if operand
    else:
        stack.append(i)
# printing final output
print(*stack)

#Q7. Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    
	stack = []
	# read prefix in reverse order
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			# symbol is operand
			stack.append(prefix[i])
			i -= 1
		else:
			# symbol is operator
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

# Driver code
if __name__=="__main__":
    #print("\nAnswer of Q.7 Starts here.")
	str = "*-A/BC-/AKL"
	print("Answer of Q.7 Starts here")
	print(prefixToInfix(str))

#Q8. Write a program to check if all the brackets are closed in a given code snippet.
def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
    
str = "{()}[]"
print("\nAnswer Of Q.8 starts here")
if matched(str)==True:
    print("Balenced")
else:
    print("Not Balenced")

#Q9. Write a program to reverse a stack.

class  Stack_to_reverse  :
    # Creates  an  empty  stack.
    def __init__(  self  ):
        self.items  =  list()
        self.size=-1
    #Returns  True  if  the  stack  is  empty  or  False  otherwise.
    def  isEmpty(  self  ):
        if(self.size==-1):
            return True
        else:
            return False
    # Removes  and  returns  the  top  item  on  the  stack.
    def  pop(  self  ):
        if  self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
            self.size-=1
    # Push  an  item  onto  the  top  of  the  stack.
    def  push(  self,  item  ):
        self.items.append(item)
        self.size+=1
    def reverse(self,string):
        n = len(string)
 
 # Push all characters of string to stack
        for i in range(0,n):
            S.push(string[i])

        string=""
 
 # Pop all characters of string and put them back to string
 
        for i in range(0,n):
            string+=S.pop()
        return string
print("\nAnswer Of Q.9 starts Here...")
S=Stack_to_reverse()
seq=input("Enter a string to be reversed:- \n")
sequence = S.reverse(seq)
print("Reversed string is " + sequence)


#Q10. Write a program to find the smallest number using a stack.

class Node:
    # Constructor which assign argument to nade's value
    def __init__(self, value):
        self.value = value
        self.next = None
    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)
     
    # __repr__ is same as __str__
    __repr__ = __str__
class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top,out))
         
    # __repr__ is same as __str__
    __repr__=__str__
     
    # This method is used to get minimum element of stack
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
 
 
 
    # Method to check if Stack is Empty or not
    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
        # If top not equal to None then stack is empty
            return False
 
    # This method returns length of stack    
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count
 
    # This method returns top of stack    
    def peek(self):
        if self.top is None:
            print ("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))
 
    # This method is used to add node to stack
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
         
        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))
    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print ("Top Most Element Removed :{} " .format(self.minimum))
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print ("Top Most Element Removed : {}" .format(removedNode))
# Driver program to test above class
print("\nAnswer of Q10. is starts here")
stack = Stack()
 
stack.push(3)
stack.push(5)
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()    
stack.pop()
stack.getMin()
stack.pop()
stack.peek()








