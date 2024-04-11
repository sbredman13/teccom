# Написать программу, которая сортирует список строк по длине,
# сначала по возрастанию, а затем по убыванию.

def sort_list(list_line):
    return [sorted(list_line, key=len), sorted(list_line, key=len, reverse=True)]


if __name__ == "__main__":
    list_of_line = list(map(str, input().split()))
    a, b = sort_list(list_of_line)
    print(a, b)
