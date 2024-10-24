import kaggle

# Authenticate Kaggle API
kaggle.api.authenticate()

# Download dataset
try:
    kaggle.api.dataset_download_files(
        'octopusteam/imdb-top-1000-tv-series',
        path='../data/',
        unzip=True
    )
    print("Dataset downloaded and unzipped successfully.")
except Exception as e:
    print(f"An error occurred while downloading the dataset: {e}")

import os
from data_loader import load_data
from data_cleaning import clean_data
from visualizations import plot_distribution

def main():
    # Load dataset
    try:
        data = load_data('../data/data.csv')
        # print("Columns in the dataset:", data.columns)
    except FileNotFoundError:
        print("The file does not exist. Please check if the dataset was downloaded and unzipped correctly.")
        exit()

    
    # Clean the data
    cleaned_data = clean_data(data)
    # Ensure the results directory exists
    results_dir = '../results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)  # Create the directory if it doesn't exist
    
    # Save cleaned data
    cleaned_data.to_csv(f'{results_dir}/cleaned_data.csv', index=False)
    
    # Visualize data
    plot_distribution(cleaned_data, 'averageRating')

if __name__ == "__main__":
    main()
