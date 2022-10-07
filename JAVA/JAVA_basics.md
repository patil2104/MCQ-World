1. Who invented Java Programming?
a) Guido van Rossum
b) James Gosling
c) Dennis Ritchie
d) Bjarne Stroustrup
View Answer

Answer: b
Explanation: Java programming was developed by James Gosling at Sun Microsystems in 1995. James Gosling is well known as the father of Java.
2. Which statement is true about Java?
a) Java is a sequence-dependent programming language
b) Java is a code dependent programming language
c) Java is a platform-dependent programming language
d) Java is a platform-independent programming language
View Answer

Answer: d
Explanation: Java is called ‘Platform Independent Language’ as it primarily works on the principle of ‘compile once, run everywhere’.
3. Which component is used to compile, debug and execute the java programs?
a) JRE
b) JIT
c) JDK
d) JVM
View Answer

Answer: c
Explanation: JDK is a core component of Java Environment and provides all the tools, executables and binaries required to compile, debug and execute a Java Program.
4. Which one of the following is not a Java feature?
a) Object-oriented
b) Use of pointers
c) Portable
d) Dynamic and Extensible
View Answer

Answer: b
Explanation: Pointers is not a Java feature. Java provides an efficient abstraction layer for developing without using a pointer in Java. Features of Java Programming are Portable, Architectural Neutral, Object-Oriented, Robust, Secure, Dynamic and Extensible, etc.
5. Which of these cannot be used for a variable name in Java?
a) identifier & keyword
b) identifier
c) keyword
d) none of the mentioned
View Answer

Answer: c
Explanation: Keywords are specially reserved words that can not be used for naming a user-defined variable, for example: class, int, for, etc.
6. What is the extension of java code files?
a) .js
b) .txt
c) .class
d) .java
View Answer

Answer: d
Explanation: Java files have .java extension.
7. What will be the output of the following Java code?

    class increment {
        public static void main(String args[]) 
        {        
             int g = 3;
             System.out.print(++g * 8);
        } 
    }
a) 32
b) 33
c) 24
d) 25
View Answer

Answer: a
Explanation: Operator ++ has more preference than *, thus g becomes 4 and when multiplied by 8 gives 32.
output:
$ javac increment.java
$ java increment
32
8. Which environment variable is used to set the java path?
a) MAVEN_Path
b) JavaPATH
c) JAVA
d) JAVA_HOME
View Answer

Answer: d
Explanation: JAVA_HOME is used to store a path to the java installation.
9. What will be the output of the following Java program?

class output {
        public static void main(String args[]) 
        {
            double a, b,c;
            a = 3.0/0;
            b = 0/4.0;
            c=0/0.0;
 
	    System.out.println(a);
            System.out.println(b);
            System.out.println(c);
        } 
    }
a) NaN
b) Infinity
c) 0.0
d) all of the mentioned
View Answer

Answer: d
Explanation: For floating point literals, we have constant value to represent (10/0.0) infinity either positive or negative and also have NaN (not a number for undefined like 0/0.0), but for the integral type, we don’t have any constant that’s why we get an arithmetic exception.
10. Which of the following is not an OOPS concept in Java?
a) Polymorphism
b) Inheritance
c) Compilation
d) Encapsulation
View Answer

Answer: c
Explanation: There are 4 OOPS concepts in Java. Inheritance, Encapsulation, Polymorphism and Abstraction.
11. What is not the use of “this” keyword in Java?
a) Referring to the instance variable when a local variable has the same name
b) Passing itself to the method of the same class
c) Passing itself to another method
d) Calling another constructor in constructor chaining
View Answer

Answer: b
Explanation: “this” is an important keyword in java. It helps to distinguish between local variable and variables passed in the method as parameters.
12. What will be the output of the following Java program?

    class variable_scope 
    {
        public static void main(String args[]) 
        {
            int x;
            x = 5;
            {
	        int y = 6;
	        System.out.print(x + " " + y);
            }
            System.out.println(x + " " + y);
        } 
    }
a) Compilation error
b) Runtime error
c) 5 6 5 6
d) 5 6 5
View Answer

Answer: a
Explanation: Second print statement doesn’t have access to y , scope y was limited to the block defined after initialization of x.
output:
$ javac variable_scope.java
Exception in thread "main" java.lang.Error: Unresolved compilation problem: y cannot be resolved to a variable
13. What will be the error in the following Java code?

    byte b = 50;
    b = b * 50;
a) b cannot contain value 50
b) b cannot contain value 100, limited by its range
c) No error in this code
d) * operator has converted b * 50 into int, which can not be converted to byte without casting
View Answer

Answer: d
Explanation: While evaluating an expression containing int, bytes or shorts, the whole expression is converted to int then evaluated and the result is also of type int.
14. Which of the following is a type of polymorphism in Java Programming?
a) Multiple polymorphism
b) Compile time polymorphism
c) Multilevel polymorphism
d) Execution time polymorphism
View Answer

Answer: b
Explanation: There are two types of polymorphism in Java. Compile time polymorphism (overloading) and runtime polymorphism (overriding).
15. What will be the output of the following Java program?

    class leftshift_operator 
    {
        public static void main(String args[]) 
        {        
             byte x = 64;
             int i;
             byte y; 
             i = x << 2;
             y = (byte) (x << 2)
             System.out.print(i + " " + y);
        } 
    }
a) 0 256
b) 0 64
c) 256 0
d) 64 0
View Answer

Answer: c
Explanation: None.
output:
$ javac leftshift_operator.java
$ java leftshift_operator
256 0
16. What will be the output of the following Java code?

    class box 
    {
        int width;
        int height;
        int length;
    } 
    class main
    {
        public static void main(String args[]) 
        {        
             box obj = new box();
             obj.width = 10;
             obj.height = 2;
             obj.length = 10;
             int y = obj.width * obj.height * obj.length; 
             System.out.print(y);
        } 
    }
a) 100
b) 400
c) 200
d) 12
View Answer

Answer: c
Explanation: None.
output:
$ javac main.java
$ java main
200
17. What is Truncation in Java?
a) Floating-point value assigned to a Floating type
b) Floating-point value assigned to an integer type
c) Integer value assigned to floating type
d) Integer value assigned to floating type
View Answer

Answer: b
Explanation: None.
18. What will be the output of the following Java program?

    class Output 
    {
        public static void main(String args[])
        {
            int arr[] = {1, 2, 3, 4, 5};
            for ( int i = 0; i < arr.length - 2; ++i)
                System.out.println(arr[i] + " ");
        } 
    }
a) 1 2 3 4 5
b) 1 2 3 4
c) 1 2
d) 1 2 3
View Answer

Answer: d
Explanation: arr.length() is 5, so the loop is executed for three times.
output:
$ javac Output.java
$ java Output
1 2 3
19. What will be the output of the following Java code snippet?

class abc
{
    public static void main(String args[])
    {
        if(args.length>0)
        System.out.println(args.length);
    }
}
a) The snippet compiles and runs but does not print anything
b) The snippet compiles, runs and prints 0
c) The snippet compiles, runs and prints 1
d) The snippet does not compile
View Answer

Answer: a
Explanation: As no argument is passed to the code, the length of args is 0. So the code will not print.
20. What is the extension of compiled java classes?
a) .txt
b) .js
c) .class
d) .java
View Answer

Answer: c
Explanation: The compiled java files have .class extension.
21. Which exception is thrown when java is out of memory?
a) MemoryError
b) OutOfMemoryError
c) MemoryOutOfBoundsException
d) MemoryFullException
View Answer

Answer: b
Explanation: The Xms flag has no default value, and Xmx typically has a default value of 256MB. A common use for these flags is when you encounter a java.lang.OutOfMemoryError.
22. What will be the output of the following Java code?

    class String_demo 
    {
        public static void main(String args[])
        {
            char chars[] = {'a', 'b', 'c'};
            String s = new String(chars);
            System.out.println(s);
        }
   }
a) abc
b) a
c) b
d) c
View Answer

Answer: a
Explanation: String(chars) is a constructor of class string, it initializes string s with the values stored in character array chars, therefore s contains “abc”.
23. Which of these are selection statements in Java?
a) break
b) continue
c) for()
d) if()
View Answer

Answer: d
Explanation: Continue and break are jump statements, and for is a looping statement.
24. What will be the output of the following Java program?

    class recursion 
    {
        int func (int n) 
        {
            int result;
            if (n == 1)
                return 1;
            result = func (n - 1);
            return result;
        }
    } 
    class Output 
    {
        public static void main(String args[]) 
        {
            recursion obj = new recursion() ;
            System.out.print(obj.func(5));
        }
    }
a) 1
b) 120
c) 0
d) None of the mentioned
View Answer

Answer: a
Explanation: None.
Output:
$ javac Output.javac
$ java Output
1
25. What will be the output of the following Java code?

    class output 
    {
        public static void main(String args[])
        { 
           String c = "Hello i love java";
           boolean var;
           var = c.startsWith("hello");
           System.out.println(var);
        }
    }
a) 0
b) true
c) 1
d) false
View Answer

Answer: d
Explanation: startsWith() method is case sensitive “hello” and “Hello” are treated differently, hence false is stored in var.
Output:
false
26. Which of these keywords is used to define interfaces in Java?
a) intf
b) Intf
c) interface
d) Interface
View Answer

Answer: c
Explanation: interface keyword is used to define interfaces in Java.
27. What will be the output of the following Java program?

    class output 
    {
        public static void main(String args[])
        { 
           StringBuffer s1 = new StringBuffer("Quiz");
           StringBuffer s2 = s1.reverse();
           System.out.println(s2);
        }
    }
a) QuizziuQ
b) ziuQQuiz
c) Quiz
d) ziuQ
View Answer

Answer: d
Explanation: reverse() method reverses all characters. It returns the reversed object on which it was called.
Output:
$ javac output.java
$ java output
ziuQ
28. What will be the output of the following Java code?

    class Output 
    {
        public static void main(String args[]) 
        {
            Integer i = new Integer(257);  
            byte x = i.byteValue();
            System.out.print(x);
        }
    }
a) 257
b) 256
c) 1
d) 0
View Answer

Answer: c
Explanation: i.byteValue() method returns the value of wrapper i as a byte value. i is 257, range of byte is 256 therefore i value exceeds byte range by 1 hence 1 is returned and stored in x.
Output:
$ javac Output.java
$ java Output
1
29. What will be the output of the following Java program?

    class Output 
    {
         public static void main(String args[]) 
        {
            double x = 2.0;  
            double y = 3.0;
            double z = Math.pow( x, y );
            System.out.print(z);
        }
    }
a) 9.0
b) 8.0
c) 4.0
d) 2.0
View Answer

Answer: b
Explanation: Math.pow(x, y) methods returns value of y to the power x, i:e x ^ y, 2.0 ^ 3.0 = 8.0.
Output:
$ javac Output.java
$ java Output
8.0
30. Which of the following is a superclass of every class in Java?
a) ArrayList
b) Abstract class
c) Object class
d) String
View Answer

Answer: c
Explanation: Object class is superclass of every class in Java.
31. What will be the output of the following Java code?

    class Output 
    {
         public static void main(String args[]) 
         {
             double x = 3.14;  
             int y = (int) Math.ceil(x);
             System.out.print(y);
         }
    }
a) 3
b) 0
c) 4
d) 3.0
View Answer

Answer: c
Explanation: ciel(double X) returns the smallest whole number greater than or equal to variable x.
Output:
$ javac Output.java
$ java Output
4
32. What will be the output of the following Java program?

    import java.net.*;
    class networking 
    {
        public static void main(String[] args) throws Exception 
        {
            URL obj = new URL("https://www.sanfoundry.com/javamcq");
            URLConnection obj1 = obj.openConnection();
            int len = obj1.getContentLength();
            System.out.print(len);
        }
    }
Note: Host URL is having length of content 127.
a) 127
b) 126
c) Runtime Error
d) Compilation Error
View Answer

Answer: a
Explanation: None.
Output:
$ javac networking.java
$ java networking 
127
33. Which of the below is not a Java Profiler?
a) JProfiler
b) Eclipse Profiler
c) JVM
d) JConsole
View Answer

Answer: c
Explanation: Memory leak is like holding a strong reference to an object although it would never be needed anymore. Objects that are reachable but not live are considered memory leaks. Various tools help us to identify memory leaks.
34. What will be the output of the following Java program?

    import java.net.*;
    class networking
    {
        public static void main(String[] args) throws MalformedURLException
        {
            URL obj = new URL("https://www.sanfoundry.com/javamcq");
            System.out.print(obj.toExternalForm());
        }
    }
a) www.sanfoundry.com
b) https://www.sanfoundry.com/javamcq
c) sanfoundry
d) sanfoundry.com
View Answer

Answer: b
Explanation: toExternalForm() is used to know the full URL of an URL object.
Output:
$ javac networking.java
$ java networking 
https://www.sanfoundry.com/javamcq
35. What will be the output of the following Java code snippet?

    import java.util.*;
    class Arraylists 
    {
        public static void main(String args[]) 
        {
            ArrayLists obj = new ArrayLists();
            obj.add("A");
            obj.add("B");
            obj.add("C");
            obj.add(1, "D");
            System.out.println(obj);
        }
    }
a) [A, D, C]
b) [A, B, C]
c) [A, B, C, D]
d) [A, D, B, C]
View Answer

Answer: d
Explanation: obj is an object of class ArrayLists hence it is an dynamic array which can increase and decrease its size. obj.add(“X”) adds to the array element X and obj.add(1,”X”) adds element x at index position 1 in the list, Hence obj.add(1,”D”) stores D at index position 1 of obj and shifts the previous value stored at that position by 1.
Output:
$ javac Arraylist.java
$ java Arraylist
[A, D, B, C].
36. Which of these packages contains the exception Stack Overflow in Java?
a) java.io
b) java.system
c) java.lang
d) java.util
View Answer

Answer: c
Explanation: None.
37. What will be the output of the following Java program?

    import java.util.*;
    class Collection_iterators 
    {
        public static void main(String args[]) 
        {
            LinkedList list = new LinkedList();
            list.add(new Integer(2));
            list.add(new Integer(8));
            list.add(new Integer(5));
            list.add(new Integer(1));
            Iterator i = list.iterator();
            Collections.reverse(list);
	    Collections.sort(list);
            while(i.hasNext())
	        System.out.print(i.next() + " ");
        }
    }
a) 1 2 5 8
b) 2 1 8 5
c) 1 5 8 2
d) 2 8 5 1
View Answer

Answer: a
Explanation: Collections.sort(list) sorts the given list, the list was 2->8->5->1 after sorting it became 1->2->5->8.
Output:
1 2 5 8
38. Which of these statements is incorrect about Thread?
a) start() method is used to begin execution of the thread
b) run() method is used to begin execution of a thread before start() method in special cases
c) A thread can be formed by implementing Runnable interface only
d) A thread can be formed by a class that extends Thread class
View Answer

Answer: b
Explanation: run() method is used to define the code that constitutes the new thread, it contains the code to be executed. start() method is used to begin execution of the thread that is execution of run(). run() itself is never used for starting execution of the thread.
39. Which of these keywords are used for the block to be examined for exceptions?
a) check
b) throw
c) catch
d) try
View Answer

Answer: d
Explanation: try is used for the block that needs to checked for exception.
40. What will be the output of the following Java code?

    class newthread extends Thread
    {
	Thread t;
	newthread()
        {
	    t1 = new Thread(this,"Thread_1");
	    t2 = new Thread(this,"Thread_2");
	    t1.start();
	    t2.start();
	}
	public void run()
        {
	    t2.setPriority(Thread.MAX_PRIORITY);	
	    System.out.print(t1.equals(t2));
        }    
    }
    class multithreaded_programing
    {
        public static void main(String args[])
        {
            new newthread();        
        }
    }
a) truetrue
b) falsefalse
c) true
d) false
View Answer

Answer: b
Explanation: This program was previously done by using Runnable interface, here we have used Thread class. This shows both the method are equivalent, we can use any of them to create a thread.
Output:
$ javac multithreaded_programing.java
$ java multithreaded_programing
falsefalse
41. Which one of the following is not an access modifier?
a) Protected
b) Void
c) Public
d) Private
View Answer

Answer: b
Explanation: Public, private, protected and default are the access modifiers.
42. What will be the output of the following Java program?

   final class A 
    {
         int i;
    }    
    class B extends A 
    {
        int j;
        System.out.println(j + " " + i);  
    }    
    class inheritance 
    {
        public static void main(String args[])
        {
            B obj = new B();
            obj.display();     
        }
   }
a) 2 2
b) 3 3
c) Runtime Error
d) Compilation Error
View Answer

Answer: d
Explanation: class A has been declared final hence it cannot be inherited by any other class. Hence class B does not have member i, giving compilation error.
output:
$ javac inheritance.java
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	i cannot be resolved or is not a field
43. What is the numerical range of a char data type in Java?
a) 0 to 256
b) -128 to 127
c) 0 to 65535
d) 0 to 32767
View Answer

Answer: c
Explanation: Char occupies 16-bit in memory, so it supports 216 i:e from 0 to 65535.
44. Which class provides system independent server side implementation?
a) Server
b) ServerReader
c) Socket
d) ServerSocket
View Answer

Answer: d
Explanation: ServerSocket is a java.net class which provides system independent implementation of server side socket connection.
45. What will be the output of the following Java program?

   class overload 
   {
        int x;
 	double y;
        void add(int a , int b) 
        {
            x = a + b;
        }
        void add(double c , double d)
        {
            y = c + d;
        }
        overload() 
        {
            this.x = 0;
            this.y = 0;
        }        
    }    
    class Overload_methods 
    {
        public static void main(String args[])
        {
            overload obj = new overload();   
            int a = 2;
            double b = 3.2;
            obj.add(a, a);
            obj.add(b, b);
            System.out.println(obj.x + " " + obj.y);     
        }
   }
a) 4 6.4
b) 6.4 6
c) 6.4 6.4
d) 6 6
View Answer

Answer: a
Explanation: For obj.add(a,a); ,the function in line number 4 gets executed and value of x is 4. For the next function call, the function in line number 7 gets executed and value of y is 6.4
output:
$ javac Overload_methods.java
$ java Overload_methods 
4 6.4
46. Which of the following is true about servlets?
a) Servlets can use the full functionality of the Java class libraries
b) Servlets execute within the address space of web server, platform independent and uses the functionality of java class libraries
c) Servlets execute within the address space of web server
d) Servlets are platform-independent because they are written in java
View Answer

Answer: b
Explanation: Servlets execute within the address space of a web server. Since it is written in java it is platform independent. The full functionality is available through libraries.
