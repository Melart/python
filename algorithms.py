list = [4, 65, 67, 1, 253, 54, 55, 33, 3, 6, 9, 876, 32, 77]

def sort_list(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def binary_search(arr, num):
    low = 0
    up = len(arr) - 1
    
    while low <= up:
        center = (low + up) // 2
        
        if arr[center] == num:
            return center
        elif arr[center] > num:
            up = center - 1
        elif arr[center] < num:
            low = center + 1
            
    return -1
            
search_list = sort_list(list)

print(search_list)
print(binary_search(search_list, 876))
