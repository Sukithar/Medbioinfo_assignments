#!/Users/srrn/miniconda3/bin/python

# Read fastQ file, count the number of seq and
# print the sequence IDs

# created: June 07, 2017
# Sukithar Rajan
##########################################

import sys
import os.path # for the file test

"""
file1 = input('Please enter a fastaQ file : ')
if not os.path.isfile(file1): # test for file existance
	sys.exit("ERROR: Input file doesnt exist")

#fin = open(file1, 'r') # open the input file for reading
"""

fin = open('test.fq', 'r')
count = 0 # initialize the number of lines
id_list = list() # initialize a list for storing seq IDs

for line in fin:
    if line.startswith('@cl'):
        count += 1
        id_list.append(line)
print('Number of sequences:', count, '\n')
for elements in id_list:
    print(elements)
