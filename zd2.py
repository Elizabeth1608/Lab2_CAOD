def tribonacci(n):
    # Базовые случаи
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Рекурсивный случай
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# Проверка
for i in range(10):
    print(f"tribonacci({i}) = {tribonacci(i)}")