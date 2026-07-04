from cyaron import *

for testCaseId in range(1,2):
    io = IO(f"./data/secret/{testCaseId}.in", f"./data/secret/{testCaseId}.ans")
    print(f"Generate testcase {testCaseId}")

    # random int
    N = randint(5, 15)
    M = randint(5, 15)

    # random array
    arr = Vector.random(N, [(1, 20), (1, 20)])
    
    # random graph
    g = Graph.graph(N, M)
    
    # generate input
    io.input_writeln(N, M)
    io.input_writeln(arr)
    for e in g.iterate_edges():
        io.input_writeln(e.start, e.end, e.weight)
    
    # run source code to generate output
    io.output_gen("a.exe")