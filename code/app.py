from flask import Flask, jsonify, request

app  = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes', methods=['GET'])
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_incomes():
    incomes.append(request.get_json())
    return jsonify(incomes)


if __name__ == "__main__":
    app.run(debug=True)
