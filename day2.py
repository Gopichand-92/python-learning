#1. Count Total Vowels
# Task: Write a function that takes a string and returns the total number of vowels (a, e, i, o, u).
# Example Input:
# programming
# Example Output:
# Total Vowels = 3

# def count_vowels(str1):
#     count = 0
#     for char in str1:
#         if char in 'aeiouAEIOU':
#             count += 1
#     return count

# str1=input('enter the string:')
# count = count_vowels(str1)
# print(f'The total vowels of the given string {str1} is {count}')


# 2. Count Total Consonants
# Task: Write a function that takes a string and returns the total number of consonants.
# Example Input:
# python
# Example Output:
# Total Consonants = 5

# def count_consonants(str):
#     count=0
#     for char in str:
#         if ('A' <= char <= 'Z' or 'a' <= char <= 'z') and char not in 'aeiouAEIOU':
#             count += 1
#     return count
# str = input('enter the string: ')
# count = count_consonants(str)
# print(f'The total consonants of the given string {str} is {count}')


# 3. Reverse a String
# Task: Write a function that takes a string and returns the string in reverse order.
# Example Input:
# computer
# Example Output:
# Reversed String = retupmoc

# str=input('enter the string :')
# rev=""
# for char in str:
#     rev=char+rev
#     print(f'the reverse of the given string {str} is {rev}')


#4. Count Uppercase and Lowercase Letters
# Task: Write a function that takes a string and returns the number of uppercase and lowercase
# letters.
# Example Input:
# PyThOn
# Example Output:
# Uppercase = 3
# Lowercase = 3

# def count_case(str):
#     uppercase_count=0
#     lowercase_count=0
#     for char in str:
#         if 'A' <= char <='Z':
#             uppercase_count+=1
#         elif 'a' <= char <='z':
#             lowercase_count+=1
#     return uppercase_count, lowercase_count

# str=input('enter the string: ')
# uppercase_count, lowercase_count = count_case(str)
# print(f'The total uppercase letters of the given string {str} is {uppercase_count}')
# print(f'The total lowercase letters of the given string {str} is {lowercase_count}')


#5. Count Digits in a String
# Task: Write a function that takes a string and returns how many digits are present.
# Example Input:
# abc12345xy
# Example Output:
# Digits = 5

# def count_digits(str):
#     count=0
#     for char in str:
#         if '0' <= char <= '9':
#             count+=1
#     return count    

# str=input('enter the string: ')
# count = count_digits(str)   
# print(f'The total digits of the given string {str} is {count}')

#6. Check Palindrome
# Task: Write a function that takes a string and checks whether it is a palindrome.
# Example Input:
# madam
# Example Output:
# Palindrome

# def check_palind(str):
#     rev=""
#     for char in str:
#             rev=char+rev
#     if str==rev:
#         return True
#     else:
#         return False
# check_palind=('madam')
# print(f'the given string {check_palind} is a palindrome')



#7. Count Occurrences of a Character
# Task: Write a function that takes a string and a character and returns how many times that
# character appears.
# Example Input:
# banana
# a
# Example Output:
# # Occurrences = 3

# def count_occur(str1, char):
#     count = 0
#     for character in str1:
#         if character == char:
#             count += 1
#     return count
# str1 = input("Enter a string: ")
# char = input("Enter a character: ")
# result = count_occur(str1, char)
# print("Occurrences =", result)

#8. Find the Longest Word
# Task: Write a function that takes a sentence and returns the longest word.
# Example Input:
# Python is an amazing language
# Example Output:
# Longest Word = language

# def long_word(sentence):
#     words=sentence.split()
#     long=words[0]
#     for word in words:
#         if len(word)>len(long):
#             long=word
#     return long
        
# sentence=input('enter the sentence:')
# result=long_word(sentence)
# print(f'the longest word  is {result}')

#9. Remove All Spaces
# Task: Write a function that takes a sentence and returns the same sentence after removing all
# spaces.
# Example Input:
# Data Science is fun
# Example Output:
# DataScienceisfun

# def remove_spaces(sentence):
#     result=""
#     for char in sentence:
#         if char!=" ":
#             result+=char
#     return result
# remove_spaces('Data Science is fun')
# result=remove_spaces('Data Science is fun')
# print(f'the given sentence after removing all spaces is {result}')

#10. Count Words in a Sentence
# Task: Write a function that takes a sentence and returns the total number of words.
# Example Input:
# Learning Python is very interesting
# Example Output:
# Total Words = 5

# def total_words(sentence):
#     words=sentence.split()
#     count=0
#     for word in words:
#         count+=1
#     return count
# total_words('Learning Python is very interesting')
# result=total_words('Learning Python is very interesting')
# print(f'the total words of the given sentence is {result}')


