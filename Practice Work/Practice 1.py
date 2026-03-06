#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


# 1) Print numbers from 1 to 5
i = 1 
while i <= 5:
    print(i)
    i += 1


# In[2]:


#2) Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1


# In[6]:


#3) Print even numbers from 2 to 10
i = 2
while i % 2 == 0 and i <= 10:
    print(i)
    i += 2


# In[7]:


i = 1
while i <= 9:
    print(i)
    i += 2


# In[8]:


count = 0
i = 1
while i <= 7:
    count += 1
    i+=1
    
print(count)


# In[20]:


sum = 0
i= 1
while i<=5:
    sum += i
    i+=1
print(sum)


# In[4]:


even = 0
i=2
while i<= 10:
    if i%2 ==0 :
        even += i
    i+=2
print(even)


# In[5]:


even = 0
i=2
while i<= 10:
    if i%2 ==0 :
        even += i
    i+=2
print(even)


# In[1]:


i= 1
while i<=4:
    i+= 1
    print(i)


# In[4]:


product = 1
i = 1

while i <= 4:
    product *= i
    i += 1

print(product)  


# In[5]:


count =0
i= 1
while i<=15:
    if i% 3==0:
        count += 1
    i+=1
print(count)


# In[7]:


n = 12345
total =0
while n >0:
    digit = n % 10
    total += digit
    n = n // 10
print(total)


# In[5]:


n = 123
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10


# In[2]:


n= 96785
count = 0 
while n>0:
    count += 1
    n = n // 10
print(count)


# In[11]:


n = input("Enter a number: ")
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse == original)



# In[10]:


n = 122
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse == original)


# In[ ]:




