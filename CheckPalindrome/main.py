class Main:
    def check_palindrome(self,inputString):
        if(inputString==(inputString[::-1])):
            return True
        else:
            return False
my_object = Main()
inputString = "aabaa"
isPalindrome= my_object.check_palindrome(inputString)
print(f"is {inputString}a palindrome?: {isPalindrome}.")
