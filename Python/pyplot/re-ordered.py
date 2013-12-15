#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# Non-Ordered
x = []
y = []
a = [1, 3]
b = [3, 4]
c = [2, 5]
d = [None,1]
e = [3, None]
sets = [a,b,c,d,e]

# Order
pairs = []
for key in sets:
  try:
    new_x = key[0]
    new_y = key[1]
    if new_x and new_y:
      pairs.append([new_x,new_y])
  except Exception as error:
    pass
for key in sorted(pairs):
  x.append(key[0])
  y.append(key[1])
plt.plot(x,y)
plt.show()
