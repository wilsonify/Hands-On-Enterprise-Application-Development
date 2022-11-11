#!/bin/python2
"""
In the days of Python 2,
str was used to support ASCII data,
unicode was used to support unicode.

When someone wanted to deal with a particular encoding,
they took a string and encoded it into the required encoding.

the language inherently supported an implicit conversion
of the string type to the unicode type.

This is shown in the following code snippet:
"""
str1 = 'Hello'
print "Type of str1 is " + str(type(str1))
str2 = u'World'
print "Type of str2 is " + str(type(str2))
str3 = str1 + str2
print "Type of str3(str1+str2) is " + str(type(str3))
