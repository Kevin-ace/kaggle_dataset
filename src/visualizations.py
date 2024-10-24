import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)  # Using KDE for a smoother distribution
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # Save the plot as a PNG file
    plt.savefig(f'../results/{column}_distribution.png')
    plt.close()  # Close the figure to free up memory
