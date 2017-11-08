
# coding: utf-8

# 实现一个阶乘程序

# In[5]:


def factorial(n):
    if n < 0:
        print 'input negative value is invalid'
        return None
    if n == 0:
        return 1
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product


# In[6]:

if __name__ == '__main__':
    print factorial(-1)
    print factorial(2)
    print factorial(3)
