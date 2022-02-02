import math

def cutting(wire_len):
    if(wire_len < 2):
        return 0
    
    if(wire_len == 2):
        return 1

    return cutting(math.ceil(wire_len/2))+1


wires = [1, 2, 5, 7, 15, 17, 32, 33, 65, 128, 129, 1024]
for wire in wires:
    print("Min num of cuts for {0}-meter-long steel wire is {1}".format(wire, cutting(wire)) )
