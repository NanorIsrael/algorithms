
def canUnlockAll(boxes):
	if not boxes or not boxes[0]:
		# Empty input or the first box is empty
		return False

	n = len(boxes)
	visited = [False] * n
	visited[0] = True  # Mark the first box as visited

	queue = [0]  # Start BFS with the first box

	while queue:
		current_box = queue.pop()

		for key in boxes[current_box]:
			if 0 <= key < n and not visited[key]:
				visited[key] = True
				queue.append(key)

	return all(visited)
 

boxes = [[1], [2], [3], [4], []]
# queue = deque([0])
# print(queue.popleft())
# print(boxes[queue.popleft()])
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))