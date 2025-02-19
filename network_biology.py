import networkx as nx
import matplotlib.pyplot as plt

def build_network(interaction_file: str):
    data = pd.read_csv(interaction_file)
    G = nx.Graph()
    for _, row in data.iterrows():
        G.add_edge(row['ncRNA'], row['RBP'], weight=row['interaction_score'])
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.savefig('results/network_plot.png')
    plt.show()

if __name__ == "__main__":
    build_network('results/ncRNA_RBP_predictions.csv')