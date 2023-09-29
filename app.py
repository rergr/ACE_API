from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def intro():
    response = {
        "Welcome to the api the endpoints are as follows": ["/api/temp?celsius={number}","/api/prime?limit={number}","/api/number?n={number}"
        ]
    }
    return jsonify(response)


@app.route('/api/temp', methods=['GET'])
def return_kelvin():
    celsius = request.args.get('celsius')
    if celsius is not None:
        try:
            celsius = float(celsius)
            kelvin = celsius + 273.15
            response = {
                "temperature_celsius": celsius,
                "temperature_kelvin": kelvin
            }
            return jsonify(response)
        except ValueError:
            error_response = {
                "error": "Invalid temperature value. Please provide a valid number."
            }
            return jsonify(error_response), 400
    else:
        error_response = {
            "error": "Temperature in Celsius is not provided. Use the 'celsius' query parameter."
        }
        return jsonify(error_response), 400


@app.route('/api/prime', methods=['GET'])
def return_primes():
    limit = request.args.get('limit')
    if limit is not None:
        try:
            limit = int(limit)
            if limit >= 10000:
                error_response = {
                    "error": "The limit is 10'000 please chose a number lower then or equal to 10'000"
                }
                return jsonify(error_response), 400

            response = {
                "prime Numbers": get_prime_numbers(limit)
            }

            return jsonify(response)
        except ValueError:
            error_response = {
                "error": "Invalid value provided. Please provide a valid number (Int)."
            }
            return jsonify(error_response), 400
    else:
        error_response = {
            "error": "Prime limit is not provided. Use the 'limit' query parameter."
        }
        return jsonify(error_response), 400


@app.route('/api/number', methods=['GET'])
def return_fibo():
    n = request.args.get('n')
    if n is not None:
        try:
            n = int(n)

            response = {
                "number": get_n_fibo_number(n)
            }

            return jsonify(response)
        except ValueError:
            error_response = {
                "error": "Invalid value provided. Please provide a valid number (int)."
            }
            return jsonify(error_response), 400
    else:
        error_response = {
            "error": "Temperature in Celsius is not provided. Use the 'celsius' query parameter."
        }
        return jsonify(error_response), 400


def get_prime_numbers(num):
    prime = [True for _ in range(num + 1)]

    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    response = []

    for p in range(2, num + 1):
        if prime[p]:
            response.append(p)

    return response


def get_n_fibo_number(n):
    a = 0
    b = 1

    for i in range(2, n):
        a, b = b, a + b

    return a + b


if __name__ == '__main__':
    app.run()