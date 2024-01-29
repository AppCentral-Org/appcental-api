import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class KNNRecommendation:
    def __init__(self):
        # Load the dataset
        self.data = pd.read_csv('datasets/googleplaystore_normalized.csv')

        # Define the features used during fit
        self.feature_names = ['Category', 'Type', 'Content Rating', 'Price', 'Genres']

        # TF-IDF Vectorizer for app names
        self.tfidf_vectorizer = TfidfVectorizer()

        # Fit TF-IDF Vectorizer on app names
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.data['App'])

        self.category_mapping = {'Arte e Design': 0.9, 'Jogo': 0.03, 'Ferramentas': 0.06, 'Negócios': 0.1, 'Médico': 0.13,
                         'Produtividade': 0.16, 'Personalização': 0.19, 'Estilo de Vida': 0.23, 'Finanças': 0.26,
                         'Esportes': 0.29, 'Comunicação': 0.32, 'Saúde e Fitness': 0.35, 'Fotografia': 0.39,
                         'Notícias e Revistas': 0.42, 'Livros e Referências': 0.45, 'Viagem e Local': 0.48,
                         'Compras': 0.52, 'Social': 0.55, 'Reprodutores de Vídeo': 0.58, 'Mapas e Navegação': 0.61,
                         'Educação': 0.65, 'Comida e Bebida': 0.68, 'Entretenimento': 0.71, 'Auto e Veículos': 0.74,
                         'Bibliotecas e Demonstração': 0.77, 'Clima': 0.81, 'Casa e Família': 0.84, 'Eventos': 0.87,
                         'Quadrinhos': 1.0}

        self.type_mapping = {'Grátis': 0.0, 'Pago': 1.0}

        self.rating_mapping = {'Todos': 0.0, 'Adolescentes': 0.33, 'Todos 10+': 0.67, 'Não Classificado': 1.0}

        self.genres_mapping = {'Ferramentas': 0.0, 'Entretenimento': 0.01, 'Educação': 0.02, 'Negócios': 0.03, 'Médico': 0.03,
                       'Produtividade': 0.04, 'Personalização': 0.05, 'Estilo de Vida': 0.06, 'Finanças': 0.07,
                       'Esportes': 0.08, 'Comunicação': 0.09, 'Saúde e Fitness': 0.09, 'Fotografia': 0.1,
                       'Ação': 0.11, 'Notícias e Revistas': 0.12, 'Livros e Referências': 0.13, 'Viagem e Local': 0.14,
                       'Compras': 0.15, 'Social': 0.16, 'Simulação': 0.16, 'Arcade': 0.17, 'Casual': 0.18,
                       'Reprodutores de Vídeo e Editores': 0.19, 'Mapas e Navegação': 0.2, 'Quebra-Cabeça': 0.21,
                       'Comida e Bebida': 0.22, 'Role Playing': 0.22, 'Estratégia': 0.23, 'Corrida': 0.24,
                       'Auto e Veículos': 0.25, 'Bibliotecas e Demonstração': 0.26, 'Clima': 0.27, 'Casa e Família': 0.28,
                       'Aventura': 0.28, 'Eventos': 0.29, 'Arte e Design': 0.3, 'Beleza': 0.31, 'Quadrinhos': 0.32,
                       'Cartão': 0.33, 'Paternidade': 0.34, 'Tabuleiro': 0.34, 'Cassino': 0.35, 'Educacional - Educação': 0.36,
                       'Trivia': 0.37, 'Educacional': 0.38, 'Educação - Educação': 0.39, 'Casual - Pretend Play': 0.4,
                       'Palavra': 0.41, 'Puzzle - Jogos Cerebrais': 0.41, 'Educação - Pretend Play': 0.42, 'Música': 0.43,
                       'Corrida - Ação e Aventura': 0.44, 'Entretenimento - Música e Vídeo': 0.45, 'Tabuleiro - Jogos Cerebrais': 0.46,
                       'Arcade - Ação e Aventura': 0.47, 'Educacional - Pretend Play': 0.47, 'Casual - Ação e Aventura': 0.48,
                       'Ação - Ação e Aventura': 0.49, 'Casualn': 0.8, 'Role Playing - Educação': 0.81, 'Puzzle - Educação': 0.82,
                       'Estilo de Vida - Educação': 0.83, 'Saúde e Fitness - Ação e Aventura': 0.84, 'Comunicação - Criatividade': 0.84,
                       'Role Playing - Jogos Cerebrais': 0.85, 'Trivia - Educação': 0.86, 'Entretenimento - Educação': 0.87,
                       'Paternidade - Jogos Cerebrais': 0.88, 'Ferramentas - Educação': 0.89, 'Viagem e Local - Ação e Aventura': 0.9,
                       'Reprodutores de Vídeo e Editores - Criatividade': 0.91, 'Casual - Música e Vídeo': 0.91, 'Tabuleiro - Pretend Play': 0.92,
                       'Aventura - Educação': 0.93, 'Saúde e Fitness - Educação': 0.94, 'Música e Áudio - Música e Vídeo': 0.95,
                       'Arcade - Pretend Play': 0.96, 'Arte e Design - Pretend Play': 0.97, 'Estilo de Vida - Pretend Play': 0.97,
                       'Quadrinhos - Criatividade': 0.98, 'Arte e Design - Ação e Aventura': 0.99, 'Estratégia - Criatividade': 1.0}

    def normalize_price(self, price):
        return price / 400

    def normalize_feature(self, value, mapping):
        return mapping[value]

    def normalize_input_data(self, input_data):
        # Normalize the 'Category' feature
        input_data['category'] = self.category_mapping[input_data['category']]
        input_data['type'] = self.type_mapping[input_data['type']]
        input_data['content_rating'] = self.rating_mapping[input_data['content_rating']]
        input_data['genres'] = self.genres_mapping[input_data['genres']]

        input_data['price'] = input_data['price'] / 400

        print(input_data)

        return input_data

    def get_recommendations(self, input_data):
        # Normalize the input data
        for key in input_data.keys():
            if type(input_data[key]) == str:
                input_data = self.normalize_input_data(input_data)
                break

        for key in input_data.keys():
            input_data[key] = [input_data[key]]

        print(input_data)

        # Convert input data dictionary into a DataFrame
        input_df = pd.DataFrame(input_data)

        print(input_df)

        # Calculate Euclidean distance between the input and each data point
        distances = np.sqrt(np.sum((self.data[self.feature_names].values - input_df.values) ** 2, axis=1))

        # Get indices of the 10 nearest neighbors
        indices = np.argsort(distances)[:10]

        # Return the corresponding rows from the original dataset
        recommendations = self.data.iloc[indices]
        return recommendations

    def recommend_by_download(self, input_data):
        recommendations = []

        # Iterate over the first 500 rows (registers) in the dataset
        for index, row in self.data.iloc[:500].iterrows():
            try:
                # Find the nearest neighbor in the input_data dictionary
                nearest_neighbor_name, nearest_neighbor_data = self.get_nearest_neighbor(row, input_data)
                
                # Check if the nearest neighbor has a 'status' equal to 1
                if nearest_neighbor_data['status'] == 1:
                    recommendations.append(row)  # Add the register to the list of recommendations
            except Exception as e:
                print("Error in recommend_by_download:", e)

        # Convert the list of recommendations to a DataFrame
        recommendations_df = pd.DataFrame(recommendations)
        return recommendations_df

    def get_nearest_neighbor(self, row, input_data):
        min_distance = float('inf')
        nearest_neighbor_name = None
        nearest_neighbor_data = None

        # Extract TF-IDF vector for the input app name
        input_app_name = next(iter(input_data))
        input_tfidf_vector = self.tfidf_vectorizer.transform([input_app_name])

        # Iterate over each entry in the input_data dictionary
        for app_name, app_data in input_data.items():
            try:
                # Calculate the Manhattan distance between the features of the row and app_data
                distance = np.sum(np.abs(row[self.feature_names].values - np.array([v for k, v in app_data.items() if k != 'status'])))

                # Calculate cosine similarity between TF-IDF vectors of app names
                app_name_index = self.data[self.data['App'] == app_name].index[0]
                app_tfidf_vector = self.tfidf_matrix[app_name_index]
                cosine_similarity = np.dot(input_tfidf_vector, app_tfidf_vector.T).toarray()[0][0]

                # Incorporate cosine similarity into distance calculation
                distance *= (1 - cosine_similarity)

                # Update the nearest neighbor if the current distance is smaller
                if distance < min_distance:
                    min_distance = distance
                    nearest_neighbor_name = app_name
                    nearest_neighbor_data = app_data
            except Exception as e:
                print("Error in get_nearest_neighbor:", e)

        return nearest_neighbor_name, nearest_neighbor_data





