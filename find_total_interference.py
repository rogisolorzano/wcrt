##
# @author Rogi Solorzano
#

import math


def find_total_interference(w, max_index, tasks):
    """
    Find the total interference of tasks up to a max_index

    :param w: the current frame size
    :param max_index: the index (inclusive) of the last task inside t that
                      is smaller than the current period
    :param tasks: the array of all tasks
    :return: result: map containing int 'total' and string 'calculation'
    """
    result = {'total': 0, 'calculation': ''}

    for i in range(0, max_index + 1):
        t = tasks[i]
        result['total'] += math.ceil(w / t['p']) * t['e']
        result['calculation'] += ' + ceil(' + str(w) + \
                                 ' / ' + str(t['p']) + ') * ' + str(t['e'])

    return result
