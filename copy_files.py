# -*- coding: utf-8 -*-
"""
Created on Fri May 31 06:32:09 2019

@author: Ravi
"""

import shutil
import os


# First, we'll create an empty list to hold the path to all of your docx files
  
source = 'E:\Test\Folder1'
dest1 = 'E:\Test\Folder2'   

# Now, we loop through every file in the folder 
# (and all it's subfolders) using os.walk().  You could alternatively use os.listdir()
# to get a list of files.  It would be recommended, and simpler, if all files are
# in the same folder.  Consider that change a small challenge for developing your skills!
for path, subdirs, files in os.walk(source):
    file_counts = dict();
    document_list = [] 
    for name in files:        
        # For each file we find, we need to ensure it is a .docx file before adding
        #  it to our list
        if os.path.splitext(os.path.join(path, name))[1] == ".docx":
            index_of_dot = name.index('.')
            fwe = name[:index_of_dot]
            
            #print(os.path.join(path, fwe))
            #print(fwe)
            #print(fwe + ".docx")
            document_list.append(fwe)
            #document_list.append(os.path.join(path, name))
         
        # For each file we find, we need to ensure it is a .pdf file before adding
        #  it to our list
        if os.path.splitext(os.path.join(path, name))[1] == ".pdf":
            index_of_dot = name.index('.')
            fwe = name[:index_of_dot]
            
            #print(fwe)
            document_list.append(fwe)
            
    for li in document_list:
        if li in file_counts:
            file_counts[li] += 1
        else:
            file_counts[li] = 1
            
    print(file_counts)
    
    for key, value in file_counts.items():
        if(value == 1):
            print(key+".docx")
            shutil.copy(source+"\\"+key+".docx", dest1)
            
    
    
    
       