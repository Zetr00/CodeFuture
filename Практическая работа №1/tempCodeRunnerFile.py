case '3':
        print("Задание №3")
        print("Выберите фигуру для расчета:")
        print("1. Прямоугольник")
        print("2. Квадрат")
        print("3. Круг")
        print("4. Треугольник")
        print("5. Прямоугольный треугольник")
        print("6. Прямоугольный параллелепипед")
        print("7. Куб")
        print("8. Шар")
        print("9. Конус")

        choice = int(input("Введите номер фигуры: "))

        if choice == 1:
            length = float(input("Введите длину прямоугольника: "))
            width = float(input("Введите ширину прямоугольника: "))
            area = length * width
            print(f"Площадь прямоугольника: {area}")
        elif choice == 2:
            side = float(input("Введите сторону квадрата: "))
            area = side * side
            print(f"Площадь квадрата: {area}")
        elif choice == 3:
            radius = float(input("Введите радиус круга: "))
            area = math.pi * (radius ** 2)
            print(f"Площадь круга: {area}")
        elif choice == 4:
            base = float(input("Введите основание треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            area = 0.5 * base * height
            print(f"Площадь треугольника: {area}")
        elif choice == 5:
            base = float(input("Введите основание прямоугольного треугольника: "))
            height = float(input("Введите высоту прямоугольного треугольника: "))
            area = 0.5 * base * height
            print(f"Площадь прямоугольного треугольника: {area}")
        elif choice == 6:
            length = float(input("Введите длину прямоугольного параллелепипеда: "))
            width = float(input("Введите ширину прямоугольного параллелепипеда: "))
            height = float(input("Введите высоту прямоугольного параллелепипеда: "))
            volume = length * width * height
            print(f"Объем прямоугольного параллелепипеда: {volume}")
        elif choice == 7:
            side = float(input("Введите длину стороны куба: "))
            volume = side ** 3
            print(f"Объем куба: {volume}")
        elif choice == 8:
            radius = float(input("Введите радиус шара: "))
            volume = (4/3) * math.pi * (radius ** 3)
            print(f"Объем шара: {volume}")
        elif choice == 9:
            radius = float(input("Введите радиус основания конуса: "))
            height = float(input("Введите высоту конуса: "))
            volume = (1/3) * math.pi * (radius ** 2) * height
            print(f"Объем конуса: {volume}")
        else:
            print("Неверный выбор фигуры. Пожалуйста, выберите корректный номер.")