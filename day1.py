# Loops

# For loops iterate over a given sequence.

# numbers = [2,3,4,3,4,5]
# for i in numbers:
#     print(i)



# Break Statement - Stop the loop
# sting = 'ManjitLuheraIsthebest'
# for s in sting:
#     if s == 'L':
#         break
#     print(s)

# Continue Statement - skip the current block and return the next
# sting = 'ManjitLuheraIsthebest'
# for s in sting:
#     if s == 'L':
#         continue
#     print(s)

# Range function - return a sequence of numbers starting with 0 , ends -1

# for i in range(10):
#     print(i+1)


# ------------------------------------------------------------------------------------

# While Loop - Execute a set of statement as long as condition is True

# num1 = 0

# while num1<10:
#     print(f'Num {num1}')
#     num1 = num1 + 1


# --------------------------------------------------------------------------------------

# Question practice

# 1. Write a Python program that uses a for loop to find and print the sum of all even numbers from 1 to 50.

# even_num = 0

# for number in range(1,51):
#     if number % 2 == 0:
#         even_num = number + even_num

# print("sum of even number from 1 to 50 is :",even_num)

# 2. Factorial Calculation:
#    Create a Python program that calculates and prints the factorial of a given number using a for loop. Take the input from the user.


number = int(input("Enter your number to calculate its factorial"))

if number < 1:
    print("invalid Number")
else: 
    factorial_num = 1

    for i in range(1,number + 1):
        factorial_num = i * factorial_num

print(factorial_num)




        
