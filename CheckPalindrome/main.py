class Main:
    def check_palindrome(self,inputString):
        return inputString == inputString[::-1]
my_object = Main()
inputString = "aabaa"
isPalindrome= my_object.check_palindrome(inputString)
print(f"is {inputString}a palindrome?: {isPalindrome}.")
