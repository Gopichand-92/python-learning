#1. Count Total Keys
# Task:
# Write a function that returns the total number of keys in a dictionary.
# Example Input:
# {"a":10,"b":20,"c":30}
# Example Output:
# 3

# def countkeys(**dic):
#     count=0
#     for key in dic:
#         count+=1
#     return count

# totkeys = countkeys(a=10, b=20, c=30)
# print(f'the total count of keys is {totkeys}')


#2. Find the Key with the Largest Value
# Task:
# Return the key whose value is the largest.
# Example Input:
# {"Math":78,"Science":92,"English":85}
# Example Output:
# Science

# def largeval(**dic):
#     largest=0
#     key=""
#     for d in dic:
#         if dic[d] > largest:
#             largest=dic[d]
#             key=d
#     return 
# sub=largeval(math=78,science=92,english=85)
# print(f'The largest value is {sub}')  

#3. Find the Key with the Smallest Value
# Task:
# Return the key whose value is the smallest.
# Example Input:
# {"Math":78,"Science":92,"English":65}
# Example Output:
# English

# def smallestval(**dic):
#     smallest=float('inf')
#     key=""
#     for d in dic:
#         if dic[d] < smallest:
#             samllest=dic[d]
#             key=d
#     return key
# sub=smallestval(math=78,science=92,english=64)
# print(f'the key with the smallest value is {sub}')

#4. Sum of All Values
# Task:
# Return the sum of all values in the dictionary.
# Example Input:
# {"Pen":20,"Book":150,"Bag":500}
# Example Output:
# 670

# def sumval(**dic):
#     total=0
#     for d in dic:
#         total+=dic[d]
#     return total
# items=sumval(pen=20,book=150,bag=500)
# print(f'the sum of all values is {items}')

#5. Count Even Values
# Task:
# Return how many values in the dictionary are even.
# Example Input:
# {"a":10,"b":7,"c":16,"d":5}
# Example Output:
# 2

# def counteven(**val):
#     count=0
#     for v in val:
#         if val[v]%2==0:
#             count+=1
#     return count
# dic=counteven(a=10,b=7,c=16,d=5)
# print(f'the total count even values are {dic}')

#6. Count Values Greater Than a Target
# Task:
# Given a target number, count how many dictionary values are greater than it.
# Example Input:
# Dictionary={"A":45,"B":80,"C":65,"D":90}
# Target=70
# Example Output:
# 2

# def countval(target,**val):
#     count=0
#     for v in val:
#         if val[v]>target:
#             count+=1
#     return count
# dic=countval(a=45,b=80,c=65,d=90,target=70)
# print(f'the count values greater than a target is {dic} ')

#7. Create a Dictionary of Squares
# Task:
# Given a list of numbers,
#  create a dictionary where the number is the key and its square is the value.
# Example Input:
# [2,3,4,5]
# Example Output:
# {2:4,3:9,4:16,5:25}

# def sq(*numbers):
#     result={}
#     for num in numbers:
#         result[num]=num**2
#     return result
# dic=sq(2,3,4,5)
# print(dic)

#8. Count Positive Values
# Task:
# Return the number of positive values in the dictionary.
# Example Input:
# {"a":-5,"b":10,"c":0,"d":8}
# Example Output:
# 2

# def countpos(**dic):
#     count=0
#     for d in dic:
#         if dic[d] > 0:
#             count += 1
#     return count
# result = countpos(a=-5, b=10, c=0, d=8)
# print(f"The number of positive values is {result}")

#9. Find the Average of All Values
# Task:
# Return the average of all values in the dictionary.
# Example Input:
# {"A":10,"B":20,"C":30}
# Example Output:
# 20.0

# def avgval(**dic):
#     total = 0
#     count = 0
#     for d in dic:
#         total += dic[d]
#         count += 1
#     return total / count
# result = avgval(A=10, B=20, C=30)
# print(f"The average of all values is {result}")


#10. Reverse Key and Value
# Task:
# Create a new dictionary where the values become keys and the keys become values.
# Example Input:
# {"A":1,"B":2,"C":3}
# Example Output:
# {1:"A",2:"B",3:"C"}

# def rev(**dic):
#     result = {}
#     for d in dic:
#         result[dic[d]]=d
#     return result
# val=rev(A=1, B=2, C=3)
# print(val)

