public class Main {
    boolean checkPalindrome(String inputString) {
        String reversedStr = "";
        for (int i = 0; i < inputString.length(); i++) {
            reversedStr = inputString.charAt(i) + reversedStr;
        }
        return inputString.equals(reversedStr) ? true : false;
    }
    public static void main(String[] args) {
        Main myObject = new Main();
        System.out.println("is aabaa a palindrome?: " + myObject.checkPalindrome("aabaa")+ ".");
    }
}