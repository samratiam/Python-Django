# Binary Search Algorithm

def binary_search(i, j, key, array):
    if i <= j:
        mid = (i + j) // 2

        if key == array[mid]:
            print(f"{key} is found at {mid+1}th position")

        elif key > array[mid]:
            i = mid + 1
            return binary_search(i, j, key, array)

        elif key < array[mid]:
            j = mid - 1
            return binary_search(i, j, key, array)

    else:
        print(f"{key} isn't found in the array")


key = 9
array = [1, 4,  5, 7, 8, 100, 20, 40, 10]
array.sort()
print("Sorted Array:", array)

i = 0
j = len(array) - 1
binary_search(i, j, key, array)
