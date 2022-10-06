# 1. A program P reads in 500 integers in the range [0..100] exepresenting the scores of 500 students. 
It then prints the frequency of each score above 50. What would be the best way for P to store the frequencies?

A. An array of 50 numbers

B. An array of 100 numbers

C. An array of 500 numbers

D. A dynamically allocated array of 550 numbers

View Answer

Ans : A
Explanation: An array of size 50 looks the best option to store number of students for each score. We need to store frequencies of scores above 50. We can ignore scores below 50 and to index the scores above 50, we can subtract 50 from the score value.

# 2. Which of these best describes an array?

A. A data structure that shows a hierarchical behavior

B. Container of objects of similar types

C. Container of objects of mixed types

D. All of the mentioned

View Answer

Ans : B
Explanation: Array contains elements only of the same type.


# 3. Let A be a square matrix of size n x n. Consider the following program. What is the expected output?

  
C = 100
for i = 1 to n do
for j = 1 to n do
{
Temp = A[i][j] + C
A[i][j] = A[j][i]
A[j][i] = Temp - C
}
for i = 1 to n do
for j = 1 to n do
Output(A[i][j]);

A. The matrix A itself

B. Transpose of matrix A

C. Adding 100 to the upper diagonal elements & subtracting 100 from diagonal elements of A

D. None of the above

View Answer

Ans : A
Explanation:If we take look at the inner statements of first loops, we can notice that the statements swap A[i][j] and A[j][i] for all i and j. Since the loop runs for all elements, every element A[l][m] would be swapped twice, once for i = l and j = m and then for i = m and j = l. Swapping twice means the matrix doesn’t change.


# 4.What is the output of the following piece of code?

  
public class array
{
public static void main(String args[])
{
int []arr = {1,2,3,4,5};
System.out.println(arr[2]);
System.out.println(arr[4]);
}
}

A. 3 and 5

B. 5 and 3

C. 2 and 4

D. 4 and 2

View Answer

Ans : A
Explanation:Array indexing starts from 0.


# 5. Consider an array A[20, 10], assume 4 words per memory cell and the base address of array A is 100. What is the address of A[11, 5] ? Assume row major storage.

A. 560

B. 565

C. 570

D. 575

View Answer

Ans : A
Explanation:No Explanation.


# 6. What is the output of the following piece of code?

  
public class array
{
public static void main(String args[])
{
int []arr = {1,2,3,4,5};
System.out.println(arr[5]);
}
}

A. 4

B. 5

C. ArrayIndexOutOfBoundsException

D. InavlidInputException

View Answer

Ans : C
Explanation: Trying to access an element beyond the limits of an array gives ArrayIndexOutOfBoundsException.

# 7. Which of the following is an illegal array definition?

A. Type COLONGE : (LIME, PINE, MUSK, MENTHOL); var a : array [COLONGE] of REAL;

B. var a : array [REAL] of REAL;

C. var a : array [‘A’…’Z’] of REAL;

D. var a : array [BOOLEAN] of REAL;

View Answer

Ans : B
Explanation:No explanation.


# 8. Which of the following concepts make extensive use of arrays?

A. Binary trees

B. Scheduling of processes

C. Caching

D. Spatial locality

View Answer

Ans : D
Explanation:Whenever a particular memory location is referred, it is likely that the locations nearby are also referred, arrays are stored as contigous blocks in memory, so if you want to access array elements, spatial locality makes it to access quickly.


# 9.Let A[1...n] be an array of n distinct numbers. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. What is the expected number of inversions in any permutation on n elements ?

A. θ(n)

B. θ(lgn)

C. θ(nlgn)

D. θ(n2)

View Answer

Ans : D
Explanation:The expected number of inversions in any permutation on n elements is θ(n2).


# 10. Which of the following operations is not O(1) for an array of sorted data. You may assume that array elements are distinct.

A. Find the ith largest element

B. Delete an element

C. Find the ith smallest element

D. All of the above

View Answer

Ans : B
Explanation:The worst case time complexity for deleting an element from array can become O(n).


# 11.The smallest element of an array's index is called its

A. lower bound.

B. upper bound.

C. range.

D. extraction.

View Answer

Ans : A


# 12. The extra key inserted at the end of the array is called a,

A. End key.

B. Stop key.

C. Sentinel.

D. Transposition.

View Answer

Ans : C
Explanation: None


# 13. The largest element of an array index is called its

A. lower bound.

B. range.

C. upper bound.

D. All of these.

View Answer

Ans : C
Explanation:None


# 14. Each array declaration need not give, implicitly or explicitly, the information about

A. the name of array

B. the data type of array

C. the first data from the set to be stored

D. the index set of the array

View Answer

Ans : C
Explanation:None


# 15. The elements of an array are stored successively in memory cells because

A. by this way computer can keep track only the address of the first element and the addresses of other elements can be calculated

B. the architecture of computer memory does not allow arrays to store other than serially

C. both of above

D. none of above

View Answer

Ans : A
Explanation:No Explanation.
