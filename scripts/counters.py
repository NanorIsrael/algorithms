def solution(N, A):
    counters = [0] * N
    max_counter = 0
    current_max = 0

    for operation in A:
        if operation == N + 1:
            max_counter = current_max
        else:
            counter_index = operation - 1
            if counters[counter_index] < max_counter:
                counters[counter_index] = max_counter
            counters[counter_index] += 1

            if counters[counter_index] > current_max:
                current_max = counters[counter_index]

    for i in range(N):
        if counters[i] < max_counter:
            counters[i] = max_counter

    return counters