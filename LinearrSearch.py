import timeit

import matplotlib.pyplot as plt


def LinearSearch(arr , key):

    for i in range(len(arr)):

        if(arr[i] == key):

            return i
        
    return -1

# Main Program 

sizes = range(1000,100001,5000)

times = []
for size in sizes:

    arr = list(range(size))

    target = size - 1

    time_taken = min(timeit.repeat(lambda:LinearSearch(arr , target),repeat=100, number=2))

    times.append(time_taken)

plt.xlabel("List Length")

plt.ylabel("Time Complexity")

plt.plot(sizes ,  times , label ="Linear Search")

plt.grid()

plt.legend()

plt.show()
