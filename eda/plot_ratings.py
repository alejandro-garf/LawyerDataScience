import seaborn as sns
import matplotlib.pyplot as plt

def plot_ratings(df):
    sns.histplot(df['rating'].dropna(), bins=10)
    plt.title("Distribution of Lawyer Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()
