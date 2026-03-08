#Author: Akshata, Amruta
def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choosing the middle element as the pivot
    pivot = arr[len(arr) // 2]
    
    # Partitioning the array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the sub-arrays and combine them
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
data = [38, 27, 43, 3, 9, 82, 10]
sorted_data = quick_sort(data)
print(f"Sorted array: {sorted_data}")