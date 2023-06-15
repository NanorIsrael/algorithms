function solution(N) {
    let binary = [];
    while (N > 0) {
        if (N == 1) {
            binary.push(1)
            break;
        } 
        binary.push(N % 2)
        N = Math.floor(N /= 2);
    }
     
    binary_length = binary.length;

    let gapContainer = [];
    let prev = binary[0];
    let counter = 0
    let i = 0
    for (i = i; i < binary_length - 1; i++) {
        if (binary[i] == 0 && prev == 1) {
            while (binary[i] != 1) {
                counter +=1;
                i++;
            }
            gapContainer.push(counter);
            counter = 0;
        } 
        prev = binary[i];
    }

    return gapContainer.length > 0 ? (gapContainer.sort())[gapContainer.length - 1] : 0
}

console.log(solution(5))
console.log(solution(9))
console.log(solution(529))
console.log(solution(20))
console.log(solution(15))
console.log(solution(1041))