def insertion_sort(array: list):
    for i in range(0, len(array)):
        min_element = 0
        min_element_index = 0
        for j in range(i, len(array)):
            if j == i or min_element > array[j]:
                min_element = array[j]
                min_element_index = j
        array[i], array[min_element_index] = array[min_element_index], array[i]


if __name__ == "__main__":
    array = [8, 1, 7, 4, 6]
    print("---- Array before ----")
    print(array)

    insertion_sort(array)
    print("---- Array after ----")
    print(array)

