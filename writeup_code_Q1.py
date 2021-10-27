import random
import timeit
import copy

# Python program for implementation of MergeSort
# Algorithm from: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Function to do insertion sort
# Algorithm from: https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def main():
    # I will use an input file with the different n values to test
    # Then random lists of length n will be initialized
    fp = open("n_inputs_Q1.txt", "r")
    master_lists = []
    for line in fp:
        # Create 5 lists for each length of input so we can average out the time per input
        # with different lists (won't be timing this part)
        for i in range(5):
            master_lists.append([random.randint(0, 500) for i in range(int(line.strip()))])

    # Using the timeit module to measure elapsed time for each sorting operation
    # Used website below to remind myself of the timeit implementation
    # https://www.geeksforgeeks.org/how-to-measure-elapsed-time-in-python/

    # make deep copies so the same list can be used in both tests
    print("Merge Sort Times")
    for lst in master_lists:
        input = copy.deepcopy(lst)
        print(timeit.timeit(lambda: mergeSort(input), number=1))

    print("Insertion Sort Times")
    for lst in master_lists:
        iniput = copy.deepcopy(lst)
        print(timeit.timeit(lambda: insertionSort(lst), number=1))

if __name__ == "__main__":
    main()
