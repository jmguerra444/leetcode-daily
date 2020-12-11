# %%

# %%

# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/


def isMountain(arr):

    peaks = 0
    valleys = 0
    flats = 0

    if len(arr) < 3:
        return False

    for i in range(len(arr) - 2):
        
        if (arr[i] < arr[i + 1]) and (arr[i + 1] > arr[i + 2]):
            peaks += 1
        
        if (arr[i] > arr[i + 1]) and (arr[i + 1] < arr[i + 2]):
            valleys += 1

        if (arr[i] == arr[i + 1]) or (arr[i + 1] == arr[i + 2]):
            flats += 1

    return peaks == 1 and valleys == 0 and flats == 0

arr = [0,1,2,1,2]
print(isMountain(arr))
print(isMountain([0,1,2,4,2,1]))
# %%
