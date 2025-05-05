'''
Construct a truth table for the expression: (A AND B) OR (NOT B)
where A and B each can be True or False.

1. Variables:
- A, B

2. Number of Rows:
- 2 possibilities for A
- 2 possibilities for B
- 2 x 2 combinations of A & B = 4 rows

3. Table Columns:
 A   B   (A AND B)   (NOT B)   (A AND B) OR (NOT B)

4. Enumerate all possible (A, B) combinations:
  A     B       (A AND B)   (NOT B)  (A AND B) OR  (NOT B)
  ---------------------------------------------------------------
  True  True                       
  True  False                      
  False True                       
  False False                      

5. Fill Each Row with Sub-Expression Results:
  A     B       (A AND B)   (NOT B)   (A AND B) OR (NOT B)
  ---------------------------------------------------------------
  True  True    True        False     True
  True  False   False       True      True
  False True    False       False     False
  False False   False       True      True
'''

