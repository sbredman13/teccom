# Написать функцию, которая принимает на вход список целых чисел
# и возвращает новый список,
# cодержащий только уникальные элементы из исходного списка.

def list_of_unique_numbers(num_list):
    unique_list = set(num_list)
    return list(unique_list)


if __name__ == "__main__":
    enter_num_list = list(map(int, input().split()))
    print(list_of_unique_numbers(enter_num_list))
