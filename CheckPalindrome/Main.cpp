#include <iostream>
#include <algorithm>
using namespace std;

bool checkPalindrome(string inputString) {
    if (inputString.size() < 2)
        return true;
    if (inputString[0] != inputString.back())
        return false;
    return checkPalindrome(inputString.substr(1, inputString.size() - 2));
}

int main() {
    string inputString = "aabaa";
    bool isPalindrome = checkPalindrome(inputString);
    cout << "Is " << inputString << " a palindrome?: " << isPalindrome << ".";
    return 0;
}