# Написать функцию, которая принимает на вход два целых числа
# (минимум и максимум) и возвращает список
# всех простых чисел в заданном диапазоне.
# Решение 2. Для случаев, где нужно генерировать диапозон чисел
# в зависимости от позиции максимального числа.

def list_gen(min_num, max_num):
    if min_num > max_num:
        gen_list = [i for i in range(min_num, max_num - 1, -1)]
    else:
        gen_list = [i for i in range(min_num, max_num + 1)]
    return gen_list

if __name__ == "__main__":
    min_n = int(input())
    max_n = int(input())
    print(list_gen(min_n, max_n))
