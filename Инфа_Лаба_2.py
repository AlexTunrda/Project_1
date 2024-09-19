from random import *
def f(a,b,c):
    max_x = max(a, b, c)
    min_x = min(a, b, c)
    if abs(max_x) > abs(min_x):
        return max_x, "max"
    else:
        return min_x, "min"
#---------------ТЕСТ------------------
maxf=0
minf=0
while maxf==0 or minf==0:
    a = randrange( -1000 , 1000 )
    b = randrange( -1000 , 1000 )
    c = randrange( -1000 , 1000 )
    x,d = f(a,b,c)
    if d=="max":maxf+=1
    else:minf+=1
    print(x, d)
print("Успех!!!!!")
'''def replace_min_with_sum(a, b, c):
    min_value = min(a, b, c)
    if min_value == a:
        a = b + c
    elif min_value == b:
        b = a + c
    else:
        c = a + b
    return a, b, c

# Тесты
test_cases = [
    (1, 2, 3),
    (4, 3, 2),
    (0, 0, 0),
    (-1, -2, -3),
    (5, 5, 5),
]

for test in test_cases:
    a, b, c = test
    result = replace_min_with_sum(a, b, c)
    expected_result = tuple(sorted([a, b, c]))  # Ожидаемый результат - кортеж, содержащий значения в порядке возрастания
    if result == expected_result:
        print(f"Тест пройден для a={a}, b={b}, c={c}")
    else:
        print(f"Тест НЕ пройден для a={a}, b={b}, c={c}. Ожидаемый результат: a={expected_result[0]}, b={expected_result[1]}, c={expected_result[2]}, Фактический результат: a={result[0]}, b={result[1]}, c={result[2]}'''