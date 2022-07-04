## ECE 653 Assignment 2

### Question 1

- 1. $1\rightarrow 2\rightarrow 3\rightarrow 4\rightarrow 9\rightarrow 11\rightarrow 12\rightarrow 13\rightarrow 17$
  2. $\displaystyle 1\rightarrow 2\rightarrow 3\rightarrow 4\rightarrow 9\rightarrow 11\rightarrow 14\rightarrow 15\rightarrow 16\rightarrow 17$
  3. $\displaystyle 1\rightarrow 2\rightarrow 5\rightarrow 6\rightarrow 7\rightarrow 9\rightarrow 11\rightarrow 12\rightarrow 13\rightarrow 17$
  4. $\displaystyle 1\rightarrow 2\rightarrow 5\rightarrow 6\rightarrow 7\rightarrow 9\rightarrow 11\rightarrow 14\rightarrow 15\rightarrow 16\rightarrow 17$

- | Edge               | PV                                                    | PC                                             |
  | ------------------ | ----------------------------------------------------- | ---------------------------------------------- |
  | $1\rightarrow 2$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$            | $true$                                         |
  | $2\rightarrow 3$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$            | $X_{0} + Y_{0}>15$                             |
  | $3\rightarrow 4$   | $x\rightarrow X_{0}+7 ,\ y\rightarrow Y_{0}$          | $X_{0} + Y_{0}>15$                             |
  | $4\rightarrow 9$   | $x\rightarrow X_{0}+9 ,\ y\rightarrow Y_{0}-12$       | $X_{0} + Y_{0}>15$                             |
  | $9\rightarrow 11$  | $x\rightarrow X_{0}+9 ,\ y\rightarrow Y_{0}-12$       | $X_{0} + Y_{0}>15$                             |
  | $11\rightarrow 12$ | $x\rightarrow X_{0}+9 ,\ y\rightarrow Y_{0}-12$       | $X_{0} +Y_{0}  >15\land 2( X_{0} +Y_{0})  >27$ |
  | $12\rightarrow 13$ | $x\rightarrow 3(X_{0}+9) ,\ y\rightarrow Y_{0}-12$    | $X_{0} +Y_{0}  >15\land 2( X_{0} +Y_{0})  >27$ |
  | $13\rightarrow 17$ | $x\rightarrow 3(X_{0}+9) ,\ y\rightarrow 2(Y_{0}-12)$ | $X_{0} +Y_{0}  >15\land 2( X_{0} +Y_{0})  >27$ |

  | Edge               | PV                                                      | PC                                                      |
  | ------------------ | ------------------------------------------------------- | ------------------------------------------------------- |
  | $1\rightarrow 2$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$              | $true$                                                  |
  | $2\rightarrow 3$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$              | $X_{0} + Y_{0}>15$                                      |
  | $3\rightarrow 4$   | $x\rightarrow X_{0}+7 ,\ y\rightarrow Y_{0}$            | $X_{0} + Y_{0}>15$                                      |
  | $4\rightarrow 9$   | $x\rightarrow X_{0}+7 ,\ y\rightarrow Y_{0}-12$         | $X_{0} + Y_{0}>15$                                      |
  | $9\rightarrow 11$  | $x\rightarrow X_{0}+9 ,\ y\rightarrow Y_{0}-12$         | $X_{0} + Y_{0}>15$                                      |
  | $11\rightarrow 14$ | $x\rightarrow X_{0}+9 ,\ y\rightarrow Y_{0}-12$         | $X_{0} +Y_{0}  >15\land 2( X_{0} +Y_{0})  \leqslant 27$ |
  | $14\rightarrow 15$ | $x\rightarrow X_{0}+9 ,\ y\rightarrow Y_{0}-12$         | $X_{0} +Y_{0}  >15\land 2( X_{0} +Y_{0})  \leqslant 27$ |
  | $15\rightarrow 16$ | $x\rightarrow 4(X_{0}+9) ,\ y\rightarrow Y_{0}-12$      | $X_{0} +Y_{0}  >15\land 2( X_{0} +Y_{0})  \leqslant 27$ |
  | $16\rightarrow 17$ | $x\rightarrow 4(X_{0}+9) ,\ y\rightarrow 3Y_{0}+4X_{0}$ | $X_{0} +Y_{0}  >15\land 2( X_{0} +Y_{0})  \leqslant 27$ |

  | Edge               | PV                                              | PC                                                    |
  | ------------------ | ----------------------------------------------- | ----------------------------------------------------- |
  | $1\rightarrow 2$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$      | $true$                                                |
  | $2\rightarrow 5$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$      | $X_{0} + Y_{0}\leqslant 15$                           |
  | $5\rightarrow 6$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$      | $X_{0} + Y_{0}\leqslant 15$                           |
  | $6\rightarrow 7$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}+10$   | $X_{0} + Y_{0}\leqslant 15$                           |
  | $7\rightarrow 9$   | $x\rightarrow X_{0}-2 ,\ y\rightarrow Y_{0}+10$ | $X_{0} + Y_{0}\leqslant 15$                           |
  | $9\rightarrow 11$  | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}+10$   | $X_{0} + Y_{0}\leqslant 15$                           |
  | $11\rightarrow 12$ | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}+10$   | $X_{0} +Y_{0} \leqslant 15\land 2( X_{0} +Y_{0})  >1$ |
  | $12\rightarrow 13$ | $x\rightarrow 3X_{0} ,\ y\rightarrow Y_{0}+10$  | $X_{0} +Y_{0} \leqslant 15\land 2( X_{0} +Y_{0})  >1$ |
  | $13\rightarrow 17$ | $x\rightarrow 3X_{0} ,\ y\rightarrow 2Y_{0}+20$ | $X_{0} +Y_{0} \leqslant 15\land 2( X_{0} +Y_{0})  >1$ |

  | Edge               | PV                                                     | PC                                                           |
  | ------------------ | ------------------------------------------------------ | ------------------------------------------------------------ |
  | $1\rightarrow 2$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$             | $true$                                                       |
  | $2\rightarrow 5$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$             | $X_{0} + Y_{0}\leqslant 15$                                  |
  | $5\rightarrow 6$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}$             | $X_{0} + Y_{0}\leqslant 15$                                  |
  | $6\rightarrow 7$   | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}+10$          | $X_{0} + Y_{0}\leqslant 15$                                  |
  | $7\rightarrow 9$   | $x\rightarrow X_{0}-2 ,\ y\rightarrow Y_{0}+10$        | $X_{0} + Y_{0}\leqslant 15$                                  |
  | $9\rightarrow 11$  | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}+10$          | $X_{0} +Y_{0} \leqslant 15\land 2( X_{0} +Y_{0})  \leqslant 1$ |
  | $11\rightarrow 15$ | $x\rightarrow X_{0} ,\ y\rightarrow Y_{0}+10$          | $X_{0} +Y_{0} \leqslant 15\land 2( X_{0} +Y_{0})  \leqslant 1$ |
  | $15\rightarrow 16$ | $x\rightarrow 4X_{0} ,\ y\rightarrow Y_{0}+10$         | $X_{0} +Y_{0} \leqslant 15\land 2( X_{0} +Y_{0})  \leqslant 1$ |
  | $16\rightarrow 17$ | $x\rightarrow 4X_{0} ,\ y\rightarrow 3Y_{0}+4X_{0}+30$ | $X_{0} +Y_{0} \leqslant 15\land 2( X_{0} +Y_{0})  \leqslant 1$ |

- 1. Path a: Feasible, $X_{0}=10, Y_{0}=20$.
  2. Path b: Not feasible.
  3. Path c: Feasible, $X_{0}=3, Y_{0}=6$.
  4. Path d: Feasible, $X_{0}=0, Y_{0}=0$.

### Question 2

- a. If we want at most one variable is true, we need to make sure that every combination is false, which means, each two variables cannot be true at the same time, we have:
  $$
  \neg (( a_{1} \land a_{2}) \lor ( a_{1} \land a_{3}) \lor ( a_{1} \land a_{4}) \lor ( a_{2} \land a_{3}) \lor ( a_{2} \land a_{4}) \lor ( a_{3} \land a_{4}))
  $$
  We can transform this equation into CNF clauses:
  $$
  ( \neg a_{1} \land \neg a_{2}) \lor ( \neg a_{1} \land \neg a_{3}) \lor ( \neg a_{1} \land \neg a_{4}) \lor ( \neg a_{2} \land \neg a_{3}) \lor ( \neg a_{2} \land \neg a_{4}) \lor ( \neg a_{3} \land \neg a_{4})
  $$

- b. For the left side:
  $$
  Left=∀x⋅∃y⋅P(x)∨Q(y)⇒∀x⋅(∃y⋅P(x))∨(∃y⋅Q(y))
  $$
  Since $y$ has no relationship with $P(x)$, we can  eliminate $y$.
  $$
  ⇒∀x⋅(P(x))∨(∃y⋅Q(y))
  $$

  $$
  ⇒∀x⋅P(x)∨∀x⋅∃y⋅Q(y)⇒∀x⋅P(x)∨∃y⋅Q(y)=Right
  $$

  For the right side:
  $$
  Right=∀x⋅P(x)∨∃y⋅Q(y)\Rightarrow ∀x⋅P(x)∨∀x⋅∃y⋅Q(y)
  $$

  $$
  \Rightarrow ∀x⋅(P(x)∨∃y⋅Q(y))
  $$

  $$
  \Rightarrow ∀x⋅(∃y⋅P(x)∨∃y⋅Q(y))
  $$

  $$
  \Rightarrow ∀x⋅∃y⋅(P(x)∨Q(y))=Left
  $$

- c. 

- d. a.

- d. b. Since $\exists x\exists y\exists z( P( x,y) \land P( z,y) \land P( x,z) \land \neg P( z,x))$ and $P_{2} =\{( x,x+1) |x\in \mathbb{N}\}$, which means we need to find a set that satisfied $y=x+1\and y=z+1\and z=x+1$, which is $\empty$. So it is violate the formula.

- d. c. Since $P_{3} =\{( A,B) |A,B\in \mathcal{P}(\mathbb{N}) \land A\subseteq B\}$, which means we need to find 3 sets $x$, $y$, and $z$ that satisfied: $x\subseteq y\land z\subseteq y\land x\subseteq z\land z\nsubseteq x$ and all of the elements of $x$, $y$, and $z$ are natural numbers.

  Suppose $x=\{1\}$, $y=\{1,2,3\}$, and $z=\{1,2\}$, we can see:
  $$
  x\subseteq y: \{1\} \subseteq \{1,2,3\}
  $$

  $$
  z\subseteq y: \{1,2\} \subseteq \{1,2,3\}
  $$

  $$
  x \subseteq z: \{1\} \subseteq \{1,2\}
  $$

  $$
  z\nsubseteq x: \{1,2\} \nsubseteq \{1\}
  $$

  So, it is satisfied the formula.

- e.
