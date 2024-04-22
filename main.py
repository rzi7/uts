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


# linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data yang disimpan dalam simpul
        self.next = None  # Referensi ke simpul berikutnya, awalnya None

class LinkedList:
    def __init__(self):
        self.head = None  # Kepala linked list, awalnya None

    def append(self, data):
        # Membuat simpul baru
        new_node = Node(data)
        # Jika linked list kosong, simpul baru menjadi kepala
        if self.head is None:
            self.head = new_node
        else:
            # Iterasi hingga akhir linked list
            current = self.head
            while current.next:
                current = current.next
            # Tambahkan simpul baru di akhir
            current.next = new_node

    def display(self):
        # Tampilkan seluruh linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, index, data):
        # Masukkan simpul baru pada posisi tertentu
        new_node = Node(data)
        # Jika index adalah 0, simpul baru menjadi kepala
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        # Iterasi hingga posisi yang diinginkan
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        # Masukkan simpul baru di posisi yang diinginkan
        new_node.next = current.next
        current.next = new_node

    def delete(self, index):
        # Hapus simpul pada posisi tertentu
        if index == 0:
            # Hapus kepala linked list
            self.head = self.head.next
            return
        # Iterasi hingga posisi yang diinginkan
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        # Hapus simpul pada posisi yang diinginkan
        current.next = current.next.next

# Contoh penggunaan
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("Linked list setelah append:")
ll.display()

ll.insert(1, 15)
print("\nLinked list setelah insert 15 pada index 1:")
ll.display()

ll.delete(2)
print("\nLinked list setelah delete index 2:")
ll.display()

