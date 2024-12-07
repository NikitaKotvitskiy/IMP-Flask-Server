from flask import Flask, jsonify, request

app = Flask(__name__)

rooms = [
    {"id": 1, "name": "Living Room"},
    {"id": 2, "name": "Bedroom"},
    {"id": 3, "name": "Storage"},
]

parameters = {
    1: [
        {"id": 1, "name": "Fan", "value": "off", "type": "boolean"},
        {"id": 2, "name": "Humidity", "value": 40.5, "type": "float", "range": [30, 70], "step": 0.5},
        {"id": 3, "name": "Light 1", "value": 0, "type": "boolean"},
        {"id": 4, "name": "Light 2", "value": 0, "type": "boolean"},
        {"id": 5, "name": "Light 3", "value": 0, "type": "boolean"},
        {"id": 6, "name": "Light 4", "value": 0, "type": "boolean"},
        {"id": 7, "name": "Temp.", "value": 18.0, "type": "float", "range": [15, 30], "step": 0.5},
        {"id": 8, "name": "Music", "value": 0, "type": "boolean"},
        {"id": 9, "name": "Volume", "value": 5, "type": "integer", "range": [0, 10], "step": 1},
    ],
    2: [
        {"id": 10, "name": "Light", "value": "on", "type": "boolean"}
    ],
    3: [
        {"id": 11, "name": "Lock", "value": 1, "type": "boolean"},
        {"id": 12, "name": "Signalization", "value": 1, "type": "boolean"},
    ],

}

@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms)

@app.route('/rooms/<int:room_id>/parameters', methods=['GET'])
def get_room_parameters(room_id):
    return jsonify(parameters.get(room_id, []))

@app.route('/parameters/<int:param_id>', methods=['GET'])
def get_parameter(param_id):
    for room_params in parameters.values():
        for param in room_params:
            if param["id"] == param_id:
                return jsonify(param)
    return jsonify({"error": "Parameter not found"}), 404

@app.route('/parameters/<int:param_id>', methods=['POST'])
def update_parameter(param_id):
    for room_params in parameters.values():
        for param in room_params:
            if param["id"] == param_id:
                data = request.get_json()
                if "value" in data:
                    param["value"] = data["value"]
                    return jsonify(param)
    return jsonify({"error": "Parameter not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)