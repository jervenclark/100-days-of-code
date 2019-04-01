# Start app

import ascii_graph
import fabric, pprint

# Establish connection
connection = fabric.Connection('web-server')

# Read nginx logs
def main():
    print('\n')
    header = ['total', 'used', 'free', 'shared', 'buffers', 'cache', 'available']
    result = connection.run('free -wm | grep Mem').stdout.split()
    result.pop(0)
    result = list(map(int, result))
    data = list(zip(header, result))
    for line in  ascii_graph.Pyasciigraph().graph('System Resource', data):
        print(line)
    print('\n')

main()
