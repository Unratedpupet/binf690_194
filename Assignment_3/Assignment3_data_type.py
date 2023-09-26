#!/usr/bin/python
import math

SEPERATOR = "-------------------------------------------------------"

# Setting up variables for questions 1-4 using positive integer values
a = 5
b = 12
c = 17
d = 28

# Questions 4-6 use the following string, as provided by the assignment.
S = "CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC"

# Question 1: Assume right angle triangle with base = b and height = a. Return the length of the hypotenuse
hypotenuse = (a**2 + b**2)**0.5

print(f"The hypotenuse of the triangle with a base of {b} and a height of {a} is {hypotenuse}.")
print(SEPERATOR)

# Question 2: Assume a rectangle of length = c and width = d. 
# 1. Return the area of the rectangle
# 2. Return the perimeter of the rectangle

rect_area = c * d
rect_perimeter = c + c + d + d

print(f"The area of the rectangle with length {c} and height {d} is {rect_area}.")
print(f"The perimeter of the rectangle with length {c} and height {d} is {rect_perimeter}.")
print(SEPERATOR)

# Question 3: Assume a circle where radius = a.
# 1. Return the area of the circle
# 2. Return the circumference of the circle.

circle_area = math.pi * a**2
print(f"The area of the circle where the radius is {a} is {circle_area:.5f}.")

circle_circumference = 2 * math.pi * a
print(f"The circumference of a circle with a radius of {a} is {circle_circumference:.5f}.")
print(SEPERATOR)

# Question 4: Given a string S of any length and four integers a, b, c, and d
# 1. Slice the string S from indices a through b and c through d (with a space in between) inclusively
# 2. Generate the reverse of string S

ab_slice = S[a:b+1]
cd_slice = S[c:d+1]
reversed_string = S[::-1]
reversed_string_as_object = ''.join(reversed(S))

print(f"Here is the AB slice of string S: {ab_slice}")
print(f"Here is the CD slice of string S: {cd_slice}")
print(f"Here is the reversed copy of string S using reverse indexing: {reversed_string}")
print(f"Here is the reversed copy of string S using the object and .join function: {reversed_string}")
print(SEPERATOR)


# Question 5: Given a DNA string S
# 1. Find first and last location of stop codon 'TAG' and report its starting locations
# 2. Split the DNA string by stop codon 'TAG' and report each fragment and their respective lengths
# 3. Report percent GC of original DNA string S
# 4. Report number of A, C, T, and G

# Finds the first and last instance of the stop codon 'TAG'
first_stop = S.find('TAG')
last_stop = S.rfind('TAG')

print(f"The start location for the first stop codon is at index: {first_stop}")
print(f"The start location for the last stop codon is at index: {last_stop}")

# Splits the S string into a list, seperated by the stop codon 'TAG'
split_S = S.split('TAG')

# Counts the number of fragments in the list to verify the correct number of fragments
fragment_count = len(split_S)

first_split_length = len(split_S[0])
second_split_length = len(split_S[1])
third_split_length = len(split_S[2])
fourth_split_length = len(split_S[3])

print(f"There are {fragment_count} fragments in the given DNA sequence.")
print(f"The first fragment is {split_S[0]} which has a length of {first_split_length}.")
print(f"The second fragment is {split_S[1]} which has a length of {second_split_length}.")
print(f"The third fragment is {split_S[2]} which has a length of {third_split_length}.")
print(f"The fourth fragment is {split_S[3]} which has a length of {fourth_split_length}.")

# Initializes variables to allow for counting, setting all to 0
a_count, t_count, g_count, c_count = 0,0,0,0
nucleotide_count = len(S)

# Iterates through the DNA string, and counts the nucleotides
for char in S:
    if char == 'A':
        a_count += 1
    elif char == 'T':
        t_count +=1
    elif char == 'G':
        g_count += 1
    else:
        c_count += 1

percent_gc = (g_count + c_count) / nucleotide_count

print(f"The percent GC in the given DNA sequence is {percent_gc:.5f}.")
print(f"The number of Adenine is {a_count}")
print(f"The number of Thymine is {t_count}")
print(f"The number of Guanine is {g_count}")
print(f"The number of Cytosine is {c_count}")

print(SEPERATOR)


# Question 6: Given two lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 1. Return a list of all unique elements
# 2. Return a list of all common elements
# 3. Return a list of all elements

# Initialize the lists
a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Create a list of all elements by joining the two lists
ab_combined_list = a_list+b_list

# Initilize a new list for unique elements, then iterate through the combined list 
# and add the element to the list if it is not already in the list
unique_elements = []
for element in ab_combined_list:
    if element not in unique_elements:
        unique_elements.append(element)

# Initialize a new list for common elements. Then, using a nested for loop, compare elements in both
# lists to check if they are common, then add them to the common list
# The second iteration removes redundencies of the common elements ie the two '1's in the first list

common_elements_not_unique = []
common_elements_unique = []
for a_list_element in a_list:
    for b_list_element in b_list:
        if a_list_element == b_list_element:
            common_elements_not_unique.append(a_list_element)

for common_element in common_elements_not_unique:
    if common_element not in common_elements_unique:
        common_elements_unique.append(common_element)


print(f"The list of unique elements is {unique_elements}.")
print(f"The list of common elements is {common_elements_unique}.")
print(f"The combined list of all elements is {ab_combined_list}.")
