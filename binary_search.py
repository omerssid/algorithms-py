def binSearch(arr, target, start, end):
    if(start > end):
        return "Not Found"
    middle = (start + end) // 2
    if arr[middle] == target:
        return "Found {} at index: {}".format(target, middle)
    elif arr[middle] > target:
        return binSearch(arr, target, start, middle - 1)
    else:
        return binSearch(arr, target, middle + 1, end)

arr1 = ['a', 'b', 'c', 'x', 'y', 'z']
arr2 = [ 2, 3, 4, 10, 40 , 100, 400]
result1 = binSearch(arr1, 'c', 0, len(arr1)-1)
result2 = binSearch(arr2, 4000, 0, len(arr2)-1)

print(str(result1))
print(str(result2))
    
    