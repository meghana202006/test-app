import timeit
import matplotlib.pyplot as plt

def BinarySearch(arr , key , low , high):

    if(low <= high):

        mid = (low + high) // 2
        
        if(arr[mid] == key):

            return mid
        elif(key > arr[mid]):

            return BinarySearch(arr , key , mid + 1 , high)
        
        else:

            return BinarySearch(arr , key , low , mid - 1)
        

# Main Program

sizes = [2 ** i for i in range(10 , 20)]

times = []
for size in sizes:

    array = list(range(size))

    target = size - 1

    time_taken = min(timeit.repeat(lambda:BinarySearch(array , target , 0 , size - 1),repeat = 10 , number=100))

    times.append(time_taken)

plt.xlabel("List Length")

plt.ylabel("Time Complexity")

plt.plot(sizes , times , label ="Binary Search")

plt.grid()

plt.legend()

plt.show()

