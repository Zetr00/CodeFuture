notes = {}

while True:
    print("Выберите действие:")
    print("1. Добавить заметку")
    print("2. Удалить заметку")
    print("3. Вывести список заметок")
    print("4. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        title = input("Введите название заметки: ")
        content = input("Введите текст заметки: ")
        notes[title] = content
        print("Заметка добавлена")

    elif choice == "2":
        if len(notes) == 0:
            print("Нет заметок для удаления.")
        else:
            print("Список заметок:")
            for title in notes:
                print(title)
            title_to_delete = input("Введите название заметки для удаления: ")
            if title_to_delete in notes:
                del notes[title_to_delete]
                print("Заметка удалена")
            else:
                print("Заметка с таким названием не найдена.")

    elif choice == "3":
        if len(notes) == 0:
            print("Нет заметок.")
        else:
            print("Список заметок:")
            for title, content in notes.items():
                print(f"{title}: {content}")

    elif choice == "4":
        print("Выход из приложения.")
        break

    else:
        print("Неверная команда. Пожалуйста, выберите действие из списка.")