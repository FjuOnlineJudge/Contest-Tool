from cyaron import *
import random

for testCaseId in range(1,2):
    io = IO("./data/secret/"+str(testCaseId)+".in","./data/secret/"+str(testCaseId)+".ans")
    print("Generate testcase" + str(testCaseId))
 
    T = randint(5,15)

    for _T in range(T):
        N = randint(3,11)
        io.input_writeln(N)
        for _N in range(N):
            arr = Vector.random(randint(1,20),[(1,20)])
            random.shuffle(arr)
            io.input_write(arr)
            io.input_writeln(0)

    io.input_writeln(0)
    io.output_gen("./a.exe")