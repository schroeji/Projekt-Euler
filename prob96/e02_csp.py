# coding=utf-8
"""
The exercise is to create a (almost) general constraint satisfaction problem
solver. You will have to use the CSP data structure from csp.py. Read it for
reference!

"""
import numpy as np
import csp
import time
from data import create_map_csp

def firstUnassigned(variables):
    """ gibt die erste nicht belegte Variable zurueck ansonsten None"""
    for var in variables:
        if (var.get_value() == None):
            return var
    return None

def backtracking(csp, ac_3=False):
    """
    Implement the basic backtracking algorithm to solve a CSP.

    Optional: if ac_3 == True use the AC-3 algorithm for constraint
              propagation. Important: if ac_3 == false don't use
              AC-3!
    :param csp: A csp.ConstrainedSatisfactionProblem object
                representing the CSP to solve
    :return: A csp.ConstrainedSatisfactionProblem, where all Variables
             are set and csp.complete() returns True. (I.e. the solved
             CSP)
    """
    if (csp.complete()):
        return csp
    var = firstUnassigned(csp.variables)
    if (var == None): # falls keine unbelegte Variable existiert ist Rekursionszweig abgeschlossen
        return csp
    for value in var.domain:
        var.set_value(value)
        fail = False # gibt an ob midnestens ein constraint verletzt wurde
        for constraint in csp.get_constraints_for_variable(var):
            if (not constraint.consistent()):
                fail = True
                break
        if (not fail):
            result = backtracking(csp,ac_3)
            if (result != None):
                return result
    var.set_value(None)
    return None

def mrv_variable_falsch(csp):
    """ choose the variable with the fewest legal values
    Annahme: wenigste mögliche Werte=meiste Constraints (???)
    """
    count=0
    res=None
    for x in csp.variables:
        constraints_length=len(list(csp.get_constraints_for_variable(x))) #list aus generator machen .... komt mir sehr sehr unschoen vor
        if x.value==None  and constraints_length > count:
            count=constraints_length
            res=x
    return res

def mrv_variable(csp):
    """ choose the variable with the fewest legal values
    Vorgehen: gehe werte durch und zähle Möglichkeiten  (bedeutet merhfache belegung)
    """
    res=firstUnassigned(csp.variables)
    if res !=None:
        count=res.domain.__len__  # initialwert auf erste mögliche setzen

        for x in csp.variables:
            constraints=csp.get_constraints_for_variable(x) #list aus generator machen .... komt mir sehr sehr unschoen vor
            if x.value==None:
                xcount=remaining_values(x,csp)
                if xcount < count:
                    count=xcount
                    res=x
    return res

def minimum_remaining_values(csp, ac_3=False):
    """
    Implement the basic backtracking algorithm to solve a CSP with
    minimum remaining values heuristic and no tie-breaker. Thus the
    first of all best solution is taken.

    Optional: if ac_3 == True use the AC-3 algorithm for constraint
              propagation. Important: if ac_3 == false don't use
              AC-3!
    :param csp: A csp.ConstrainedSatisfactionProblem object
                representing the CSP to solve
    :return: A tuple of 1) a csp.ConstrainedSatisfactionProblem, where
             all Variables are set and csp.complete() returns True. (I.e.
             the solved CSP) and 2) a list of all variables in the order
             they have been assigned.
    """
    return mrv_rec(csp, []) #ac3 kann später gemacht werden

def mrv_rec (csp, order):
    if (csp.complete()):
        return (csp, order)
    var = mrv_variable(csp)
    order.append(var)
    if (var == None): # falls keine unbelegte Variable existiert ist Rekursionszweig abgeschlossen
        return (csp, order)
    for value in var.domain:
        var.set_value(value)
        fail = False # gibt an ob midnestens ein constraint verletzt wurde
        for constraint in csp.get_constraints_for_variable(var):
            if (not constraint.consistent()):
                fail = True
                break
        if (not fail):
            result = mrv_rec(csp,order)
            if (result != None):
                return result #hier auf keinen Fall ein Tupel übergeben. war ein ganz dummer fehler
    var.set_value(None)
    return None


def minimum_remaining_values_with_degree(csp, ac_3=False):
    """
    Implement the basic backtracking algorithm to solve a CSP with
    minimum remaining values heuristic and the degree heuristic as
    tie-breaker.

    Optional: if ac_3 == True use the AC-3 algorithm for constraint
              propagation. Important: if ac_3 == false don't use
              AC-3!
    :param csp: A csp.ConstrainedSatisfactionProblem object
                representing the CSP to solve
    :return: A tuple of 1) a csp.ConstrainedSatisfactionProblem, where
             all Variables are set and csp.complete() returns True. (I.e.
             the solved CSP) and 2) a list of all variables in the order
             they have been assigned.
    """
    return mrvwd_rec(csp, []) #ac3 kann später gemacht werden

def mrvwd_rec (csp, order):
    if csp.complete():
        return (csp, order)
    else:
        var=mrv_variable_degree(csp)
        order.append(var)
        for value in var.domain:
            var.value=value
            if csp.consistent():
                result=mrvwd_rec(csp,order)
                if result!="failure":
                    return result
            var.value=None
        return "failure"

def mrv_variable_degree(csp):
    """ choose the variable with the fewest legal values
    Vorgehen: gehe werte durch und zähle Möglichkeiten  (bedeutet merhfache belegung)
    """
    candidates = [variable for variable in csp.variables if variable.value is None ]
    candidates.sort(key=lambda x: (remaining_values(x,csp), -degree(x,csp)))
    #mrv = []
    #for x in candidates:
       # mrv.append(x)
       # if remaining_values(x, csp) > remaining_values(candidates[0], csp):
           # break


   # mrv = sorted(mrv, key = lambda x: degree(x,csp), reverse=True)
    return candidates[0]

def remaining_values(variable,csp):
    res=0
    for value in variable.domain:
        variable.value=value
        if csp.consistent():
            res += 1
        variable.value=None
    return res

def degree(variable,csp):
    return len([x for x in variable.peers if x.value is None])
    #return len(variable.peers)
    #return len([x for x in csp.get_constraints_for_variable(variable)])
    #return len([x for x in csp.get_constraints_for_variable(variable) if x.var1.value is None and x.var2.value is None])
    #return 0
def create_sudoku_csp(sudoku):
    """
    Creates a csp.ConstrainedSatisfactionProblem from a numpy array
    `sudoku` which has shape (9, 9). Each entry of the sudoku is either
    0, which means it is not set yet or in [1, ..., 9], which means
    it is already assigned a number.

    The CSP should contain all constraints necessary to solve the sudoku.
    I.e. no two numbers in a row must be equal, no two numbers in a column
    must be equal and no two numbers in one of the 9 3x3 blocks must be
    equal. All numbers in the array must be already set.

    :param sudoku: A numpy array representing a unsolved sudoku
    :return: A csp.ConstrainedSatisfactionProblem which can be used
             to solve the sudoku
    """
    domain = [1,2,3,4,5,6,7,8,9]
    variables = []
    row_count = 1
    
    reihen = []
    quadrate = {}
    spalten = []
    
    for i in range(1,10):
        reihen.append([])
        spalten.append([])
    for i in range(0,3):
        for j in range(0,3):
            quadrate[(i,j)] = []
        
    for row in sudoku:
        col_count = 1
        for wert in row:
            value = None
            if(int(wert) != 0):
                value = int(wert)
            var = csp.Variable( (row_count,col_count), domain, value )
            variables.append(var)
            
            spalten[col_count - 1].append(var)
            reihen[row_count - 1].append(var)
            
            quadrate[((col_count-1) / 3,(row_count-1) / 3)].append(var)
            
            col_count += 1
        row_count += 1
        
    constraints = []
    for quad in quadrate.values():
        for i in range(0,9):
            for j in range(i + 1,9):
                constraints.append(csp.UnequalConstraint(quad[i], quad[j]))
    for row in reihen:
        for i in range(0,9):
            for j in range(i + 1,9):
                constraints.append(csp.UnequalConstraint(row[i], row[j]))
    for col in spalten:
        for i in range(0,9):
            for j in range(i + 1,9):
                constraints.append(csp.UnequalConstraint(col[i], col[j]))
    return csp.ConstrainedSatisfactionProblem(variables,constraints)


def sudoku_csp_to_array(csp):
    """
    Takes a sudoku CSP from `create_sudoku_csp()` as you implemented
    it and returns a numpy array s with `s.shape == (9, 9)` (i.e. a
    9x9 matrix) representing the sudoku.

    :param csp: The CSP created with `create_sudoku_csp()`
    :return: A numpy array with shape (9, 9)
    """
    a = []
    for i in range(1,10):
        a.append([])
    i = 0
    j = 0
    for var in csp.variables:
        a[j].append( var.get_value())
        i += 1
        if(i == 9):
            i = 0
            j += 1
    s = np.array(a)
    return s

def read_sudokus():
    """
    Reads the sudokus in the sudoku.txt and saves them as numpy arrays.
    :return: A list of np.arrays containing the sudokus
    """
    with open("sudoku.txt", "r") as f:
        lines = f.readlines()
    sudoku_strs = []
    for line in lines:
        if line[0] == 'G':
            sudoku_strs.append("")
        else:
            sudoku_strs[-1] += line.replace("", " ")[1:]
    sudokus = []
    for sudoku_str in sudoku_strs:
        sudokus.append(np.fromstring(sudoku_str, sep=' ',
                                     dtype=np.int).reshape((9, 9)))
    return sudokus


def main():
    """
    A main function. This might be useful for developing, if you don't
    want to run all tests all the time. Just write here what ever you
    want to develop your code. If you use pycharm you can run the unittests
    also by right-clicking them and then e.g. "Run 'Unittest test_sudoku_1'".
    """

    # first lets test with a already created csp:
    csp = create_map_csp()
    solution = backtracking(csp)
    print(solution)

    # and now with our own generated sudoku CSP
    sudokus = read_sudokus()
    csp = create_sudoku_csp(sudokus[5])
    t1 = time.time();
    solution, _ = minimum_remaining_values_with_degree(csp)
    print(time.time() - t1)
    print(sudoku_csp_to_array(solution))

if __name__ == '__main__':
    main()
