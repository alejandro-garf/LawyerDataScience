import matplotlib.pyplot as plt
import seaborn as sns

def plot_ratings(df):
    sns.histplot(df['rating'].dropna(), bins=10)
    plt.title("Distribution of Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()
