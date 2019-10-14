#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys

inversion = 0

def merge(arr, front, mid, end):
    
    global inversion
    
    leftSub = arr[front : mid + 1]
    rightSub = arr[mid + 1 : end + 1]
    
    leftSub.append(sys.maxsize)
    rightSub.append(sys.maxsize)
    
    indexLeft, indexRight = 0, 0
    
    for index in range(front, end + 1):
        if leftSub[indexLeft] <= rightSub[indexRight]:
            arr[index] = leftSub[indexLeft]
            indexLeft += 1
        else:
            inversion += len(leftSub[indexLeft:]) - 1
            arr[index] = rightSub[indexRight]
            indexRight += 1
            
def mergeSort(arr, front, end):
    
    if front < end:
        mid = (front + end) // 2
        mergeSort(arr, front, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, front, mid, end)

if __name__ == '__main__':
    
    data = pd.read_csv(r'C:\Users\USER\Desktop\input_100.txt')
    arr = []

    for num in data['100']:
        arr.append(num)
    
    print('Original array:\n', arr, '\n')
    mergeSort(arr, 0, len(arr) - 1)
    print('Sorted array:\n', arr, '\n')
    print('The number of inversion in any permuatation on these {num} elements is {inversion}'.format(num = len(arr), inversion = inversion)) 