# #wekcome user
# import operator


# print ("wekcome to calculator system")
# # #ask user to enter first
# print ("please enter first number")
# # #take first number from user
# firstnumber=int (input())

# #ask user to enter operator
# print ("please enter operator")
# # #take operator from user
# operator=input()
# # #ask user to enter second number
# print ("please enter second number")
# #take second number from user
# secondnumber=int(input())
# #add 2 numbers and store them result
# if operator=="+":
#     result=firstnumber+secondnumber
# elif operator=="-":
#     result=firstnumber-secondnumber
# elif operator=="*":
#     result=firstnumber*secondnumber
# elif operator=="/":
#     result=firstnumber/secondnumber
# else:
#  operator=="//"
# result=firstnumber//secondnumber

# #print result to user
# print(result) 

# import math
# number = int(input("Enter an integer: "))

# result = math.factorial(number)

# print(f"The factorial of {number} is: {result}")
# Get an integer input from the user
# number = int(input("Enter an integer: "))

# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:

#     factorial_result = 1

    
#     for i in range(1, number + 1):
#         factorial_result *= i

    
#     print(f"The factorial of {number} is: {factorial_result}")

# for i in range(1,10):
#     for j in range(1, 13):
#         print(f"{i} x {j} = {i * j}")
#     print()
# n1=2
# n2,n3=3,4
# n1+=1
# n2+=n1
# print(f"n1= {n1} , n2= {n2} , n3= {n3}")
# L = ['t', 'a', 'r', 1, 'rokaia', '8', 'r', 'r']
# count_of_t = L.count('t')


# for item in L:
#     if item != 't':
#         print(item)
# print(f"number of r in L = {count_of_t}")



# user_input = input("Enter a list of numbers separated by spaces: ")
# numbers = [float(num) for num in user_input.split()]
# print("List of numbers:", numbers)
# if len(numbers) > 0:
#     average = sum(numbers) / len(numbers)
#     print("Average:", average)