#!/usr/bin/env python
# coding: utf-8

# # Functions
# Procedural decomposition

# In[54]:


#define a function
def add(a,b):
    mysum= a + b
    return mysum

def add_and_substract(a,b):
    mysum = a+b
    mydiff = a-b
    return(mysum,mydiff) # returns tuple

    

#call function seperately, provin´ding inputs
add(3,4)

#to modify global statement, 

def update(n,x):
    n = 2
    x.append(4)
    print('update: ', n, x)
    


# In[48]:


x= [1,2,3,5]


# In[96]:



def modify(mylist):
    mylist[0] += 10 #first element in L is modified
L=[1,3,5,7,9] 
modify(L)
L


# In[99]:


def intersect(s1, s2):
    res=[] #create output
    for x in s1:
        if x in s2:
            res.append(x)
    return res

intersect([1,2,3,4,5],[3,4,5,6,7])


# In[83]:


def main():
    n=1
    x= [0,1,2,3] #in local scope
    print('main: ', n, x)
    update(n,x) #
    print('main: ', n, x)
    
    


# In[5]:


main()


# Remember an argument is an object, that is passed to a function as its input when it is called. A parameter in oposite is a variable, that is used in the function definition

# # Fingerexercise

# In[9]:


def increment(n):
    n+=1
    print(n)
    
n=1 #global definition
increment(n) #local definition
print(n) # local n doesn not change


# In[17]:


def increment(n):
    n += 1
    return(n)
    

n = 1
while n < 10:
    n = increment(n)
print(n)


# # Classes and Object-Oriented Programming

# In general objects consist of data and methods (operations on data)
#     Inheritance is a fundamental aspect of OOP. It means, that you can define a 
#     new object or object class, that inherents attributes of an existing class

# In[28]:


ml = [5,9,3,6,8,11]
ml.sort()
ml


# class MyList(list): 
#     def remove_min(self):
#         self.remove(min(self))
#     def remove_max(self):
#         self.remove(max(self))
#         
#         # the new, 'derived class' inherents attributes of the existing class passes, in this case, type list
#     #what methods are supported, but does not create an object of this type
#     #object wOUld be instance of a class, class statement no instances

# In[29]:


# now, remove the 6th item in list nl
ml.remove(6)
ml


# In[41]:


#now, create a list x and a new variable y, copy of x

class MyList(list):#new class inherits attributes of class 'list' and also its own new attributes; class specifies methods that are supported, but does not create any instances of a class
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))
x=[1,2,3,4,5,6,7,8,9]
dir(x) #which methods are supported by the object?
y =MyList(x)


# In[43]:


y


# In[44]:


dir(y)


# In[45]:


y.remove_min()


# In[46]:


y


# # Fingerexercise
# #Lösung: nie endende Schleife NewList= 1,2,3
