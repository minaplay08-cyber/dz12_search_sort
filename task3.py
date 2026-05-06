import random
import time


class Student:
    def __init__(self, name, group, gpa):
        self.name = name
        self.group = group
        self.gpa = gpa

    def __repr__(self):
        return f"Student(name='{self.name}', group='{self.group}', gpa={self.gpa})"


def generate_students(n):
    first_names = ["Анна", "Иван", "Мария", "Пётр", "Елена", "Дмитрий",
                   "Ольга", "Сергей", "Наталья", "Алексей", "Татьяна", "Михаил",
                   "Екатерина", "Андрей", "Юлия", "Николай", "Светлана", "Владимир"]
    last_names = ["Иванова", "Петров", "Сидорова", "Козлов", "Новикова",
                  "Морозов", "Волкова", "Соколов", "Лебедева", "Кузнецов"]
    groups = ["ИС-101", "ИС-102", "П-201", "П-202", "М-301", "М-302"]
    students = []
    for i in range(n):
        name = random.choice(last_names) + " " + random.choice(first_names)
        group = random.choice(groups)
        gpa = round(random.uniform(2.0, 5.0), 2)
        students.append(Student(name, group, gpa))
    return students


def linear_search_by_name(students, target_name):
    for i, s in enumerate(students):
        if s.name == target_name:
            return i
    return -1


def binary_search_by_gpa(students_sorted, target_gpa):
    left, right = 0, len(students_sorted) - 1
    while left <= right:
        mid = (left + right) // 2
        if abs(students_sorted[mid].gpa - target_gpa) < 0.005:
            return mid
        elif students_sorted[mid].gpa < target_gpa:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    print("=" * 60)
    print("Задача 3: Поиск студента")
    print("=" * 60)

    students = generate_students(10_000)
    print(f"Количество студентов: {len(students)}\n")

    target_student = random.choice(students)
    target_name = target_student.name
    target_gpa = target_student.gpa
    print(f"Ищем по имени: {target_name}")
    print(f"Ищем по GPA: {target_gpa}\n")

    start = time.perf_counter()
    idx_name = linear_search_by_name(students, target_name)
    time_name = time.perf_counter() - start
    if idx_name != -1:
        print(f"Поиск по имени (линейный): найден -> {students[idx_name]}")
    else:
        print("Поиск по имени (линейный): не найден")
    print(f"Время: {time_name:.6f} сек\n")

    students_by_gpa = sorted(students, key=lambda s: s.gpa)
    start = time.perf_counter()
    idx_gpa = binary_search_by_gpa(students_by_gpa, target_gpa)
    time_gpa = time.perf_counter() - start
    if idx_gpa != -1:
        print(f"Поиск по GPA (бинарный): найден -> {students_by_gpa[idx_gpa]}")
    else:
        print("Поиск по GPA (бинарный): не найден")
    print(f"Время: {time_gpa:.6f} сек\n")


if __name__ == "__main__":
    main()
