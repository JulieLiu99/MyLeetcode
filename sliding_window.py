arr = [1, 2, 4, 1, 3]
k = 2
max = 5

"""
sliding window: arr[pre + 1: nxt]

[1, 2, 4, 1, 3]
 ^  ^ 
window = 1 + 2 = 3, <
pre = 0, nxt = 2

[1, 2, 4, 1, 3]
    ^  ^ 
window = 3 - 1 + 4 = 6, > 

"""


def sliding_window(): 
    if len(arr) < k: 
        return sum[arr] <= max
    nxt = k
    window = sum(arr[:nxt])
    pre = 0
    while nxt < len(arr):
        if window > max: return False
        window -= arr[pre]
        window += arr[nxt]
        pre += 1
        nxt += 1
    return True


print(sliding_window() == False)

max = 6
print(sliding_window() == True)
