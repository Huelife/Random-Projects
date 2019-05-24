#random_48_10000.py: rolls 26 random numbers from 1-50, 10000 times

from random import randint

#int variables
x_random = 0
FIND_VALUE = 48
Y_RANGE = 10000
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

#random numbers are iterated 10000 times
for i in range(Y_RANGE):
  numbers_set = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,z]
  a = randint(1,50)
  b = randint(1,50)
  c = randint(1,50)
  d = randint(1,50)
  e = randint(1,50)
  f = randint(1,50)
  g = randint(1,50)
  h = randint(1,50)
  i = randint(1,50)
  j = randint(1,50)
  k = randint(1,50)
  l = randint(1,50)
  m = randint(1,50)
  n = randint(1,50)
  o = randint(1,50)
  p = randint(1,50)
  q = randint(1,50)
  r = randint(1,50)
  s = randint(1,50)
  t = randint(1,50)
  u = randint(1,50)
  v = randint(1,50)
  w = randint(1,50)
  x = randint(1,50)
  y = randint(1,50)
  z = randint(1,50)
  if FIND_VALUE in numbers_set:
    x_random += 1

#percentage of times random 48 pops up
x_random_percent = round(((x_random/Y_RANGE)*100),1)

#4 different information printed
print("Finding {} in numbers_set,\n{}/{},\n{}%"
     .format(FIND_VALUE,x_random,Y_RANGE,x_random_percent))
