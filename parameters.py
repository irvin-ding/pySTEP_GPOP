"""
Created on Wed June 28 11:49 2017

@author: irvin.ding

"""

import numpy as np
#import psyco
from data_reader import data_extract
import evalfitness
from treeutil import WrongValues
from collections import deque
import random

#psyco.profile()

# data extraction
data = data_extract('data_test_4.csv')
n = len(data)
m = len(data[0])

# define computations
def add(listElem):
    try:
        return listElem[0]+listElem[1]
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def sub(listElem):
    try:
        return listElem[0]-listElem[1]
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def neg(listElem):
    try:
        return 0-listElem[0]
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def multiply(listElem):
    try:
        return listElem[0]*listElem[1]
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def square(listElem):
    try:
        return listElem[0]*listElem[0]
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

#==============================================================================
# def divide(listElem):
#     try:
#         return listElem[0]/listElem[1]
#     except:
#         raise WrongValues, "Wrong values sent to function node.\nCan't get result"
#         exit
#==============================================================================

def cos(listElem):
    try:
        return np.cos(listElem[0])
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit
    
def sin(listElem):
    try:
        return np.sin(listElem[0])
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit



def rootBranch(x):
    try:
        return x
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

# list of functions
functions = {
    '+':add,
    '-':sub,
    'neg':neg,
    '*':multiply,
    '^2':square,
    #'/':divide,
    'root':rootBranch,
    'cos':cos,
    'sin':sin
}

# list of all possible value of a variable from data set
nb_eval = n*m
all_x=[]
all_y=[]


for i in range(0,n):
    for j in range(0,m):
        all_x.append(data[i][j][1])
        all_y.append(data[i][j][2])
         
# a mapping of terminals
terminals = {
    'x':all_x,
    'y':all_y
}



ideal_results=[]
# ideal data from data set
def GetIdealResultsData():
    for i in range(0,n):
        for j in range(0,m):
            ideal_results.append([(data[i][j][0])])
    return ideal_results


# setting of specs
crossover_mapping = []
Strongly_Typed_Crossover_degree = 0
Substitute_Mutation = 0
adfOrdered = False


# define a fitness function
def FitnessFunction(my_tree):
    return evalfitness.FinalFitness(evalfitness.EvalTreeForAllInputSets(my_tree, xrange(nb_eval)))

#   default function set
defaultFunctionSet = [(1,2,'+'),(1,2,'-'),(1,2,'*'),(1,1,'neg'),(1,1,'^2'),(1,1,'cos'),(1,1,'sin')]
# default terminal set
defaultTerminalSet = [(3,0,'x'),(3,0,'y')]
treeRules = {
    'root':[(defaultFunctionSet,defaultTerminalSet),(defaultFunctionSet,defaultTerminalSet)],
    '+':[(defaultFunctionSet,defaultTerminalSet),(defaultFunctionSet,defaultTerminalSet)],
    '-':[(defaultFunctionSet,defaultTerminalSet),(defaultFunctionSet,defaultTerminalSet)],
    '*':[(defaultFunctionSet,defaultTerminalSet),(defaultFunctionSet,defaultTerminalSet)],
    '^2':[(defaultFunctionSet,defaultTerminalSet)],
    'neg':[([(1,2,'+'),(1,2,'-'),(1,2,'*'),(1,1,'^2'),(1,1,'sin'),(1,1,'cos')],defaultTerminalSet)],
    'cos':[([(1,2,'+'),(1,2,'*'),(1,2,'-'),(1,1,'sin'),(1,1,'neg'),(1,1,'^2')],defaultTerminalSet)],
    'sin':[([(1,2,'+'),(1,2,'*'),(1,2,'-'),(1,1,'cos'),(1,1,'neg'),(1,1,'^2')],defaultTerminalSet)]
}
































