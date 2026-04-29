#!/usr/bin/env python
# coding: utf-8

# In[11]:


nums = [3, 4, 7, 10, 11, 12]

even_sum = 0
for i in nums:
    if i % 2 == 0:
        even_sum += i
print (even_sum)


# In[22]:


s = "leetcode"
e = 0
for i in s:
    if i == "e":
        e += 1
print(e)

        


# In[27]:


nums = [1, 2, 3, 4]
squares = []
for i in nums:
    squares.append(i**2)
print(squares)


# In[28]:


nums =[1,2,3,4,5,6,7,8]
for i in nums:
    print(i)
    


# In[31]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
Sum = 0
for i in nums:
    Sum += i
print(Sum)


# In[36]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
positive = 0
negative = 0
zero = 0
for i in nums:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else :
        zero += 1
print( f"total positive numbers in: {nums} is {positive}")
print( f"total negavtive numbers in: {nums} is {negative}")            
print( f"total zero numbers in: {nums} is {zero}")


# In[43]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
biggest = nums[0]

for i in nums:
    if i > biggest:
        biggest = i 
print (biggest)


# In[65]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
g = []
for i in nums:
    if i > 5:
        g.append(i)
print(g)


# In[72]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
squares = []

for i in nums:
    squares.append(i**2)
print(squares)


# In[74]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
R = []

for i in nums:
    R.insert(0,i)
print(R)


# In[75]:


s = "leetcode"
frequency = {}

for char in s:
    if char in frequency:
        frequency[char] += 1  # If it exists, add 1 to the count
    else:
        frequency[char] = 1   # If it's new, set count to 1

print(frequency)


# In[11]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
target = -29

for i, x in enumerate(nums):
    if x == target:
        print(i)


# In[13]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
target = 0
for i, x in enumerate(nums):
    if i % 2 == 0:
        target += x
print(target)


# In[18]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
biggest  = nums[0]
index = [0]
for i, x in enumerate(nums):
    if x > biggest:
        biggest = x
        index = i
print(biggest)
print(index)


# In[21]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
for i , x in enumerate(nums):
        print(i,x)


# In[24]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
target = 6

for i, x in enumerate(nums):
    if x == target:
        print(i)


# In[35]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
count = 0

for i,x in enumerate(nums):
    if x > 5:
        print(i)
        count += 1
print( f"count= {count}")


# In[36]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]

for i, x in enumerate(nums):
    if x% 2 == 0:
        print(i)


# In[40]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
list = [] 

for i, x in enumerate(nums):
     list.append(i+x)
print(list)


# In[41]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]


# In[55]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
for i, x in enumerate(nums):
    if x < 0:
        print(i)     


# In[59]:


s = "leetcode"

for i, x in enumerate(s):
    print(i,x)


# In[64]:


s = "leetcode"

for i, x in enumerate(s):
    if x == "e":
        print(i)


# In[72]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
target = -29
list = []
for i,x in enumerate(nums):
    if x == target:
        list.insert(0,x)
    else:
        list = -1
print(list)


# In[73]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]
avg = sum(nums)/len(nums)

for i, x in enumerate(nums):
    if x > avg:
        print(i)


# In[74]:


nums =[-1,2,-3,-4,5,6,-7,8,0, 10, -22, 0, -29]


# In[ ]:





# In[76]:


nums = [-1, 2, -3, -4, 5, 6, -7, 8, 0, 10, -22, 0, -29]
results = []

for i in range(len(nums) - 1):
    pair_sum = nums[i] + nums[i+1]
    results.append(pair_sum)

print(results)


# In[77]:


nums = [-1, 2, -3, -4, 5, 6, -7, 8, 0, 10, -22, 0, -29]
results = []

for i, x in enumerate(nums):
    if x + ()


# In[1]:


for i in range(3):
    for j in range(2):
        print(i, j)


# In[3]:


for i in range(3):
    for j in range(3):
        print(i, j)


# In[7]:


nums = [-1, 2, -3, -4, 5, 6, -7, 8, 0, 10, -22, 0, -29]
taget = 11

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] +nums[j] == taget:
            print(i,j)


# In[2]:


nums = [1, 2, 2, 3,3,3,3,3]

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    print(nums[i], count)


# In[ ]:




