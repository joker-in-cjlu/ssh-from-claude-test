def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("add-hello")

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("before sort:", data)
    sorted_data = selection_sort(data)
    print("after sort: ", sorted_data)
