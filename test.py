
from __future__ import print_function

print("One: {x}".format(x='hello'))

for element in [1,2,3,4,5]:
    print(element)

x = 0

while x<10:
    print('x is currently',x)
    x += 1
    if x==3:
        print('x is 3, break')
        break

else:
    print('all done')

print('after a while')

listX = list(xrange(0, 10))
print(listX)
print(type(listX))

l = []
for letter in 'word':
    l += letter
    print(type(l))
    #l.append(letter)

print(l)
lst = [letter for letter in 'word']
print(lst)

lst2 = [3**x for x in xrange(2,5)]
print(lst2)

lst3 = [number for number in range(11) if number % 3 ==0]
print(lst3)

st = 'Print only the words that start with s in this sentence'
for word in st.split( ):
    if word[0] == 's':
        print(word)
print([word for word in st.split( ) if word[0] == 's'])

print(range(0,11,2))

divisionList = [number for number in xrange(50) if number % 3 == 0]
print(divisionList)

st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split( )])

import math

def vol(rad):
    return rad**2*math.pi

print(vol(2))

def unique_list(l):
    return list(set(l))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

import string
def ispangram(str1, alphabet = string.ascii_lowercase):
    s = set(alphabet)
    # 
    # return s <= set(str1.lower()) #it assumes we the input in str1 is ascii alphabet
    for let in str1.lower():
        if let in s:
            s.remove(let)
    return len(s) == 0

print(ispangram("The quick brown fox jumps over the lazy dog"))

print(ispangram('abc'))