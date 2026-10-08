import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(100000)

# Обычные рекурсивные версии - O(2^n)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


# Быстрая версия Фибоначчи через Люка - O(log n)
# Формула из задания: Fn = (Fi + Lj)(Fi + Li) // 2, где i = n//2, j = n-i
def fib_with_lucas(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    i = n // 2
    j = n - i

    fi = fib_with_lucas(i)   # F(i)
    li = lucas(i)            # L(i) - обычная медленная (только для малых i)
    lj = lucas(j)            # L(j) - обычная медленная

    return (fi + lj) * (fi + li) // 2


# Быстрая версия Люка через Фибоначчи - O(log n)
# Формула из задания: Ln = F(n-1) + F(n+1)
def lucas_with_fib(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return fib_with_lucas(n - 1) + fib_with_lucas(n + 1)


print("Проверка корректности:")
print(f"{'n':>5} | {'fib':>10} | {'fib_lucas':>10} | {'lucas':>10} | {'lucas_fib':>10}")
for n in range(11):
    print(f"{n:>5} | {fibonacci(n):>10} | {fib_with_lucas(n):>10} | {lucas(n):>10} | {lucas_with_fib(n):>10}")

print("\nЗамеряем время...")
sizes = [5, 10, 15, 20, 25, 30, 32, 35]
times_fib = []
times_fast = []

for n in sizes:
    start = time.perf_counter()
    fibonacci(n)
    times_fib.append(time.perf_counter() - start)

    start = time.perf_counter()
    fib_with_lucas(n)
    times_fast.append(time.perf_counter() - start)

print(f"\n{'N':>5} | {'fibonacci':>15} | {'fib_with_lucas':>15}")
print("-" * 50)
for i, n in enumerate(sizes):
    print(f"{n:>5} | {times_fib[i]:>15.6f}с | {times_fast[i]:>15.6f}с")


plt.figure(figsize=(10, 6))
plt.plot(sizes, times_fib, 'o-', color='blue', label='fibonacci (обычная, O(2^n))')
plt.plot(sizes, times_fast, 's-', color='red', label='fib_with_lucas (быстрая, O(log n))')
plt.xlabel('N')
plt.ylabel('Время (секунды)')
plt.title('Сравнение fibonacci и fib_with_lucas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()