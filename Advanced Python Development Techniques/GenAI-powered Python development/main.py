from statistics import mean, median, mode
import numpy as np
import pandas as pd

# Write a Python function that takes a list of numbers and returns the mean, median, and mode.
def calculate_stats(numbers):
    """
    Calculate the mean, median, and mode of a list of numbers.
    """
    if not numbers:
        return None, None, None
    try:
        return mean(numbers), median(numbers), mode(numbers)
    except Exception:
        # In case there is no unique mode
        return mean(numbers), median(numbers), None
    finally:
        # Cleanup code if needed
        pass

numbers = [1, 2, 3, 4, 4, 5, 5, 5]
mean, median, mode = calculate_stats(numbers)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
import matplotlib.pyplot as plt

def run_experiments():
    # 1) Generate a random sample and show basic stats
    sample = np.random.normal(loc=10, scale=2, size=1000)
    print("Sample mean:", float(np.mean(sample)))
    print("Sample median:", float(np.median(sample)))
    print("Mode not computed for continuous data (use binning or discrete data)")

    # 2) Build a small DataFrame and explore
    df = pd.DataFrame({
        "x": sample,
        "y": sample * 0.5 + np.random.normal(scale=1.0, size=sample.size)
    })
    print("\nPandas describe():\n", df.describe())

    # 3) Correlation and a simple linear fit
    corr = df["x"].corr(df["y"])
    slope, intercept = np.polyfit(df["x"], df["y"], 1)
    print(f"\nCorrelation: {corr:.4f}")
    print(f"Linear fit: y = {slope:.4f} * x + {intercept:.4f}")

    # 4) Save a histogram to disk (example of visualization output)
    plt.figure()
    plt.hist(df["x"], bins=30, alpha=0.7)
    plt.title("Histogram of x")
    plt.xlabel("x")
    plt.ylabel("count")
    plt.tight_layout()
    plt.savefig("hist_x.png")
    plt.close()
    print("Saved histogram to hist_x.png")

if __name__ == "__main__":
    run_experiments()