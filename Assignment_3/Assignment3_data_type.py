#!/usr/bin/python
import math

# Setting up variables for questions 1-4 using positive integer values
a = 12
b = 5
c = 28
d = 17

# Questions 4-6 use the following string, as provided by the assignment.
S = "CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC"

# Question 1: Assume right angle triangle with base = b and height = a. Return the length of the hypotenuse
hypotenuse = (a**2 + b**2)**0.5

print(f"The hypotenuse of the triangle with a base of {b} and a height of {a} is {hypotenuse}.")

# Question 2: Assume a rectangle of length = c and width = d. 
# 1. Return the area of the rectangle
# 2. Return the perimeter of the rectangle

rect_area = c * d
rect_perimeter = c + c + d + d

print(f"The area of the rectangle with length {c} and height {d} is {rect_area}.")
print(f"The perimeter of the rectangle with length {c} and height {d} is {rect_perimeter}.")

# Question 3: Assume a circle where radius = a.
# 1. Return the area of the circle
# 2. Return the circumference of the circle.

circle_area = math.pi * a**2
print(f"The area of the circle where the radius is {a} is {circle_area:.5f}.")

circle_circumference = 2 * math.pi * a
print(f"The circumference of a circle with a radius of {a} is {circle_circumference:.5f}.")

# Question 4: Given a string S of any length and four integers a, b, c, and d
# 1. Slice the string S from indices a through b and c through d (with a space in between) inclusively
# 2. Generate the reverse of string S

ab_slice = S[a:b+1]
cd_slice = S[c:d+1]

print(ab_slice + cd_slice)


# Question 5: Given a DNA string S
# 1. Find first and last location of stop codon 'TAG' and report its starting locations
# 2. Split the DNA string by stop codon 'TAG' and report wach fragment and their respective lengths
# 3. Report percent GC of original DNA string S
# 4. Report number of A, C, T, and G



# Question 6: Given two lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 1. Return a list of all unique elements
# 2. Return a list of all common elements
# 3. Return a list of all elements

