#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    
    max_val = 0;
    key = ''
    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            key = k
    return key


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
best_key = best_score({})
print("Best score: {}".format(best_key))