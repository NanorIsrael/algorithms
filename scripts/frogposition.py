def solution(X, A):
    leaf_positions = [False] * (X + 1)
    target_position = 1
    covered_positions = 0

    for time, leaf_position in enumerate(A):
        if not leaf_positions[leaf_position]:
            leaf_positions[leaf_position] = True
            covered_positions += 1

            while target_position <= X and leaf_positions[target_position]:
                target_position += 1

            if covered_positions == X:
                return time

    return -1
                                                                                      




A = [1, 3, 1, 4, 2, 3, 5, 4]
A = [1, 3, 1, 4, 2, 3, 5, 4]
print('6', solution(5, A))
print('4', solution(4, A))
