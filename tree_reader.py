import numpy as np
import parameters
import treeutil

terminals = parameters.terminals
functions = parameters.functions

def branch_reader(t, *arg):
    if isinstance(t[0],int):
        return arg[terminals.keys().index(t[2])]
    else:
        if (t[0][0] == 0):
            return
        if (t[0][0] == 3):
            return arg[terminals.keys().index(t[0][2])]
        else:
            n = t[0][1]
            use = functions[t[0][2]]
            if n == 1:
                return use([np.array(branch_reader(t[1], *arg))])
            if n == 2:
                return use([np.array(branch_reader(t[1], *arg)),np.array(branch_reader(t[2], *arg))])
        

