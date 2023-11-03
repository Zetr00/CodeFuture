def count_substring_occurrences(substring, main_string):
    count = 0
    start = 0
    while True:
        start = main_string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

main_string = input("Введите строку для поиска подстроки: ")
substring = input("Введите подстроку: ")

result = count_substring_occurrences(substring, main_string)
print(f"Количество встреченных подстрок: {result}")
