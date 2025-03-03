import pprint
import networkx as nx
from collections import defaultdict, deque
import pandas as pd


graph = "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"

# parse input string
def string_to_graph(input_str):

    str_list = input_str.split(',')
    
    graph_list = []
    for item in str_list:
        graph_list.append(tuple(item.split('->')))

    return graph_list

result_tst = string_to_graph(graph)
print(result_tst)

# create graph of edges
graph_loc = defaultdict(list)
for k, v  in result_tst:
    #print(f"source: {k} and destination: {v}")
    graph_loc[k].append(v)
    graph_loc[v].append(k)

pprint.pprint(f"graph: {graph_loc}")

# BFS 
def bfs_shortest_paths(graph_loc, start_node):
    distances = {node: float('inf') for node in graph_loc}
    distances[start_node] = 0
    queue = deque([start_node])
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph_loc[current_node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
    return distances

# create list of start nodes 
start_nodes = []
for t in result_tst:
    start_nodes.extend(t)

start_nodes = list(set(start_nodes))

source = []
destination = []
distance_src_dst = []

for start_node in start_nodes:
    shortest_paths = bfs_shortest_paths(graph_loc, start_node)

    for node, distance in shortest_paths.items():
        #print(f"Shortest distance from {start_node} to {node}: {distance}")
        source.append(start_node)
        destination.append(node)
        distance_src_dst.append(distance)


d = {'source': source, 'destination': destination, 'distance': distance_src_dst}
df = pd.DataFrame(data=d)
df = df[df['distance'] != 0]
df['source_destination'] = df['source'] + '_' + df['destination']

df = df.loc[df.groupby('source_destination')['distance'].idxmin()]
print(df)
i = 5
#df = df.iloc[0]
print(f"df range: , {len(df)}")
print(df.iloc[i]['source'],
      df.iloc[i]['destination'],
      df.iloc[i]['source_destination'],
      df.iloc[i]['distance'])
"""
G = nx.Graph()
G.add_edges_from(result_tst)

shortest_path = dict(nx.shortest_path_length(G))
#pprint.pprint(shortest_path)


for source, destination in shortest_path.items():
    #print(f"key: {source}, value: {destination}")
    insert_source = source
    for k, v in destination.items():
        insert_pk = source + '_' + k
        insert_destination = k
        insert_distance = v
        if v > 0:
            print(f"PK: {insert_pk}, source: {insert_source}, destination: {insert_destination}, distance: {insert_distance}")
"""