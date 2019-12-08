#!/usr/bin/env python
# coding: utf-8

# In[2]:


for num in range(2000,3201):
    if (num % 7 == 0 and num % 5 != 0):
        print(num,end=",")


# In[3]:


first = input("Enter first name : ")
last =input("Enter last name : ")
def reverse(first,last):
    firstrev = ""
    lastrev = ""
    for i in first:
        firstrev = i + firstrev
    for i in last:
        lastrev = i + lastrev
    return(firstrev + " " + lastrev)
l = reverse(first,last)
print(l)


# In[7]:


diameter = 12
π = 22/7
def vol(d,π):
    r = d/2
    volume = 4/3 * π * r ** 3
    return (volume)
V = vol(diameter,π)
print(V)


# In[8]:


listNum = input("Enter List :")
store = ""
lis = []
for n in listNum:
    if n != ',':
        store = store + n
    elif n == ',':
        lis.append(store)
        store = ""
lis.append(store)
print(lis)


# In[9]:


for i in range(1,6):
    print("")
    for j in range(1,i):
        print("*", end = "")
for i in range(6,1,-1):
    print("")
    for j in range(i,1,-1):
        print("*",end="")


# In[10]:


inp = input("Enter String")
reverse = ""
for ch in inp:
    reverse= ch + reverse
    
print(reverse)


# In[19]:


def strFormat(newStr, li):
        frmStr = ""
        for n in li:
            newStr = newStr + n
            if n == 'INDIA, ':
                frmStr = frmStr + newStr
                newStr = ""
            if n == 'SOVEREIGN, ':
                frmStr = frmStr +'\n \t \t'+ newStr + '!'
                newStr = ""
            if n == 'INDIA, ':
                frmStr = frmStr +'\n \t \t \t' + newStr 
                newStr = ""
        else :
            frmStr = frmStr +'\n \t \t \t' + ' ' + newStr
        return (frmStr)
def takeInpt():
    inp = input("Enter String : ")
    li = []
    strn = ""
    newStr = ""
    for n in inp:
        strn = strn + n
        if (n == " "):
            li.append(strn)
            strn = ""
    li.append(strn)
    prntStr = strFormat(newStr,li)
    print("\n Output : ", prntStr)

    
takeInpt()


# In[ ]:




