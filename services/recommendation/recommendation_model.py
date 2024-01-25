import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.neighbors import NearestNeighbors

class KNNRecommendation:
    def __init__(self):
        # Load the normalized dataset
        self.data = pd.read_csv('datasets/googleplaystore_normalized.csv')

        # Define the features used during fit, including 'Gender'
        self.feature_names = ['Category', 'Type', 'Content Rating', 'Price', 'Genres']

        # Create a scaler and fit on the features
        self.scaler = StandardScaler()
        self.data[self.feature_names] = self.scaler.fit_transform(self.data[self.feature_names])

        # Create an imputer and fit on the features
        self.imputer = SimpleImputer()
        self.data[self.feature_names] = self.imputer.fit_transform(self.data[self.feature_names])

        # Create a Nearest Neighbors model
        self.knn_model = NearestNeighbors(n_neighbors=10, algorithm='auto', metric='euclidean')
        self.knn_model.fit(self.data[self.feature_names])

    def get_recommendations(self, input_data):
        # Ensure the input data has the same columns as the features used during fit
        input_df = pd.DataFrame([input_data], columns=self.feature_names)

        # Replace missing values with the mean in the input data
        input_df = pd.DataFrame(self.imputer.transform(input_df), columns=self.feature_names)

        # Standardize the input data
        input_df = pd.DataFrame(self.scaler.transform(input_df), columns=self.feature_names)

        # Find 10 nearest neighbors
        distances, indices = self.knn_model.kneighbors(input_df)

        # Return the corresponding rows from the original dataset
        recommendations = self.data.iloc[indices[0]]
        return recommendations
