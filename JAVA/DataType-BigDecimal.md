1. Which of the following is the advantage of BigDecimal over double?
a) Syntax
b) Memory usage
c) Garbage creation
d) Precision
View Answer

Answer: d
Explanation: BigDecimal has unnatural syntax, needs more memory and creates a great amount of garbage. But it has a high precision which is useful for some calculations like money.
2. Which of the below data type doesn’t support overloaded methods for +,-,* and /?
a) int
b) float
c) double
d) BigDecimal
View Answer

Answer: d
Explanation: int, float, double provide overloaded methods for +,-,* and /. BigDecimal does not provide these overloaded methods.
3. What will be the output of the following Java code snippet?

Note: Join free Sanfoundry classes at Telegram or Youtube
   double a = 0.02;
   double b = 0.03;
   double c = b - a;
   System.out.println(c);
 
   BigDecimal _a = new BigDecimal("0.02");
   BigDecimal _b = new BigDecimal("0.03");
   BigDecimal _c = b.subtract(_a);
   System.out.println(_c);
a)

   0.009999999999999998
   0.01
Take Java Programming Tests Now!
b)

   0.01
   0.009999999999999998
c)

   0.01
   0.01
d)

   0.009999999999999998
   0.009999999999999998
View Answer
Answer: a
Explanation: BigDecimal provides more precision as compared to double. Double is faster in terms of performance as compared to BigDecimal.
 
 
4. What is the base of BigDecimal data type?
a) Base 2
b) Base 8
c) Base 10
d) Base e
View Answer

Answer: c
Explanation: A BigDecimal is n*10^scale where n is an arbitrary large signed integer. Scale can be thought of as the number of digits to move the decimal point to left or right.
5. What is the limitation of toString() method of BigDecimal?
a) There is no limitation
b) toString returns null
c) toString returns the number in expanded form
d) toString uses scientific notation
View Answer

Answer: d
Explanation: toString() of BigDecimal uses scientific notation to represent numbers known as canonical representation. We must use toPlainString() to avoid scientific notation.
6. Which of the following is not provided by BigDecimal?
a) scale manipulation
b) + operator
c) rounding
d) hashing
View Answer

7. BigDecimal is a part of which package?
a) java.lang
b) java.math
c) java.util
d) java.io
View Answer

Answer: b
Explanation: BigDecimal is a part of java.math. This package provides various classes for storing numbers and mathematical operations.
8. What is BigDecimal.ONE?
a) wrong statement
b) custom defined statement
c) static variable with value 1 on scale 10
d) static variable with value 1 on scale 0
View Answer

Answer: d
Explanation: BigDecimal.ONE is a static variable of BigDecimal class with value 1 on scale 0.
9. Which class is a library of functions to perform arithmetic operations of BigInteger and BigDecimal?
a) MathContext
b) MathLib
c) BigLib
d) BigContext
View Answer

Answer: a
Explanation: MathContext class is a library of functions to perform arithmetic operations of BigInteger and BigDecimal.
10. What will be the output of the following Java code snippet?

public class AddDemo 
{
	public static void main(String args[]) 
        {
		BigDecimal b = new BigDecimal("23.43");
		BigDecimal br = new BigDecimal("24");
		BigDecimal bres = b.add(new BigDecimal("450.23"));
		System.out.println("Add: "+bres);
 
		MathContext mc = new MathContext(2, RoundingMode.DOWN);
		BigDecimal bdecMath = b.add(new BigDecimal("450.23"), mc);
		System.out.println("Add using MathContext: "+bdecMath);
	}
}
a) Compilation failure
b)

Add: 473.66
Add using MathContext: 4.7E+2
c)

Add 4.7E+2
Add using MathContext: 473.66
d) Runtime exception
View Answer

Answer: b
Explanation: add() adds the two numbers, MathContext provides library for carrying out various arithmetic operations.
