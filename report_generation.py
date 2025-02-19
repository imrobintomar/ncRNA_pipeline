import matplotlib.pyplot as plt
import pandas as pd

def generate_report(prioritized_file: str):
    data = pd.read_csv(prioritized_file)
    plt.hist(data['priority_score'], bins=10, color='skyblue')
    plt.title('ncRNA Priority Score Distribution')
    plt.xlabel('Priority Score')
    plt.ylabel('Frequency')
    plt.savefig('results/priority_distribution.png')
    with open('results/final_report.txt', 'w') as f:
        f.write("ncRNA Prioritization Report\n")
        f.write("Top ncRNAs:\n")
        f.write(data.head().to_string())

if __name__ == "__main__":
    generate_report('results/prioritized_ncRNAs.csv')