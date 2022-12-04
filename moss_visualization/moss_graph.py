from pyvis.network import Network
import networkx as nx

import requests
from bs4 import BeautifulSoup
import numpy
import re

def parse(url):
    res = requests.get(url)
    dom = BeautifulSoup(res.text, 'lxml')

    rows = dom.select('table tr')  #table
    rows = [row.select('td') for row in rows if row.select('td')]
    return rows

def get_min_max(rows):
    max_val = min_val = int(rows[0][2].text.strip())

    for data in rows: 
        if (int(data[2].text.strip()) > max_val):
            max_val = int(data[2].text.strip())
        elif (int(data[2].text.strip()) < min_val):
            min_val = int(data[2].text.strip())

    return min_val, max_val

def create(rows, node_distance = 200, spring_length = 200, edge_scale = 10, node_size = 20, node_color = '#97c2fc', edge_color = '#97c2fc'):
    node_name_full_p = r'.*/(.*)\..*'
    node_similarity = r"\(([^)]+)\)"

    G = nx.Graph()
    min_val, max_val = get_min_max(rows)

    for data in rows:
        node1 = re.search(node_name_full_p, data[0].text.strip())[1]
        node2 = re.search(node_name_full_p, data[1].text.strip())[1]
        node1_similarity = re.search(node_similarity, data[0].text.strip())[1]
        node2_similarity = re.search(node_similarity, data[1].text.strip())[1]

        G.add_node(node1, title=node1, size=node_size, color=node_color)
        G.add_node(node2, title=node2, size=node_size, color=node_color)
        weight = numpy.interp(data[2].text.strip(),[min_val,max_val],[0,1])
        scaled_weight = weight * edge_scale
        title_weight = str(round(weight, 3))
        G.add_edge(node1, node2, weight=scaled_weight, title=f'{node1}: {node1_similarity}\n{node2}: {node2_similarity}\nLines Matched: {data[2].text.strip()}\nWeight: {title_weight}', color=edge_color)

    nt = Network('800px', '800px', neighborhood_highlight=True)
    nt.repulsion(node_distance = node_distance, spring_length = spring_length)
    nt.from_nx(G)
    nt.show('test.html')

if __name__ == "__main__":
    url = "http://moss.stanford.edu/results/5/1684016372050"
    data = parse(url)
    create(data)
