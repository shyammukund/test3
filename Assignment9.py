#!/usr/bin/env python
# coding: utf-8

# Write a regular expression to match words that begin with at least two uppercase letters or two lowercase letters. For example, it will match UCX, AM, PM or hello, but reject University or Programming. 
#  

# In[141]:


import re

pattern = r'\b(?:[A-Z]{2}|[a-z]{2})\w*\b'
string = 'MAtch'

match_object = re.match(pattern,string)

if match_object:
    print('Matched')
else:
    print('No Match')


# Write a program that reads a Python file and removes any comments that it may have.  Comments include anything that starts with #.
# For example, if given the following Python file:
# # this is a comment
# print("hello world") # this is another comment
# 
# It should output:
# print("hello world")

# In[138]:


import os 
import sys
import re

file = os.getcwd() + '/PythonFile.py'

def remove_comments(file):
    pattern = r'#.*'
    no_comments = re.sub(pattern,'',file)
    return no_comments
       
try:
    with open(file, 'r') as file_in:
        original_file = file_in.read()
        new_file = remove_comments(original_file)
        print(new_file)
    
         
except FileNotFoundError:
    print(f'{file} does not exist.')


# Write a program that reads a file and prints out all of the valid email addresses. A valid email address has a pattern of prefix@domain.
# 
# Prefix can contain letters, numbers, underscore, dots and dashes.
# Domain can also contain letters, numbers, dashes. However, the last portion must contain a dot followed by at least two characters (example: .com, .cc, .edu, etc…)

# In[139]:


import os 
import sys
import re

file = os.getcwd() + '/emails.txt'

def print_emails(file):
    pattern = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', file)
    for email in pattern:
        print(email)
try:
    with open(file, 'r') as file_in:
        original_file = file_in.read()
        print_emails(original_file)
except FileNotFoundError:
    print(f'{file} does not exist.')                   


# Write a regular expression that will accept following phone numbers and reformat them into a standard format.
# 
# For example, the following phone numbers:
# 
# (415)555-1212
# 510-778-1234Write a regular expression that will accept following phone numbers and reformat them into a standard format.
# 
# For example, the following phone numbers:
# 
# (415)555-1212
# 510-778-1234
# 408 555 4321
# 650.444.1213
# 
# should be standardized to:
# 
# 415-555-1212
# 510-778-1234
# 408-555-4321
# 650-444-1213
# 408 555 4321
# 650.444.1213
# 
# should be standardized to:
# 
# 415-555-1212
# 510-778-1234
# 408-555-4321
# 650-444-1213

# In[53]:


def formatNumbers(*numbers):
    for number in numbers:
        
        # regular expression to take out the inputted formatting
        just_digits = re.sub(r'\D','',number)
        if len(just_digits) == 10:
            # regular expression to split the ten digit number in 3 seperate groups
            phone_pattern = re.compile(r'^(\d{3})(\d{3})(\d{4})$')
            # regular expression inserts the dashes to standardize the phone number
            insert_dashes = re.sub(phone_pattern,r'\1-\2-\3',just_digits)
            print(insert_dashes)   
        else: 
            print('Invalid Number')


# In[140]:


formatNumbers('(425)773-9619','425.392.4754','abd1325677','(123)4567890','1113334444')

