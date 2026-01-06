# Bertrand's box paradox

## Author

Dominik Rappaport, dominik@rappaport.at

## Introduction

In probability therory we often encounter so-called paradoxes. These are specially constructed experiments whose
results are not aligned to what you would expect. On of them is Bertrand's box paradox.

## Experiment

Imagine three boxes containing two coins each. In the first box there are two golden coins, in the second box one
golden and one silver coin, and in the third box there are two silver coins. In step one you randomly select one of the
boxes and blindly take out one coin. Suppose that coin is golden. What is the probability that the other coin in the
same box is also golden?

Many people, and I was one of them, think the answer is $\frac{1}{2}$. The intuition is that once you know you picked a
golden coin, you know you selected the first or the second box, for the third one doesn't contain any golden coins. If 
you picked box 1, the second coin is golden, and if you picked box 2, the second coin is silver. As both options
are equally likely, the probability for a second golden coin seems to be $\frac{1}{2}$. In reality though, the 
probability is $\frac{2}{3}$. Why's that?

## Explanation

The best approach is always to define a proper sample space. We assign the numbers 1 to 6 to the six coins. We
first select one out of the 6 positions at random. Then we select the other coin of the same box. So, the following
six selections are possible:

| Box | First Coin | Second Coin | Sequence       |
|-----|------------|-------------|----------------|
| 1   | 1          | 2           | Golden, Golden |
| 1   | 2          | 1           | Golden, Golden |
| 2   | 3          | 4           | Golden, Silver |
| 2   | 4          | 3           | Silver, Golden |
| 3   | 5          | 6           | Silver, Silver |
| 3   | 6          | 5           | Silver, Silver |

All six sequences are equally likely. You will also notice that once you selected the first coin, the second coin
is is fully determined as we need to take it out of the same box as the first one.

Now let's consider the following two events:

$$ P(\text{"first coin is golden"}) = \frac{3}{6} = \frac{1}{2}$$

and

$$ P(\text{"first coin is golden and second coin is golden"}) = \frac{2}{6} = \frac{1}{3}.$$

The (conditional) probability we are looking for is

$$ P(\text{"second coin is golden"} \vert \text{"first coin is golden"}) = 
\frac{P(\text{"first coin is golden and second coin is golden"})}{P(\text{"first coin is golden"})} = 
\frac{\frac{1}{3}}{\frac{1}{2}} = \frac{2}{3}.$$

## Interpretation

If you consider the table, the probability of $\frac{2}{3}$ becomes clear. There are three sequences with the
first coin being golden and out of these three, the second coin is golden in exactly two of them. The mistake
you intuitively make is to miss that you can get two golden coins in two ways. Drawing coin 1 and then 2 or, 
coin 2 and then 1.

## Simulation

A little [simulation](/main.py)

```python
def betrandsbox(n):
    colour = {
        1: "golden",
        2: "golden",
        3: "golden",
        4: "silver",
        5: "silver",
        6: "silver",
    }
    other_coin = {1: 2, 2: 1, 3: 4, 4: 3, 5: 6, 6: 5}
    total = 0
    two_golden = 0

    for _ in range(n):
        r = randint(1, 6)
        total += colour[r] == "golden"
        two_golden += colour[r] == "golden" and colour[other_coin[r]] == "golden"

    return two_golden / total
```
confirms the result:
```
% python main.py
Probability of second coin being golden given first coin is golden: 0.67
```