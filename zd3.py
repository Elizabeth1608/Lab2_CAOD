def recursive_count(some_list, t):
    # Базовый случай: список пустой
    if len(some_list) == 0:
        return 0
    
    # Рекурсивный случай: проверяем первый элемент
    if some_list[0] == t:
        return 1 + recursive_count(some_list[1:], t)
    else:
        return recursive_count(some_list[1:], t)


print("Проверка работы функции:")

print(recursive_count([1, 2, 3, 2, 4, 2], 2))   
print(recursive_count([1, 1, 1, 1], 1))         
print(recursive_count([1, 2, 3], 5))            
print(recursive_count([], 1))                  
print(recursive_count(["a", "b", "a", "c"], "a"))  
