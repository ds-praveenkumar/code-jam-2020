
***1. Vestigium (google code JAM Qualifer )***
###
Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).

An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is a natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated values.
* Input:<br />
The first line of the input gives the number of test cases, T. T test cases follow. Each starts with a line containing a single integer N: the size of the matrix to explore. Then, N lines follow. The i-th of these lines contains N integers Mi,1, Mi,2 ..., Mi,N. Mi,j is the integer in the i-th row and j-th column of the matrix.
* Output: <br />
For each test case, output one line containing Case #x: k r c, where x is the test case number (starting from 1), k is the trace of the matrix, r is the number of rows of the matrix that contain repeated elements, and c is the number of columns of the matrix that contain repeated elements.
* Constraints: <br />
Time limit: 20 seconds per test set.<br />
Memory limit: 1GB.<br />
1 ≤ T ≤ 100.<br />
2 ≤ N ≤ 100.<br />
1 ≤ Mi,j ≤ N, for all i, j.<br />
* Input <br/>
1 <br/>
4 <br/>
1 2 3 4 <br/>
2 1 4 3 <br/>
3 4 1 2 <br/>
4 3 2 1 <br/>
* Output: <br />
4 0 0
* Explanation : <br />
the input is a natural Latin square, which means no row or column has repeated elements. All four values in the main diagonal are 1, and so the trace (their sum) is 4.

***2. Nesting Depths***
###
Given a string of digits S, insert a minimum number of opening and closing parentheses into it such that the resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.

Let the nesting of two parentheses within a string be the substring that occurs strictly between them. An opening parenthesis and a closing parenthesis that is further to its right are said to match if their nesting is empty, or if every parenthesis in their nesting matches with another parenthesis in their nesting. The nesting depth of a position p is the number of pairs of matching parentheses m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth: 0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1). The first three strings have minimum length among those that have the same digits in the same order, but the last one does not since ((22)1) also has the digits 221 and is shorter.

Given a string of digits S, find another string S', comprised of parentheses and digits, such that:
all parentheses in S' match some other parenthesis,
removing any and all parentheses from S' results in S,
each digit in S' is equal to its nesting depth, and
S' is of minimum length.
* Input:<br />
The first line of the input gives the number of test cases, T. T lines follow. Each line represents a test case and contains only the string S.
* Output: <br />
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the string S' defined above.
* Constraints: <br />
Time limit: 20 seconds per test set.<br />
Memory limit: 1GB.<br />
1 ≤ T ≤ 100.<br />
1 ≤ length of S ≤ 100.<br />
* Input <br/>
Each character in S is either 0 or 1.
* Output: <br />
Each character in S is a decimal digit between 0 and 9, inclusive.
* Explanation : <br />
Input<br />
4<br />
0000<br />
101<br />
111000<br />
1<br />
#
Output<br />
Case #1: 0000<br />
Case #2: (1)0(1)<br />
Case #3: (111)000<br />
Case #4: (1)<br />