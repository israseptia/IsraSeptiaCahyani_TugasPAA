def bubble_sort(arr):
    n = len(arr)
    #perulangan untuk mengiterasi sebanyak n - 1 kali
    for i in range(n):
        swapped = False
        #perulangan untuk membandingkan pasangan elemen yang berdekatan
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Jika tidak ada pertukaran atau array sudah terurut maka perulangan berhenti
        if not swapped:
            break
        # Menampilkan array pada setiap iterasi
        print(f"Iterasi {i + 1}: {arr}")
    return arr

# contoh nilai
arr = [27, 25, 11, 18, 16, 9]
print("Array sebelum diurutkan:", arr)
sorted_arr = bubble_sort(arr) #memanggil fungsi bubble sort yang telah didefinisikan
print("Array setelah diurutkan:", sorted_arr)