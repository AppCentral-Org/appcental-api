from flask import Flask, request, jsonify
import sys
import os

sys.path.insert(1, 'services')

from services.db_connection.user_history import UserHistory

app = Flask(__name__)

@app.route('/content', methods=['POST'])
def receive_data():
    data_rec = request.json 
    print(data_rec)

    user_connect = UserHistory('datasets/users.csv')
    added_user = user_connect.add_record(data_rec)
    # recommend = RecommendByUser()
    # k_neighbors = recommend.find_nearest_neighbors()
    # print(k_neighbors)
    # places = recommend.get_places(recommend.find_nearest_neighbors())
    # print(places)

    # Returning a response
    response = {'message': 'Data received successfully'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application