import sys
def board_array(board_size):
	two_by_two = []
	for i in range(board_size[0]):
		two_by_two.append([])
		for j in range(board_size[1]):
			two_by_two[i].append(0)
	return(two_by_two)

def min_path(two_by_two, num_paths, board_size, queue):
	length = 0
	num_paths[0][0] = 1
	while len(queue) != 0:
		check = queue.pop(0)
		c0, c1 = check[0], check[1]
		curr_len = two_by_two[c0][c1]

		if c0 == board_size[0] and c1 == board_size[1]:
			length = curr_len
			
		else:
			for i in [-2, 2]:
				for j in [1, -1]:
					a = [c0+i, c1+j]
					if bound(a, board_size):
						if two_by_two[a[0]][a[1]] == 0:
							two_by_two[a[0]][a[1]] = curr_len + 1
							num_paths[a[0]][a[1]] = num_paths[c0][c1]
							queue.append(a)
							
						elif two_by_two[a[0]][a[1]] == (curr_len+1):
							num_paths[a[0]][a[1]] += num_paths[c0][c1]

					a = [c0+j, c1+i]
					if bound(a, board_size):
						if two_by_two[a[0]][a[1]] == 0:
							two_by_two[a[0]][a[1]] = curr_len + 1
							num_paths[a[0]][a[1]] = num_paths[c0][c1]
							queue.append(a)
							
						elif two_by_two[a[0]][a[1]] == (curr_len+1):
							num_paths[a[0]][a[1]] += num_paths[c0][c1]
							
	num_end_paths = num_paths[board_size[0]][board_size[1]] 
	if length == 0 and num_end_paths == 0:
		return None
	return length, num_end_paths

def bound(a, board_size):
	if (a[0] < 0) or (a[0] > board_size[0]) or (a[1] < 0) or (a[1] > board_size[1]):
		return False
	return True
		
while True:
	line = sys.stdin.readline()
	if not line or line == "\n":
		break
	board_size = line.split(" ")
	for i in range(len(board_size)):
		board_size[i] = int(board_size[i])
	queue = [[0,0]]
	output = min_path(board_array(board_size), board_array(board_size), [board_size[0]-1, board_size[1]-1], queue)
	if output:
		print(str(output[0]) + " " + str(output[1]))