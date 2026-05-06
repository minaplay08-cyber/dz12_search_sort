import random
import time


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    print("=" * 60)
    print("Задача 1: Сравнение линейного и бинарного поиска")
    print("=" * 60)

    data = [random.randint(1, 10_000_000) for _ in range(1_000_000)]
    target = random.choice(data)
    print(f"Размер списка: {len(data)}")
    print(f"Искомое число: {target}\n")

    start = time.perf_counter()
    linear_idx = linear_search(data, target)
    linear_time = time.perf_counter() - start
    print(f"Линейный поиск: индекс={linear_idx}, время={linear_time:.6f} сек")

    data_sorted = sorted(data)
    start = time.perf_counter()
    binary_idx = binary_search(data_sorted, target)
    binary_time = time.perf_counter() - start
    print(f"Бинарный поиск: индекс={binary_idx}, время={binary_time:.6f} сек")

    print(f"\nБинарный поиск быстрее в {linear_time / binary_time:.1f} раз\n")


if __name__ == "__main__":
    main()
