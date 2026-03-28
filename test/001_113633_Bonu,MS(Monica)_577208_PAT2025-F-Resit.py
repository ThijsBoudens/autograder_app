#!/usr/bin/env python
# coding: utf-8

# # Programming and Algorithmic Thinking resit exam
# 
# 

# Welcome to the resit examination of the course Programming and Algorithmic Thinking. **Please read these instructions carefully.** This is a graded exam.
# 
# The questions in this exercise instruct you to define a function inside of a template. Any code written outside of that function will not be considered. 
# 
# You can define the function inside the code cell of this notebook and then convert this entire document to a .py file (we'll give instructions at the end on how to do so), or type your answer directly in a separate .py file and save it there.
# 
# **Do not change the name of the function** - make sure to keep the function-name the same as it is in the template answer. 
# 
# You should add arguments to the function definitions according to the excercises' instructions. You can name the arguments as you prefer.
# 
# You can import basic python modules (e.g., os, math, etc.) if necessary.
# 
# The code cell with the template answer includes several `print()` functions with testing inputs. You can therefore run the code in the cell to test your answer. If your code gives the correct output for the test input, that is an indication, but **not a guarantee(!)**, that your answer is completely correct. 
# 
# To get all the points, your code should be generalizable and work on any valid inputs of the type specified in the question. This exercise will be graded using different inputs from the ones provided in the question. You can get partial points for functions that work partially, but your code should at least run.
# 
# You can add print statements to extend testing if you want, but make sure to leave them inside of the `if __name__ == '__main__':` statement and **do not change this statement itself in any way**.
# 
# At the end of the exam, upload the .py file containing your function to Canvas. Double-check it to see if everything is in there. Make sure to save yourself enough time to do this step!
# 
# --------------------------------------------------------------------------------------------------------

# ## Question 1 [2 points]
# 
# Define a function called balanced() that accepts one argument: a string.
# 
# Your funtion should return True (as a boolean) if the argument string contains an equal amount of English vowels and consonants, or False (as a boolean) otherwise. You should consider every letter, no matter how many times it appears in the argument string.
# 
# Your function should be case-insensitive.
# 
# English vowels: AEIOUaeiou
# 
# English consonants: BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz

# In[145]:


def balanced(strg):
    vowel = "AEIOUaeiou"
    cons = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    clean = " ".join(i if i.isalpha() else"" for i in strg.lower())
    clean2 = clean.split()

    vcount = 0
    ccount = 0
    for char in clean2:
        if char in vowel:
            vcount += 1
        else:
            ccount +=1

    if vcount == ccount:
        return True

    return False
    
    # your code here


    
    
#----------- DO NOT WRITE CODE BELOW THIS LINE ------------------------------------------   
if __name__ == '__main__':
    print(balanced("HellO Anna!")) #expected output: False
    print(balanced("a BALANCED() woooord?")) #expected output: True
    print(balanced("a b c d e f.")) #expected output: False
    print(balanced("a b c d E f e E")) #expected output: True


# ## Question 2 [2 points]
# 
# Define a function called firstPrime() that accepts one argument: an integer (let's call it n). Your function should calculate and return (as an integer) the first prime number greater than n.
# 
# To help, the function isPrime() is provided. This function returns True (as a boolean) if a number (provided as argument) is prime or False (as a boolean) otherwise.

# In[144]:


def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True



def firstPrime(n):
    n2 = n*n

    for i in range(2,n2):
        if isPrime(i) and i > n:
            return i
    # your code here



    
    
#------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print(firstPrime(6)) #Expected output: 7
    print(firstPrime(100)) #Expected output: 101
    print(firstPrime(233)) #Expected output: 239
    print(firstPrime(888)) #Expected output: 907
    


# ## Question 3 [2 points]
# 
# Define a function called alphabetical() which receives one argument: a list of strings.
# 
# Your function should return True (as a boolean) when the argument list is alphabetically sorted, or False (as a boolean) otherwise. In an alphabetically sorted list, each element (at position i) should be alphabetically below the next element (at position i+1). For example, ['a', 'b', 'c'] is sorted since 'a'<'b'<'c'.
# 
# Your function should be case-insensitive.
# 
# You can assume the argument list will contain no duplicate elements.
# 
# 
# 

# In[141]:


def alphabetical(lst):

    nlst = []
    for i in lst:
        nlst.append(i.lower())
    
    less = False
    for i in range(len(nlst)-1):
        if ord(nlst[i]) < ord(nlst[i+1]):
            less = True
        elif ord(nlst[i][0]) < ord(nlst[i+1][0]):
            less = True
        else:
            less

    if less == True:
        return True
    return False
        

        
     

        


        
    
    
#----------- DO NOT WRITE CODE BELOW THIS LINE ------------------------------------------   
if __name__ == '__main__':
    print(alphabetical(['a', 'b', 'c'])) #Expected output: True
    print(alphabetical(['a', 'c', 'b'])) #Expected output: False
    print(alphabetical(['aeroplane', 'asparagus', 'aspirine'])) #Expected output: True
    print(alphabetical(['BEER', 'water', 'Wine'])) #Expected output: True
    print(alphabetical(['Beef', 'pasta', 'Ramen', 'STEw', 'Wagyu steak'])) #Expected output: True
    print(alphabetical(['Beef', 'pasta', 'Ramen', 'STEw', 'Aspirine'])) #Expected output: False
    


# ## Question 4 [2 points]
# 
# Define a function called dinner() which receives two dictionaries as arguments. 
# 
# The first dictionary represents a recipe that you would like to cook, and contains string keys representing ingredients. Each respective value is the amount of that ingredient that is required for the recipe.
# 
# The second dictionary represents your pantry, and contains string keys representing ingredients you have available. The respective value is the amount you have available for each ingredient.
# 
# Your function should return True (as a boolean) if you have all the ingredients (and adequate amounts thereof) in your pantry to cook the recipe, or False (as a boolean) otherwise. To be able to cook the recipe, for each ingredient in it (first argument), your pantry (second argument) should have equal to or more than the required amount.
# 
# 
# 

# In[142]:


def dinner(dictR, dictH):
    
    for ing in dictR:
        if ing in dictH: 
            if dictH[ing] >= dictR[ing]:
                return True
                
    return False
    # your code here
    
            
    
    

#----------- DO NOT WRITE CODE BELOW THIS LINE ------------------------------------------   
if __name__ == '__main__':
    print(dinner({'pasta': 150, 'tomato': 10, 'oil': 50}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20})) #Expected output: True
    print(dinner({'beef': 1000, 'wine': 100, 'onion': 1}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20})) #Expected output: False
    print(dinner({'ramen': 200, 'broth': 500, 'pork': 200, 'egg': 2}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1})) #Expected output: False
    print(dinner({'flour': 200, 'water': 200}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1})) #Expected output: False
    print(dinner({'flour': 200, 'water': 200}, {'flour':300, 'water': 500, 'pork': 200, 'salt': 200, 'egg':10})) #Expected output: True



# ## Question 5 [2 points]
# 
# Define a function called standings() that receives one argument: a (string) path to a text file.
# 
# The text file contains the final standings of a football league, and is formatted as follows:
# Every line of the file contains a team name, followed by a space, followed by the points (in digits) that team managed to collect. 
# 
# Your function should calculate and return (as a string) the name of the team with the most points.
# 
# You can assume team names contain no spaces.

# In[143]:


def standings(strg2):
    with open(strg2, 'r') as fp:
        buffer = fp.read()

    clean2 = buffer.split()
    club = []
    point = []

    for i in clean2:
        if i.isalpha():
            club.append(i)
        else:
            point.append(int(i))
  
    maxpoint = max(point)
    for i in range (len(point)):
        if point[i] == maxpoint:
            inx = i
            
    return club[inx]
    #your code here
                
    
    
# --------------- DO NOT WRITE CODE BELOW THIS LINE -------------------------
if __name__ == '__main__':
    print(standings('test1.txt')) #Expected output: 'Barcelona'
    print(standings('test2.txt')) #Expected output: 'Napoli'


# -----------------------------------------------------------------------------------------------------
# ## Done with all the Questions? Save your code as a .py file!
# 
# First save this document, then convert it to a .py file:
# - Make sure it is selected in the list on the left
# - Click 'File' in the upper left hand corner of the screen
# - Choose 'Export Notebook As...' and 'Export Notebook as Executable Script'
# - The notebook is saved (in the same folder) as a .py file
# 
# **Open the .py version and check whether all your functions are in there** (if not, save this document and go through the steps again). The normal text in this file will appear as comments in the .py version, that is not a problem and you can leave them there. 
# 
# If the file conversion does not work for you, you can also create a new .py file and copy all of your functions into it.
# 
# You can then upload the .py file to the exam on TestVision. Go to the next question, open the .py file again, and copy-paste the entire contents of the file into Testvision as a backup.
