I figured out the solution after several attempts in python before translating to other languages, there is no record because this repo was actually inspired by the struggles to get this done, So this commit is after I have found the solution on my own.
Subsequently I would make a commit for every test I do until all test pass.

while translating to java I had a problem, some test were failing, after several unsuccessful trials I consulted my good friend ChatGPT to take a look at the code and I was surprised... I don't know when I was going to figure that out LOL.

Here is chatGPT fix

User
is this a java valid program?

ChatGPT
I'm here to help you with your Java code! Please provide the code you'd like me to review or assist you with, and I'll do my best to help.

User
Class main{
    int solution(int year) {
        return (int) Math.ceil(year/100);
        }
}

ChatGPT
Your code seems to be a Java class named main with a method named solution. However, there are a couple of things to note:

The convention in Java is to start class names with an uppercase letter. Therefore, you might want to rename your class from main to Main for better adherence to naming conventions.

The method solution takes an integer parameter year and returns the ceiling value of the division of year by 100. However, based on your method name, it's not clear what problem or solution you are addressing. The method might benefit from a more descriptive name.

Here's a slightly modified version with improved naming conventions:

java
Copy code
public class Main {
    // Rename the method for better clarity
    int getCentury(int year) {
        return (int) Math.ceil(year / 100.0);
    }
}
In this version, the class name is capitalized, and the method name is changed to getCentury to better reflect its purpose. Additionally, I added .0 to 100.0 in the division to ensure that the division is performed in floating-point arithmetic, which is necessary if you want an accurate result when calculating the century.


some test failed because I was dividing by integer instead of float.


#interesting solutions

#Solution by amar_m6 on code signal

int solution(int year) {
    return year%100==0 ? year/100 : year/100+1;
}

#Solution by Eduard_P_2 on code signal
int solution(int year) {
    return (year + 99)/ 100;
}

#Solution by Yuval_Scharf on code signal

int solution(int year) {
    return 1 + (year - 1) / 100;
}