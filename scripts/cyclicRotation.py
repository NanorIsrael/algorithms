A = [3, 8, 9, 7, 6]

def solution(A, K):
    i = 0
    j = len(A)

    K = K % j
    if K == 0:
        return A
   
    reverse(A, 0, j - 1)
    reverse(A, 0, K - 1)
    reverse(A, K, j - 1)
      
    return A


def reverse(A, start, end):
    while start < end:
        tmp = A[start]
        A[start] = A[end]
        A[end] = tmp
        start += 1;
        end -= 1;


b = solution(A, 3)
print(b)