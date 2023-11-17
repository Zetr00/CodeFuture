from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [
    {"id": 1, "brand": "Мерседес", "model": "E-Class", "year": 2020},
    {"id": 2, "brand": "БМВ", "model": "5 Series", "year": 2021},
    {"id": 3, "brand": "Ауди", "model": "A4", "year": 2019},
    {"id": 4, "brand": "БМВ", "model": "X3", "year": 2022},
    {"id": 5, "brand": "Мерседес", "model": "S-Class", "year": 2023}
]

# Получение всех машин
@app.route('/api/cars', methods=['GET'])
def get_cars():
    return jsonify({"машины": cars})

# Получение информации о конкретной машине по ID
@app.route('/api/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car:
        return jsonify({"машина": car})
    return jsonify({"сообщение": "Машина не найдена"}), 404

# Поиск машины по бренду, модели или году
@app.route('/api/search', methods=['GET'])
def search_cars():
    query = request.args.get('q')
    if query:
        result = [car for car in cars if query.lower() in car['brand'].lower() or query.lower() in car['model'].lower() or query.lower() in str(car['year'])]
        if result:
            return jsonify({"результат": result})
    return jsonify({"сообщение": "Машины не найдены"}), 404

# Добавление новой машины
@app.route('/api/cars', methods=['POST'])
def add_car():
    data = request.json
    if data and 'brand' in data and 'model' in data and 'year' in data:
        new_id = max(car['id'] for car in cars) + 1
        new_car = {"id": new_id, "brand": data['brand'], "model": data['model'], "year": data['year']}
        cars.append(new_car)
        return jsonify({"машина": new_car}), 201
    return jsonify({"сообщение": "Неверные данные"}), 400

# Удаление машины по ID
@app.route('/api/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    global cars
    cars = [car for car in cars if car['id'] != car_id]
    return jsonify({"сообщение": "Машина удалена"}), 200

if __name__ == '__main__':
    app.run(debug=True)
