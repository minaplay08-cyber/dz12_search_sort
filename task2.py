import random
import time


def bubble_sort(arr):
    n = len(arr)
    a = arr[:]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def main():
    print("=" * 60)
    print("Задача 2: Сортировка пузырьком vs встроенная сортировка")
    print("=" * 60)

    data = [random.randint(1, 100_000) for _ in range(10_000)]
    print(f"Размер списка: {len(data)}\n")

    start = time.perf_counter()
    bubble_sorted = bubble_sort(data)
    bubble_time = time.perf_counter() - start
    print(f"Сортировка пузырьком: время={bubble_time:.6f} сек")

    start = time.perf_counter()
    builtin_sorted = sorted(data)
    builtin_time = time.perf_counter() - start
    print(f"Встроенная сортировка: время={builtin_time:.6f} сек")

    print(f"\nВстроенная сортировка быстрее в {bubble_time / builtin_time:.1f} раз\n")


if __name__ == "__main__":
    main()
