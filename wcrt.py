##
# This script generates the Worst Case Response Time for a set of tasks,
# taking into account the phase, period, execution time, relative deadline
# and blocking time of the tasks.
#
# Prints the calculations performed and the point of convergence to give
# a better understanding of how the algorithm works.
#
# Usage format:
#   python3 thisScriptName.py tasksFile.txt monotonicType[rate|deadline]
#
# Usage examples:
#   python3 wcrt.py test_cases/set1_schedulable.txt deadline
#   python3 wcrt.py test_cases/set3_unschedulable.txt rate
#
# @author Rogi Solorzano
#

from sys import argv
from load_file import *
from find_total_interference import *

##
# Handle arguments from the command line.
##

if len(argv) < 2:
    print('Error: parameters table file was not provided')
    exit()

monotonicSortMap = {'rate': 'p', 'deadline': 'd'}
monotonicType = 'rate'

if len(argv) < 3:
    print('NOTICE: third parameter "rate" or "deadline" monotonic type ' +
          'was not given, using rate monotonic by default')
else:
    monotonicType = argv[2]

##
# Load tasks and sort so we can determine priorities.
##

tasks = load_file(argv[1])
tasks = sorted(tasks, key=lambda x: x[monotonicSortMap[monotonicType]])

##
# Calculate WCRT.
##

unfeasibleCount = 0

for i in range(0, len(tasks)):
    print('\nTask ' + str(i + 1))
    n = 0

    wP = tasks[i]['e'] + tasks[i]['B']

    while True:
        interference = find_total_interference(wP, i - 1, tasks)
        w = tasks[i]['e'] + tasks[i]['B'] + interference['total']

        print('R: ' + str(tasks[i]['e']) +
              ' + ' + str(tasks[i]['B']) +
              interference['calculation'] + ' = ' + str(w))

        # Algorithm converged. Task is feasible.
        if w == wP:
            print('Feasible R: ' + str(w))
            break

        # Algorithm did not converge. Task is unfeasible.
        if w > tasks[i]['d']:
            print('No solution, w is ' + str(w) +
                  ' and deadline is ' + str(tasks[i]['d']))
            unfeasibleCount += 1
            break

        wP = w
        n += 1

##
# Print result.
##

if unfeasibleCount == 0:
    print('\nTask set is schedulable!')
else:
    print('\nTask set is not schedulable, unfeasible tasks: ' + str(unfeasibleCount))
