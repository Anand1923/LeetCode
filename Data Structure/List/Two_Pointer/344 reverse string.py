def reverse(num):
    i=0
    j=len(num)-1
    while (i<j):
        num[i],num[j]=num[j],num[i]
        i+=1
        j-=1



#Leetcode 344
def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0
    MAX_INT = 2**31 - 1

    while x > 0:
        digit = x % 10
        if reversed_num > MAX_INT // 10 or (reversed_num == MAX_INT // 10 and digit > 7):
            return 0
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return sign * reversed_num if -2**31 <= reversed_num <= MAX_INT else 0

 
# 🧠 Step-by-Step Thought Process 
# 🔍 1. Understand the Problem 

# You're given an integer (positive or negative), and you need to reverse its digits. 

# Examples:  

#     Input: 123 → Output: 321
#     Input: -123 → Output: -321
#     Input: 120 → Output: 21
     

# Also, if the reversed number overflows a 32-bit signed integer , return 0. 

#     32-bit signed int range: from -2³¹ to 2³¹ - 1 , i.e., -2147483648 to 2147483647  
     

# ✨ 2. Think About How You Reverse Digits 

# You can't just flip the number like a string (though that’s a possible solution). But for better efficiency, try doing it digit by digit using math . 

# So, think: 

#     "I’ll take one digit at a time from the end of the number..."
#     "...and build the reversed number step by step."
     

# This leads to: 
# python
 
 
# 1
# 2
# 3
# digit = x % 10   # get last digit
# x = x // 10      # remove last digit
# reversed_num = reversed_num * 10 + digit
 
 
 
# 🧮 3. Handle the Sign 

# Before reversing, save the sign so you can apply it back later. 
# python
 
 
# 1
# 2
# sign = -1 if x < 0 else 1
# x = abs(x)
 
 
 
# ⚠️ 4. Handle Overflow 

# Since Python doesn’t restrict integers, you must manually check  whether the reversed number would overflow a 32-bit signed integer before  it happens. 

# Use this condition before updating reversed_num: 
# python
 
 
# 1
# 2
# ⌄
# if reversed_num > (MAX_INT - digit) // 10:
#     return 0
 
 
 

# Where MAX_INT = 2**31 - 1 
# ✅ 5. Put It All Together 

# Now combine all steps into a function. 
# 🧪 Final Simple Thought Flow Summary 

#     Check the sign  → store it.
#     Work with absolute value  of the number.
#     Loop through each digit :
#         Get the last digit (x % 10)
#         Remove it from the original number (x //= 10)
#         Build the reversed number (reversed_num = reversed_num * 10 + digit)
#         Before building , check for overflow 
         
#     Apply the sign  at the end.
#     Return  reversed number or 0 if overflow.
     
