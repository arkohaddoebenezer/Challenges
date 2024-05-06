<?php
function check_palindrome($inputString) {
    return $inputString === strrev($inputString);
}

$inputString = "aabaa";
$isPalindrome = check_palindrome($inputString);
echo "Is $inputString a palindrome?: " . ($isPalindrome ? 'true' : 'false') . ".";
?>
