import sqlite3
import sys
sys.modules['pysqlite2'] = sqlite3
import evolver
from tree_reader import branch_reader
from data_reader import data_extract

if __name__ == "__main__":
    
    dbname=r'C:\pop_db1'
    tree = evolver.EvolutionRun(1000, (0,1,'root'), 2, 12,'AddHalfNode',
                         301, 0.1, 0.4, 0.5, 0.05, 7, 0.8, dbname, False)
    
    
    
    data = data_extract('data_test_630_1.csv')
    n = len(data)
    m = len(data[0])
    nb_eval = n*m
    all_x=[]
    all_y=[]


    for i in range(0,n):
        for j in range(0,m):
            all_x.append(data[i][j][1])
            all_y.append(data[i][j][2])

    fit = branch_reader(tree[1], all_x, all_y)
    
    f = open('data1.txt','a')
    for i in xrange(84):
        f.write(str(fit[i]) + '\n')
    f.close()