def solution(A):
    # Implement your solution here
    if A is None or len(A) == 0:
        return 1
    
    size_a = len(A)
    sorted_a = sorted(A)
    prev = sorted_a[0]

    if size_a == 0:
        return (1)

    if sorted_a[0] != 1:
        return (1)

    if size_a == 1:
        return (sorted_a[0] + 1)

    for x in range(1, size_a):
        print("", prev)
        print('sorted val', sorted_a[x])
        if sorted_a[x] != prev + 1:
            return (sorted_a[x] - 1)
        else:
            prev = sorted_a[x]
    return (sorted_a[x] + 1)





A = [5, 3, 1, 2]
print("4 ", solution(A))
print("1 ", solution([]))
print("2 ", solution([1]))
print("1 ", solution([2]))
print(str.rjust("prev", 9))