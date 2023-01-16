print("Ex1:")

with open("my_id", "w") as f:
    f.write("My name is amne\n")
    f.write("My family is ghazale!\n")
    f.write("I'am 28 years old\n")
    f.write("My phone number is 0522463323")

print("Ex2:")

from collections import Counter
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("number of words:", word_count("my_id"))

print("Ex3:")

def file_read(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print (line)
file_read("my_id", 1)

print("Ex4:")

import re

regex = re.compile('[^a-zA-Z]')

def longest_words(path):
        list = []
        f = open(path, "r")
        data = f.read().split()
        d = {}
        for word in data:
            word = regex.sub('', word)
            d[word] = len(word)

        d_keys = d.keys()
        max_length=0
        for k in d_keys:
            if len(k)>max_length:
                max_length=len(k)
        for word in data:
            word = regex.sub('', word)
            if max_length == len(word):
                list.append(word)

        return list
print(longest_words("my_id"))

print("EX5:")

class py_soultion:
    def revese_word(self, s):
        return ' '.join(reversed(s.split()))
print(py_soultion().revese_word("hello .py"))

print("Ex6:")

class THEstring:
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input()
    def print_string(self):
        print(self.str1.upper())
str1=THEstring()
str1.get_string()
str1.print_string()

print("Ex7:")

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def rectangle_area(self):
        return self.length*self.width
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
