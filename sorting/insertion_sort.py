def swap(array: list, i: int, j: int):
    temp = array[i]

    array[i] = array[j]
    array[j] = temp


def insert(array: list, index: int):
    for i in range(index)[::-1]:
        if array[i] > array[i + 1]:
            swap(array, i, i + 1)
        else:
            break


def insertion_sort(array: list):
    for j in range(len(array)):
        insert(array, j)


if __name__ == "__main__":
    a1 = [1, 3, 2, 8, 90, 44, 56]
    a2 = [2, 7, 4, 1, 3, 6, 5, 0]
    
    insertion_sort(a1)
    insertion_sort(a2)
    
    print(a1)
    print(a2)
