# Orden de mejor a peor

# Counting Sort - O(n + k) (El más eficiente, pero solo para enteros en rangos acotados).
# Timsort (sorted() y list.sort()) - O(n log n) (Uno de los algoritmos más rápidos y optimizados para uso general.)
# Heap Sort - O(n log n)
# Merge Sort - O(n log n)
# Quick Sort - O(n log n) (Promedio; en el peor caso es O(n²).)
# Insertion Sort - O(n²) (Muy eficiente cuando la lista está casi ordenada.)
# Selection Sort - O(n²)
# Bubble Sort - O(n²)

# -------------------------------------------------------------
# COUNTING SORT - O(n + k) (más eficiente si k es pequeño)
# -------------------------------------------------------------
mi_set = {10, 3, 50, 1}
lista = list(mi_set)

max_val = max(lista)
count = [0] * (max_val + 1)

for num in lista:  # O(n)
    count[num] += 1

resultado = []
for i in range(len(count)):  # O(k)
    for _ in range(count[i]):  # total O(n)
        resultado.append(i)

print("Counting Sort:", resultado)


# -------------------------------------------------------------
# HEAP SORT - O(n log n)
# -------------------------------------------------------------
import heapq

mi_set = {10, 3, 50, 1}
lista = list(mi_set)

heapq.heapify(lista)  # O(n)
resultado = [heapq.heappop(lista) for _ in range(len(lista))]  # n * log n

print("Heap Sort:", resultado)


# -------------------------------------------------------------
# MERGE SORT - O(n log n)
# -------------------------------------------------------------
mi_set = {10, 3, 50, 1}
lista = list(mi_set)


def merge_sort(arr):  # O(n log n)
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


merge_sort(lista)
print("Merge Sort:", lista)


# -------------------------------------------------------------
# QUICK SORT - O(n log n) promedio, O(n²) peor caso
# -------------------------------------------------------------
mi_set = {10, 3, 50, 1}
lista = list(mi_set)


def quick_sort(arr):  # O(n log n) promedio
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menores = [x for x in arr[1:] if x <= pivot]
    mayores = [x for x in arr[1:] if x > pivot]
    return quick_sort(menores) + [pivot] + quick_sort(mayores)


lista = quick_sort(lista)
print("Quick Sort:", lista)


# -------------------------------------------------------------
# INSERTION SORT - O(n²)
# -------------------------------------------------------------
mi_set = {10, 3, 50, 1}
lista = list(mi_set)

for i in range(1, len(lista)):  # O(n²)
    key = lista[i]
    j = i - 1

    while j >= 0 and lista[j] > key:
        lista[j + 1] = lista[j]
        j -= 1

    lista[j + 1] = key

print("Insertion Sort:", lista)


# -------------------------------------------------------------
# SELECTION SORT - O(n²)
# -------------------------------------------------------------
mi_set = {10, 3, 50, 1}
lista = list(mi_set)

for i in range(len(lista)):  # O(n²)
    min_index = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[min_index]:
            min_index = j
    lista[i], lista[min_index] = lista[min_index], lista[i]

print("Selection Sort:", lista)


# -------------------------------------------------------------
# BUBBLE SORT - O(n²) (el más lento)
# -------------------------------------------------------------
mi_set = {10, 3, 50, 1}
lista = list(mi_set)

for i in range(len(lista)):  # O(n²)
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Bubble Sort:", lista)
