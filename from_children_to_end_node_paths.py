# https://www.careercup.com/question?id=5713002834165760

# Given a Start Node and an End Node in a graph.
# Report if they are “necessarily connected”.
# This means that all paths from the start node lead to the end node.
# Report true all paths from start node lead to end node and false if
# at least one path does not lead to the end node.
# This is a directed graph which can have cycles


# Будем считать, что граф задан следующим образом:
# массив vertices задает множество вершин,
# edges - множество ребер,
# причем edges[j] - это список вершин, в которые переходит i-ая вершина.


def inverse_graph(vertices, edges):
    new_edges = [list() for i in range(0, len(vertices))]
    j = 0
    for children in edges:
        for child in children:
            new_edges[child].append(j)
        j += 1
    return new_edges


def end_reachable_from_children(vertices, edges):

    if len(edges) == 0:
        return False

    nodes = [vertices[-1]]
    local_nodes = []
    reverse_edges = inverse_graph(vertices, edges)
    existed_path_from_end = [False for i in edges]

    while len(nodes) != 0:
        for node in nodes:
            if not existed_path_from_end[node]:
                local_nodes.extend(reverse_edges[node])
                existed_path_from_end[node] = True
        nodes = local_nodes
        local_nodes = []

    t = True
    for child in edges[0]:
        t = existed_path_from_end[child] and t

    return t


if __name__ == '__main__':
    example_vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    example_edges = [[1, 2, 3], [4], [1], [5], [3, 7], [2, 8, 10], [8], [6, 9], [7, 10], [], []]

    reachable = end_reachable_from_children(example_vertices, example_edges)
    print(reachable)
