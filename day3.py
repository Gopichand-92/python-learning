#1. Count Even Numbers
# Write a function that returns the number of even numbers in a list.
# Example
# Input: [2, 5, 8, 11, 14]
# Output: 3

# def count_even(*numbers):
#     count = 0
#     for n in numbers:
#         if n % 2 == 0:
#             count += 1
#     return count
# print(f'count_even={count_even(2,5,8,11,14)}')

#2. Find the Largest Element
# Return the largest element in a list.
# Example
# Input: [12, 45, 7, 89, 23]
# Output: 89

# def largelem(*number):
#     largest=number[0]
#     for nnum in number:
#         if nnum > largest:
#             largest = num
#     return largest
# print(f'largest is {largelem(12,45,7,89,23)}')

#3. Find the Smallest Element
# Return the smallest element in a list.
# Example
# Input: [12, 45, 7, 89, 23]
# Output: 7

# def smallelem(*number):
#     smallest=number[0]
#     for num in number:
#         if num < smallest:
#             smallest=num
#             return smallest
# print(f'smallest is {smallelem(12,45,7,89,23)}')

#4. Reverse a List
# Return the list in reverse order.
# Example
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1

# def rever_list(*number):
#     rev=[]
#     for num in number:
#         rev=[num]+rev
#     return rev
# print(f'reverse list is {rever_list(1,2,3,4,5)}')

#5. Sum of All Elements
# Return the sum of all numbers in the list.
# Example
# Input: [4, 8, 10]
# Output: 22

# def sum(*list):
#     total=0
#     for num in list:
#         total+=num
#     return total
# print(f'sum of all elements is {sum(4,8,10)}')

#6. Count Occurrences
# Count how many times a target appears.
# Example
# Input: List=[1,2,3,2,4,2], Target=2
# Output: 3

# def count_occur(*list, target):
#     count=0
#     for num in list:
#         if num==target:
#             count+=1
#     return count
# print(f'Count of occurrences is {count_occur(1,2,3,2,4,2, target=2)}')


#7. Remove Duplicates
# Remove duplicates while preserving order.
# Example
# Input: [1,2,2,3,1,4]
# Output: [1,2,3,4]

# def rem_dupli(*list):
#     result=[]
#     for num in list:
#         if num not in result:
#             result.append(num)
#     return result
# print(f'Removed duplicates: {rem_dupli(1,2,2,3,1,4)}')

#8. Find the Average
# Return the average of all numbers.
# Example
# Input: [10,20,30,40]
# Output: 25.0

# def ave(*list):
#     total=0
#     for num in list:
#         total+=num
#     return total/len(list)
# print(f'Average is {ave(10,20,30,40)}')

#9. Create a List of Squares
# Return a new list containing the square of every element.
# Example
# Input: [2,3,4,5]
# Output: [4,9,16,25]

# def sq(*list):
#     result=[]
#     for num in list:
#         result.append(num**2)
#     return result
# print(f'Squares of the list: {sq(2,3,4,5)}')

#10. Count Positive Numbers
# Return the number of positive numbers.
# Example
# Input: [-2,5,0,7,-1,9]
# Output: 3

# def count_posi(list):
#     count=0
#     for num in list:
#         if num>0:
#             count+=1
#     return count
# print(f'Count of positive numbers: {count_pos([-2,5,0,7,-1,9])}')