class Engine:
    def __init__(self, weight, max_speed, fuel_consumption):
        self.weight = weight
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption


class Tank:
    def __init__(self, weight, tank_volume):
        self.weight = weight
        self.tank_volume = tank_volume


class Brakes:
    def __init__(self, weight, brake_efficiency):
        self.weight = weight
        self.brake_efficiency = brake_efficiency


class Body:
    def __init__(self, weight):
        self.weight = weight


class Car:
    def __init__(self, name, engine, tank, brakes, body):
        self.name = name
        self.engine = engine
        self.tank = tank
        self.brakes = brakes
        self.body = body

        self.weight = self.engine.weight + self.tank.weight + self.brakes.weight + self.body.weight
        self.max_distance_per_tank = (self.tank.tank_volume / self.engine.fuel_consumption) * self.engine.max_speed
        self.braking_distance = self.weight / self.brakes.brake_efficiency


if __name__ == "__main__":
    engine_weight = float(input("Введите вес двигателя: "))
    engine_max_speed = float(input("Введите максимальную скорость двигателя: "))
    engine_fuel_consumption = float(input("Введите потребление топлива двигателем: "))

    tank_weight = float(input("Введите вес бака: "))
    tank_volume = float(input("Введите объем бака: "))

    brakes_weight = float(input("Введите вес тормозов: "))
    brake_efficiency = float(input("Введите эффективность тормозов: "))

    body_weight = float(input("Введите вес кузова: "))

    engine = Engine(engine_weight, engine_max_speed, engine_fuel_consumption)
    tank = Tank(tank_weight, tank_volume)
    brakes = Brakes(brakes_weight, brake_efficiency)
    body = Body(body_weight)

    car_name = input("Введите название машины: ")

    car = Car(car_name, engine, tank, brakes, body)

    print(f"Название машины: {car.name}")
    print(f"Вес машины: {car.weight} кг")
    print(f"Максимальный пробег на одном баке: {car.max_distance_per_tank} км")
    print(f"Тормозной путь: {car.braking_distance} метров")
