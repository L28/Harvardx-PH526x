#!/usr/bin/env python
# coding: utf-8

# for each number, we are adding up the neighbors 
# and deviding them by the number of neighboors x[2,3] would be x[2.5,2.5] #Markdown
# 
# 
#     
# 

# In[24]:


def moving_window_average(x,n_neighbors):
    n=len(x)
    width=n_neighbors*2+1 # on both sides plus the element itself
    x=[x[0]]*n_neighbors + x + [x[-1]]*n_neighbors 
    # the first and last element are multiplied by the number of neighbors, 
    #then the lists are concatinated by the + operator
    # x is reassigned
    return[sum(x[i:(i+width)])/width for i in range(n)]
x=[0,10,5,3,1,5]
print(moving_window_average(x,1))
    
print("\N{WAVING HAND SIGN}, \N{EARTH GLOBE ASIA-AUSTRALIA}!")
    
    
    


# In[16]:


random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
    
R = 1000
x=random
x = [random.uniform(0, 1) for i in range(0, 1000)] #Return a random floating point number N such that
   #a <= N <= b for a <= b 
   #and b <= N <= a for b < a.
Y = [x] + [moving_window_average(x, n_neighbors=5) for n_neighbors in range(1, 10)]
print(Y[5][9])

#For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
#Print your answer. As the window width increases, does the range of each list increase or decrease? Why do you think that is?
#As window width increases, does the range of each list increase or decrease?

ranges = [max(x) - min(x) for x in Y]
print(ranges) #-> it is decreasing


# In[ ]:




