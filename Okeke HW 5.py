#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1a
#I thought it would print out 6:30
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
        
Clock = Clock('5:30')
Clock.print_time()




# It printed out 5:30 because the clock object was instantiated with the time of 5:30 and because you said self.time 
#rather than time in the print function, the print function is printing out the time associated with the object 
#that called print_time()


# In[5]:


#2
#2a I guessed 5:30
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)
        
Clock = Clock('5:30')
Clock.print_time('10:30')



#It printed out 10:30 because although the clock object was instantiated with the time of 5:30 you said time 
#rather than self.time in the print function, the print function is printing out the time that was passed into the 
#print_time() function


# In[8]:


#3a
#I guessed 5:30 and 10:30 in that order
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

        
class Clock1(Clock):
    pass
        
boston_clock = Clock('5:30')
paris_clock = Clock1('10:30')

boston_clock.print_time()
paris_clock.print_time()

# It printed out 5:30 and 10:30 because the clock objects were instantiated with the times of 5:30 and 10:30 and 
#because you said self.time print function, the print function is printing out the time associated with the object 
#that called print_time() also Clock1 was able to work because it just refers to the Clock object 


# In[9]:


#4
class Queue():
    def __init__(self):
        self.line=[]
    def print(self):
        print(self.line)
    def insert(self,elem):
        self.line.append(elem)
    def remove(self):
        if len(self.line)==0:
            print("The Queue is empty")
            return
        else:
            num=self.line[0]
            self.line=self.line[1:]
            return num


queue=Queue()
queue.insert(5)
queue.insert(6)
queue.print()

queue.insert(7)
queue.remove()
queue.print()


queue.remove()
queue.remove()
queue.remove()


# In[ ]:




