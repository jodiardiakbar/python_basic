# gunakan marker pada index 0
# geser nilai terkecil ke index 0
# setelah mencapai index -1, geser marker satu index ke kanan
# ulangi

def selection_sort(arr):
    marker = 0
    while marker < len(arr):
        print(f"marker: {arr[marker]}")
        print(f"selection sort status : {arr}")
        start = marker + 1
        while start < len(arr):
            if arr[marker] > arr[start]:
                arr[marker], arr[start] = arr[start], arr[marker]
            start += 1
        marker += 1

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)