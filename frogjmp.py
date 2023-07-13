def solution(X, Y, D):
    if X is None or  Y is None  or D is None:
        return 0
    # Implement yoxur solution here
    if X == Y or D == 0:
        return 0
    
    distance = Y - X
    jumps = distance // D
    if distance % D != 0:
        jumps += 1
    return jumps


# 3
# 0
# 34
# 2
# 142730189

print(solution(10, 85, 30))
print(solution(1, 1, 3))
print(solution(5, 105, 3))
print(solution(1, 5, 2))
print(solution(3, 999111321, 7))