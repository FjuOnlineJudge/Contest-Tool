from cyaron import *


def generate_array(T, total):
    """
    Generate an array of length T:
    - Each element >= 1
    - The sum of the array = total
    """
    if T > total:
        raise ValueError("Impossible: each element must be >=1, so total must be >= T")

    # Initialize array with all 1s
    arr = [1] * T
    remain = total - T

    # Randomly distribute the remaining value
    while remain > 0:
        i = randrange(T)  # choose a random position
        arr[i] += 1
        remain -= 1

    return arr


def tree_parents(edge_list, N):
    """
    Given a tree edge list and number of nodes N,
    return parent array (1-indexed), with root=1 having parent=-1.
    """
    from collections import defaultdict, deque
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edge_list:
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * (N + 1)  # parent[0] unused
    parent[1] = -1  # root

    # BFS
    q = deque([1])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if parent[v] == -1 and v != 1:  # not visited
                parent[v] = u
                q.append(v)

    return parent[2:]  # drop index 0


for testCaseId in range(1,2):
    io = IO(f"./data/secret/{testCaseId}.in", f"./data/secret/{testCaseId}.ans")
    print(f"Generate testcase {testCaseId}")

    # random int
    N = randint(5,15)
    M = randint(5,15)

    # random array
    arr = Vector.random(N, [(1,20), (1, 20)])
    
    # random graph
    g = Graph.graph(N, M)
    
    # generate input
    io.input_writeln(N, M)
    io.input_writeln(arr)
    for e in g.iterate_edges():
        io.input_writeln(e.start, e.end, e.weight)
    
    # run source code to generate output
    io.output_gen("./a.exe")