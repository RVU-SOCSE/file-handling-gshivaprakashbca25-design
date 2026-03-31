Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as s
>>> df=s.read_csv("C:/Users/G SHIVAPRAKASH/Downloads/5prog_1experience - 5prog_1experience.csv")
>>> df
   YearsExperience
0              1.1
1              1.3
2              1.5
3              2.0
4              2.2
5              2.9
6              3.0
7              3.2
8              3.2
>>> df.shape
(9, 1)
>>> len(df)
9
>>> df.head(2)
   YearsExperience
0              1.1
1              1.3
