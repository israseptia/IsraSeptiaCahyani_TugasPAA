# Pengurutkan Bubble Sort dengan python
def bubbleSort(array):
    # loop melalui setiap elemen array
    for i in range(len(array)):

        # melacak swapping
        swapped = False

        # loop untuk membandingkan elemen array
        for j in range(0, len(array) - i - 1):

            # Bandingkan dua elemen yang berdekatan
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True
        print("Iterasi Ke-", i)

        # jika tidak ada lagi swapping berarti array sudah diurutkan
        # sehingga tidak perlu perbandingan lebih lanjut
        if not swapped:
            break

data = [25, 27, 8, -7, 11]
print("Data : ", data)
bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)