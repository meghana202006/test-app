import timeit
import matplotlib.pyplot as plt

# Linear Search Function
def LinearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Recursive Binary Search Function
def BinarySearch(arr, key, low, high):
    if low > high:
        return -1  # Element not found

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return BinarySearch(arr, key, mid + 1, high)
    else:
        return BinarySearch(arr, key, low, mid - 1)

# Different input sizes for each search algorithm
sizes_linear = range(1000, 100001, 5000)  # Linear Search
sizes_binary = [2 ** i for i in range(10, 20)]  # Binary Search (Powers of 2)

times_linear = []
times_binary = []

# Measure Linear Search Time
for size in sizes_linear:
    arr = list(range(size))
    target = size - 1  # Worst case: last element

    time_taken = min(timeit.repeat(lambda: LinearSearch(arr, target), \
    repeat=10, number=100))
    times_linear.append(time_taken)

# Measure Binary Search Time
for size in sizes_binary:
    arr = list(range(size))
    target = size - 1  # Worst case: last element

    time_taken = min(timeit.repeat(lambda: BinarySearch(arr, target, 0, size-1)\
    ,repeat=10, number=100))
    times_binary.append(time_taken)

# Plot both graphs on the same plot
plt.figure(figsize=(10, 6))
plt.xlabel("List Length")
plt.ylabel("Time Complexity")

plt.plot(sizes_linear, times_linear, label="Linear Search")
plt.plot(sizes_binary, times_binary, label="Recursive Binary Search")

plt.grid()
plt.legend()
plt.title("Linear Search vs. Binary Search Time Complexity")
plt.show()
