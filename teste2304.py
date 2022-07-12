Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 4
>>> b = 10
>>> c = 50
>>> d = 1
>>> e = 5
>>> a ==c
False
>>> a < b
True
>>> d > b
False
>>> c != e
True
>>> a == b
False
>>> c < d
False
>>> b > a
True
>>> c <= c
True
>>> c <= e
False
>>> c <= e
False
>>> d != a
True
>>> e != e
False
>>> true and false (10 < 0) and (10 > 2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    true and false (10 < 0) and (10 > 2)
NameError: name 'true' is not defined
>>> True or false (10 < 0) or (10 > 2)
True
>>> not True or True  not (3 != 0) or (8 > 5)
SyntaxError: invalid syntax
>>> not True or True not (3 != 0) or (8 > 5)
SyntaxError: invalid syntax
>>> 