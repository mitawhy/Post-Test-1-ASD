# Mengurutkan data menggunakan Merge Sort

import os
os.system("cls")

def flatten(arr):
    list_flatten = []

    for i in arr:
        if isinstance(i, list):
            list_flatten.extend(flatten(i))
        else:
            list_flatten.append(i)

    return list_flatten

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    hasil = []

    while left and right:
        if left[0] <= right[0]:
            hasil.append(left.pop(0))
        else:
            hasil.append(right.pop(0))

    hasil.extend(left)
    hasil.extend(right)
    return hasil

listawal = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
listurut = mergeSort(flatten(listawal))

print("Sebelum diurutkan:", listawal)
print("Setelah diurutkan:", listurut)