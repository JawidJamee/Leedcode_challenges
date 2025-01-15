def addDigits(num):
    """compute the digital root of a given number"""
    sum = 0
    while num > 9:
        while num:
            sum += (num%10)
            #sum = sum + (num%10)# 0 + 8 = 8
            num = num//10
        num = sum
        sum = 0
    return num

print(addDigits(38))
print(addDigits(0))


"""
Input: 38
Step 1: 3+8=11
3+8=11
Step 2: 1+1 = 2
Output: 2

Input: 0
Already a single-digit number.
Output: 0
"""