

# Question 1
from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

# Question 2

from flask import Flask, jsonify, abort
import mysql.connector

app = Flask(__name__)


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Finland@123',
    database='fight_game'
)

def get_airport_from_db(icao):

    try:
        connection = mysql.connector.connect
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT icao, Name, Location FROM airports WHERE icao = %s",)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    airport = get_airport_from_db(icao)
    if not airport:
        abort(404, description="Airport not found")

    response = {
        "ICAO": airport['ICAO'],
        "Name": airport['Name'],
        "Location": airport['Location']
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)





