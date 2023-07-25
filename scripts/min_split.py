# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    
    t_sum = sum(A)
    l_sum = 0
    min_diff = float('inf')

    for idx in range(len(A)):
        l_sum += A[idx]
        r_sum = t_sum - l_sum
        diff = abs(l_sum - r_sum)
        min_diff = min(min_diff, diff)
    return min_diff


# P = 1, difference = |3 − 10| = 7 
# P = 2, difference = |4 − 9| = 5 
# P = 3, difference = |6 − 7| = 1 
# P = 4, difference = |10 − 3| = 7 
A = [3, 1, 2, 4, 3]
print('1', solution(A))

# [0] = 1 = 
# [1] = 2

# P = 1, difference = |1 − 3| = 2
# P = 2, difference = |3 − 1| = 2

A = [1, 2]
print('1', solution(A))