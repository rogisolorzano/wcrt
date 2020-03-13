##
# @author Rogi Solorzano
#


def load_file(file_name):
    """
    Loads task set from file

    :param file_name:
    :return: nodes: array of tasks maps
    """

    nodes = []

    with open(file_name, 'r') as fp:
        line = fp.readline()

        while line:
            line = line.replace('(', '').replace(')', '')
            task = list(
                map(
                    lambda val: val.strip(),
                    line.split(',')
                )
            )
            nodes.append({
                'o': float(task[0]),  # phase
                'p': float(task[1]),  # period
                'e': float(task[2]),  # execution time
                'd': float(task[3]),  # relative deadline
                'B': float(task[4]),  # blocking time
            })

            line = fp.readline()

    return nodes
