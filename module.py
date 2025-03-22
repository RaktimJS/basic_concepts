"""

+-------------------------------------------------------------------+
|***------------   MYMODULE   ------------***                       |
|                                                                   |
|                                                                   |
|Author: Raktim JS                                                  |
|Institution: Pathsala Public School, Pathsala, Seuj Nagar, 781325  |
|Date: 16/10/2024                                                   |
|Email: raktimunreal4@gmail.com                                     |
|                                                                   |
|                                                                   |
|                        DO NOT PLAGIARISE                          |
|                                                                   |
|                                                                   |
|Includes functions to:                                             |
|        1. FIND FACTORIAL                                          |
|        2. CHECK PRIMES                                            |
|        3. CHECK IF A NUMBER IS EVEN OR ODD                        |
|        4. PRINT REVERSE OF A NUMBER                               |
|        5. CHECK IF A NUMBER IS PALINDROME                         |
|        6. CHECK IF A NUMBER IS ARMSTRONG                          |
|        7. CHECK DIVISIBILITY OF 2 NUMBERS                         |
|        8. COUNT NUMBER OF DIGITS OF A NUMBER                      |
|        9. FIND SUM OF DIGITS OF A NUMBER                          |
|        10. PRINT DIGITS OF A NUMBER IN WORDS                      |
+-------------------------------------------------------------------+

"""




import math




# Factorial function
def factorial(num):
        currentNum = 1
        base = 1

        if num < 0:
                print(f"Since {num} negative, it is being set to {num * (-1)}\n")
                num = num * (-1)

                while currentNum <= num:
                        base = base * currentNum
                        currentNum += 1

                print(f"\n{num}! = {base}")
        elif num > 0:
                while currentNum <= num:
                        base = base * currentNum
                        currentNum += 1

                print(f"\n{num}! = {base}")
        else:
                base = 1

                print(f"\n{num}! = {base}")

# Check Primes function
def isPrime(num):
        counter = 3
        isPrime_Var = True

        if num == 2:
                isPrime_Var = True
        elif num % 2 == 0 or num <= 0 or num == 1:
                isPrime_Var = False
        else:
                while counter < num**(0.5):
                        if num % counter == 0:
                                isPrime_Var = False
                                break
                        elif num % counter != 0:
                                isPrime_Var = True
                        
                        counter += 1
                
        if isPrime_Var == True:
                print("\nYes, the number is a prime!")
        else:
                print("\nNo, the number is not a prime!")


# Check Odd/Even function
def oddOrEven(num):
        if num % 2 == 0:
                print("The number is even")
        else: print("The number is odd")


# Reverse number maker function
def reverse(num):
        placeholder = num
        num = abs(num)
        placeholder2 = num
        revNum = 0

        while num > 0:
                revNum = (10*revNum) + (num % 10)
                num = math.floor(num/10)
        
        if placeholder < 0:
                print(f"\nThe reverse of -{placeholder2} is -{revNum}")
        else:
                print(f"\nThe reverse of {placeholder2} is {revNum}")


# Palindrome checker function
def isPalindrome(num):
        placeholder = num
        num = num.lower()
        revStr = ""

        for i in num:
                revStr = i + revStr

        if placeholder.lower() == revStr:
                print(f"\nYes! {placeholder.upper()} is palindrome")
        else:
                print(f"\nNo! {placeholder.upper()} is not palindrome")


# Armstrong number checker function
def isArmstrong(num):
        placeholder = num
        sum_Of_Cubes = 0

        while num > 0:
                sum_Of_Cubes = sum_Of_Cubes + (num % 10) ** 3
                num = math.floor(num/10)

        if sum_Of_Cubes == placeholder:
                print(f"Yes! {placeholder} is an Armstrong number")
        else: print(f"No! {placeholder} is not an Armstrong number")


# Divisibility checker function
def divisible(num1, num2):
        if num1 % num2 == 0 and num2 != 0:
                print(f"Yes! {num1} is divisible by {num2}")
        elif num2 == 0:
                print("Division by 0 is invalid")
        else: 
                print(f"No! {num1} is not divisible by {num2}")


# Number of digits counter function
def numOfDigits(num):
        placeholder = num
        digits = 0

        for i in str(num):
                digits += 1

        if placeholder < 0:
                print(f"{placeholder} has {digits - 1} number of digits")
        else:
                print(f"{placeholder} has {digits} number of digits")


# Sum of digits of a number finder functions
def sumOfDigits(num):
        placeholder = num
        num = abs(num)
        # numString = str(num)
        finalSum = 0

        for i in str(num):
                finalSum = finalSum + (num % 10)
                num = math.floor(num/10)

        print(f"Sum of digits of {placeholder} is {finalSum}")


# Digits of a number to word function
def toWord(num):
        placeholder = num
        placeholder2 = num
        revNum = 0
        zeroCounter = 0
        zeroWriter = 0

        while num > 0:
                revNum = (10*revNum) + (num % 10)
                num = math.floor(num/10)

        while placeholder % 10 == 0:
                zeroCounter += 1
                placeholder = math.floor(placeholder/10)

        while revNum > 0 :
                if revNum % 10 == 0:
                        print("Zero", end=" ")
                elif revNum % 10 == 1:
                        print("One", end=" ")
                elif revNum % 10 == 2:
                        print("Two", end=" ")
                elif revNum % 10 == 3:
                        print("Three", end=" ")
                elif revNum % 10 == 4:
                        print("Four", end=" ")
                elif revNum % 10 == 5:
                        print("Five", end=" ")
                elif revNum % 10 == 6:
                        print("Six", end=" ")
                elif revNum % 10 == 7:
                        print("Seven", end=" ")
                elif revNum % 10 == 8:
                        print("Eight", end=" ")
                else:
                        print("Nine", end=" ")

                revNum = math.floor(revNum / 10)
        
        while zeroWriter < zeroCounter:
                print("Zero", end=" ")
                zeroWriter += 1

# SPECIAL: Function to desrcibe all functions:
def description():
        print("1. FACTORIAL: Multiplies all the numbers from a specific number to 1 (both included)\n")
        print("2. PRIME NUMBER: A number having only 2 factors, 1 and the number itself\n")
        print("3. EVEN: A number divisible by 2; ODD: A number not divisible by 2\n")
        print("4. REVERSE: Writes a number in reverse\n")
        print("5. PALINDROME: A string or a number which is the same as original if written in reverse\n")
        print("6. ARMSTRONG NUMBER: A number whose sum of cubes of its digits equal to the original number\n")
        print("7. DIVISIBILITY: Checks if the 1st user input is divisible by the 2nd user input\n")
        print("8. NUMBER OF DIGITS: Counts the number of digits in a number\n")
        print("9. SUM OF DIGITS: Finds the sum of all the digits of a number\n")
        print("10. DIGITS to WORD: Writes every single digit as word in any number\n")


# SPECIAL: Function to generate password
def pswrd(string):
        encoded = ''
        ASCII = ''
        
        for i in string:
                stringOrd_i = str(ord(i))
                encoded = encoded + stringOrd_i
        
        ASCII = encoded

        if ASCII == '7210110810811187111114108100':
                return True
        else:
                return False        

        encoded = ''
        ASCII = ''
        i = None
        stringOrd_i = None
