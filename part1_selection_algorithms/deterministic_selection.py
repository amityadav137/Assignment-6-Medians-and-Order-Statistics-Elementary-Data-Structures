def median_of_medians(arr, k):
    if len(arr) < 10:
        return sorted(arr)[k]

    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    pivot = median_of_medians(medians, len(medians)//2)

    low = [el for el in arr if el < pivot]
    high = [el for el in arr if el > pivot]
    equal = [el for el in arr if el == pivot]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))