#include <stdio.h>
#include <stdlib.h>

int main() {
    int A[] = {3, 8, 9, 7, 6, 8};
    int N = sizeof(A) / sizeof(A[0]);
    int K = 3;
    
     printf("%d\n ", N);
    // printf("Original Array: ");
    // for (int i = 0; i < N; i++) {
    //     printf("%d ", A[i]);
    // }
    
    // rotateArray(A, N, K);
    
    // printf("\nRotated Array: ");
    // for (int i = 0; i < N; i++) {
    //     printf("%d ", A[i]);
    // }
    
    return 0;
}