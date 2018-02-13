"""
Name: Cheuk Pan, Mak
Compsci 320
Assignment 3
Question 2
"""
import sys

def recursive_count(pairs):
	size = len(pairs)
	if size <= 1:
		return (0, pairs)
	
	else:
		mid_point = size//2
		(count_a, a) = recursive_count(pairs[:mid_point])
		(count_b, b) = recursive_count(pairs[mid_point:])
		(count_merge, merge) = merge_count(a, b)
	return  (count_a + count_b + count_merge, merge)
	
def merge_count(a, b):
	i, j, count = 0, 0, 0
	size_a, size_b = len(a), len(b)
	c = list()
	while (i < size_a) and (j < size_b):
		if a[i][1] < b[j][1]:
			c .append(a[i])
			count += (size_b-j)
			i+=1
		else:
			c.append(b[j])
			j+=1
	if i == size_a:
		c.extend(b[j:])
	else:
		c.extend(a[i:])
	return (count, c)
	
tc = int(sys.stdin.readline())
for i in range(tc):
	n = int(sys.stdin.readline())
	wires = list()
	for j in range(n):
		pairs = [int(m) for m in sys.stdin.readline().split(" ")]
		wires += [pairs]
	(count, wires)  = recursive_count(sorted(wires,reverse = True))
	print("Case #" + str(i+1) + ":", count)
		