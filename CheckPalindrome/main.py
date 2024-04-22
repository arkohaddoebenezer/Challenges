def check_palindrome(inputString):
    return inputString == inputString[::-1]
inputString = "aabaa"
isPalindrome= check_palindrome(inputString)
print(f"is {inputString}a palindrome?: {isPalindrome}.")
