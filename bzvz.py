"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

"""

# string1 = input("Please write a word: ")
string1 = "klitoris"

duljina = len(string1)
for i in range(0, duljina, 2):
    print(string1[i])
