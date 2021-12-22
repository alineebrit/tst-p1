
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

import math
dis1 = math.sqrt ((x1-x2)**2 + (y1-y2)**2)
dis2 = math.sqrt ((x1-x3)**2 + (y1-y3)**2)
dis3 = math.sqrt ((x2-x3)**2 + (y2-y3)**2)

p = dis1+dis2+dis3

print(f"O perímetro é de {p:.2f}")
