import random

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

array = [random.randint(0,100) for i in range(10)]

#one liner

print(array)
# print(selectionSort(array))