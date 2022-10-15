# Edit Distance Calculator

This is my homework assignment for my CPSC 485 (Computational Bioinformatics) that demonstrates the **edit distance**
algorithm, which is responsible for finding the least amount of operations (Insertions, removal and deletions) on 2 input strings to 
make them exactly similar.

For example, consider the strings `str1 = "revolution"` and `str2 = "evaluation"`. Here is how the edit distance is calculated:
```
REVOLU_TION
_EVALUATION
```
 - In this example, the edit distance is 3.
 - To convert "revolution" --> "evaluation", we **delete** the first "r", **replace** the first "o" to an "a", and **insert** the "a" after the first "u"
 - In the perspective of "evaluation" --> "revolution" we **insert** the "r" at the front, **replace** the first "a" to an "o", then **delete** the "a" after the "t"

## Technologies:
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="html" style="vertical-align:top; margin:3px">