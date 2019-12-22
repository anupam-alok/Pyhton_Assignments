#!/usr/bin/env python
# coding: utf-8
# 1.1 Write a Python Program to implement your own myreduce() function which works exactly likePython's built-in function reduce()
# In[3]:


print("Enter 4 elements : ",end="")
li = []
for n in range(0,4):
    inpt = int(input())
    li.append(inpt)
def myReduce(li):
    product = 1
    for k in li:
        product = product * k
    return (product)
    
result = myReduce(li)
print("Result : ",result)

# 1.2 Write a Python program to implement your own myfilter() function which works exactly likePython's built-in function filter()
# In[ ]:


print("Enter 5 Elements : ")

li = []
for i in range(5):
    a = int(input())
    li.append(a)
print("Your Elements : ",li)

def myFilter (li):
    evenli = []
    posli = []
    negli = []
    oddli = []
    for x in range(len(li)):
        if (li[x] % 2 == 0):
            evenli.append(li[x])
           
        else:
            oddli.append(li[x])
            
    rtrnO =  print("Even number",evenli)
    rtrnE = print("Odd number",oddli)
    
    for x in range(len(li)):
        if (li[x] > 0):
            posli.append(li[x])
            
        else:
            negli.append(li[x])
            
    rtrnP = print("Positive number is : ",posli)
    rtrnN = print("Negative number is : ",negli)
    return (rtrnO,rtrnE,rtrnP,rtrnN)
        
resultFilter = myFilter(li)


# # Implement List comprehensions to produce the following lists.
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# In[1]:


a = input()
liCom = [x for x in a]
print(liCom)


# In[5]:


str = ['X','Y','Z']
licom = [x*i for x in str for i in range(1,5)]
print(licom)


# In[10]:


str = ['X','Y','Z']
licom = [x*i for i in range(1,5) for x in str ]
print(licom)


# In[14]:


inp = [2,3,4]
l = [[x+i] for x in inp for i in range(0,4)]
print (l)


# In[15]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


# In[16]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


# In[17]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# 1.1Write a Python Program(with class concepts) to find the area of the triangle using the belowformula.area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

# In[31]:


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
t = Triangle()
t.inputSides()
t.findArea()


# Write a function filter_long_words() that takes a list of words and an integer n and returns the listof words that are longer than n.

# In[1]:


def longestWord(li):
    for i in range(len(li)-1):
        if len(li[i]) >len(li[i+1]):
            temp = li[i]
            li[i] = li[i+1]
            li[i+1] = temp
    print("Longest String is : ", li[len(li)-1])
        
def inputTake():
    print("Enter words")
    li = []
    for i in range(3):
        a = input()
        li.append(a)
    print("Your Strng ; ", li)
    longestWord(li)
inputTake()


# 2.1Write a Python program using function concept that maps  list of words into a list of integers representing the lengths of the corresponding words​.Hint

# In[11]:


def filter_long_words(myDict):
    newDict = {}
    for x,y in myDict.items():
        if len(x) > y:
           newDict[x] = y
    print("New Dict : ",newDict)
        
def takeInput():
    myDict = {}
    for i in range(3):
        print("Enter Word")
        a = input()
        print("Enter Number")
        b =int(input())
        myDict[a]=b
    print("Your Dict : ", myDict)
    filter_long_words(myDict)
takeInput()


# In[13]:


def count(li):
    newli = []
    for i in range(len(li)):
        newli.append(len(li[i]))
    print("count item length " ,newli)
def takeInpt():
    li = []
    print("Enter element for list")
    for i in range(3):
        li.append(input())
    print("List : ", li)
    count(li)
takeInpt()


# Write a Python function which takes a character (i.e. a string of length 1) and returns True if it isa vowel, False otherwise.

# In[27]:


def isVowel(v):
    if v == ('a') or v == ('e') or v == ('i') or v ==('o') or v == ('u'):
        return True
    else:
        return False
inp = input("Enter a charater : ")
vowel = isVowel(inp)
print(vowel)


# In[ ]:





# In[ ]:




