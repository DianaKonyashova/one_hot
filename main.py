import random
import numpy as np

alphabet = ['robot', 'human']
print(f"alphabet = {alphabet}")

randomData = ['robot','robot','robot','human', 'human']
print(f"random data = {randomData}")

mapping = {}
for x in range(len(alphabet)):
  mapping[alphabet[x]] = x
print(f"mapping={mapping}")

one_hot_encode = []

for c in randomData:
  arr = list(np.zeros(len(alphabet), dtype = int))
  arr[mapping[c]] = 1
  one_hot_encode.append(arr)

print(f"result = {one_hot_encode}")