## ECE 653 Assignment 1

### Question 1

1. `a = [], b = []`. The fault is at row 8, and if the input is `a = [], b = []`, the program will crash at row 7, which does not execute the fault.

2. When a and b are square matrix and the dimension is same, for example `a = [[1, 2], [3, 4]], b = [[1, 2], [3, 4]]`.

3. Any list that the dimension is incompatible, for example, `a = [[1]], b = [[2], [1]]`an exception is thrown (which is expected and is not a failure).

4. ```python
   a = [[5, 7], [8, 21]]
   b = [[8], [4]]
   p = 2
   p1 = 1
   pc = at line 10
   ```

5. ```c
   digraph G {
       "7, 8" -> "9";
       "9" -> "10" [label = "T"];
       "9" -> "11" [label = "F"];
       "11" -> "12";
       "12" -> "15" [label = "F"];
       "12" -> "13" [label = "T"];
       "13" -> "12" [label = "F"];
       "13" -> "14" [label = "T"];
       "14" -> "13";
   }
   ```

   ![](D:\Waterloo\term3\ECE 653\Assignment\k47xie\a1\q1.png)

### Question 2

1. ```python
   class RepeatUntilStmt():
       def __init__(self, statement, condition):
           self.statement = statement
           self.condition = conditon
           
       def __eq__(self, other):
           return (
               type(self) == type(other)
               and self.statement == other.statement
               and self.condition == other.condition
           )
   ```

2. $$
   \begin{equation*}
   \frac{< S,q >\Downarrow q^{'} \ < b,q^{'}  >\Downarrow false\ < repeat\ S\ until\ b,q^{'}  >\Downarrow q^{''}}{< repeat\ S\ until\ b,q^{'}  >\Downarrow q^{''}}
   \end{equation*}
   $$

   $$
   \begin{equation*}
   \frac{< S,q >\Downarrow q^{'} \ < b,q^{'}  >\Downarrow true}{< repeat\ S\ until\ b,q^{'}  >\Downarrow q^{'}}
   \end{equation*}
   $$

   

3. ![](D:\Waterloo\term3\ECE 653\Assignment\k47xie\a1\q2.png)

4. We need to prove:
   $$
   < \mathbf{repeat\ } S\ \mathbf{until} \ b,\ q >\Downarrow \ q^{''} \ \Leftrightarrow \ < S;\ \mathbf{if} \ b\ \mathbf{then} \ skip\ \mathbf{else} \ (\mathbf{repeat} \ S\ \mathbf{until} \ b) ,\ q >\Downarrow q^{''}
   $$
   For the left side we have:
   $$
   \frac{\frac{< S,\ q >\ \Downarrow \ q^{'} \ < q^{'} ,\ b >\ \Downarrow \ false}{< \mathbf{repeat\ } S >} \ \frac{< S,\ q >\ \Downarrow \ q^{''} \ < q^{''} ,\ b >\ \Downarrow \ True}{skip}}{< S;\mathbf{if} \ b\ \mathbf{then} \ skip\ \mathbf{else} \ (\mathbf{repeat} \ S\ \mathbf{until} \ b)  >}
   $$
   For the right side we have:
   $$
   \frac{< S,\ q >\ \Downarrow \ q'\ < q^{'} ,\ b >\ \Downarrow \ \mathbf{repeat} \ < q^{'} ,\ b >\ \Downarrow \ skip}{< \mathbf{repeat\ } S\ \mathbf{until} \ b >}
   $$
   In this case, we can prove $left \Rightarrow right$.

   For the reverse prove, for the left side we have:
   $$
   < \mathbf{repeat} \ S\ \mathbf{until} \ b,q^{'}  >\Downarrow q^{''}
   $$
   For the right side we have:
   $$
   < skip,\ q^{'}  >\ \Downarrow \ q^{''}
   $$
   We know $q^{'}$ is equivalent to $q^{''}$. We can prove $left \Leftarrow right$.

### Question 3

3. As for the first mutant, I change from `state = 0` to `state = 2`, this will cause the program jump out of the `for` loop immediately and cause the failure. And for the second one, I change from `elif c == separator:` to `elif c != separator:`, which can also cause the failure. The test cases are same, `"He^llo|world"`, which contains both `^` and `|`.

### Question 4

Int.py: 75, for RelExp, it is impossible to assert False.

parse.py: 118, for \_stmt\_, it is impossible to return self.error.

parse.py: 268, for \_bfactor\_, it is impossible to return self.error.

