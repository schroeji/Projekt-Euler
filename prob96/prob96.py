import e02_csp
from thread import start_new_thread, allocate_lock

num_threads = 0
s = 0
lock = allocate_lock()

def thread_solver(i):
    global s, num_threads
    num_threads += 1
    csp = e02_csp.create_sudoku_csp(sudokus[i])
    solution, _ = e02_csp.minimum_remaining_values_with_degree(csp)
    solution = e02_csp.sudoku_csp_to_array(csp)
    lock.acquire();
    s += int( str(solution[0][0]) + str(solution[0][1]) + str(solution[0][2]) )
    num_threads -= 1
    lock.release()
    
sudokus = e02_csp.read_sudokus()


for i in range (0,50): 
    thread_solver(i)

print s