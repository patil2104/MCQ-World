1. What is the numerical range of a char data type in Java?
a) -128 to 127
b) 0 to 256
c) 0 to 32767
d) 0 to 65535
View Answer

Answer: d
Explanation: Char occupies 16-bit in memory, so it supports 216 i:e from 0 to 65535.
2. Which of these coding types is used for data type characters in Java?
a) ASCII
b) ISO-LATIN-1
c) UNICODE
d) None of the mentioned
View Answer

Answer: c
Explanation: Unicode defines fully international character set that can represent all the characters found in all human languages. Its range is from 0 to 65536.
3. Which of these values can a boolean variable contain?
a) True & False
b) 0 & 1
c) Any integer value
d) true
View Answer

Answer: a
Explanation: Boolean variable can contain only one of two possible values, true and false.
4. Which of these occupy first 0 to 127 in Unicode character set used for characters in Java?
a) ASCII
b) ISO-LATIN-1
c) None of the mentioned
d) ASCII and ISO-LATIN1
View Answer

Answer: d
Explanation: First 0 to 127 character set in Unicode are same as those of ISO-LATIN-1 and ASCII.
Sanfoundry Certification Contest of the Month is Live. 100+ Subjects. Participate Now!
5. Which one is a valid declaration of a boolean?
a) boolean b1 = 1;
b) boolean b2 = ‘false’;
c) boolean b3 = false;
d) boolean b4 = ‘true’
View Answer

Answer: c
Explanation: Boolean can only be assigned true or false literals.
6. What will be the output of the following Java program?

Check this: Programming Books | Java Books
    class array_output {
        public static void main(String args[]) 
        {    
            char array_variable [] = new char[10];
	    for (int i = 0; i < 10; ++i) {
                array_variable[i] = 'i';
                System.out.print(array_variable[i] + "" );
                i++;
            }
        } 
    }
a) i i i i i
b) 0 1 2 3 4
c) i j k l m
d) None of the mentioned
View Answer

Answer: a
Explanation: None.
output:
$ javac array_output.java
$ java array_output
i i i i i
7. What will be the output of the following Java program?

    class mainclass {
        public static void main(String args[]) 
        {
            char a = 'A';
            a++;
	    System.out.print((int)a);
        } 
    }
a) 66
b) 67
c) 65
d) 64
View Answer

Answer: a
Explanation: ASCII value of ‘A’ is 65, on using ++ operator character value increments by one.
output:
$ javac mainclass.java
$ java mainclass
66
8. What will be the output of the following Java program?

    class mainclass {
        public static void main(String args[]) 
        {
            boolean var1 = true;
	    boolean var2 = false;
	    if (var1)
	        System.out.println(var1);
	    else
	        System.out.println(var2);
       } 
    }
a) 0
b) 1
c) true
d) false
View Answer

Answer: c
Explanation: None.
output:
$ javac mainclass.java
$ java mainclass
true
9. What will be the output of the following Java code?

    class booloperators {
        public static void main(String args[]) 
        {
            boolean var1 = true;
	    boolean var2 = false;
	    System.out.println((var1 & var2));
        } 
    }
a) 0
b) 1
c) true
d) false
View Answer

Answer: d
Explanation: boolean ‘&’ operator always returns true or false. It returns true when both the values are true and false otherwise. Since, var1 is defined true and var2 is defined false hence their ‘&’ operator result is false.
output:

$ javac booloperators.java
$ java booloperators
false
10. What will be the output of the following Java code?

    class asciicodes {
        public static void main(String args[]) 
        {
            char var1 = 'A';
	    char var2 = 'a';
	    System.out.println((int)var1 + " " + (int)var2);
        } 
    }
a) 162
b) 65 97
c) 67 95
d) 66 98
View Answer

Answer: b
Explanation: ASCII code for ‘A’ is 65 and for ‘a’ is 97.
output:
$ javac asciicodes.java
$ java asciicodes
65 97
