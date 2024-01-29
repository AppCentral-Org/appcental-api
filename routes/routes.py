from flask import Flask, request, jsonify
import sys
import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from services.recommendation.recommendation_model import KNNRecommendation  # Update this import

app = Flask(__name__)

# Instantiate the KNNRecommendation class
recommendation_model = KNNRecommendation()

@app.route('/get_user_name', methods=['POST'])
def get_user_name():
    try:
        data = request.get_json()

        print(data)

        # Return the user's name as a JSON response
        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    try:
        data = request.get_json()

        # Get recommendations using the content-based model
        recommendations = recommendation_model.get_recommendations(data)

        # Convert recommendations to a list of dictionaries
        recommendations_list = recommendations.to_dict(orient='records')

        # Return the recommendations as a JSON response
        return jsonify({"recommendations": recommendations_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_recommendations_by_download', methods=['POST'])
def get_recommendations_by_download():
    try:
        data = request.get_json()


        # Get recommendations using the download-based model
        recommendations = recommendation_model.recommend_by_download(data)


        # Convert recommendations to a list of dictionaries
        recommendations_list = recommendations.to_dict(orient='records')

        # Return the recommendations as a JSON response
        return jsonify({"recommendations": recommendations_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
