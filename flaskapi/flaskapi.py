from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)

@app.route('/data/', methods=['GET'])
def get_data():
    connection = sqlite3.connect(r'C:\Users\tyler\OneDrive - SNHU\Desktop\Data Scraping API\db.sqlite3')

    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM flaskapi_table")
    return jsonify({'data': data.fetchall()})

@app.route('/data/<string:id>', methods=['GET'])
def get_id(id):
    connection = sqlite3.connect(r'C:\Users\tyler\OneDrive - SNHU\Desktop\Data Scraping API\db.sqlite3')
    cursor = connection.cursor()
    data = cursor.execute(f"SELECT * FROM flaskapi_table WHERE id={id}")
    return jsonify({'data': data.fetchall()})

if __name__ == '__main__':
    app.run(debug=True)