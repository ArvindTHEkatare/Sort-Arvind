import matplotlib.pyplot as plt
import pandas as pd
import random
import PySimpleGUI 
def insertionSort(arr):
    n = len(arr)
      
    if n <= 1:
        return arr
      
    for i in range(1, n): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 

    return arr

arr = [12, 11, 13, 5, 6]
sorted_arr = insertionSort(arr)
plt.figure(figsize=(6, 4))
plt.bar(range(len(sorted_arr)), sorted_arr)
plt.title('Sorted Array')
plt.xlabel('Index')
plt.ylabel('Value')
plt.xticks(range(len(sorted_arr)), sorted_arr)
plt.tight_layout()
plt.show()
