# queue
from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)

print(q.get()) # 1
print(q.get()) # 2

print(list(q.queue)) # [3]
q.put('X')
q.put('Y')
q.put('Z')
print(list(q.queue)) # [3, 'X', 'Y', 'Z']
print(q.empty())   # False

# bubble sort
def bubble_sort(arr):
    n = len(arr)
    # Lakukan iterasi melalui daftar
    for i in range(n):
        swapped = False
        # Lakukan iterasi pada elemen-elemen yang berdekatan
        for j in range(0, n - i - 1):
            # Jika elemen yang di sebelah kanan lebih kecil daripada elemen yang di sebelah kiri, tukar
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Jika tidak ada penukaran yang terjadi, itu berarti daftar sudah terurut
        if not swapped:
            break
    return arr

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum pengurutan:", arr)
sorted_arr = bubble_sort(arr)
print("Array setelah pengurutan:", sorted_arr)

# selection sort
def selection_sort(arr):
    n = len(arr)
    # Iterasi melalui setiap elemen dalam daftar
    for i in range(n):
        # Temukan indeks elemen terkecil dalam daftar yang belum terurut
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Tukar elemen pertama dengan elemen terkecil yang ditemukan
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Contoh penggunaan
arr = [29, 10, 14, 37, 13]
print("Array sebelum pengurutan:", arr)
sorted_arr = selection_sort(arr)
print("Array setelah pengurutan:", sorted_arr)

# insertion sort
def insertion_sort(arr):
    # Iterasi melalui setiap elemen dalam daftar, dimulai dari indeks 1
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Pindahkan elemen-elemen yang lebih besar dari 'key' ke posisi selanjutnya
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Tempatkan 'key' di posisinya yang benar
        arr[j + 1] = key
    
    return arr

# Contoh penggunaan
arr = [12, 11, 13, 5, 6]
print("Array sebelum pengurutan:", arr)
sorted_arr = insertion_sort(arr)
print("Array setelah pengurutan:", sorted_arr)
