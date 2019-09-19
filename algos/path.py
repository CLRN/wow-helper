from scipy.spatial.kdtree import KDTree
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, breadth_first_order
import numpy as np
import math


points = list()
for x in range(100):
    for y in range(100):
        points.append([x, y])

t = KDTree(points)

distance, location = t.query([11.3, 35.7], k=5, distance_upper_bound=10)
for l in location:
    print(points[l])


print(distance, t.data[location])

pairs = t.query_pairs(8)
arr = np.zeros((len(pairs), len(pairs)))

for p in pairs:
    arr[p[0], p[1]] = 1

print(pairs)

graph = csr_matrix(arr)

# dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=0, return_predecessors=True)
# print(dist_matrix)
# print(predecessors)
#
# res = breadth_first_order(graph, 0)
# print(res)