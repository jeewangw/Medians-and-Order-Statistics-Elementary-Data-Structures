
import random

# Deterministic Algorithm: Median of Medians
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    pivot = median_of_medians(medians, len(medians)//2)
    
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(pivots):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(pivots))

# Randomized Algorithm: Randomized Quickselect
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + len(pivots):
        return pivot
    else:
        return randomized_quickselect(high, k - len(low) - len(pivots))

# Example usage
if __name__ == "__main__":
    arr = [3, 2, 1, 5, 4, 6, 7, 9, 8]
    k = 4  # Find the 4th smallest element (0-based index)
    print("Median of Medians result:", median_of_medians(arr, k))
    print("Randomized Quickselect result:", randomized_quickselect(arr, k))
