import array
#import psyco
from data_reader import data_extract
import evalfitness
from treeutil import PostOrder_Search
from collections import deque
import math
import random

#psyco.profile()

# data extraction
data = data_extract()
n = len(data)
m = len(data[0])

# define computations
def add(listElem):
    try:
        result=[]
        for i in xrange(len(listElem[0])):
            result.append(listElem[0][i]+listElem[1][i])
        return result
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def sub(listElem):
    try:
        result=[]
        for i in xrange(len(listElem[0])):
            result.append(listElem[0][i]-listElem[1][i])
        return result
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def neg(listElem):
    try:
        result=[]
        for i in xrange(len(listElem[0])):
            result.append(0-listElem[0][i])
        return result
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def multiply(listElem):
    try:
        result=[]
        for i in xrange(len(listElem[0])):
            result.append(listElem[0][i]*listElem[1][i])
        return result
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def square(listElem):
    try:
        result=[]
        for i in xrange(len(listElem[0])):
            result.append(listElem[0][i]*listElem[0][i])
        return result
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
        result=[]
        for i in xrange(len(listElem[0])):
            result.append(math.cos(listElem[0][i]))
        return result
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit
        
def sin(listElem):
    try:
        result=[]
        for i in xrange(len(listElem[0])):
            result.append(math.sin(listElem[0][i]))
        return result
    except:
        raise WrongValues, "Wrong values sent to function node.\nCan't get result"
        exit

def adfBranch(x):
    try:
        return x
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
    'cos':cos,
    'sin':sin,
    'adf2_+':add,
    'adf2_-':sub,
    'adf2_neg':neg,
    'adf2_*':multiply,
    'adf_^2':square,
    'adf2_cos':cos,
    'adf2_sin':sin,
    'adf1':adfBranch,
    'adf2':adfBranch,
    'root':rootBranch
    
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
































