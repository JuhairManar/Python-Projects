from flask import Flask, request, jsonify

database = {'Hasib': '625', 'Kelvin': '355'}

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to my cute web API"

@app.route('/data/', methods=['GET'])
def get_data():
    return jsonify(database)

@app.route('/data/', methods=['POST'])
def add_data():
    data = request.get_json()
    if 'name' in data and 'id' in data:
        database[data['name']] = data['id']
        return jsonify({"message": "Data added successfully"})
    else:
        return jsonify({"error": "Name and id are required"}), 400

@app.route('/data/<name>/', methods=['DELETE'])
def delete_data(name):
    if name in database:
        database.pop(name)
        return jsonify({"message": f"Data for {name} deleted successfully"})
    else:
        return jsonify({"error": f"No data found for {name}"}), 404

if __name__ == '__main__':
    app.run(debug=True)
