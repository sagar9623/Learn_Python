def find_largest_smallest(arr):
    if not arr:
        return None, None

    largest = arr[0]
    smallest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num
        
    return largest, smallest


input_array = [11,2,3,4,-5]
print(input_array)
print(f"input array: {input_array}")

largest, smallest = find_largest_smallest(input_array)

print(f"The largest element in the array is: {largest}")
print(f"The smallest element in the array is: {smallest}")