import sys

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from ucimlrepo import fetch_ucirepo
except ImportError as ie:
    print("Missing Package", ie)
    print("Install required packages and try again, for example:")
    print("pip install pandas matplotlib seaborn ucimlrepo")
    sys.exit(1)

sns.set()

def fetch_dataset():
    """
    Idea: load the iris dataset from the UCI machine learning repo using Ucimlrepo.
    Why: shows you how to use external dataset source. no need for manual CSV download
    """
    try:
        iris = fetch_ucirepo(id=53)

    except Exception as e:
        print("Error fetching dataset, check internet connection and unimlrepo installation.")
        print("Full error:", e)
        raise
    return iris

def build_dataframe(iris):
    """
    Idea: load the Iris dataset from the UCI machine learning repo using UCIMLREPO.
    We combine them into one DataFrame for easier analysis.
    """
    X = iris.data.features 
    y = iris.data.targets

    # Combine it Horizontally fess
    df = pd.concat([X, y], axis=1)

    # Standardize the species column name to 'species'
    if 'class' in df.columns:
        df = df.rename(columns={'class': 'species'})
    elif 'target' in df.columns:
        df = df.rename(columns={'target': 'species'})
    elif 'species' not in df.columns:
        try:
            if isinstance(y, pd.DataFrame):
                first_col = y.columns[0]
                df = df.rename(columns={first_col: 'species'})
            else:
                df['species'] = y
        except Exception:
            df['species'] = y

    return df

def explore_data(df):
     """
    Idea: Explore the structure of the dataset by checking the data types and any missing values.
    """
     print("\n--- First 5 rows ---")
     print(df.head(), "\n")

     print("--- Data Types and Non-null counts ---")
     print(df.info(), "\n")

     print("--- Missing Values per column ---")
     print(df.isnull().sum(), "\n")

     print("--- Basic Descriptive Statistic (numeric) ---")
     print(df.describe(), "\n")


def basic_analysis(df):
     """
    Idea: compute group-level statistics to find the pattern by species
    """
     print("--- Group Means by Species ---")
     grouped = df.groupby('species').mean(numeric_only=True)
     print(grouped, "\n")
     return grouped

def plot_Visualization(df):
     """
    Idea: To produce the four required charts; line, bar, histogram, scatter.
    Each plot will appear as png.
    """
     
     df = df.reset_index(drop=True)

     # Line Chart beginssssssssssssssssssssssss
     plt.figure(figsize=(10,5))
     plt.plot(df.index, df["Sepal length (cm)"], label="Sepal length (cm)")
     plt.title("Line: Sepal Length Across Samples")
     plt.xlabel("Sample Index")
     plt.ylabel("Sepal Length (cm)")
     plt.legend()
     plt.tight_layout()
     plt.savefig("line_sepal_length.png")
     plt.show()


     # Bar Chart strts here
     plt.figure(figsize=(8,5))
     sns.barplot(x="species", y="Petal length (cm)", data=df, ci=None)
     plt.title("Bar: Average Petal Length by Samples")
     plt.xlabel("Species")
     plt.ylabel("Petal Length (cm)")
     plt.tight_layout()
     plt.savefig("bar_petal_length_by_species.png")
     plt.show()


     # Histogram: begins here
     plt.figure(figsize=(8,5))
     plt.hist(df["Sepal width (cm)"], bins=15)
     plt.title("Histogram: Sepal with description")
     plt.xlabel("Sepal Width (cm)")
     plt.ylabel("Frequency")
     plt.tight_layout()
     plt.savefig("hist_sepal_width.png")
     plt.show()


     # Scatter plot here
     plt.figure(figsize=(8,6))
     sns.scatterplot(x="sepal length (cm)", y="Petal length (cm)", hue="species", data=df)
     plt.title("Scatter: Sepal Length vs petal length")
     plt.xlabel("Sepal Length (cm)")
     plt.ylabel("Petal Length (cm)")
     plt.legend(tittle="Species")
     plt.tight_layout()
     plt.savefig("Scatter_sepal_vs_petal.png")
     plt.show()

     
def error_handlings():
    """
    Try & Except Error
    """

    print("\n --- Error handling: reading a local CSV")
    try:
        temp = pd.read_csv("Some_files_that_doesn't exist.csv")
    except FileNotFoundError:
        print("FileNotFoundError caught: some CSV not found , this is expected though")
        print("Remedy: place your csv filee in the same folder")
    except Exception as e:
        print("Other read error: ", e)


def findings_and_notes(grouped):
    """
    Finding for submission
    """
    print("\n --- Findings / Observations")
    print(" - Setos has clearly smaller petal lengths, on average, compared to Versciolor and virginica")

    print("\n Notes")
    print("- PNG files for each plot are saved in the script folder: line_sepal_length.png, bar_petal_length_by_species.png, hist_sepal_width.png and Scatter_sepal_vs_petal.png")
    print("- If plots do not pop up on your device, open thoes PNG files manually")
    print("- Make sure your device is compatible")


def main():
    iris = fetch_dataset()
    df = build_dataframe(iris)
    explore_data(df)
    grouped = basic_analysis(df)
    plot_Visualization(df)
    error_handlings()
    findings_and_notes(grouped)



if __name__ == "__main__":
    main()

