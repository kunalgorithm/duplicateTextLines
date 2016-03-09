
## Written by Kunal Shah on 2/24/2016


import os
import sys

i = 0

# Define the file name
filename = "angelbysignal.txt"

# Label the input and output filenames
f = open(filename,"r")
copy = open(filename+"-processed","wt")


number_of_lines = 1852
line_before = ''

#loop that copies file line by line and terminates loop when i reaches 10
while i < number_of_lines:

	# Read each line of the program into a string
     line = f.readline()
     line = line.strip()

     # Compare the string to the last string, and remove '-' lines
     if (line == line_before) & (line != '-'):

     	# Write the line and add a new line character
     	copy.write(str(line) + '\n')
     i = i +1
     line_before = line

# close the file
f.close()
copy.close()