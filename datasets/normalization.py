# Define mappings for 'Category'
category_mapping = {
  'FAMILY': 0.0,
  'GAME': 0.1,
  'TOOLS': 0.2,
  'BUSINESS': 0.3,
  'MEDICAL': 0.4,
  'PRODUCTIVITY': 0.5,
  'PERSONALIZATION': 0.6,
  'LIFESTYLE': 0.7,
  'FINANCE': 0.8,
  'SPORTS': 0.9,
  'COMMUNICATION': 1.0,
  'HEALTH_AND_FITNESS': 1.1,
  'PHOTOGRAPHY': 1.2,
  'NEWS_AND_MAGAZINES': 1.3,
  'BOOKS_AND_REFERENCE': 1.4,
  'TRAVEL_AND_LOCAL': 1.5,
  'SHOPPING': 1.6,
  'SOCIAL': 1.7,
  'VIDEO_PLAYERS': 1.8,
  'MAPS_AND_NAVIGATION': 1.9,
  'EDUCATION': 2.0,
  'FOOD_AND_DRINK': 2.1,
  'ENTERTAINMENT': 2.2,
  'AUTO_AND_VEHICLES': 2.3,
  'LIBRARIES_AND_DEMO': 2.4,
  'WEATHER': 2.5,
  'HOUSE_AND_HOME': 2.6,
  'EVENTS': 2.7,
  'ART_AND_DESIGN': 2.8,
  'PARENTING': 2.9,
  'BEAUTY': 3.0,
  'COMICS': 3.1,
}

# Define mappings for 'Type'
type_mapping = {
  'Free': 0.0,
  'Paid': 1.0,
}

# Define mappings for 'Content Rating'
content_rating_mapping = {
  'Everyone': 0.0,
  'Teen': 0.1,
  'Everyone 10+': 0.2,
  'Unrated': 0.3,
}

# Define mappings for 'Genres'
genres_mapping = {
  'Tools': 0.0,
  'Entertainment': 0.1,
  'Education': 0.2,
  'Business': 0.3,
  'Medical': 0.4,
  'Productivity': 0.5,
  'Personalization': 0.6,
  'Lifestyle': 0.7,
  'Finance': 0.8,
  'Sports': 0.9,
  'Communication': 1.0,
  'Health & Fitness': 1.1,
  'Photography': 1.2,
  'Action': 1.3,
  'News & Magazines': 1.4,
  'Books & Reference': 1.5,
  'Travel & Local': 1.6,
  'Shopping': 1.7,
  'Social': 1.8,
  'Simulation': 1.9,
  'Arcade': 2.0,
  'Casual': 2.1,
  'Video Players & Editors': 2.2,
  'Maps & Navigation': 2.3,
  'Puzzle': 2.4,
  'Food & Drink': 2.5,
  'Role Playing': 2.6,
  'Strategy': 2.7,
  'Racing': 2.8,
  'Auto & Vehicles': 2.9,
  'Libraries & Demo': 3.0,
    'Weather': 3.1,
    'House & Home': 3.2,
    'Adventure': 3.3,
    'Events': 3.4,
    'Art & Design': 3.5,
    'Beauty': 3.6,
    'Comics': 3.7,
    'Card': 3.8,
    'Parenting': 3.9,
    'Board': 4.0,
    'Casino': 4.1,
    'Educational;Education': 4.2,
    'Trivia': 4.3,
    'Educational': 4.4,
    'Education;Education': 4.5,
    'Casual;Pretend Play': 4.6,
    'Word': 4.7,
    'Puzzle;Brain Games': 4.8,
    'Education;Pretend Play': 4.9,
    'Music': 5.0,
    'Racing;Action & Adventure': 5.1,
    'Entertainment;Music & Video': 5.2,
    'Board;Brain Games': 5.3,
    'Arcade;Action & Adventure': 5.4,
    'Educational;Pretend Play': 5.5,
    'Casual;Action & Adventure': 5.6,
    'Action;Action & Adventure': 5.7,
    'Casual;Brain Games': 5.8,
    'Parenting;Education': 5.9,
    'Simulation;Action & Adventure': 6.0,
    'Entertainment;Brain Games': 6.1,
    'Art & Design;Creativity': 6.2,
    'Parenting;Music & Video': 6.3,
    'Casual;Creativity': 6.4,
    'Education;Creativity': 6.5,
    'Educational;Brain Games': 6.6,
    'Adventure;Action & Adventure': 6.7,
    'Educational;Creativity': 6.8,
    'Role Playing;Action & Adventure': 6.9,
    'Education;Brain Games': 7.0,
    'Sports;Action & Adventure': 7.1,
    'Role Playing;Pretend Play': 7.2,
    'Education;Action & Adventure': 7.3,
    'Entertainment;Action & Adventure': 7.4,
    'Simulation;Education': 7.5,
    'Casual;Education': 7.6,
    'Music;Music & Video': 7.7,
    'Simulation;Pretend Play': 7.8,
    'Entertainment;Creativity': 7.9,
    'Puzzle;Action & Adventure': 8.0,
    'Education;Music & Video': 8.1,
    'Board;Action & Adventure': 8.2,
    'Educational;Action & Adventure': 8.3,
    'Card;Action & Adventure': 8.4,
    'Video Players & Editors;Music & Video': 8.5,
    'Strategy;Action & Adventure': 8.6,
    'Books & Reference;Education': 8.7,
    'Puzzle;Creativity': 8.8,
    'Entertainment;Pretend Play': 8.9,
    'Racing;Pretend Play': 9.0,
    'Books & Reference;Creativity': 9.1,
    'Adventure;Brain Games': 9.2,
    'Strategy;Education': 9.3,
    'Role Playing;Education': 9.4,
    'Puzzle;Education': 9.5,
    'Lifestyle;Education': 9.6,
    'Health & Fitness;Action & Adventure': 9.7,
    'Communication;Creativity': 9.8,
    'Role Playing;Brain Games': 9.9,
    'Trivia;Education': 10.0,
    'Entertainment;Education': 10.1,
    'Parenting;Brain Games': 10.2,
    'Tools;Education': 10.3,
    'Travel & Local;Action & Adventure': 10.4,
    'Video Players & Editors;Creativity': 10.5,
    'Casual;Music & Video': 10.6,
    'Board;Pretend Play': 10.7,
    'Adventure;Education': 10.8,
    'Health & Fitness;Education': 10.9,
    'Music & Audio;Music & Video': 11.0,
    'Arcade;Pretend Play': 11.1,
    'Art & Design;Pretend Play': 11.2,
    'Lifestyle;Pretend Play': 11.3,
    'Comics;Creativity': 11.4,
    'Art & Design;Action & Adventure': 11.5,
    'Strategy;Creativity': 11.6,
}


def normalize_mapping(mapping):
    max_value = max(mapping.values())
    min_value = min(mapping.values())

    normalized_mapping = {key: round((value - min_value) / (max_value - min_value), 2) for key, value in mapping.items()}

    return normalized_mapping

# Normalize 'Category' mapping
category_mapping_normalized = normalize_mapping(category_mapping)

# Normalize 'Type' mapping
type_mapping_normalized = normalize_mapping(type_mapping)

# Normalize 'Content Rating' mapping
content_rating_mapping_normalized = normalize_mapping(content_rating_mapping)

# Normalize 'Genres' mapping
genres_mapping_normalized = normalize_mapping(genres_mapping)

# Print the normalized mappings with limited precision
print("Normalized Category Mapping:", category_mapping_normalized)
print("Normalized Type Mapping:", type_mapping_normalized)
print("Normalized Content Rating Mapping:", content_rating_mapping_normalized)
print("Normalized Genres Mapping:", genres_mapping_normalized)

category_mapping = {'FAMILY': 0.0, 'GAME': 0.03, 'TOOLS': 0.06, 'BUSINESS': 0.1, 'MEDICAL': 0.13, 'PRODUCTIVITY': 0.16, 'PERSONALIZATION': 0.19, 'LIFESTYLE': 0.23, 'FINANCE': 0.26, 'SPORTS': 0.29, 'COMMUNICATION': 0.32, 'HEALTH_AND_FITNESS': 0.35, 'PHOTOGRAPHY': 0.39, 'NEWS_AND_MAGAZINES': 0.42, 'BOOKS_AND_REFERENCE': 0.45, 'TRAVEL_AND_LOCAL': 0.48, 'SHOPPING': 0.52, 'SOCIAL': 0.55, 'VIDEO_PLAYERS': 0.58, 'MAPS_AND_NAVIGATION': 0.61, 'EDUCATION': 0.65, 'FOOD_AND_DRINK': 0.68, 'ENTERTAINMENT': 0.71, 'AUTO_AND_VEHICLES': 0.74, 'LIBRARIES_AND_DEMO': 0.77, 'WEATHER': 0.81, 'HOUSE_AND_HOME': 0.84, 'EVENTS': 0.87, 'ART_AND_DESIGN': 0.9, 'PARENTING': 0.94, 'BEAUTY': 0.97, 'COMICS': 1.0}
type_mapping = {'Free': 0.0, 'Paid': 1.0}
rating_mapping = {'Everyone': 0.0, 'Teen': 0.33, 'Everyone 10+': 0.67, 'Unrated': 1.0}
genres_mapping = {'Tools': 0.0, 'Entertainment': 0.01, 'Education': 0.02, 'Business': 0.03, 'Medical': 0.03, 'Productivity': 0.04, 'Personalization': 0.05, 'Lifestyle': 0.06, 'Finance': 0.07, 'Sports': 0.08, 'Communication': 0.09, 'Health & Fitness': 0.09, 'Photography': 0.1, 'Action': 0.11, 'News & Magazines': 0.12, 'Books & Reference': 0.13, 'Travel & Local': 0.14, 'Shopping': 0.15, 'Social': 0.16, 'Simulation': 0.16, 'Arcade': 0.17, 'Casual': 0.18, 'Video Players & Editors': 0.19, 'Maps & Navigation': 0.2, 'Puzzle': 0.21, 'Food & Drink': 0.22, 'Role Playing': 0.22, 'Strategy': 0.23, 'Racing': 0.24, 'Auto & Vehicles': 0.25, 'Libraries & Demo': 0.26, 'Weather': 0.27, 'House & Home': 0.28, 'Adventure': 0.28, 'Events': 0.29, 'Art & Design': 0.3, 'Beauty': 0.31, 'Comics': 0.32, 'Card': 0.33, 'Parenting': 0.34, 'Board': 0.34, 'Casino': 0.35, 'Educational;Education': 0.36, 'Trivia': 0.37, 'Educational': 0.38, 'Education;Education': 0.39, 'Casual;Pretend Play': 0.4, 'Word': 0.41, 'Puzzle;Brain Games': 0.41, 'Education;Pretend Play': 0.42, 'Music': 0.43, 'Racing;Action & Adventure': 0.44, 'Entertainment;Music & Video': 0.45, 'Board;Brain Games': 0.46, 'Arcade;Action & Adventure': 0.47, 'Educational;Pretend Play': 0.47, 'Casual;Action & Adventure': 0.48, 'Action;Action & Adventure': 0.49, 'Casualn': 0.8, 'Role Playing;Education': 0.81, 'Puzzle;Education': 0.82, 'Lifestyle;Education': 0.83, 'Health & Fitness;Action & Adventure': 0.84, 'Communication;Creativity': 0.84, 'Role Playing;Brain Games': 0.85, 'Trivia;Education': 0.86, 'Entertainment;Education': 0.87, 'Parenting;Brain Games': 0.88, 'Tools;Education': 0.89, 'Travel & Local;Action & Adventure': 0.9, 'Video Players & Editors;Creativity': 0.91, 'Casual;Music & Video': 0.91, 'Board;Pretend Play': 0.92, 'Adventure;Education': 0.93, 'Health & Fitness;Education': 0.94, 'Music & Audio;Music & Video': 0.95, 'Arcade;Pretend Play': 0.96, 'Art & Design;Pretend Play': 0.97, 'Lifestyle;Pretend Play': 0.97, 'Comics;Creativity': 0.98, 'Art & Design;Action & Adventure': 0.99, 'Strategy;Creativity': 1.0}

price_column = df['Price']

# Normalize the 'Price' column to the range [0, 1]
min_price = price_column.min()
max_price = price_column.max()

df['Price'] = (price_column - min_price) / (max_price - min_price)

# Print the updated DataFrame
print(df)