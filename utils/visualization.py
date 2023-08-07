import seaborn as sns
import matplotlib.pyplot as plt

def DistributionChart(df, output_path):
    """Plots the distribution of overall ratings."""
    ax = sns.countplot(x="overall", data=df)
    ax.set_title("Distribution of Ratings")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path / "distribution_ratings.png")
    plt.show()