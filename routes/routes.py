from flask import Flask, request, jsonify
import numpy as np
import sys
import os

import pandas as pd

class UserHistory:
    def __init__(self, file_path, data_dict):
        self.data_dict = data_dict
        self.file_path = file_path
        self.users = pd.read_csv(file_path)

    def add_record(self):
        try:
            user_data = [self.data_dict["name"]] + [0] * (35)

            user_att = list(self.users.columns)

            user_data[user_att.index(self.data_dict["category"])] = 1
            user_data[user_att.index(self.data_dict["contentRating"])] = 1
            user_data[1] = self.data_dict["price"]

            self.users.loc[len(self.users)] = user_data

            self.users.to_csv(self.file_path, index=False)
            
            return True  # Indicates successful addition
            

        except Exception as e:
            print(f"Error: {e}")
            return False  # Indicates failure
        
    def check_name(self):
        return self.users.loc[self.users["User"] == self.data_dict["name"]]["User"].count()



class ContentRec:

    def find_nearest_neighbors(self, k=5):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv('datasets/apps.csv')

            # Extract values from the last record for specific columns
            last_record_values = df[df.columns.tolist()[1:]].iloc[-1].values

            # Calculate Euclidean distance between new record and existing records
            df['euclidean_distance'] = np.linalg.norm(df[df.columns.tolist()[1:]].values - last_record_values, axis=1)

            # Get k records with shortest Euclidean distance (excluding the last record)
            nearest_neighbors = df.nsmallest(k + 1, 'euclidean_distance')

            # Return a list of indices of the nearest neighbors
            return nearest_neighbors.index.tolist()[1:]
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    #  


app = Flask(__name__)

@app.route('/content', methods=['POST'])
def receive_data():
    data_rec = request.json

    user_connect = UserHistory('datasets/users.csv', data_rec)
    user_connect.add_record()
    if(user_connect.check_name() > 5):
        recommend = ContentRec()
        k_neighbors = recommend.find_nearest_neighbors()
        print(k_neighbors)

    # places = recommend.get_places(recommend.find_nearest_neighbors())
    # print(places)

    # Returning a response
    response = {'message': 'Data received successfully'}
    return jsonify(response), 200


# @app.route('/appstatus', methods=['POST'])
# def receive_data():
#     data_rec = request.json

#     user_connect = UserHistory('datasets/users.csv')
#     user_connect.add_record(data_rec)

    
#     # recommend = RecommendByUser()
#     # k_neighbors = recommend.find_nearest_neighbors()
#     # print(k_neighbors)
#     # places = recommend.get_places(recommend.find_nearest_neighbors())
#     # print(places)

#     # Returning a response
#     response = {'message': 'Data received successfully'}
#     return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application