import matplotlib.pyplot as plt
import time
import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def random_list(n):
    return [random.randint(1, 100000) for _ in range(n)]

def sorted_list(n):
    return list(range(n))

def reverse_list(n):
    return list(range(n, 0, -1))

sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

data_types = {
    "Случайные числа": random_list,
    "Отсортированный список": sorted_list,
    "Обратно отсортированный список": reverse_list
}

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for ax, (name, generator) in zip(axes, data_types.items()):
    times_sel = []
    times_quick = []
    
    for size in sizes:
        data = generator(size)
        t = time.time(); selection_sort(data.copy()); times_sel.append(time.time() - t)
        t = time.time(); quick_sort(data.copy()); times_quick.append(time.time() - t)
    
    ax.plot(sizes, times_sel, 'o-', color='blue', label='Выбором (O(n²))')
    ax.plot(sizes, times_quick, 's-', color='red', label='Быстрая (O(n log n))')
    ax.set_xlabel('Размер массива (n)')
    ax.set_ylabel('Время (сек)')
    ax.set_title(name)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

plt.tight_layout()
plt.show()